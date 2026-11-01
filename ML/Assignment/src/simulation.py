"""
simulation.py
=============
Multi-regime Ornstein-Uhlenbeck and Market Factor Synthetic Asset Generator.

Generates realistic non-stationary financial asset prices with cointegrating
mean-reverting spreads across diverse market regimes:
1. Strong Mean-Reversion (Fast half-life, highly stationary spread)
2. Moderate Mean-Reversion (Institutional-grade statistical arbitrage pair)
3. Weak / Slow Mean-Reversion (Prolonged deviations, high persistence)
4. Structural Break / Regime Shift (Stable cointegration breaking down at T/2)
5. Spurious Correlation (Correlated to common factor, but spread is a random walk)
"""

from typing import Dict, Tuple, Optional
import numpy as np
import pandas as pd


def exact_ou_step(
    s_prev: float,
    kappa: float,
    theta: float,
    sigma: float,
    dt: float = 1.0,
    rng: Optional[np.random.Generator] = None,
) -> float:
    """Computes an exact discrete step for an Ornstein-Uhlenbeck process.
    
    Exact transition distribution:
        S_t | S_{t-1} ~ Normal(mean, variance)
        mean = S_{t-1} * exp(-kappa * dt) + theta * (1 - exp(-kappa * dt))
        variance = (sigma^2 / (2 * kappa)) * (1 - exp(-2 * kappa * dt))
    """
    if rng is None:
        rng = np.random.default_rng()
    
    if kappa <= 1e-8:
        # Non-stationary driftless random walk (kappa -> 0)
        return float(s_prev + sigma * np.sqrt(dt) * rng.standard_normal())

    exp_term = np.exp(-kappa * dt)
    mean = s_prev * exp_term + theta * (1.0 - exp_term)
    variance = (sigma**2 / (2.0 * kappa)) * (1.0 - exp_term**2)
    std_dev = np.sqrt(max(variance, 1e-12))
    
    return float(rng.normal(loc=mean, scale=std_dev))


def simulate_ou_series(
    n_steps: int,
    kappa: float,
    theta: float,
    sigma: float,
    s0: float = 0.0,
    dt: float = 1.0,
    rng: Optional[np.random.Generator] = None,
) -> np.ndarray:
    """Simulates a continuous trajectory of an Ornstein-Uhlenbeck process."""
    if rng is None:
        rng = np.random.default_rng()
        
    s = np.zeros(n_steps)
    s[0] = s0
    
    if kappa <= 1e-8:
        # Pure Random Walk
        shocks = sigma * np.sqrt(dt) * rng.standard_normal(n_steps)
        s = s0 + np.cumsum(shocks)
        s[0] = s0
        return s
        
    exp_term = np.exp(-kappa * dt)
    mean_scale = theta * (1.0 - exp_term)
    std_dev = np.sqrt(max((sigma**2 / (2.0 * kappa)) * (1.0 - exp_term**2), 1e-12))
    shocks = rng.standard_normal(n_steps)
    
    for t in range(1, n_steps):
        s[t] = s[t - 1] * exp_term + mean_scale + std_dev * shocks[t]
        
    return s


def simulate_pair(
    pair_type: str = "moderate",
    n_steps: int = 5000,
    alpha: float = 0.5,
    beta: float = 1.2,
    market_vol: float = 0.012,
    idio_vol_x: float = 0.008,
    s0: float = 0.0,
    seed: Optional[int] = 42,
) -> pd.DataFrame:
    """Simulates a cointegrated or spurious asset pair under specific regime dynamics.
    
    Parameters
    ----------
    pair_type : str
        One of {'strong', 'moderate', 'weak', 'structural_break', 'spurious'}
    n_steps : int
        Number of time steps (e.g. 5000 trading bars)
    alpha : float
        True intercept in cointegrating relation: log(Y) = alpha + beta * log(X) + S
    beta : float
        True slope / hedge ratio
    market_vol : float
        Volatility of common latent market factor
    idio_vol_x : float
        Idiosyncratic volatility of Asset X
    s0 : float
        Initial spread value
    seed : Optional[int]
        Random seed for reproducibility

    Returns
    -------
    pd.DataFrame
        DataFrame with columns:
        ['time', 'market_factor', 'price_x', 'price_y', 'log_x', 'log_y', 'true_spread', 'regime', 'pair_type']
    """
    rng = np.random.default_rng(seed)
    
    # 1. Simulate Latent Market Factor M_t (Geometric Brownian Motion)
    market_returns = rng.normal(loc=0.0002, scale=market_vol, size=n_steps)
    log_market = np.log(100.0) + np.cumsum(market_returns)
    
    # 2. Simulate Base Asset X_t (Exposure to market factor + idiosyncratic noise)
    idio_x = rng.normal(loc=0.0, scale=idio_vol_x, size=n_steps)
    log_x = 0.8 * log_market + np.cumsum(idio_x)
    price_x = np.exp(log_x)
    
    # 3. Regime Parameter Calibration
    regimes = np.array([pair_type] * n_steps, dtype=object)
    
    if pair_type == "strong":
        # Fast half-life ~ 7 bars (kappa = 0.10)
        kappa, theta, sigma_s = 0.10, 0.0, 0.025
        spread = simulate_ou_series(n_steps, kappa, theta, sigma_s, s0=s0, rng=rng)
        
    elif pair_type == "moderate":
        # Medium half-life ~ 23 bars (kappa = 0.03)
        kappa, theta, sigma_s = 0.03, 0.0, 0.030
        spread = simulate_ou_series(n_steps, kappa, theta, sigma_s, s0=s0, rng=rng)
        
    elif pair_type == "weak":
        # Slow half-life ~ 86 bars (kappa = 0.008)
        kappa, theta, sigma_s = 0.008, 0.0, 0.035
        spread = simulate_ou_series(n_steps, kappa, theta, sigma_s, s0=s0, rng=rng)
        
    elif pair_type == "structural_break":
        # Phase 1 (0 to T/2): Stable cointegration (kappa = 0.04)
        # Phase 2 (T/2 to T): Breakdown into random walk (kappa -> 0) + mean jump
        half = n_steps // 2
        spread = np.zeros(n_steps)
        spread[:half] = simulate_ou_series(half, kappa=0.04, theta=0.0, sigma=0.025, s0=s0, rng=rng)
        
        # Breakdown phase: sudden equilibrium shift + random walk drift
        regimes[half:] = "breakdown"
        jump = 0.08
        s_mid = spread[half - 1] + jump
        spread[half:] = simulate_ou_series(
            n_steps - half, kappa=0.0001, theta=0.15, sigma=0.040, s0=s_mid, rng=rng
        )
        
    elif pair_type == "spurious":
        # Spread is pure non-stationary random walk (kappa = 0)
        kappa, theta, sigma_s = 0.0, 0.0, 0.028
        spread = simulate_ou_series(n_steps, kappa, theta, sigma_s, s0=s0, rng=rng)
        
    else:
        raise ValueError(f"Unknown pair_type '{pair_type}'. Choose from strong, moderate, weak, structural_break, spurious.")
        
    # 4. Formulate Paired Asset Y_t
    # log(Y_t) = alpha + beta * log(X_t) + spread_t
    log_y = alpha + beta * log_x + spread
    price_y = np.exp(log_y)
    
    df = pd.DataFrame({
        "time": np.arange(n_steps),
        "market_factor": np.exp(log_market),
        "price_x": price_x,
        "price_y": price_y,
        "log_x": log_x,
        "log_y": log_y,
        "true_spread": spread,
        "regime": regimes,
        "pair_type": pair_type,
    })
    
    return df


def simulate_multi_pair_universe(
    n_steps: int = 5000,
    base_seed: int = 42,
) -> Dict[str, pd.DataFrame]:
    """Generates the full multi-regime universe containing all 5 distinct pair types.
    
    Returns
    -------
    Dict[str, pd.DataFrame]
        Dictionary mapping pair archetype names to their simulated time-series DataFrames.
    """
    pair_types = ["strong", "moderate", "weak", "structural_break", "spurious"]
    universe = {}
    
    for idx, p_type in enumerate(pair_types):
        seed = base_seed + (idx * 101)
        df_pair = simulate_pair(pair_type=p_type, n_steps=n_steps, seed=seed)
        universe[p_type] = df_pair
        
    return universe
