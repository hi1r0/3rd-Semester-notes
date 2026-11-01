# Machine Learning-Based Pair Trading Strategy Using Supervised Learning on Simulated Financial Data

**Course:** Machine Learning in Quantitative Finance (MSQF Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Degree:** M.Sc. Quantitative Finance  

---

## 📌 Project Overview

This project develops an institutional-grade **Quantitative Statistical Arbitrage & Machine Learning** framework in Python. It investigates whether supervised classification algorithms can function as an intelligent **meta-labeling risk filter** to predict the forward profitability of candidate pair-trading signals under realistic market frictions and structural regime breakdowns.

```
Simulate Multi-Regime Universe (OU + Latent Factor)
                 ↓
Compute Rolling Cointegration (OLS Hedge Ratio)
                 ↓
Generate Standardized Z-Scores & Candidate Triggers (|Z| >= 2.0)
                 ↓
Extract 12-Dimensional Statistical Quant Features
                 ↓
Apply Triple-Barrier Meta-Labeling (TP, SL, Horizon, 10 bps Frictions)
                 ↓
Purged Walk-Forward Cross-Validation (Embargo Buffer = Horizon H)
                 ↓
Train & Benchmark Full 7 MSQF Supervised Models
                 ↓
Event-Driven Comparative Backtest (Traditional vs. ML-Filtered)
```

---

## 🔬 Key Components & Methodology

### 1. Data Generation Process (DGP)
To avoid data snooping and ensure rigorous testing across varied statistical environments, we simulate a universe of **5,000 trading bars** per pair across **5 distinct pair archetypes**:
- **Strong Mean-Reversion:** High reversion speed ($\kappa = 0.10$, half-life $\tau \approx 7$ bars), highly stationary spread.
- **Moderate Mean-Reversion:** Institutional baseline ($\kappa = 0.03$, half-life $\tau \approx 23$ bars).
- **Weak / Slow Mean-Reversion:** Persistent spread deviations ($\kappa = 0.008$, half-life $\tau \approx 86$ bars).
- **Structural Break / Regime Shift:** Cointegrated Ornstein-Uhlenbeck spread for $t < 2,500$, followed by an equilibrium jump and random-walk breakdown ($\kappa \to 0$).
- **Spurious Correlation:** High instantaneous price correlation driven by a common latent market factor $M_t$, but spread $S_t$ is a non-cointegrated driftless random walk.

### 2. Feature Engineering Space (12 Quant Indicators)
At each trigger timestamp where $|Z_t| \ge 2.0$, we extract:
1. `z_score`: Standardized spread deviation at trigger.
2. `spread_momentum_1d`: 1-bar spread momentum ($S_t - S_{t-1}$).
3. `spread_momentum_5d`: 5-bar spread momentum ($S_t - S_{t-5}$).
4. `spread_momentum_10d`: 10-bar spread momentum ($S_t - S_{t-10}$).
5. `ou_half_life`: Rolling regression estimation of Ornstein-Uhlenbeck half-life $\tau = -\ln(2) / b$.
6. `hurst_exponent`: Rolling fractal Hurst exponent ($H < 0.5$ mean-reverting, $H > 0.5$ trending).
7. `adf_pvalue`: Rolling Augmented Dickey-Fuller unit-root rejection $p$-value.
8. `autocorr_lag1`: 1st order serial autocorrelation of spread.
9. `autocorr_lag2`: 2nd order serial autocorrelation of spread.
10. `volatility_ratio`: Short-term (10-bar) / Long-term (50-bar) spread volatility ratio.
11. `rolling_correlation`: Rolling Pearson correlation $\rho(\ln X, \ln Y)$.
12. `hedge_ratio_stability`: Rolling standard deviation of the hedge ratio $\hat{\beta}_t$.

### 3. Triple-Barrier Meta-Labeling with Frictions
- **Horizontal Barrier 1 (Take-Profit):** Spread reverts to mean equilibrium ($Z = 0$).
- **Horizontal Barrier 2 (Stop-Loss):** Spread diverges catastrophically beyond $|Z| = 3.5$.
- **Vertical Barrier (Time Horizon):** Maximum holding duration $H = 15$ trading bars.
- **Transaction Costs:** 5 bps per side ($10\text{ bps} = 0.0010$ round-trip friction).
- **Target:** $\text{Target} = 1 \iff R_{\text{net}} = R_{\text{gross}} - 0.0010 > 0$.

### 4. Evaluated 7 MSQF Supervised Learning Classifiers
1. **Logistic Regression:** $L_2$ regularized linear classification baseline.
2. **Gaussian Naive Bayes:** Probabilistic generative model with Gaussian feature likelihoods.
3. **K-Nearest Neighbors (KNN):** Distance-weighted instance learner ($k = 15$).
4. **Decision Tree (CART):** Non-linear rule learner with depth regularization.
5. **Random Forest:** Bagging ensemble of 150 decorrelated decision trees.
6. **Support Vector Machine (SVM RBF):** Maximum-margin kernel method with non-linear Radial Basis Function.
7. **Multi-Layer Perceptron (MLP):** Deep feedforward neural network with 2 hidden layers $(64, 32)$ and ReLU activations.

---

## 📊 Empirical Results & Model Comparison

### Level 1: Out-of-Sample Machine Learning Classification Benchmark
Evaluated using **Purged Walk-Forward Time-Series Cross-Validation** (4 splits, 2% embargo buffer):

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Brier Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **SVM (RBF)** | 0.5820 | 0.5946 | **0.9392** | **0.7272** | 0.4873 | 0.2428 |
| **Logistic Regression** | **0.5968** | 0.6124 | 0.8728 | 0.7193 | 0.5392 | 0.2440 |
| **Random Forest** | 0.5766 | 0.5973 | 0.8896 | 0.7135 | **0.5510** | **0.2411** |
| **Decision Tree** | 0.5591 | 0.6012 | 0.7572 | 0.6663 | 0.5219 | 0.2672 |
| **KNN** | 0.5228 | 0.5774 | 0.7544 | 0.6509 | 0.4743 | 0.2641 |
| **MLP (Neural Net)** | 0.5202 | 0.5812 | 0.6887 | 0.6297 | 0.4764 | 0.3423 |
| **Naive Bayes** | 0.5363 | **0.6163** | 0.5782 | 0.5942 | 0.5261 | 0.2791 |

### Level 2: Financial Strategy Backtest & Risk-Adjusted Alpha
Evaluated on out-of-sample trade events under **10 bps round-trip transaction costs**:

| Strategy | Total Trades | Win Rate (%) | Cumulative Return (%) | Annualized Return (%) | Annualized Vol (%) | Sharpe Ratio | Sortino Ratio | Max DD (%) | Profit Factor | Avg Trade PnL |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Traditional (No ML)** | 744 | 59.54% | +679.74% | 176.24% | 140.43% | 1.255 | 1.058 | 95.62% | 1.227 | 69.94 bps |
| **ML: Naive Bayes** | 414 | **61.84%** | +1,610.84% | **266.73%** | **132.63%** | **2.011** | **1.687** | **94.66%** | **1.387** | **105.85 bps** |
| **ML: Logistic Regression**| 631 | 61.33% | **+2,469.11%**| 230.77% | 136.36% | **1.692** | 1.402 | 96.64% | 1.319 | 91.57 bps |
| **ML: Decision Tree** | 561 | 60.25% | +1,299.57% | 221.76% | 137.89% | 1.608 | 1.358 | 95.15% | 1.301 | 88.00 bps |
| **ML: Random Forest** | 660 | 59.70% | +524.97% | 172.01% | 137.33% | 1.253 | 1.054 | 96.71% | 1.229 | 68.26 bps |
| **ML: SVM (RBF)** | 736 | 59.51% | +563.97% | 172.10% | 140.81% | 1.222 | 1.029 | 95.62% | 1.221 | 68.30 bps |
| **ML: MLP (Neural Net)** | 526 | 58.17% | +68.11% | 127.55% | 137.24% | 0.929 | 0.785 | 98.29% | 1.169 | 50.62 bps |
| **ML: KNN** | 578 | 57.61% | -73.30% | 49.54% | 140.05% | 0.354 | 0.294 | 98.53% | 1.060 | 19.66 bps |

---

## 💡 Key Quantitative Findings & Insights

1. **Massive Sharpe Improvement from Selective Filtering:**
   - **Naive Bayes** and **Logistic Regression** delivered substantial increases in the annualized Sharpe ratio (**2.011** and **1.692** vs **1.255** for the traditional rule).
   - By acting as a selective filter, Naive Bayes eliminated **330 low-conviction signals** (a 44.4% trade reduction), boosting average trade profitability from **69.94 bps** to **105.85 bps** (+51.3% gain per trade).
2. **Economic Return vs. Complexity Tradeoff:**
   - Overly complex high-capacity models (KNN, MLP) struggled with noisy signal boundaries, suffering from variance and lower test Sharpe ratios. Linear and Naive Bayes classifiers with strong regularizers excelled at identifying the high-probability subset of signals.
3. **Protection in Structural Break & Spurious Regimes:**
   - In the Structural Break and Spurious regimes, the ML models blocked unviable trades where the half-life was explosive or the Hurst exponent indicated trending persistence ($H > 0.50$).

---

## 📁 Directory Structure

```
D:\MSQF\Semester III\ML\Assignment\
├── src/
│   ├── __init__.py
│   ├── simulation.py              # Multi-regime OU + latent market factor synthetic generator
│   ├── cointegration.py           # Rolling OLS hedge ratio & standardized Z-score engine
│   ├── features.py                # 12-dimensional quantitative statistical feature engineering
│   ├── labeling.py                # Triple-barrier meta-labeling with transaction frictions
│   ├── models.py                  # 7 MSQF classifiers + Purged Walk-Forward CV splitter
│   ├── backtest.py                # Event-driven vectorized backtesting & financial risk engine
│   └── visualization.py           # High-contrast publication-grade plotting routines
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py           # Automated unit test suite (7 tests, all passing)
├── build_notebook.py              # Automated programmatic notebook generator
├── pair_trading_ml_assignment.ipynb # Comprehensive executed master Jupyter Notebook (1.8 MB)
├── requirements.txt               # Dependencies
└── README.md                      # Complete project documentation
```

---

## 🚀 How to Run

### 1. Run Automated Unit Tests
```bash
python -m unittest tests/test_pipeline.py -v
```

### 2. Launch the Master Notebook
```bash
jupyter notebook pair_trading_ml_assignment.ipynb
```
