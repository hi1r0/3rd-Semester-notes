"""
labeling.py
===========
Triple-Barrier Meta-Labeling for Statistical Arbitrage Pairs Trading.

Implements Marcos López de Prado's meta-labeling approach:
1. Horizontal Barrier 1 (Take-Profit): Mean-reversion back to equilibrium (|Z| <= exit_z, e.g. 0.0).
2. Horizontal Barrier 2 (Stop-Loss): Catastrophic spread divergence (|Z| >= stop_z, e.g. 3.5).
3. Vertical Barrier (Horizon Limit): Maximum holding duration H (e.g. 15 bars).
4. Realistic Transaction Friction: Deducts round-trip cost (10 bps).
"""

from typing import Tuple, Dict, Any
import numpy as np
import pandas as pd


def apply_triple_barrier_labeling(
    df: pd.DataFrame,
    features_df: pd.DataFrame,
    horizon: int = 15,
    exit_z: float = 0.0,
    stop_z: float = 3.5,
    transaction_cost: float = 0.0010,  # 10 bps round-trip
) -> pd.DataFrame:
    """Labels candidate trading signals based on actual future realization.
    
    Parameters
    ----------
    df : pd.DataFrame
        Complete time-series DataFrame with 'price_x', 'price_y', 'z_score', 'beta'.
    features_df : pd.DataFrame
        Feature DataFrame containing 'entry_index' and 'signal_type'.
    horizon : int
        Maximum holding bars (vertical barrier).
    exit_z : float
        Z-score target for take-profit exit (mean-reversion).
    stop_z : float
        Z-score threshold for stop-loss exit.
    transaction_cost : float
        Round-trip transaction cost fraction (e.g., 0.0010 = 10 bps).
        
    Returns
    -------
    pd.DataFrame
        Merged dataset with features, realized trade metrics, and binary target.
    """
    labeled_records = []
    
    price_x = df["price_x"].to_numpy()
    price_y = df["price_y"].to_numpy()
    z_scores = df["z_score"].to_numpy()
    betas = df["beta"].to_numpy()
    n_total = len(df)
    
    for _, row in features_df.iterrows():
        entry_idx = int(row["entry_index"])
        sig = int(row["signal_type"])  # +1: Long spread (Buy Y, Sell beta X), -1: Short spread
        
        # Ensure we have at least 1 bar ahead
        if entry_idx >= n_total - 1:
            continue
            
        max_idx = min(entry_idx + horizon, n_total - 1)
        beta_entry = betas[entry_idx]
        px_entry = price_x[entry_idx]
        py_entry = price_y[entry_idx]
        
        exit_idx = max_idx
        exit_reason = "horizon_limit"
        
        # Scan through future path for barrier hits
        for step in range(entry_idx + 1, max_idx + 1):
            curr_z = z_scores[step]
            
            if sig == 1:  # Long spread entered at Z <= -entry_z
                if curr_z >= exit_z:
                    exit_idx = step
                    exit_reason = "take_profit"
                    break
                elif curr_z <= -stop_z:
                    exit_idx = step
                    exit_reason = "stop_loss"
                    break
            elif sig == -1:  # Short spread entered at Z >= +entry_z
                if curr_z <= -exit_z:
                    exit_idx = step
                    exit_reason = "take_profit"
                    break
                elif curr_z >= stop_z:
                    exit_idx = step
                    exit_reason = "stop_loss"
                    break
                    
        # Calculate economic portfolio return from entry to exit
        # Capital base: Py + |beta| * Px
        px_exit = price_x[exit_idx]
        py_exit = price_y[exit_idx]
        capital_base = py_entry + abs(beta_entry) * px_entry
        
        if sig == 1:
            # Long Y, Short beta X
            pnl_gross = (py_exit - py_entry) - beta_entry * (px_exit - px_entry)
        else:
            # Short Y, Long beta X
            pnl_gross = -(py_exit - py_entry) + beta_entry * (px_exit - px_entry)
            
        ret_gross = pnl_gross / capital_base
        ret_net = ret_gross - transaction_cost
        
        # Binary target: 1 if strictly profitable after transaction costs, 0 otherwise
        target = 1 if ret_net > 0 else 0
        
        rec = row.to_dict()
        rec.update({
            "exit_index": exit_idx,
            "holding_period": exit_idx - entry_idx,
            "exit_reason": exit_reason,
            "gross_return": ret_gross,
            "net_return": ret_net,
            "target": target,
        })
        labeled_records.append(rec)
        
    labeled_df = pd.DataFrame(labeled_records)
    return labeled_df
