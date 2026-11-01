"""
cointegration.py
================
Rolling Cointegration, Hedge Ratio Estimation, and Z-Score Generation.

Avoids lookahead bias by using strictly backward-looking rolling estimation
windows for hedge ratios (beta), intercepts (alpha), and spread standardization.
"""

from typing import Tuple
import numpy as np
import pandas as pd


def compute_rolling_ols(
    y: np.ndarray,
    x: np.ndarray,
    window: int = 120,
) -> Tuple[np.ndarray, np.ndarray]:
    """Computes rolling Ordinary Least Squares (OLS) regression parameters.
    
    Fits: y_t = alpha_t + beta_t * x_t + epsilon_t
    
    Parameters
    ----------
    y : np.ndarray
        Dependent variable array (e.g., log_y)
    x : np.ndarray
        Independent variable array (e.g., log_x)
    window : int
        Rolling lookback window length
        
    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        (alpha, beta) arrays of shape (len(y),) with NaNs for t < window - 1.
    """
    n = len(y)
    alpha = np.full(n, np.nan)
    beta = np.full(n, np.nan)
    
    # Vectorized moving sums for rolling covariance and variance
    # sum(x), sum(y), sum(x^2), sum(x*y)
    x_series = pd.Series(x)
    y_series = pd.Series(y)
    
    mean_x = x_series.rolling(window=window).mean().to_numpy()
    mean_y = y_series.rolling(window=window).mean().to_numpy()
    
    cov_xy = (x_series * y_series).rolling(window=window).mean().to_numpy() - (mean_x * mean_y)
    var_x = (x_series * x_series).rolling(window=window).mean().to_numpy() - (mean_x * mean_x)
    
    # Avoid zero division
    var_x = np.where(var_x <= 1e-12, 1e-12, var_x)
    
    b = cov_xy / var_x
    a = mean_y - b * mean_x
    
    return a, b


def compute_spread_and_zscore(
    df_pair: pd.DataFrame,
    ols_window: int = 120,
    z_window: int = 40,
    entry_threshold: float = 2.0,
    exit_threshold: float = 0.0,
    stop_threshold: float = 3.5,
) -> pd.DataFrame:
    """Computes rolling hedge ratio, spread series, and standardized Z-scores.
    
    Parameters
    ----------
    df_pair : pd.DataFrame
        Pair DataFrame containing 'log_x', 'log_y', 'price_x', 'price_y'.
    ols_window : int
        Lookback window for hedge ratio estimation.
    z_window : int
        Lookback window for spread mean/standard deviation normalization.
    entry_threshold : float
        Z-score magnitude threshold for candidate trade triggers (e.g., 2.0).
    exit_threshold : float
        Z-score target for mean-reversion exit (e.g., 0.0).
    stop_threshold : float
        Z-score magnitude threshold for stop-loss exit (e.g., 3.5).
        
    Returns
    -------
    pd.DataFrame
        Enriched DataFrame with columns:
        ['alpha', 'beta', 'est_spread', 'spread_mean', 'spread_std', 'z_score', 'signal_type', 'is_entry']
    """
    df = df_pair.copy()
    log_x = df["log_x"].to_numpy()
    log_y = df["log_y"].to_numpy()
    
    # 1. Rolling Hedge Ratio
    alpha, beta = compute_rolling_ols(y=log_y, x=log_x, window=ols_window)
    df["alpha"] = alpha
    df["beta"] = beta
    
    # 2. Estimated Spread: S_t = log(Y_t) - (alpha_t + beta_t * log(X_t))
    est_spread = log_y - (alpha + beta * log_x)
    df["est_spread"] = est_spread
    
    # 3. Rolling Z-Score Standardization
    spread_series = pd.Series(est_spread)
    spread_mean = spread_series.rolling(window=z_window).mean().to_numpy()
    spread_std = spread_series.rolling(window=z_window).std(ddof=1).to_numpy()
    
    spread_std = np.where(np.isnan(spread_std) | (spread_std <= 1e-8), 1e-8, spread_std)
    z_score = (est_spread - spread_mean) / spread_std
    
    df["spread_mean"] = spread_mean
    df["spread_std"] = spread_std
    df["z_score"] = z_score
    
    # 4. Entry Signals
    # signal_type: +1 (Long Spread: Z <= -entry_thresh), -1 (Short Spread: Z >= +entry_thresh), 0 (None)
    signal_type = np.zeros(len(df), dtype=int)
    signal_type[z_score >= entry_threshold] = -1  # Short spread (sell Y, buy beta X)
    signal_type[z_score <= -entry_threshold] = 1   # Long spread (buy Y, sell beta X)
    
    # Prevent consecutive repeated entries in the same direction before exiting
    # Entry trigger is considered only at the frontier of entering the trigger zone
    is_entry = np.zeros(len(df), dtype=bool)
    prev_sig = 0
    for i in range(1, len(df)):
        current = signal_type[i]
        if current != 0 and prev_sig == 0:
            is_entry[i] = True
            prev_sig = current
        elif current == 0:
            prev_sig = 0
            
    df["signal_type"] = signal_type
    df["is_entry"] = is_entry
    
    return df
