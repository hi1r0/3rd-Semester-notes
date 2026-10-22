# Financial Risk Management (MSQF 533)

**Course:** MSQF 533: Financial Risk Management  
**Credits:** 4  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Student:** N Rohit Vedhanandh (Reg. No.: 25MSQUFPY0002)  
**Date:** October 2026  

---

## 📂 Directory Contents

| File / Folder | Description |
| :--- | :--- |
| [`latex/`](./latex/) | Master LaTeX project containing complete, modular, publication-grade notes for Unit I and Unit II. |
| ├── [`main.pdf`](./latex/main.pdf) | Compiled master lecture monograph with cover page, official syllabus, TOC, high-resolution TikZ diagrams, worked numerical examples, and consolidated formula sheet. |
| ├── [`main.tex`](./latex/main.tex) | Master document entry point. |
| ├── [`preamble/`](./latex/preamble/) | Typography, tcolorbox environments, math macros, title page, and Roman-numeral syllabus. |
| ├── [`chapters/`](./latex/chapters/) | Chapter source files: `ch01_introduction_to_risk_management.tex`, `ch02_var_methods_and_hedging.tex`, and `formula_reference.tex`. |
| └── [`figures/`](./latex/figures/) | University crest and graphics. |
| [`MSQF_533_Unit_I_Financial_Risk_Management.pdf`](./MSQF_533_Unit_I_Financial_Risk_Management.pdf) | Faculty lecture slides (Dr. Kamalakkannan Adhisekar) covering Unit I foundations. |
| [`MSQF-Introduction_to_Risk_Management-Class.pptx`](./MSQF-Introduction_to_Risk_Management-Class.pptx) | Core presentation deck (Prof. D. Lazar, 150 slides across 18 sections) grounded in Indian financial markets (NSE, BSE, MCX, RBI, SEBI, IRDAI). |

---

## 📑 Curriculum Coverage: Units I & II

### Unit I: Introduction to Risk Management
1. **Foundations of Risk & Uncertainty:** Knightian uncertainty vs financial risk; volatility ($\sigma$), skewness, kurtosis, and downside risk.
2. **Classification of Risks:**
   - Systematic (market-wide, non-diversifiable) vs Unsystematic (idiosyncratic, diversifiable).
   - Single Index risk decomposition: $\sigma_i^2 = \beta_i^2 \sigma_m^2 + \sigma_{\epsilon_i}^2$.
   - Comprehensive taxonomy: Market, Credit, Liquidity, Operational, and Sovereign/Systemic risks.
3. **Enterprise Risk Management (ERM) & Governance:**
   - The Three Lines of Defence framework (Business Units $\rightarrow$ CRO/Compliance $\rightarrow$ Internal Audit).
   - ISO 31000 / COSO ERM continuous closed-loop cycle.
4. **Asset-Class Specific Risk Profiles:**
   - **Commodity Investment Risk:** Carrying cost model ($F_0 = S_0 e^{(r + u - y)T}$), convenience yield, contango vs backwardation, basis risk on MCX.
   - **Equity Investment Risk:** Portfolio Beta ($\beta_P$), asymmetric leverage effect, multiple compression on NSE Nifty 50.
   - **Fixed Income Investment Risk:** Modified duration ($D^*$), convexity ($C$), second-order price change ($\Delta P/P \approx -D^* \Delta y + \frac{1}{2} C (\Delta y)^2$), and $\DV / \PVBP$ under RBI rate shocks.
   - **Currency (FX) Investment Risk:** Covered Interest Parity (CIP), transaction, translation, and economic exposures.
5. **Market Risk Measurement Framework:** Historical evolution from Greeks to VaR and coherent risk measures.

### Unit II: Value at Risk (VaR) Methods and Hedging
1. **Overview of Value at Risk (VaR):**
   - Mathematical definition: $\Prob(L > \VaR_\alpha) = 1 - \alpha$.
   - Time horizon scaling: Square-root-of-time rule ($\VaR_{\alpha, T} = \VaR_{\alpha, 1} \sqrt{T}$) and its limitations.
   - Shortcomings of VaR: Failure of subadditivity (non-coherence) and tail blindness.
   - Expected Shortfall ($\ES_\alpha$ / CVaR): Subadditive, coherent tail conditional expectation.
2. **VaR Estimation Methodologies:**
   - **Delta-Normal (Parametric):** Linear Taylor approximation, portfolio covariance matrix $\sigma_P^2 = \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}$, and diversification benefit.
   - **Historical Simulation (Non-Parametric):** Full revaluation across historical scenario paths, empirical quantile ranking, and handling of fat tails.
   - **Monte Carlo Simulation:** Geometric Brownian Motion (GBM) paths, Cholesky decomposition ($\boldsymbol{\Sigma} = \mathbf{L} \mathbf{L}^T$) for correlated variables, and full repricing.
   - Comparative synthesis matrix evaluating accuracy, speed, and non-linear performance.
3. **Stress Testing & Scenario Analysis:** Historical crises (1987 Black Monday, 2008 GFC, March 2020 COVID shock), hypothetical stress testing, and reverse stress testing.
4. **Linear Risk Hedging:**
   - Basis risk ($b_t = S_t - F_t$).
   - Optimal minimum-variance hedge ratio derivation: $h^* = \rho_{SF} \frac{\sigma_S}{\sigma_F}$.
   - Equivalence to OLS regression slope and hedging effectiveness ($R^2 = \rho^2$).
   - Sizing hedging futures contracts ($N^* = h^* \frac{Q_A}{Q_F}$ and $N^* = \beta_P \frac{V_P}{V_F}$).
5. **Non-Linear Risk Hedging:**
   - Options Greeks and second-order Taylor series approximation: $\Delta V \approx \Delta \cdot \Delta S + \frac{1}{2} \Gamma (\Delta S)^2 + \Theta \Delta t + \mathcal{V} \Delta \sigma$.
   - Delta neutrality ($\Delta_P = 0$) and dynamic rebalancing.
   - Gamma neutrality ($w_T = -\Gamma_P / \Gamma_T$) and two-stage portfolio immunization.

---

## 📐 TikZ Visual Architecture & Design Invariants

All diagrams in `latex/` adhere strictly to the repository standards:
- **Figure 1.1:** Systematic vs Unsystematic Risk Decomposition (Symmetrical Dual-Pillar Architecture).
- **Figure 1.2:** Enterprise Financial Risk Taxonomy Tree.
- **Figure 1.3:** The Three Lines of Defence Governance Architecture (Symmetrical branch lines with clearance $\ge 0.8\,\text{cm}$).
- **Figure 1.4:** Four-Pillar Asset Class Risk Comparison Grid ($2 \times 2$ grid with identical $6.6\,\text{cm} \times 5.5\,\text{cm}$ cards).
- **Figure 2.1:** Portfolio Return Distribution, $\VaR_\alpha$ Cutoff, and Shaded Expected Shortfall Tail.
- **Figure 2.2:** VaR Estimation Methodologies Architecture (Local vs Full Valuation pipeline).
- **Figure 2.3:** Ordinary Least Squares (OLS) Minimum-Variance Hedge Ratio Regression Diagram.
- **Figure 2.4:** Non-Linear Option Price Curvature, First-Order Delta Tangency, and Gamma Convexity Error.

---

## 🧮 Comprehensive Multi-Chapter Formula Reference Section

Placed at the end of the monograph (`chapters/formula_reference.tex`), grouping all formulas by chapter with structured **"Where:"** parameter definition lists and zero conversational filler.
