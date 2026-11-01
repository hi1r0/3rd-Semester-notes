"""
visualization.py
================
Publication-Grade Visualizations for ML Pair Trading Strategies.

Generates high-contrast, publication-quality graphics for:
- Historical asset price and spread dynamics across real equity & ETF pairs
- Standardized Z-scores with entry triggers and barrier exits
- Model ROC curves & AUC comparisons across the 7 MSQF classifiers
- Random Forest feature importance distributions
- Strategy equity curves and underwater drawdown comparisons
"""

from typing import Dict, List, Optional, Any
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc

# Clean financial styling
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#2c3e50"
plt.rcParams["axes.linewidth"] = 0.8


def plot_market_regimes(universe: Dict[str, pd.DataFrame], save_path: Optional[str] = None):
    """Plots the historical asset prices and spread dynamics across the multi-pair universe."""
    fig, axes = plt.subplots(len(universe), 2, figsize=(14, 15), sharex=True)
    fig.suptitle("Multi-Asset Pair Trading Universe: Historical Price & Spread Dynamics (2015–2024)", fontsize=16, weight="bold", y=0.99)
    
    pair_labels = {
        "KO_PEP": "KO vs. PEP (Coca-Cola vs. PepsiCo — Consumer Staples)",
        "XOM_CVX": "XOM vs. CVX (ExxonMobil vs. Chevron — Energy)",
        "JPM_BAC": "JPM vs. BAC (JPMorgan Chase vs. Bank of America — Financials)",
        "BP_SHEL": "BP vs. SHEL (BP vs. Shell — Integrated Oil)",
        "GLD_SPY": "GLD vs. SPY (SPDR Gold vs. S&P 500 ETF — Macro Asset Pair)",
        "strong": "Strong Mean-Reversion Benchmark (Fast Half-Life)",
        "moderate": "Moderate Mean-Reversion Benchmark (Institutional)",
        "weak": "Weak / Slow Mean-Reversion Benchmark",
        "structural_break": "Structural Break / Regime Shift Benchmark",
        "spurious": "Macro / Spurious Non-Cointegrated Pair",
    }
    
    colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
    
    for idx, (p_type, df) in enumerate(universe.items()):
        color = colors[idx % len(colors)]
        title_label = pair_labels.get(p_type, df.get("pair_name", pd.Series([p_type])).iloc[0] if "pair_name" in df else p_type)
        tx = df["ticker_x"].iloc[0] if "ticker_x" in df.columns else "Asset X"
        ty = df["ticker_y"].iloc[0] if "ticker_y" in df.columns else "Asset Y"
        
        # Left: Asset prices
        ax_p = axes[idx, 0]
        ax_p.plot(df["time"], df["price_x"], label=f"{tx} (Base)", color="#7f7f7f", alpha=0.75, lw=1.2)
        ax_p.plot(df["time"], df["price_y"], label=f"{ty} (Paired)", color=color, lw=1.4)
        ax_p.set_title(f"Prices: {title_label}", fontsize=11, weight="bold")
        ax_p.set_ylabel("Price ($)")
        ax_p.legend(loc="upper left", frameon=True, fontsize=9)
        
        # Right: Spread
        ax_s = axes[idx, 1]
        ax_s.plot(df["time"], df["true_spread"], color=color, lw=1.2, label="Estimated Spread S_t")
        ax_s.axhline(0, color="black", linestyle="--", alpha=0.6, lw=0.8)
        ax_s.set_title(f"Spread: {tx} - {ty}", fontsize=11, weight="bold")
        ax_s.set_ylabel("Spread")
        ax_s.legend(loc="upper left", frameon=True, fontsize=9)
        
    axes[-1, 0].set_xlabel("Time (Trading Days)")
    axes[-1, 1].set_xlabel("Time (Trading Days)")
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_zscore_and_signals(df: pd.DataFrame, max_bars: int = 1000, save_path: Optional[str] = None):
    """Plots rolling Z-score with trade entry triggers and barrier thresholds."""
    sub_df = df.iloc[:max_bars].copy()
    
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(sub_df["time"], sub_df["z_score"], color="#2b5c8f", lw=1.2, label="Spread Z-Score")
    
    # Thresholds
    ax.axhline(2.0, color="#d9534f", linestyle="--", lw=1.2, label="Short Entry (+2.0)")
    ax.axhline(-2.0, color="#5cb85c", linestyle="--", lw=1.2, label="Long Entry (-2.0)")
    ax.axhline(0.0, color="#333333", linestyle=":", lw=1.0, label="Equilibrium / Exit (0.0)")
    ax.axhline(3.5, color="#8b0000", linestyle="-.", lw=1.0, alpha=0.7, label="Stop-Loss (+3.5)")
    ax.axhline(-3.5, color="#006400", linestyle="-.", lw=1.0, alpha=0.7, label="Stop-Loss (-3.5)")
    
    # Entry Markers
    long_entries = sub_df[(sub_df["is_entry"]) & (sub_df["signal_type"] == 1)]
    short_entries = sub_df[(sub_df["is_entry"]) & (sub_df["signal_type"] == -1)]
    
    ax.scatter(long_entries["time"], long_entries["z_score"], marker="^", color="#2e7d32", s=70, label="Long Trigger", zorder=5)
    ax.scatter(short_entries["time"], short_entries["z_score"], marker="v", color="#c62828", s=70, label="Short Trigger", zorder=5)
    
    ax.set_title("Standardized Spread Z-Score & Candidate Entry Signals", fontsize=13, weight="bold")
    ax.set_xlabel("Time (Bars)")
    ax.set_ylabel("Standardized Z-Score")
    ax.legend(loc="upper right", ncol=4, frameon=True, fontsize=9)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_roc_curves(detailed_outputs: Dict[str, Dict[str, Any]], save_path: Optional[str] = None):
    """Plots multi-model ROC curves with AUC annotations."""
    fig, ax = plt.subplots(figsize=(9, 7))
    
    palette = sns.color_palette("tab10", len(detailed_outputs))
    
    for idx, (name, out) in enumerate(detailed_outputs.items()):
        targets = out["oof_targets"]
        probs = out["oof_probs"]
        fpr, tpr, _ = roc_curve(targets, probs)
        roc_auc = auc(fpr, tpr)
        
        ax.plot(fpr, tpr, lw=1.8, color=palette[idx], label=f"{name} (AUC = {roc_auc:.3f})")
        
    ax.plot([0, 1], [0, 1], color="#888888", linestyle="--", lw=1.2, label="Random Guess (AUC = 0.500)")
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.02])
    ax.set_xlabel("False Positive Rate (1 - Specificity)", fontsize=11)
    ax.set_ylabel("True Positive Rate (Sensitivity / Recall)", fontsize=11)
    ax.set_title("Out-of-Fold Receiver Operating Characteristic (ROC) Comparison", fontsize=13, weight="bold")
    ax.legend(loc="lower right", frameon=True, fontsize=10)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_feature_importance(feature_names: List[str], importances: np.ndarray, model_name: str = "Random Forest", save_path: Optional[str] = None):
    """Plots feature importance bar chart."""
    feat_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(feat_df["Feature"], feat_df["Importance"], color="#1f77b4", edgecolor="#0e4d77", alpha=0.85)
    
    ax.set_title(f"Feature Importance Distribution ({model_name})", fontsize=13, weight="bold")
    ax.set_xlabel("Relative Importance Score", fontsize=11)
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.003, bar.get_y() + bar.get_height() / 2, f"{width:.3f}", va="center", fontsize=9)
        
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig


def plot_equity_and_drawdown(equity_curves: Dict[str, np.ndarray], save_path: Optional[str] = None):
    """Plots comparative cumulative equity curves and underwater drawdowns."""
    fig, (ax_eq, ax_dd) = plt.subplots(2, 1, figsize=(13, 9), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
    
    colors = {
        "Traditional Strategy": "#333333",
        "ML: Random Forest": "#2ca02c",
        "ML: Gradient Boosting": "#1f77b4",
        "ML: Logistic Regression": "#ff7f0e",
        "ML: SVM (RBF)": "#9467bd",
        "ML: MLP (Neural Net)": "#d62728",
        "ML: KNN": "#8c564b",
        "ML: Decision Tree": "#e377c2",
        "ML: Naive Bayes": "#17becf",
    }
    
    for name, equity in equity_curves.items():
        color = colors.get(name, None)
        lw = 2.4 if ("Traditional" in name or "Random Forest" in name) else 1.3
        alpha = 1.0 if ("Traditional" in name or "Random Forest" in name) else 0.75
        ls = "--" if "Traditional" in name else "-"
        
        # Equity curve
        ax_eq.plot(equity, label=name, color=color, lw=lw, alpha=alpha, linestyle=ls)
        
        # Drawdown curve
        running_max = np.maximum.accumulate(equity)
        dd = (equity - running_max) / running_max * 100.0
        ax_dd.plot(dd, label=name, color=color, lw=lw, alpha=alpha, linestyle=ls)
        
    ax_eq.set_title("Strategy Performance: Traditional vs. ML-Filtered Pairs Trading", fontsize=14, weight="bold")
    ax_eq.set_ylabel("Growth of $1.00 (Compounded)", fontsize=11)
    ax_eq.legend(loc="upper left", ncol=3, frameon=True, fontsize=9)
    
    ax_dd.set_title("Underwater Portfolio Drawdown Profile (%)", fontsize=12, weight="bold")
    ax_dd.set_xlabel("Signal Events (Chronological Out-of-Sample Trades)", fontsize=11)
    ax_dd.set_ylabel("Drawdown (%)", fontsize=11)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    return fig
