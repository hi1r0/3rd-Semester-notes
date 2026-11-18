"""
Generate Consolidated Greyscale Figures for Condensed Academic Paper
Author: Quantitative Finance Research Team
Pondicherry University (MSQF 533)
"""

import os
import json
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.style.use('default')
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10.5,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8.5,
    'legend.fontsize': 8,
    'figure.titlesize': 11.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'lines.linewidth': 1.4,
    'grid.color': '#D0D0D0',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'image.cmap': 'gray'
})

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_FIG_DIR = os.path.join(BASE_DIR, "condensed_paper", "figures")
os.makedirs(OUTPUT_FIG_DIR, exist_ok=True)

# Load metrics
with open(os.path.join(DATA_DIR, "itc_analysis_metrics.json"), "r") as f:
    metrics = json.load(f)

# Load historical data
df = pd.read_csv(os.path.join(DATA_DIR, "itc_historical_1y.csv"), index_col=0, parse_dates=True)
df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
returns = df['Log_Return'].dropna()

S0 = metrics['spot_price']
lot_size = metrics['lot_size']
vol_annual = metrics['annual_volatility']
mean_daily = metrics['mean_daily_return']
std_daily = metrics['std_daily']

var_param_95 = metrics['var_metrics']['param_95_1d_pct']
var_param_99 = metrics['var_metrics']['param_99_1d_pct']
var_hist_95  = metrics['var_metrics']['hist_95_1d_pct']
var_hist_99  = metrics['var_metrics']['hist_99_1d_pct']

# Save dual PDF & PNG helper
def save_dual(fig, filename):
    pdf_p = os.path.join(OUTPUT_FIG_DIR, f"{filename}.pdf")
    png_p = os.path.join(OUTPUT_FIG_DIR, f"{filename}.png")
    fig.savefig(pdf_p, format="pdf", bbox_inches="tight")
    fig.savefig(png_p, format="png", bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Generated: {filename}.pdf & .png")

# ------------------------------------------------------------------------------
# Figure 1: 2-Panel Return Distribution & Kupiec Backtesting Timeline
# ------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.8))

# Panel A: Return Distribution
count, bins, ignored = ax1.hist(returns, bins=30, density=True, color='#D8D8D8', edgecolor='black', linewidth=0.7, label='Empirical Returns')
x_ax = np.linspace(returns.min() - 0.005, returns.max() + 0.005, 250)
fitted_norm = stats.norm.pdf(x_ax, mean_daily, std_daily)
ax1.plot(x_ax, fitted_norm, color='black', linewidth=1.6, linestyle='-', label=f'Normal (sigma={vol_annual:.1%})')
ax1.axvline(-var_param_95, color='#606060', linestyle='--', linewidth=1.3, label=f'95% Param ({var_param_95:.2%})')
ax1.axvline(-var_hist_99, color='black', linestyle=':', linewidth=1.6, label=f'99% Hist ({var_hist_99:.2%})')
ax1.set_title('(a) Return Distribution vs. Normal Density', fontweight='bold')
ax1.set_xlabel('Daily Log Return')
ax1.set_ylabel('Probability Density')
ax1.legend(loc='upper right', frameon=True, edgecolor='#A0A0A0')
ax1.grid(True)

# Panel B: Kupiec Backtest Timeline
ax2.plot(returns.index, returns, color='#606060', linewidth=0.9, alpha=0.85, label='Daily Returns')
ax2.axhline(-var_param_95, color='#808080', linestyle='--', linewidth=1.1, label=f'95% VaR Bound (-{var_param_95:.2%})')
ax2.axhline(-var_param_99, color='black', linestyle='-', linewidth=1.3, label=f'99% VaR Bound (-{var_param_99:.2%})')

breach_mask_95 = returns < -var_param_95
breach_mask_99 = returns < -var_param_99
ax2.scatter(returns.index[breach_mask_95], returns[breach_mask_95], color='white', edgecolor='#404040', s=35, marker='o', linewidth=1.3, zorder=5, label='95% Breaches (x=9)')
ax2.scatter(returns.index[breach_mask_99], returns[breach_mask_99], color='black', s=45, marker='x', linewidth=1.6, zorder=6, label='99% Breaches (x=4)')

ax2.set_title('(b) Kupiec Backtesting Exception Events', fontweight='bold')
ax2.set_ylabel('Daily Return')
ax2.set_xlabel('Date')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %y'))
ax2.legend(loc='lower left', frameon=True, edgecolor='#A0A0A0')
ax2.grid(True)

plt.tight_layout()
save_dual(fig, "fig1_diagnostics_backtest")

# ------------------------------------------------------------------------------
# Figure 2: 2-Panel Option Volatility Smile & Greeks Sensitivity Profiles
# ------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.8))

pricing_records = metrics['option_pricing_records']
strikes_arr = [r['strike'] for r in pricing_records]
iv_put_arr  = [r['iv_put'] * 100.0 for r in pricing_records]
iv_call_arr = [r['iv_call'] * 100.0 for r in pricing_records]
hist_vol_arr = [vol_annual * 100.0] * len(strikes_arr)

# Panel A: Volatility Smile
ax1.plot(strikes_arr, iv_put_arr, marker='s', markersize=5, color='black', linestyle='-', linewidth=1.6, label='Put Implied Vol (IV)')
ax1.plot(strikes_arr, iv_call_arr, marker='o', markersize=5, color='#606060', linestyle='--', linewidth=1.4, label='Call Implied Vol (IV)')
ax1.plot(strikes_arr, hist_vol_arr, color='#909090', linestyle=':', linewidth=1.4, label=f'Historical Vol ({vol_annual:.1%})')
ax1.axvline(S0, color='#606060', linestyle='-.', linewidth=0.9, label=f'ATM Spot (Rs.{S0:.0f})')
ax1.set_title('(a) Implied Volatility Smile / Skew', fontweight='bold')
ax1.set_xlabel('Option Strike Price (INR)')
ax1.set_ylabel('Annualized Volatility (%)')
ax1.set_xticks(strikes_arr)
ax1.legend(loc='upper right', frameon=True, edgecolor='#A0A0A0')
ax1.grid(True)

# Panel B: Delta & Gamma Greeks
s_sim = np.linspace(240.0, 330.0, 150)
T = metrics['time_to_expiry_years']
r = metrics['risk_free_rate']
q = metrics['dividend_yield']

def bs_greeks(S, K, T, r, q, sigma):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    nd1 = stats.norm.pdf(d1)
    delta_call = np.exp(-q * T) * stats.norm.cdf(d1)
    delta_put = -np.exp(-q * T) * stats.norm.cdf(-d1)
    gamma = (np.exp(-q * T) * nd1) / (S * sigma * np.sqrt(T))
    return delta_call, delta_put, gamma

deltas_c = []
deltas_p = []
gammas   = []
for s in s_sim:
    dc, dp, gm = bs_greeks(s, 285.0, T, r, q, vol_annual)
    deltas_c.append(dc)
    deltas_p.append(dp)
    gammas.append(gm * 50.0)  # scale gamma for visual overlay

ax2.plot(s_sim, deltas_c, color='black', linestyle='-', linewidth=1.5, label=r'Call $\Delta$')
ax2.plot(s_sim, deltas_p, color='#505050', linestyle='--', linewidth=1.5, label=r'Put $\Delta$')
ax2.plot(s_sim, gammas, color='#808080', linestyle=':', linewidth=1.5, label=r'Gamma $\Gamma$ ($\times 50$)')
ax2.axvline(285.0, color='#909090', linestyle='-.', linewidth=0.9, label='ATM Strike (Rs.285)')
ax2.set_title(r'(b) Option Delta ($\Delta$) and Gamma ($\Gamma$)', fontweight='bold')
ax2.set_xlabel('Spot Price (INR)')
ax2.set_ylabel(r'Sensitivity Magnitude')
ax2.legend(loc='center left', frameon=True, edgecolor='#A0A0A0')
ax2.grid(True)

plt.tight_layout()
save_dual(fig, "fig2_volatility_greeks")

# ------------------------------------------------------------------------------
# Figure 3: Comparative Hedging Payoffs & Downside Capital Floor
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.8, 4.2))

atm_put_price = 8.86
otm_put_price = 6.82
otm_call_price = 4.32
net_collar_cost = otm_put_price - otm_call_price  # Rs 2.50
st_var_10d_99 = metrics['hedging_summary']['st_var_10d_99']

st_range = np.linspace(240.0, 330.0, 250)
pl_unhedged = st_range - S0
pl_atm_prot_put = (st_range - S0) + np.maximum(285.0 - st_range, 0.0) - atm_put_price
pl_otm_prot_put = (st_range - S0) + np.maximum(280.0 - st_range, 0.0) - otm_put_price
pl_collar = (st_range - S0) + np.maximum(280.0 - st_range, 0.0) - np.maximum(st_range - 295.0, 0.0) - net_collar_cost

ax.plot(st_range, pl_unhedged, color='#A0A0A0', linestyle=':', linewidth=1.6, label='Unhedged Stock ($S_T - S_0$)')
ax.plot(st_range, pl_atm_prot_put, color='black', linestyle='-', linewidth=1.8, label=f'ATM Protective Put (K=285, Prem=Rs.{atm_put_price:.2f})')
ax.plot(st_range, pl_otm_prot_put, color='#505050', linestyle='--', linewidth=1.6, label=f'OTM Protective Put (K=280, Prem=Rs.{otm_put_price:.2f})')
ax.plot(st_range, pl_collar, color='#202020', linestyle='-.', linewidth=1.6, label=f'Zero-Cost Collar (Put 280 / Call 295, Net=Rs.{net_collar_cost:.2f})')

ax.axhline(0.0, color='#B0B0B0', linestyle='-', linewidth=0.7)
ax.axvline(S0, color='#B0B0B0', linestyle='--', linewidth=0.7)
ax.axvline(st_var_10d_99, color='black', linestyle=':', linewidth=1.2, label=f'10d 99% VaR Horizon (Rs.{st_var_10d_99:.1f})')

ax.set_title('Figure 3: Comparative Net Payoff Profiles Across Derivative Hedging Strategies at Expiry', fontweight='bold')
ax.set_xlabel('Underlying ITC Spot Price at Expiry $S_T$ (INR)')
ax.set_ylabel('Net Profit / Loss per Share (INR)')
ax.legend(loc='upper left', frameon=True, edgecolor='#A0A0A0')
ax.grid(True)
plt.tight_layout()
save_dual(fig, "fig3_hedging_payoffs")

print("--- All 3 Consolidated Figures Successfully Rendered ---")
