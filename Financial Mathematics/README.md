# Financial Mathematics (MSQF 532)

**Course:** MSQF 532: Financial Mathematics  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Credits:** 4  

---

## 📂 Directory Contents

| Directory / File | Description |
| :--- | :--- |
| [`latex/`](./latex/) | Modular LaTeX lecture notes covering Unit I (Interest Theory), Unit II (Valuation of Financial Instruments), Unit III (Financial Ratios and Cash Flow Analysis), and Unit IV (Risk, Return, and Portfolio Mathematics), with unified Formula Reference Sheet and compiled [`main.pdf`](./latex/main.pdf) (97 pages). |
| [`latex/README.md`](./latex/README.md) | Detailed syllabus roadmap, lecture date logs (`13/08/2026` to `30/10/2026`), solved problem sets, and compilation guides. |
| [`Assignment/`](./Assignment/) | Monochromatic LaTeX research report on FMCG Sector Equity Valuation using a Tri-Partite valuation architecture, with compiled [`main.pdf`](./Assignment/main.pdf). |
| [`Assignment/README.md`](./Assignment/README.md) | Assignment summary, valuation models, consolidated decision matrix, and empirical takeaways. |
| [`notes.docx`](./notes.docx) | Comprehensive Word document of course notes. |

---

## 📑 Core Topics Covered

1. **Unit I: Theory of Interest & Time Value of Money**
   - Simple & compound interest dynamics, sub-annual compounding, and effective interest rates ($\ERI$).
   - Rule of 72, Rule of 69, continuous doubling formulas.
   - Present value factors ($\text{PVF}$), ordinary annuities ($\PVAF$), annuities due, constant & growing perpetuities, sinking funds ($\text{S.F.}$).
   - Exponential growth and decay models with market microstructure spread decay applications.
2. **Unit II: Valuation of Financial Instruments**
   - Going concern, book value, liquidation value, market yields, and intrinsic value rules.
   - Yield to maturity ($\YTM$), holding period return ($\HPR$), and general dividend discount models.
   - Gordon's Dividend Growth Model: Growth firm ($r > K_e$), normal firm ($r = K_e$), and declining firm ($r < K_e$) regimes.
   - Walter's Dividend Valuation Model and corporate investment optimization.
   - Modigliani-Miller (MM) Dividend Irrelevance Theorem: Market value invariance proof and external financing schedules.
   - Bond Valuation & Yield to Call ($\YTC$), call penalty premium, and discount bond yield inequalities ($\YTC \ge \YTM$).
   - Loan Amortization: Equated Periodic Installment (EMI), interest/principal schedule mechanics, and corporate loan archetypes.
   - Price-Earnings Valuation Model ($\text{P/E}$), Earnings Per Share ($\EPS$), and Gordon theoretical multiple alignment.
3. **Unit III: Financial Ratios and Cash Flow Analysis**
   - Diagnostic taxonomy of financial ratios: Profitability, Activity/Turnover, Short-Term Liquidity, and Long-Term Leverage.
   - Profitability margin identities: Gross Profit Ratio, Operating Profit Ratio, Operating Ratio, Fundamental Invariance Identity ($85.63\% + 14.38\% = 100\%$), Net Profit Ratio, and ROI.
   - Turnover / Activity Ratios: Inventory turnover ($\text{ITR}$), Debtors turnover ($\text{DTR}$), Creditors turnover ($\text{CTR}$), Working Capital turnover, and Fixed Assets turnover.
   - Operational velocity conversion cycles (holding period, collection period, and payment period in days and months).
   - Solvency Ratios & Liquidity Diagnostics: Current Ratio ($2:1$ norm), Quick / Acid-Test Ratio ($1:1$ norm), Cash Position Ratio ($0.75:1$ norm), Debt-to-Equity, and Proprietary Ratio.
   - Flow Analysis: Funds Flow Statement (Net Working Capital) vs. Cash Flow Statement (Cash & Cash Equivalents); Funds from Operations ($\FFO$), Cash from Operations ($\CFO$), and full source/application balancing.
   - Cost-Volume-Profit (CVP) and Break-Even Analysis: Contribution margin, P/V ratio, Break-Even Point (units and sales value), Margin of Safety ($\MOS$), Angle of Incidence ($\theta$), and Sensitivity Analysis. Native vector TikZ/pgfplots Break-Even charts.
4. **Unit IV: Risk, Return, and Portfolio Mathematics**
   - Axiomatic foundations of investment return and risk (capital impairment, volatility, downside probability).
   - Measures of Central Tendency: Simple and Weighted Arithmetic Mean ($\bar{X}, \bar{X}_w$), Mode, Geometric Mean ($\GM$, multi-period compounding), Harmonic Mean ($\HM$, average rates and SIP rupee-cost averaging), and Classical Mean Inequality ($\AM \ge \GM \ge \HM$).
   - Portfolio diversification mathematics: Linear additivity of portfolio expected return ($E[R_p]$) vs. non-linear sub-additivity of portfolio risk ($\sigma_p^2 < \sum w_i \sigma_i$ when $\rho_{ij} < 1$).
   - Measures of Dispersion & Security Stability: Population vs. sample variance/SD ($N$ vs. $n-1$ degrees of freedom), Assumed Mean Shortcut ($d_i = X_i - A$), Shift of Origin and Scaling ($u_i = (X_i - A)/h$), and Coefficient of Variation ($\CV = \frac{\sigma}{\bar{X}} \times 100$) for cross-sectional stability profiling.
   - Bivariate Risk & Co-movement: Covariance ($\Cov(X, Y)$), Karl Pearson Correlation Coefficient ($r_{XY}$) direct raw-score formula, systematic market beta exposure, and coefficient of determination ($R^2$).
   - Foreign Exchange Exposure and Currency Risk: Structural regression sensitivity ($\beta_{\text{FX}}$) vs. firm valuation variance ($\Var(R_i)$), and tripartite exposure classification (Transaction, Translation, Operating/Economic exposure).
5. **Comprehensive Multi-Chapter Formula Reference Sheet**
   - Single consolidated reference section at document end, partitioned into 22 self-contained formula cards across Chapters 1, 2, 3, and 4 with mandatory structured `Where:` parameter lists.
6. **FMCG Equity Valuation Assignment**
   - Rigorous empirical valuation across ten major Indian FMCG corporations (HUL, ITC, Nestle, Varun Beverages, Britannia, Marico, Tata Consumer, Godrej Consumer, Dabur, Colgate-Palmolive).
   - Liquidation Value floor, Market-Implied growth ($g^*$), and Dividend Discount Model consensus synthesis.
