"""
market_data.py
==============
Market Data Ingestion and Multi-Asset Universe Pipeline for Real Equities & ETFs.

Loads historical daily market prices (2015-2024) across 10 liquid US equities and ETFs:
- Market Benchmark: SPY (SPDR S&P 500 ETF Trust)
- Pair 1: KO (Coca-Cola) vs. PEP (PepsiCo) - Consumer Staples Titans
- Pair 2: XOM (ExxonMobil) vs. CVX (Chevron) - Integrated Oil & Gas Megacaps
- Pair 3: JPM (JPMorgan Chase) vs. BAC (Bank of America) - Money Center Banking
- Pair 4: BP (BP p.l.c.) vs. SHEL (Shell plc) - Transatlantic Energy / Regime Transition
- Pair 5: GLD (SPDR Gold Shares) vs. SPY (S&P 500 ETF) - Macro Equity/Commodity Arbitrage
"""

import os
from typing import Dict, Optional, Tuple
import numpy as np
import pandas as pd


PAIR_DEFINITIONS = {
    "KO_PEP": {
        "ticker_x": "KO",
        "ticker_y": "PEP",
        "name": "Coca-Cola vs. PepsiCo",
        "sector": "Consumer Staples",
        "rationale": "High-conviction consumer brand cointegration with stable demand.",
    },
    "XOM_CVX": {
        "ticker_x": "XOM",
        "ticker_y": "CVX",
        "name": "ExxonMobil vs. Chevron",
        "sector": "Energy (Oil & Gas)",
        "rationale": "Co-movement driven by global crude oil and upstream refining margins.",
    },
    "JPM_BAC": {
        "ticker_x": "JPM",
        "ticker_y": "BAC",
        "name": "JPMorgan Chase vs. Bank of America",
        "sector": "Financials (Banks)",
        "rationale": "Sensitivity to US Treasury yield curve, net interest margins, and credit cycles.",
    },
    "BP_SHEL": {
        "ticker_x": "BP",
        "ticker_y": "SHEL",
        "name": "BP vs. Shell",
        "sector": "Integrated Energy",
        "rationale": "Cross-border European oil majors subject to energy transition policy shifts.",
    },
    "GLD_SPY": {
        "ticker_x": "GLD",
        "ticker_y": "SPY",
        "name": "SPDR Gold vs. S&P 500 ETF",
        "sector": "Macro Commodity / Equity",
        "rationale": "Macro risk asset pair; correlated sentiment without long-run stationarity.",
    },
}


def load_raw_market_data(csv_path: Optional[str] = None) -> pd.DataFrame:
    """Loads historical adjusted close prices from CSV or downloads via yfinance."""
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "market_data.csv")
        
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
        return df
        
    # Fallback to direct yfinance download
    import yfinance as yf
    tickers = ["SPY", "KO", "PEP", "XOM", "CVX", "JPM", "BAC", "BP", "SHEL", "GLD"]
    df = yf.download(tickers, start="2015-01-01", end="2024-01-01", auto_adjust=True)["Close"]
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    df.to_csv(csv_path)
    return df


def extract_pair_dataframe(
    prices_df: pd.DataFrame,
    pair_id: str,
) -> pd.DataFrame:
    """Extracts and structures a standardized pair dataset for econometric analysis."""
    if pair_id not in PAIR_DEFINITIONS:
        raise ValueError(f"Unknown pair_id '{pair_id}'. Available: {list(PAIR_DEFINITIONS.keys())}")
        
    cfg = PAIR_DEFINITIONS[pair_id]
    tx = cfg["ticker_x"]
    ty = cfg["ticker_y"]
    
    px = prices_df[tx].to_numpy()
    py = prices_df[ty].to_numpy()
    market = prices_df["SPY"].to_numpy()
    dates = prices_df.index
    
    log_x = np.log(px)
    log_y = np.log(py)
    
    # Static OLS spread as reference benchmark
    var_x = np.var(log_x)
    beta_static = np.cov(log_x, log_y)[0, 1] / var_x if var_x > 1e-12 else 1.0
    alpha_static = np.mean(log_y) - beta_static * np.mean(log_x)
    ref_spread = log_y - (alpha_static + beta_static * log_x)
    
    df_pair = pd.DataFrame({
        "time": np.arange(len(dates)),
        "date": dates,
        "market_factor": market,
        "price_x": px,
        "price_y": py,
        "log_x": log_x,
        "log_y": log_y,
        "true_spread": ref_spread,
        "pair_id": pair_id,
        "ticker_x": tx,
        "ticker_y": ty,
        "pair_name": cfg["name"],
        "sector": cfg["sector"],
    })
    
    return df_pair


def load_multi_pair_universe(csv_path: Optional[str] = None) -> Dict[str, pd.DataFrame]:
    """Loads all 5 real equity and ETF pairs into a standardized dictionary."""
    raw_prices = load_raw_market_data(csv_path)
    universe = {}
    
    for pair_id in PAIR_DEFINITIONS.keys():
        df_pair = extract_pair_dataframe(raw_prices, pair_id)
        universe[pair_id] = df_pair
        
    return universe
