"""
backtest.py
===========
Event-Driven Vectorized Backtesting Engine for Pairs Trading Strategies.

Compares:
1. Traditional Statistical Arbitrage Strategy (Unfiltered: takes all |Z| >= 2 signals)
2. ML-Enhanced Strategy (Filtered: executes only when ML predicts P(Profit) >= threshold)

Computes institutional quantitative finance metrics:
- Cumulative Return & Equity Curve
- Annualized Sharpe & Sortino Ratios
- Maximum Drawdown (MDD) & Calmar Ratio
- Hit Ratio (Win Rate %) & Profit Factor
- Average Trade PnL & Efficiency
"""

from typing import Dict, Any, List, Optional, Tuple
import numpy as np
import pandas as pd


def compute_drawdown(equity_curve: np.ndarray) -> Tuple[np.ndarray, float]:
    """Computes the underwater drawdown series and maximum drawdown percentage."""
    running_max = np.maximum.accumulate(equity_curve)
    drawdowns = (equity_curve - running_max) / running_max
    max_dd = float(np.min(drawdowns))
    return drawdowns, max_dd


def evaluate_trading_performance(
    returns: np.ndarray,
    periods_per_year: int = 252,
) -> Dict[str, float]:
    """Computes quantitative performance metrics from a sequence of trade returns."""
    if len(returns) == 0:
        return {
            "Total Trades": 0,
            "Win Rate (%)": 0.0,
            "Cumulative Return (%)": 0.0,
            "Annualized Return (%)": 0.0,
            "Annualized Volatility (%)": 0.0,
            "Sharpe Ratio": 0.0,
            "Sortino Ratio": 0.0,
            "Max Drawdown (%)": 0.0,
            "Calmar Ratio": 0.0,
            "Profit Factor": 0.0,
            "Avg Trade PnL (bps)": 0.0,
        }
        
    n_trades = len(returns)
    wins = returns[returns > 0]
    losses = returns[returns < 0]
    
    win_rate = (len(wins) / n_trades) * 100.0 if n_trades > 0 else 0.0
    
    # Cumulative compounded equity
    equity = np.cumprod(1.0 + returns)
    cum_return = (equity[-1] - 1.0) * 100.0
    
    # Per-trade statistics
    mean_ret = np.mean(returns)
    std_ret = np.std(returns, ddof=1) if n_trades > 1 else 1e-6
    std_ret = 1e-6 if std_ret <= 1e-8 else std_ret
    
    # Annualized approximations
    ann_return = mean_ret * periods_per_year * 100.0
    ann_vol = std_ret * np.sqrt(periods_per_year) * 100.0
    sharpe = (mean_ret / std_ret) * np.sqrt(periods_per_year)
    
    # Downside deviation for Sortino
    downside_returns = returns[returns < 0]
    if len(downside_returns) > 0:
        downside_std = np.sqrt(np.mean(downside_returns**2))
        sortino = (mean_ret / downside_std) * np.sqrt(periods_per_year) if downside_std > 1e-8 else 0.0
    else:
        sortino = sharpe * 1.5 if sharpe > 0 else 0.0
        
    # Drawdown
    _, max_dd = compute_drawdown(equity)
    max_dd_pct = abs(max_dd) * 100.0
    calmar = (ann_return / max_dd_pct) if max_dd_pct > 1e-4 else 0.0
    
    # Profit Factor: sum(gains) / sum(|losses|)
    sum_gains = np.sum(wins) if len(wins) > 0 else 0.0
    sum_losses = np.sum(np.abs(losses)) if len(losses) > 0 else 0.0
    profit_factor = (sum_gains / sum_losses) if sum_losses > 1e-8 else (10.0 if sum_gains > 0 else 0.0)
    
    avg_pnl_bps = mean_ret * 10000.0
    
    return {
        "Total Trades": int(n_trades),
        "Win Rate (%)": round(win_rate, 2),
        "Cumulative Return (%)": round(cum_return, 2),
        "Annualized Return (%)": round(ann_return, 2),
        "Annualized Volatility (%)": round(ann_vol, 2),
        "Sharpe Ratio": round(sharpe, 3),
        "Sortino Ratio": round(sortino, 3),
        "Max Drawdown (%)": round(max_dd_pct, 2),
        "Calmar Ratio": round(calmar, 3),
        "Profit Factor": round(profit_factor, 3),
        "Avg Trade PnL (bps)": round(avg_pnl_bps, 2),
    }


def run_strategy_backtests(
    labeled_df: pd.DataFrame,
    detailed_outputs: Dict[str, Dict[str, Any]],
    prob_threshold: float = 0.50,
) -> Tuple[pd.DataFrame, Dict[str, np.ndarray]]:
    """Runs comparative backtests across Traditional and all 7 ML-filtered strategies.
    
    Parameters
    ----------
    labeled_df : pd.DataFrame
        Complete labeled dataset containing 'net_return' for all candidate trades.
    detailed_outputs : Dict[str, Dict[str, Any]]
        Outputs from evaluate_models_walk_forward containing 'oof_indices' and 'oof_probs'.
    prob_threshold : float
        Probability threshold for taking an ML-filtered trade.
        
    Returns
    -------
    Tuple[pd.DataFrame, Dict[str, np.ndarray]]
        - Performance summary comparison table for all strategies.
        - Dictionary of cumulative equity curves for plotting.
    """
    # Identify out-of-fold indices common across all evaluated models
    first_model = list(detailed_outputs.keys())[0]
    oof_idx = detailed_outputs[first_model]["oof_indices"]
    
    # Subset labeled data to out-of-fold evaluation sample
    eval_df = labeled_df.iloc[oof_idx].copy().reset_index(drop=True)
    all_net_returns = eval_df["net_return"].to_numpy()
    
    # 1. Baseline Strategy: Traditional Pair Trading (trade all signals)
    trad_metrics = evaluate_trading_performance(all_net_returns)
    equity_curves = {
        "Traditional Strategy": np.cumprod(1.0 + all_net_returns)
    }
    
    results = {
        "Traditional (No ML)": trad_metrics
    }
    
    # 2. ML-Filtered Strategies
    for model_name, out in detailed_outputs.items():
        probs = out["oof_probs"]
        # Take trade only if P(profitable) >= prob_threshold
        mask = probs >= prob_threshold
        
        # Returns when traded; 0.0 return when staying in cash
        filtered_returns = all_net_returns[mask]
        
        perf = evaluate_trading_performance(filtered_returns)
        results[f"ML: {model_name}"] = perf
        
        # Build aligned equity series for plotting (tracking all event timestamps)
        aligned_trade_series = np.where(mask, all_net_returns, 0.0)
        equity_curves[f"ML: {model_name}"] = np.cumprod(1.0 + aligned_trade_series)
        
    comparison_df = pd.DataFrame(results).T
    return comparison_df, equity_curves
