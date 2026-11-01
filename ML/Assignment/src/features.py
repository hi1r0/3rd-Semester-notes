"""
features.py
===========
Quantitative & Statistical Feature Engineering for Pairs Trading Signals.

Extracts an informative 12-dimensional feature representation at every
candidate trading signal timestamp, capturing:
- Deviation & momentum dynamics
- Ornstein-Uhlenbeck mean-reversion kinetics (half-life)
- Fractal memory / long-range persistence (Hurst exponent)
- Unit root stationarity rejection (ADF p-value)
- Serial dependency structure (Autocorrelations)
- Volatility regime changes (Volatility ratios)
- Cointegration parameter stability (Hedge ratio variance)
"""

from typing import List, Optional
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller


def compute_half_life(series: np.ndarray) -> float:
    """Estimates the Ornstein-Uhlenbeck half-life of mean-reversion.
    
    Fits: delta_S_t = a + b * S_{t-1} + epsilon_t
    Half-life = -ln(2) / b, where b is negative for mean-reverting series.
    """
    clean_series = series[np.isfinite(series)]
    if len(clean_series) < 15:
        return 200.0
        
    s_lag = clean_series[:-1]
    s_diff = np.diff(clean_series)
    
    # OLS of s_diff on s_lag
    var_lag = np.var(s_lag)
    if not np.isfinite(var_lag) or var_lag <= 1e-12:
        return 200.0
        
    cov_matrix = np.cov(s_lag, s_diff)
    if not np.isfinite(cov_matrix).all():
        return 200.0
        
    cov = cov_matrix[0, 1]
    b = cov / var_lag
    
    if not np.isfinite(b) or b >= -1e-6:
        # Non mean-reverting or explosive
        return 200.0
        
    half_life = -np.log(2.0) / b
    if not np.isfinite(half_life):
        return 200.0
    return float(np.clip(half_life, 1.0, 200.0))


def compute_hurst_exponent(series: np.ndarray, max_lags: int = 20) -> float:
    """Estimates the Hurst Exponent H using the variance of differences method.
    
    Var(S_{t+tau} - S_t) ~ tau^(2 * H)
    H < 0.5: Mean-reverting series
    H = 0.5: Geometric Brownian motion / random walk
    H > 0.5: Trending / persistent series
    """
    clean_series = series[np.isfinite(series)]
    n = len(clean_series)
    if n < 30:
        return 0.5
        
    lags = np.unique(np.linspace(2, min(max_lags, n // 3), num=6, dtype=int))
    tau_vars = []
    
    for tau in lags:
        diffs = clean_series[tau:] - clean_series[:-tau]
        var = np.var(diffs)
        if np.isfinite(var) and var > 1e-12:
            tau_vars.append(var)
        else:
            tau_vars.append(1e-12)
            
    log_lags = np.log(lags)
    log_vars = np.log(tau_vars)
    
    try:
        slope, _ = np.polyfit(log_lags, log_vars, 1)
        hurst = slope / 2.0
        if not np.isfinite(hurst):
            return 0.5
        return float(np.clip(hurst, 0.01, 0.99))
    except Exception:
        return 0.5


def compute_adf_pvalue(series: np.ndarray) -> float:
    """Computes the p-value of the Augmented Dickey-Fuller test.
    
    p < 0.05 rejects the unit-root null hypothesis (indicates stationarity).
    """
    clean_series = series[np.isfinite(series)]
    if len(clean_series) < 25 or np.all(clean_series == clean_series[0]):
        return 1.0
        
    try:
        res = adfuller(clean_series, maxlag=1, autolag=None)
        p_val = float(res[1])
        if not np.isfinite(p_val):
            return 1.0
        return float(np.clip(p_val, 0.0, 1.0))
    except Exception:
        return 1.0


def extract_signal_features(
    df: pd.DataFrame,
    lookback: int = 60,
    feature_cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    """Extracts the comprehensive 12-dimensional feature vector at all signal points.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with 'est_spread', 'z_score', 'log_x', 'log_y', 'beta', 'is_entry'.
    lookback : int
        Window size for statistical properties (half-life, Hurst, ADF).
    feature_cols : Optional[List[str]]
        Specific list of feature columns to return.
        
    Returns
    -------
    pd.DataFrame
        Feature matrix aligned with signal entry rows.
    """
    entry_indices = np.where(df["is_entry"].to_numpy())[0]
    spread = df["est_spread"].to_numpy()
    
    # Filter indices that have sufficient prior valid history without NaNs
    valid_indices = [
        idx for idx in entry_indices
        if idx - lookback >= 0 and not np.isnan(spread[idx - lookback + 1 : idx + 1]).any()
    ]
    
    records = []
    spread = df["est_spread"].to_numpy()
    z_score = df["z_score"].to_numpy()
    log_x = df["log_x"].to_numpy()
    log_y = df["log_y"].to_numpy()
    beta = df["beta"].to_numpy()
    sig_type = df["signal_type"].to_numpy()
    
    for idx in valid_indices:
        w_spread = spread[idx - lookback + 1 : idx + 1]
        w_log_x = log_x[idx - lookback + 1 : idx + 1]
        w_log_y = log_y[idx - lookback + 1 : idx + 1]
        w_beta = beta[idx - lookback + 1 : idx + 1]
        
        # 1. Z-score at trigger
        z_val = z_score[idx]
        
        # 2. Spread momentum over multiple horizons
        mom_1 = spread[idx] - spread[idx - 1]
        mom_5 = spread[idx] - spread[idx - 5]
        mom_10 = spread[idx] - spread[idx - 10]
        
        # 3. Ornstein-Uhlenbeck Half-Life
        half_life = compute_half_life(w_spread)
        
        # 4. Hurst Exponent
        hurst = compute_hurst_exponent(w_spread)
        
        # 5. ADF Test p-value
        adf_p = compute_adf_pvalue(w_spread)
        
        # 6. Serial Autocorrelations (Lags 1 and 2)
        s_series = pd.Series(w_spread)
        ac1 = s_series.autocorr(lag=1)
        ac2 = s_series.autocorr(lag=2)
        ac1 = 0.0 if np.isnan(ac1) else ac1
        ac2 = 0.0 if np.isnan(ac2) else ac2
        
        # 7. Volatility Ratio (Short-term 10 vs Long-term 50)
        std_short = np.std(spread[idx - 10 + 1 : idx + 1], ddof=1)
        std_long = np.std(spread[idx - 50 + 1 : idx + 1], ddof=1)
        vol_ratio = (std_short / std_long) if std_long > 1e-8 else 1.0
        
        # 8. Rolling Pearson Correlation between Asset X and Asset Y
        corr = np.corrcoef(w_log_x, w_log_y)[0, 1]
        corr = 0.0 if np.isnan(corr) else corr
        
        # 9. Hedge Ratio Stability (recent beta standard deviation)
        beta_stab = np.std(w_beta, ddof=1)
        beta_stab = 0.0 if np.isnan(beta_stab) else beta_stab
        
        record = {
            "entry_index": idx,
            "signal_type": sig_type[idx],
            "z_score": z_val,
            "spread_momentum_1d": mom_1,
            "spread_momentum_5d": mom_5,
            "spread_momentum_10d": mom_10,
            "ou_half_life": half_life,
            "hurst_exponent": hurst,
            "adf_pvalue": adf_p,
            "autocorr_lag1": ac1,
            "autocorr_lag2": ac2,
            "volatility_ratio": float(np.clip(vol_ratio, 0.1, 10.0)),
            "rolling_correlation": corr,
            "hedge_ratio_stability": beta_stab,
        }
        records.append(record)
        
    feat_df = pd.DataFrame(records)
    if not feat_df.empty:
        # Fill any unexpected residual NaN with column median / safe defaults
        feat_df = feat_df.fillna(feat_df.median(numeric_only=True)).fillna(0.0)
    return feat_df
