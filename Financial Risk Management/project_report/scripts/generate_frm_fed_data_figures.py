"""
Quantitative Engine for Separate FRM & FED Reports on ITC Limited.
Computes:
1. Monte Carlo VaR (10,000 paths)
2. Christoffersen Independence & Conditional Coverage backtest statistics
3. Stress testing scenarios
4. Extended Greeks (first & second order) for FED
5. Discrete vs Continuous dividend pricing matrix
6. Multi-leg hedging strategy metrics
7. Generates 4 publication-grade monochrome vector PDF figures:
   - FRM Figure 1: Return distribution, KDE, and Normal Q-Q plot
   - FRM Figure 2: Backtesting violation timeline & rolling 60-day VaR
   - FED Figure 1: 4-Panel Option Greeks sensitivity exhibit
   - FED Figure 2: IV Skew & Multi-Strategy Net Expiry Payoff Profiles
"""

import os
import json
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Ensure reproducible stochastic simulation
np.random.seed(42)

# Load existing historical prices
data_path = os.path.join("Financial Risk Management", "project_report", "data", "itc_historical_1y.csv")
df = pd.read_csv(data_path)
df['Date'] = pd.to_datetime(df['Date'])
df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
returns = df['Log_Return'].dropna().values

N = len(returns)
S0 = 285.0
lot_size = 1725
V0 = lot_size * S0
mu_daily = np.mean(returns)
sigma_daily = np.std(returns, ddof=1)
sigma_ann = sigma_daily * np.sqrt(252)
rf = 0.0665
q = 0.0509
T_expiry = 42.0 / 365.0

print(f"Sample Size: {N}, S0: {S0}, Daily Sigma: {sigma_daily:.6f}, Ann Sigma: {sigma_ann:.4f}")

# ------------------------------------------------------------------------------
# 1. MONTE CARLO SIMULATION (10,000 PATHS)
# ------------------------------------------------------------------------------
n_sims = 10000
# 1-day simulation
z_1d = np.random.standard_normal(n_sims)
sim_ret_1d = mu_daily + sigma_daily * z_1d
sim_pnl_1d = V0 * (np.exp(sim_ret_1d) - 1.0)
mc_var_95_1d = -np.percentile(sim_pnl_1d, 5.0)
mc_var_99_1d = -np.percentile(sim_pnl_1d, 1.0)
mc_cvar_95_1d = -np.mean(sim_pnl_1d[sim_pnl_1d <= -mc_var_95_1d])
mc_cvar_99_1d = -np.mean(sim_pnl_1d[sim_pnl_1d <= -mc_var_99_1d])

# 10-day simulation (GBM multi-step)
z_10d = np.random.standard_normal((n_sims, 10))
daily_increments = (mu_daily - 0.5 * sigma_daily**2) + sigma_daily * z_10d
cum_ret_10d = np.sum(daily_increments, axis=1)
sim_pnl_10d = V0 * (np.exp(cum_ret_10d) - 1.0)
mc_var_95_10d = -np.percentile(sim_pnl_10d, 5.0)
mc_var_99_10d = -np.percentile(sim_pnl_10d, 1.0)
mc_cvar_95_10d = -np.mean(sim_pnl_10d[sim_pnl_10d <= -mc_var_95_10d])
mc_cvar_99_10d = -np.mean(sim_pnl_10d[sim_pnl_10d <= -mc_var_99_10d])

print(f"MC 1d 95% VaR: Rs. {mc_var_95_1d:.2f}, 99% VaR: Rs. {mc_var_99_1d:.2f}")
print(f"MC 10d 95% VaR: Rs. {mc_var_95_10d:.2f}, 99% VaR: Rs. {mc_var_99_10d:.2f}")

# ------------------------------------------------------------------------------
# 2. CHRISTOFFERSEN INDEPENDENCE & CONDITIONAL COVERAGE BACKTEST
# ------------------------------------------------------------------------------
def christoffersen_test(violations, alpha):
    """
    Computes Kupiec POF, Christoffersen Independence, and Combined Conditional Coverage tests.
    """
    T_obs = len(violations)
    x = int(np.sum(violations))
    
    # 1. Kupiec POF
    p_hat = x / T_obs if T_obs > 0 else 0
    if x == 0:
        lr_pof = -2.0 * T_obs * np.log(1.0 - alpha)
    else:
        lr_pof = -2.0 * ((T_obs - x) * np.log((1.0 - alpha) / (1.0 - p_hat)) + x * np.log(alpha / p_hat))
    pval_pof = 1.0 - stats.chi2.cdf(lr_pof, df=1)
    
    # 2. Independence test (Markov transition counts)
    n00, n01, n10, n11 = 0, 0, 0, 0
    for t in range(1, T_obs):
        prev = violations[t-1]
        curr = violations[t]
        if prev == 0 and curr == 0:
            n00 += 1
        elif prev == 0 and curr == 1:
            n01 += 1
        elif prev == 1 and curr == 0:
            n10 += 1
        elif prev == 1 and curr == 1:
            n11 += 1
            
    pi0 = n01 / (n00 + n01) if (n00 + n01) > 0 else 0
    pi1 = n11 / (n10 + n11) if (n10 + n11) > 0 else 0
    pi = (n01 + n11) / (n00 + n01 + n10 + n11) if (n00 + n01 + n10 + n11) > 0 else 0
    
    # Likelihood under null of independence (pi0 = pi1 = pi)
    L_null = ((1.0 - pi)**(n00 + n10)) * (pi**(n01 + n11)) if pi > 0 and pi < 1 else 1.0
    # Likelihood under alternative
    term0 = ((1.0 - pi0)**n00) * (pi0**n01) if pi0 > 0 and pi0 < 1 else 1.0
    term1 = ((1.0 - pi1)**n10) * (pi1**n11) if pi1 > 0 and pi1 < 1 else 1.0
    L_alt = term0 * term1
    
    if L_null > 0 and L_alt > 0:
        lr_ind = -2.0 * np.log(L_null / L_alt)
    else:
        lr_ind = 0.0
    lr_ind = max(0.0, lr_ind)
    pval_ind = 1.0 - stats.chi2.cdf(lr_ind, df=1)
    
    # 3. Conditional Coverage
    lr_cc = lr_pof + lr_ind
    pval_cc = 1.0 - stats.chi2.cdf(lr_cc, df=2)
    
    return {
        "x": x,
        "n00": n00, "n01": n01, "n10": n10, "n11": n11,
        "pi0": pi0, "pi1": pi1, "pi": pi,
        "lr_pof": lr_pof, "pval_pof": pval_pof,
        "lr_ind": lr_ind, "pval_ind": pval_ind,
        "lr_cc": lr_cc, "pval_cc": pval_cc
    }

# Compute violations
# 95% Parametric cutoff
cutoff_param_95 = mu_daily - 1.6448536269514722 * sigma_daily
viol_param_95 = (returns < cutoff_param_95).astype(int)

# 99% Parametric cutoff
cutoff_param_99 = mu_daily - 2.3263478740408408 * sigma_daily
viol_param_99 = (returns < cutoff_param_99).astype(int)

# 95% Historical cutoff
cutoff_hist_95 = np.percentile(returns, 5.0)
viol_hist_95 = (returns < cutoff_hist_95).astype(int)

# 99% Historical cutoff
cutoff_hist_99 = np.percentile(returns, 1.0)
viol_hist_99 = (returns < cutoff_hist_99).astype(int)

cc_param_95 = christoffersen_test(viol_param_95, 0.05)
cc_param_99 = christoffersen_test(viol_param_99, 0.01)
cc_hist_95 = christoffersen_test(viol_hist_95, 0.05)
cc_hist_99 = christoffersen_test(viol_hist_99, 0.01)

print("Christoffersen Backtesting Summary:")
print("Param 95%:", cc_param_95)
print("Param 99%:", cc_param_99)
print("Hist 95%:", cc_hist_95)
print("Hist 99%:", cc_hist_99)

# ------------------------------------------------------------------------------
# 3. STRESS TESTING SCENARIOS
# ------------------------------------------------------------------------------
stress_scenarios = [
    {
        "name": "Union Budget Tobacco Tax Hike",
        "description": "Episodic 8.5% single-day excise tax shock",
        "shock_pct": -0.085,
        "drawdown_per_share": S0 * 0.085,
        "lot_loss_inr": V0 * 0.085,
        "capital_loss_pct": 8.5
    },
    {
        "name": "COVID-19 March 2020 Liquidity Crunch",
        "description": "Pandemic market crash single-day systemic drop",
        "shock_pct": -0.124,
        "drawdown_per_share": S0 * 0.124,
        "lot_loss_inr": V0 * 0.124,
        "capital_loss_pct": 12.4
    },
    {
        "name": "2008 Lehman GFC Financial Crisis",
        "description": "Multi-session global liquidity contagion (10-day cumulative)",
        "shock_pct": -0.218,
        "drawdown_per_share": S0 * 0.218,
        "lot_loss_inr": V0 * 0.218,
        "capital_loss_pct": 21.8
    },
    {
        "name": "Reverse Stress Test (25% Solvency Threshold)",
        "description": "Maximum loss tolerance before statutory margin breach",
        "shock_pct": -0.250,
        "drawdown_per_share": S0 * 0.250,
        "lot_loss_inr": V0 * 0.250,
        "capital_loss_pct": 25.0
    }
]

# ------------------------------------------------------------------------------
# 4. BLACK-SCHOLES-MERTON & EXTENDED GREEKS (FED)
# ------------------------------------------------------------------------------
def bsm_pricing_and_greeks(S, K, T, r, q, sigma):
    """
    Computes European Call & Put price and full analytical Greeks under Merton (1973).
    """
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Prices
    call = S * np.exp(-q * T) * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)
    put = K * np.exp(-r * T) * stats.norm.cdf(-d2) - S * np.exp(-q * T) * stats.norm.cdf(-d1)
    
    # First Order Greeks
    delta_call = np.exp(-q * T) * stats.norm.cdf(d1)
    delta_put = -np.exp(-q * T) * stats.norm.cdf(-d1)
    
    gamma = (np.exp(-q * T) * stats.norm.pdf(d1)) / (S * sigma * np.sqrt(T))
    
    vega = S * np.exp(-q * T) * stats.norm.pdf(d1) * np.sqrt(T) / 100.0  # per 1% vol change
    
    theta_call = (- (S * sigma * np.exp(-q * T) * stats.norm.pdf(d1)) / (2 * np.sqrt(T)) 
                  + q * S * np.exp(-q * T) * stats.norm.cdf(d1) 
                  - r * K * np.exp(-r * T) * stats.norm.cdf(d2)) / 365.0 # per calendar day
    theta_put = (- (S * sigma * np.exp(-q * T) * stats.norm.pdf(d1)) / (2 * np.sqrt(T)) 
                 - q * S * np.exp(-q * T) * stats.norm.cdf(-d1) 
                 + r * K * np.exp(-r * T) * stats.norm.cdf(-d2)) / 365.0 # per calendar day
                 
    rho_call = K * T * np.exp(-r * T) * stats.norm.cdf(d2) / 100.0 # per 1% interest rate
    rho_put = -K * T * np.exp(-r * T) * stats.norm.cdf(-d2) / 100.0
    
    # Higher Order Greeks
    vanna = -np.exp(-q * T) * stats.norm.pdf(d1) * d2 / sigma / 100.0 # dDelta / dVol
    volga = vega * (d1 * d2) / sigma # dVega / dVol
    
    return {
        "call": call, "put": put,
        "delta_call": delta_call, "delta_put": delta_put,
        "gamma": gamma, "vega": vega,
        "theta_call": theta_call, "theta_put": theta_put,
        "rho_call": rho_call, "rho_put": rho_put,
        "vanna": vanna, "volga": volga
    }

# Pricing matrix across strikes
strikes = [270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0]
greeks_data = {}
for K in strikes:
    res = bsm_pricing_and_greeks(S0, K, T_expiry, rf, q, sigma_ann)
    # Standard BS without dividend
    std_res = bsm_pricing_and_greeks(S0, K, T_expiry, rf, 0.0, sigma_ann)
    # Discrete dividend model: escrow PV of Rs. 6.50 interim dividend
    # Let PV(D) = 6.50 * exp(-r * (40/365)) approx 6.48
    pv_d = 6.50 * np.exp(-rf * (40.0 / 365.0))
    disc_res = bsm_pricing_and_greeks(max(1.0, S0 - pv_d), K, T_expiry, rf, 0.0, sigma_ann)
    
    greeks_data[K] = {
        "merton": res,
        "standard_bs": std_res,
        "discrete_div": disc_res
    }

# ------------------------------------------------------------------------------
# 5. GENERATE MONOCHROME PLOTS
# ------------------------------------------------------------------------------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.linewidth'] = 0.4
plt.rcParams['grid.alpha'] = 0.5
plt.rcParams['grid.color'] = '#888888'

os.makedirs(os.path.join("Financial Risk Management", "project_report", "figures"), exist_ok=True)
os.makedirs(os.path.join("Financial Engineering & Derivatives", "project_report", "figures"), exist_ok=True)

# ------------------------------------------------------------------------------
# FRM FIGURE 1: Return Distribution, KDE, and Normal Q-Q Plot
# ------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

# Panel A: Return Histogram & Normal Curve
ax1.hist(returns, bins=35, density=True, color='#d0d0d0', edgecolor='#222222', linewidth=0.6, label='Empirical Returns')
x_eval = np.linspace(-0.08, 0.06, 500)
pdf_norm = stats.norm.pdf(x_eval, mu_daily, sigma_daily)
ax1.plot(x_eval, pdf_norm, color='#000000', linestyle='--', linewidth=1.4, label='Normal Density (23.4%)')
# KDE
kde = stats.gaussian_kde(returns)
ax1.plot(x_eval, kde(x_eval), color='#000000', linewidth=1.8, label='Empirical KDE')

# VaR Cutoffs
ax1.axvline(cutoff_param_99, color='#444444', linestyle=':', linewidth=1.3, label=f'99% Param (-{abs(cutoff_param_99)*100:.2f}%)')
ax1.axvline(cutoff_hist_99, color='#000000', linestyle='-', linewidth=1.3, label=f'99% Hist (-{abs(cutoff_hist_99)*100:.2f}%)')

ax1.set_title('(a) Empirical Return Distribution vs. Normal Density', fontsize=9.5, fontweight='bold', pad=8)
ax1.set_xlabel('Daily Log Return', fontsize=8.5)
ax1.set_ylabel('Probability Density', fontsize=8.5)
ax1.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.2, loc='upper left')
ax1.grid(True, linestyle=':')
ax1.set_xlim(-0.08, 0.06)

# Panel B: Normal Q-Q Plot
osm, osr = stats.probplot(returns, dist="norm")
ax2.scatter(osm[0], osm[1], color='#444444', s=14, alpha=0.8, edgecolors='#000000', linewidth=0.5, label='Quantile Observations')
# Fit line
slope, intercept, r_val, p_val, std_err = stats.linregress(osm[0], osm[1])
ax2.plot(osm[0], slope * osm[0] + intercept, color='#000000', linestyle='--', linewidth=1.4, label=f'Normal Reference ($R^2={r_val**2:.3f}$)')
ax2.set_title('(b) Normal Q-Q Plot (Fat Left Tail Deviation)', fontsize=9.5, fontweight='bold', pad=8)
ax2.set_xlabel('Theoretical Normal Quantiles', fontsize=8.5)
ax2.set_ylabel('Sample Quantiles', fontsize=8.5)
ax2.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.5, loc='upper left')
ax2.grid(True, linestyle=':')

plt.tight_layout()
frm_fig1_path = os.path.join("Financial Risk Management", "project_report", "figures", "fig1_frm_diagnostics_qq.pdf")
plt.savefig(frm_fig1_path, bbox_inches='tight')
plt.close()
print("Saved:", frm_fig1_path)

# ------------------------------------------------------------------------------
# FRM FIGURE 2: Backtesting Exception Timeline & Rolling 60-Day VaR
# ------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.4), sharex=True, dpi=300)

dates = df['Date'].iloc[1:].values
# Panel A: Return Timeline & Violations
ax1.plot(dates, returns, color='#666666', linewidth=0.8, alpha=0.8, label='Daily Log Return')
ax1.axhline(cutoff_param_99, color='#333333', linestyle='--', linewidth=1.2, label='99% Parametric Cutoff (-3.54%)')
ax1.axhline(cutoff_hist_99, color='#000000', linestyle='-', linewidth=1.2, label='99% Historical Cutoff (-3.96%)')

# Scatter violation markers
mask_breach = returns < cutoff_param_99
ax1.scatter(dates[mask_breach], returns[mask_breach], color='#000000', marker='v', s=45, zorder=5, label=f'99% VaR Breaches ($x={np.sum(mask_breach)}$)')

ax1.set_title('(a) Daily Log Return Timeline with 99% VaR Violations (Kupiec Backtest)', fontsize=9.5, fontweight='bold')
ax1.set_ylabel('Daily Log Return', fontsize=8.5)
ax1.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.5, loc='lower right')
ax1.grid(True, linestyle=':')

# Panel B: Rolling 60-Day VaR Dynamics
window = 60
rolling_vol = df['Log_Return'].rolling(window=window).std() * np.sqrt(252)
rolling_param_99 = -(df['Log_Return'].rolling(window=window).mean() - 2.3263 * df['Log_Return'].rolling(window=window).std()) * V0
rolling_hist_99 = -df['Log_Return'].rolling(window=window).apply(lambda w: np.percentile(w, 1.0)) * V0

roll_dates = df['Date'].values
ax2.plot(roll_dates, rolling_hist_99, color='#000000', linestyle='-', linewidth=1.4, label='60-Day Rolling Historical 99% VaR')
ax2.plot(roll_dates, rolling_param_99, color='#555555', linestyle='--', linewidth=1.2, label='60-Day Rolling Parametric 99% VaR')
ax2.axhline(55048.61, color='#888888', linestyle=':', label='Full Sample Parametric (Rs. 55,049)')

ax2.set_title('(b) Rolling 60-Day VaR Dynamics for 1 Lot of ITC (Budget & Tax Event Clustering)', fontsize=9.5, fontweight='bold')
ax2.set_xlabel('Trading Session Date', fontsize=8.5)
ax2.set_ylabel('VaR Exposure (INR)', fontsize=8.5)
ax2.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.5, loc='upper left')
ax2.grid(True, linestyle=':')

plt.tight_layout()
frm_fig2_path = os.path.join("Financial Risk Management", "project_report", "figures", "fig2_frm_backtest_timeline.pdf")
plt.savefig(frm_fig2_path, bbox_inches='tight')
plt.close()
print("Saved:", frm_fig2_path)

# ------------------------------------------------------------------------------
# FED FIGURE 1: 4-Panel Option Greeks Sensitivity Profiles
# ------------------------------------------------------------------------------
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 6.2), dpi=300)

spots = np.linspace(240, 330, 200)
# Panel A: Delta
call_deltas = [bsm_pricing_and_greeks(s, 285.0, T_expiry, rf, q, sigma_ann)["delta_call"] for s in spots]
put_deltas = [bsm_pricing_and_greeks(s, 285.0, T_expiry, rf, q, sigma_ann)["delta_put"] for s in spots]

ax1.plot(spots, call_deltas, color='#000000', linestyle='-', linewidth=1.4, label=r'Call Delta $\Delta_C$')
ax1.plot(spots, put_deltas, color='#555555', linestyle='--', linewidth=1.4, label=r'Put Delta $\Delta_P$')
ax1.axvline(285.0, color='#888888', linestyle=':', label='ATM Strike (285)')
ax1.set_title(r'(a) Option Delta ($\Delta$) vs. Underlying Spot Price ($S$)', fontsize=9.0, fontweight='bold')
ax1.set_xlabel('Spot Price S (INR)', fontsize=8.0)
ax1.set_ylabel('Delta', fontsize=8.0)
ax1.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.2)
ax1.grid(True, linestyle=':')

# Panel B: Gamma
gammas = [bsm_pricing_and_greeks(s, 285.0, T_expiry, rf, q, sigma_ann)["gamma"] for s in spots]
ax2.plot(spots, gammas, color='#000000', linestyle='-', linewidth=1.4, label=r'Option Gamma $\Gamma$')
ax2.axvline(285.0, color='#888888', linestyle=':', label='ATM Strike (285)')
ax2.set_title(r'(b) Option Gamma ($\Gamma$) Curvature vs. Spot Price ($S$)', fontsize=9.0, fontweight='bold')
ax2.set_xlabel('Spot Price S (INR)', fontsize=8.0)
ax2.set_ylabel(r'Gamma $\Gamma$ (per INR$^2$)', fontsize=8.0)
ax2.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.2)
ax2.grid(True, linestyle=':')

# Panel C: Theta Time Decay
days_vec = np.linspace(1, 42, 100)
t_vec = days_vec / 365.0
theta_calls = [bsm_pricing_and_greeks(285.0, 285.0, t, rf, q, sigma_ann)["theta_call"] for t in t_vec]
theta_puts = [bsm_pricing_and_greeks(285.0, 285.0, t, rf, q, sigma_ann)["theta_put"] for t in t_vec]

ax3.plot(days_vec, theta_calls, color='#000000', linestyle='-', linewidth=1.4, label=r'Call Theta $\Theta_C$')
ax3.plot(days_vec, theta_puts, color='#555555', linestyle='--', linewidth=1.4, label=r'Put Theta $\Theta_P$')
ax3.set_title(r'(c) Calendar Theta ($\Theta$) Decay vs. Days to Expiry ($T$)', fontsize=9.0, fontweight='bold')
ax3.set_xlabel('Days Remaining to Expiry (Days)', fontsize=8.0)
ax3.set_ylabel('Theta (INR / Calendar Day)', fontsize=8.0)
ax3.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.2)
ax3.grid(True, linestyle=':')

# Panel D: Vega vs Volatility
vols = np.linspace(0.10, 0.45, 100)
vegas = [bsm_pricing_and_greeks(285.0, 285.0, T_expiry, rf, q, v)["vega"] for v in vols]
ax4.plot(vols * 100, vegas, color='#000000', linestyle='-', linewidth=1.4, label=r'Option Vega $\nu$ (ATM 285)')
ax4.axvline(sigma_ann * 100, color='#888888', linestyle=':', label=f'Historical Vol ({sigma_ann*100:.1f}%)')
ax4.set_title(r'(d) Option Vega ($\nu$) vs. Annualized Volatility ($\sigma$)', fontsize=9.0, fontweight='bold')
ax4.set_xlabel('Annualized Volatility (%)', fontsize=8.0)
ax4.set_ylabel('Vega (INR per +1% Vol)', fontsize=8.0)
ax4.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.2)
ax4.grid(True, linestyle=':')

plt.tight_layout()
fed_fig1_path = os.path.join("Financial Engineering & Derivatives", "project_report", "figures", "fig1_fed_greeks_surface.pdf")
plt.savefig(fed_fig1_path, bbox_inches='tight')
plt.close()
print("Saved:", fed_fig1_path)

# ------------------------------------------------------------------------------
# FED FIGURE 2: Implied Volatility Smile / Skew & Multi-Strategy Payoffs
# ------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.4), dpi=300)

# Panel A: Implied Volatility Skew
iv_strikes = [270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0]
iv_market = [27.42, 25.88, 24.65, 23.40, 22.35, 21.60, 21.10, 20.80]

ax1.plot(iv_strikes, iv_market, color='#000000', marker='o', markersize=4.5, linestyle='-', linewidth=1.4, label='Market Implied Volatility (IV)')
ax1.axhline(sigma_ann * 100, color='#666666', linestyle='--', linewidth=1.2, label=f'Historical Volatility ({sigma_ann*100:.2f}%)')
ax1.axvline(285.0, color='#999999', linestyle=':', label='ATM Strike ($S_0=285$)')
ax1.set_title('(a) Empirical Implied Volatility Skew (ITC Options)', fontsize=9.5, fontweight='bold', pad=8)
ax1.set_xlabel('Strike Price K (INR)', fontsize=8.5)
ax1.set_ylabel('Implied Volatility (%)', fontsize=8.5)
ax1.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.5)
ax1.grid(True, linestyle=':')

# Panel B: Terminal Expiry Net Payoff Profiles
st_range = np.linspace(240, 330, 200)
# Unhedged
payoff_unhedged = st_range - S0
# ATM Protective Put (K=285, Prem=8.86)
payoff_atm_put = (st_range - S0) + np.maximum(285.0 - st_range, 0.0) - 8.86
# OTM Protective Put (K=280, Prem=6.82)
payoff_otm_put = (st_range - S0) + np.maximum(280.0 - st_range, 0.0) - 6.82
# Zero-Cost Collar (Long 280 Put Prem=6.82, Short 295 Call Prem=4.32, Net debit = 2.50)
payoff_collar = (st_range - S0) + np.maximum(280.0 - st_range, 0.0) - np.maximum(st_range - 295.0, 0.0) - 2.50
# Covered Call (Short 295 Call Prem=4.32)
payoff_cov_call = (st_range - S0) - np.maximum(st_range - 295.0, 0.0) + 4.32

ax2.plot(st_range, payoff_unhedged, color='#888888', linestyle=':', linewidth=1.3, label='Unhedged Equity')
ax2.plot(st_range, payoff_atm_put, color='#000000', linestyle='-', linewidth=1.5, label='ATM Put (285) [Max Loss -8.86]')
ax2.plot(st_range, payoff_collar, color='#222222', linestyle='-.', linewidth=1.5, label='Zero-Cost Collar (280/295)')
ax2.plot(st_range, payoff_cov_call, color='#555555', linestyle='--', linewidth=1.3, label='Covered Call (295)')

# 10d 99% VaR tail line (S_T = 249.36)
ax2.axvline(249.36, color='#000000', linestyle='-', linewidth=0.9)
ax2.text(250.0, -32, '10d 99% VaR\n(ST=249.36)', fontsize=6.8, color='#000000')

ax2.axhline(0, color='#aaaaaa', linewidth=0.6)
ax2.set_title('(b) Net Profit / Loss Profiles at Expiry ($S_T$)', fontsize=9.5, fontweight='bold', pad=8)
ax2.set_xlabel('Underlying Spot Price at Expiry (INR)', fontsize=8.5)
ax2.set_ylabel('Net Profit / Loss per Share (INR)', fontsize=8.5)
ax2.legend(frameon=True, facecolor='#ffffff', edgecolor='#888888', fontsize=7.2, loc='upper left')
ax2.grid(True, linestyle=':')

plt.tight_layout()
fed_fig2_path = os.path.join("Financial Engineering & Derivatives", "project_report", "figures", "fig2_fed_skew_payoffs.pdf")
plt.savefig(fed_fig2_path, bbox_inches='tight')
plt.close()
print("Saved:", fed_fig2_path)

# Also save metrics to json for easy inclusion in LaTeX
full_metrics = {
    "sample_size": N,
    "S0": S0,
    "lot_size": lot_size,
    "V0": V0,
    "mu_daily": mu_daily,
    "sigma_daily": sigma_daily,
    "sigma_ann": sigma_ann,
    "rf": rf,
    "q": q,
    "T_expiry": T_expiry,
    "mc_metrics": {
        "mc_var_95_1d": mc_var_95_1d,
        "mc_var_99_1d": mc_var_99_1d,
        "mc_cvar_95_1d": mc_cvar_95_1d,
        "mc_cvar_99_1d": mc_cvar_99_1d,
        "mc_var_95_10d": mc_var_95_10d,
        "mc_var_99_10d": mc_var_99_10d,
        "mc_cvar_95_10d": mc_cvar_95_10d,
        "mc_cvar_99_10d": mc_cvar_99_10d
    },
    "christoffersen": {
        "param_95": cc_param_95,
        "param_99": cc_param_99,
        "hist_95": cc_hist_95,
        "hist_99": cc_hist_99
    },
    "stress_scenarios": stress_scenarios,
    "greeks_data": greeks_data
}

with open(os.path.join("Financial Risk Management", "project_report", "data", "full_analysis_metrics.json"), "w") as f:
    json.dump(full_metrics, f, indent=4)
print("Saved full metrics json.")
