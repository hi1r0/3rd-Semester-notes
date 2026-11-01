"""
simulation.py
=============
Market Data Pipeline & Pair Loader for Real Equity and ETF Universes.

Provides unified access to historical daily market prices (2015-2024) across:
- Market Benchmark: SPY (SPDR S&P 500 ETF)
- KO vs. PEP (Coca-Cola vs. PepsiCo - Consumer Staples)
- XOM vs. CVX (ExxonMobil vs. Chevron - Energy)
- JPM vs. BAC (JPMorgan Chase vs. Bank of America - Financials)
- BP vs. SHEL (BP vs. Shell - Transatlantic Oil)
- GLD vs. SPY (SPDR Gold vs. S&P 500 ETF - Macro Asset Pair)
"""

from typing import Dict, Optional
import os
import numpy as np
import pandas as pd
from src.market_data import (
    load_raw_market_data,
    extract_pair_dataframe,
    load_multi_pair_universe,
    PAIR_DEFINITIONS,
)

# Archetype mapping to real market tickers
ARCHETYPE_MAPPING = {
    "strong": "KO_PEP",
    "moderate": "XOM_CVX",
    "weak": "JPM_BAC",
    "structural_break": "BP_SHEL",
    "spurious": "GLD_SPY",
    "KO_PEP": "KO_PEP",
    "XOM_CVX": "XOM_CVX",
    "JPM_BAC": "JPM_BAC",
    "BP_SHEL": "BP_SHEL",
    "GLD_SPY": "GLD_SPY",
}


def simulate_pair(
    pair_type: str = "moderate",
    n_steps: Optional[int] = None,
    **kwargs,
) -> pd.DataFrame:
    """Loads and formats the real market price data for the specified pair."""
    pair_id = ARCHETYPE_MAPPING.get(pair_type, "XOM_CVX")
    raw_prices = load_raw_market_data()
    df_pair = extract_pair_dataframe(raw_prices, pair_id)
    
    if n_steps is not None and n_steps < len(df_pair):
        df_pair = df_pair.iloc[:n_steps].copy().reset_index(drop=True)
        df_pair["time"] = np.arange(len(df_pair))
        
    return df_pair


def simulate_multi_pair_universe(
    n_steps: Optional[int] = None,
    base_seed: Optional[int] = None,
) -> Dict[str, pd.DataFrame]:
    """Loads the real market price series across all 5 equity and ETF pairs."""
    universe = load_multi_pair_universe()
    if n_steps is not None:
        for k in universe:
            if n_steps < len(universe[k]):
                universe[k] = universe[k].iloc[:n_steps].copy().reset_index(drop=True)
                universe[k]["time"] = np.arange(len(universe[k]))
    return universe
