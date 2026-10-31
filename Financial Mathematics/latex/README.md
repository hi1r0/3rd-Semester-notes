# Financial Mathematics — LaTeX Notes (MSQF Semester III)

This directory contains the modular LaTeX sources, custom styling, problem sets, and compiled notes for the **Financial Mathematics** course (M.Sc. Quantitative Finance, Semester III).

---

## 📑 Syllabus & Course Coverage Roadmap

### **Unit I: Theory of Interest & Time Value of Money**
- **1.1 Time Value of Money & Simple Interest Fundamentals**
  - Definitions of Principal, Simple Interest (SI), Accrued Amount, and Exact/Ordinary time conversion fractions.
  - Additivity and inverse principal schedules.
  - *Solved Examples:* `1.1.1` to `1.1.5` (*Lectures: 13/08/2026, 17/08/2026*).
- **1.2 Compound Interest & Exponential Growth Dynamics**
  - Compounding principles, depreciation (reducing balance), sub-annual conversion, and demographic decay models.
  - *Solved Examples:* `1.2.1` to `1.2.4` (*Lectures: 17/08/2026, 18/08/2026*).
- **1.3 Methods of Analysis**
  - **1.3.1 Compounding:**
    - Multiple compounding conversion periods ($m = 1, 2, 4, 12$).
    - Effective Rate of Interest ($\ERI = (1 + R/m)^m - 1$).
    - Doubling Period formulations: Continuous limit ($\ln 2 \approx 0.693$), Rule of 72, and Rule of 69 ($T = 0.35 + 69/R$).
    - Uneven series of payments & Compound Value Annuity Factor ($\CVAF$).
    - Compound Value of Annuities: Closed-form factors and Year-by-Year Compound Accumulation Method ($\sum_{t=1}^n A(1+r)^{n-t}$ for Ordinary Annuity and $\sum_{t=0}^{n-1} A(1+r)^{n-t}$ for Annuity Due).
    - *Solved Examples:* `1.3.1` to `1.3.6` (*Lectures: 18/08/2026, 24/08/2026, 25/08/2026, 27/08/2026*).
  - **1.3.2 Discounting & Present Value Techniques:**
    - Present Value of a Lump Sum & Series of Cash Flows.
    - Construction of Present Value Factor ($\text{PVF}$) schedules.
    - Present Value of Ordinary Annuities ($\PVAF$) and Annuities Due: Closed-form factors and Year-by-Year Discounting Summation Formulations ($\sum_{t=1}^n \frac{A}{(1+r)^t}$ and $\sum_{t=0}^{n-1} \frac{A}{(1+r)^t}$).
    - Constant Perpetuities ($C/R$) & Growing Perpetuities ($C_1/(R-G)$).
    - Finite Growing Annuity streams: Analytical factor formula and Two-Step Year-by-Year Summation Formulation ($\sum_{t=1}^n \frac{C_1(1+g)^{t-1}}{(1+r)^t}$).
    - Sinking Fund ($\text{S.F.}$) reserve accumulations (Ordinary & Annuity Due).
    - *Solved Examples:* `1.3.7` to `1.3.16` (*Lectures: 18/08/2026, 27/08/2026, 28/08/2026, 31/08/2026, 01/09/2026*).
- **1.4 Growth and Decay Curves:**
  - Continuous exponential growth ($n_0 e^{kt}$) and decay ($n_0 e^{-kt}$) dynamics.
  - Rate parameter calibration ($k = \frac{\ln(n_{\max}/n_{\min})}{T} \approx 0.389182$).
  - Research-style greyscale side-by-side TikZ/pgfplots curves for growth (solid) and decay (dashed).
  - Market microstructure applications: Trade price impact decay curves, large banks' monitoring, toxic flow detection, and market stability.
  - *Lecture Date:* `03/09/2026`.

### Chapter 2: Valuation of Financial Instruments
- **2.1 Foundations of Valuation & Yield Concepts:**
  - Balance sheet book value, market value, going concern value, liquidating breakup value, and capitalised value.
  - Market yield, current yield, and equity/preference dividend yield ($dY = \DPS / P_0$).
  - Intrinsic valuation decision rules (undervalued vs. overvalued securities).
  - *Solved Examples:* `2.1.1` to `2.1.3` (*Lecture: 07/09/2026*).
- **2.2 Yield to Maturity, Holding Period Return, & Equity Valuation Approaches:**
  - Yield to Maturity ($\YTM$ / redemption yield) mechanics and capital appreciation/depreciation.
  - Holding Period Return ($\HPR = \frac{D_t + \Delta P}{P_1}$).
  - Accounting gross yield vs. net investor earnings yield ($\EPS / P_0$).
  - Four equity valuation approaches: Accounting/Balance Sheet, Dividend Discount (DDM), DCF (FCFF/FCFE), and Relative multiples ($P/E, P/B, P/S$).
  - General Dividend Discount Models: Finite $n$-year holding horizon and infinite perpetual DDM.
  - *Lecture Date:* `08/09/2026`.
- **2.3 Dividend Valuation Models: Constant Dividend & Gordon Basics:**
  - Model 1: Zero-growth perpetual dividend ($P_0 = D / K_e$).
  - Model 2: Constant dividend growth model ($P_0 = D_1 / (K_e - g)$).
  - Gordon model endogenous growth fundamentals: $g = b \times r$, retention ratio $b$, and capitalization rate $K_e$.
  - *Solved Examples:* `2.3.1` to `2.3.3` (*Lecture: 10/09/2026*).
- **2.4 Gordon's Model: Growth, Normal, and Declining Firm Dynamics:**
  - Endogenous dividend capitalization: $P_0 = \frac{\EPS_1(1-b)}{K_e - br}$.
  - Growth Firm ($r > K_e$): Optimal payout is NIL ($0\%$), maximum retention maximizes share price (XY Ltd).
  - Normal Firm ($r = K_e$): Dividend payout is neutral / irrelevant (MN Ltd).
  - Declining Firm ($r < K_e$): Optimal payout is $100\%$, full distribution maximizes share price (ABC Ltd).
  - *Solved Examples:* `2.4.1` to `2.4.3` (*Lecture: 15/09/2026*).
- **2.5 Walter's Dividend Valuation Model & Policy Decisions:**
  - Theories of dividend policy: Relevance (Gordon, Walter) vs. Irrelevance (Modigliani-Miller).
  - Walter's model assumptions, internal financing, and mathematical formulation: $P = \frac{D + \frac{r}{k}(E-D)}{k}$, Total Firm Value $V = N \times P$.
  - Policy optimization across firm regimes: Growth firm ($r > k$, optimal payout $0\%$, Nirmal Ltd), Normal firm ($r = k$, payout indifferent), Declining firm ($r < k$, optimal payout $100\%$).
  - *Solved Examples:* `2.5.1` to `2.5.3` (*Lecture: 16/09/2026*).
- **2.6 Modigliani--Miller (MM) Dividend Irrelevance Theory & Capital Budgeting Dynamics:**
  - Foundations of dividend irrelevance: firm value governed by earning power and real investment policy under perfect capital markets.
  - End-of-period share price formulation: $P_1 = P_0(1 + K_e) - D_1$.
  - Capital budgeting deficit & external equity financing: $\Delta M = I - (E - n D_1)$, and new shares issued $m = \Delta n = \Delta M / P_1$, formatted as a structured corporate financing statement (with accounting amount columns).
  - Mathematical invariance proof: Total market value $V_1 = (n + m) P_1 = n P_0(1 + K_e) + I - E$ is independent of dividend payout.
  - Empirical validity and limitations: Impact of taxes, flotation costs, information asymmetry/signaling, and investment policy interdependence.
  - *Solved Example:* `2.6.1` Stewart Ltd comprehensive valuation, share issuance, and market value invariance proof (*Lecture: 17/09/2026*).
- **2.7 Bond Valuation & Yield to Call (YTC):**
  - Discrete annual coupon bond valuation, face value, coupon cash flows, and call features.
  - Approximate Yield to Call formula: $\text{Approximate YTC} = \frac{C + \frac{CP - P_0}{N_c}}{\frac{CP + P_0}{2}}$.
  - Exact discounted cash flow equation: $P_0 = \sum_{t=1}^{N_c} \frac{C}{(1 + k_c)^t} + \frac{CP}{(1 + k_c)^{N_c}}$.
  - Comparative Analysis: $\YTM$ vs. $\YTC$, and proof that $\YTC \ge \YTM$ for discount bonds.
  - *Solved Example:* `2.7.1` Callable 10-year bond with 4-year call horizon and 3% penalty fee (*Lecture: 22/09/2026*).
- **2.8 Loan Amortization Models:**
  - Equated Periodic Installment (EMI) formulation: $A = \frac{P}{\PVAF(r, n)} = P \left[\frac{r}{1 - (1+r)^{-n}}\right]$.
  - Mathematical mechanics: Monotonically decreasing interest component ($I_t = B_{t-1} \times r$) and monotonically increasing principal amortization component ($\Delta B_t = A - I_t$).
  - Four loan archetypes: Fixed-Rate Fully Amortized Loans, Adjustable-Rate Mortgages (ARM / SOFR), Bullet/Balloon Loans, and Negative Amortization Loans.
  - Strategic corporate and consumer advantages: Predictable cash budgeting, equity accumulation, interest tax deductibility, credit profile enhancement, and borrower default mitigation.
  - *Lecture Date:* `23/09/2026`.
- **2.9 Price-Earnings Valuation Model & Earnings Per Share:**
  - Fundamental definitions: Price-Earnings Ratio ($\text{P/E} = P_0 / \EPS$) and Earnings Per Share ($\EPS = \frac{\EAT - D_p}{N}$).
  - Link between P/E and Gordon DDM: Theoretical forward P/E multiple $\frac{P_0}{\EPS_1} = \frac{1 - b}{K_e - g}$.
  - Managerial and investor interpretation: Growth expectations, cost of capital, earnings quality, risk pricing, and cross-sectional benchmarking.
  - *Lecture Date:* `08/10/2026`.

### Chapter 3: Financial Ratios and Cash Flow Analysis (Unit III)
- **3.1 Fundamentals of Ratio Analysis & Classification:**
  - Definition of financial ratios and diagnostic role of ratio analysis.
  - Seven core managerial advantages: Financial Forecasting, Managerial Control, Corporate Communication, Operational Efficiency, Investment Decision Support, Solvency Diagnostics, and Inter/Intra-Firm Benchmarking.
  - Functional Taxonomy Tree: Research-grade TikZ visual classification tree organizing ratios into Profitability, Turnover/Activity, and Solvency (Short-Term Liquidity & Long-Term Gearing).
  - Profitability ratio formulations: Gross Profit Ratio, Operating Profit Ratio, Operating Ratio, Fundamental Invariance Identity ($\text{Operating Ratio} + \text{Operating Profit Ratio} = 100\%$), Net Profit Ratio, and Return on Investment (ROI).
  - *Solved Example:* `3.1.1` Comprehensive multi-column Trading, Operating, and Profit & Loss Account reconstruction and profitability ratio computation (*Lecture: 12/10/2026*).
- **3.2 Turnover / Activity Ratios & Operational Velocity:**
  - Velocity and asset conversion frequency principles (expressed in annual rotation multiples).
  - Formulations: Stock / Inventory Turnover Ratio ($\text{ITR} = \COGS / \text{Average Stock}$), Debtors / Receivables Turnover Ratio ($\text{DTR} = \text{Credit Sales} / \text{Average Receivables}$), Creditors / Payables Turnover Ratio ($\text{CTR} = \text{Credit Purchases} / \text{Average Payables}$), Working Capital Turnover, and Fixed Assets Turnover (on Cost of Sales and Net Sales bases).
  - Conversion Velocity Periods: Inventory holding period ($365 / \text{ITR}$ days), Debtors collection velocity ($365 / \text{DTR}$ days or $12 / \text{DTR}$ months), and Creditors payment velocity ($365 / \text{CTR}$ days or $12 / \text{CTR}$ months).
  - *Solved Example:* `3.2.1` Comprehensive operational turnover analysis, intermediate aggregate reconciliation, and velocity period evaluation (*Lecture: 13/10/2026*).
- **3.3 Solvency Ratios: Liquidity & Financial Gearing:**
  - Solvency and Liquidity Diagnostic Framework: Temporal horizons of Short-Term Solvency (Liquidity) vs. Long-Term Solvency (Capital Gearing).
  - Short-Term Liquidity Ratios with conventional benchmark norms:
    - Current Ratio / Working Capital Ratio ($\text{CA} / \text{CL}$, Ideal Norm $2:1$).
    - Quick / Acid-Test Ratio ($\text{QA} / \text{CL} = (\text{CA} - \text{Stock} - \text{Prepaids}) / \text{CL}$, Ideal Norm $1:1$).
    - Cash Position Ratio / Absolute Liquid Ratio ($(\text{Cash} + \text{Bank} + \text{Marketable Securities}) / \text{CL}$, Norm $0.75:1$ or $0.5:1$).
  - Long-Term Gearing Ratios: Debt-to-Equity Ratio and Proprietary Ratio.
  - *Solved Example:* `3.3.1` Comprehensive evaluation of liquidity, working capital components, inventory distortion, and acid-test solvency (*Lecture: 15/10/2026*).
- **3.4 Fund Flow & Cash Flow Statement Analysis:**
  - Financial Flow Statement Framework: Funds Flow Statement (movements in Net Working Capital, $\NWC = \text{CA} - \text{CL}$) vs. Cash Flow Statement (movements in Cash and Cash Equivalents across Operating, Investing, and Financing activities).
  - Principles Governing Working Capital and Cash Movements: Comparative adjustment matrix for Current Assets and Current Liabilities.
  - Mathematical identities and formulas:
    - Funds from Operations ($\FFO = \text{Net Operating Profit} + \text{Depreciation} + \text{Amortization} + \text{Losses} - \text{Gains}$).
    - Cash Flow from Operations ($\CFO = \FFO + \sum \uparrow\text{CL} + \sum \downarrow\text{CA} - \sum \downarrow\text{CL} - \sum \uparrow\text{CA}$).
    - Funds Flow Balance Identity ($\text{Total Sources} - \text{Total Applications} = \Delta \NWC$).
  - *Solved Examples:*
    - `3.4.1` Computation of Cash Flow from Operations ($\CFO$) with multi-step non-cash and working capital adjustments (*Lecture: 20/10/2026*).
    - `3.4.2` Comprehensive Funds Flow Statement formulation for Mr. Rajan, including Schedule of Changes in Working Capital, Working Note 1 (Adjusted Net Profit & $\FFO$), Working Note 2 (Machinery Ledger Account at cost), and balanced Sources vs. Applications statement (*Lecture: 20/10/2026*).
- **3.5 Cost-Volume-Profit (CVP) and Break-Even Analysis:**
  - Theoretical Foundations: CVP Analysis and Marginal Costing.
  - Cost Architecture: Fixed Costs (Period/Time costs) vs. Variable Costs (Product/Marginal costs).
  - Mathematical formulations & identity mechanics:
    - Contribution Margin: $C = S - V = F + P$, Unit Contribution: $C_{\text{unit}} = s - v$.
    - Profit-Volume Ratio: $\text{P/V} = \frac{C}{S} \times 100 = \frac{s - v}{s} \times 100 = \frac{\Delta P}{\Delta S} \times 100$.
    - Break-Even Point: $\BEP_{\text{units}} = \frac{F}{s - v}$, $\BEP_{\text{sales}} = \frac{F}{\text{P/V}} = \BEP_{\text{units}} \times s$.
    - Break-Even Ratio: $\text{BE Ratio} = \frac{\BEP_{\text{sales}}}{\text{Actual Sales}} \times 100$.
    - Margin of Safety: $\MOS = \text{Actual Sales} - \BEP_{\text{sales}} = \frac{P}{\text{P/V Ratio}}$.
    - Margin of Safety Ratio: $\text{MOS Ratio} = \frac{\MOS}{\text{Actual Sales}} \times 100 = 100\% - \text{BE Ratio}$.
    - Target Volume for Profit $P_{\text{target}}$: $S_{\text{target}} = \frac{F + P_{\text{target}}}{\text{P/V Ratio}}$.
    - Angle of Incidence: $\theta = \arctan(m_S - m_{\text{TC}})$.
  - 8 Strategic Managerial Advantages and 7 Critical Analytical Limitations of Break-Even Analysis.
  - Research-grade native TikZ/pgfplots Break-Even vector graphics (Fixed Cost dashed line, Total Cost line, Sales Revenue line, shaded Loss and Profit areas, Angle of Incidence, and Margin of Safety dimension lines).
  - *Solved Examples:*
    - `3.5.1` Break-Even formulation, intermediate computations, native vector graphic chart, and 4-point managerial operational diagnostics for A Ltd (*Lecture: 26/10/2026*).
    - `3.5.2` Contribution Break-Even modeling, budgeted capacity analysis, native vector contribution chart, and 3-scenario Sensitivity Analysis for selling price, variable cost, and fixed overhead shifts (*Lecture: 27/10/2026*).

- **Comprehensive Multi-Chapter Formula Reference Sheet:**
  - Dedicated multi-page formula section at the end of the document, partitioned by Chapter 1, Chapter 2, and Chapter 3 (20 formula cards).
  - High-density mathematical formula boxes with explicit itemized `Where:` parameter definitions, validity conditions, and policy decision matrices.
  - Zero awkward splits: Every formula box is completely self-contained.

---

## 📂 Folder Structure

```text
latex/
├── main.tex                                       # Master root file to compile
├── preamble/
│   ├── packages.tex                               # Geometry, AMS-Math, TikZ, tcolorbox, hyperref, enumitem
│   ├── environments.tex                           # Section-scoped Theorem, Definition, Example & Formulaboxes
│   ├── macros.tex                                 # Shorthands for finance/actuarial/quant notations
│   ├── syllabus.tex                               # Pondicherry University syllabus page
│   └── titlepage.tex                              # Formal cover page
├── chapters/
│   ├── ch01_interest_theory.tex                   # Chapter 1: Interest Theory (Lectures: 13/08 – 03/09/2026)
│   ├── ch02_valuation_of_financial_instruments.tex # Chapter 2: Valuation of Instruments (Lectures: 07/09 – 08/10/2026)
│   ├── ch03_financial_ratios_and_cash_flow.tex     # Chapter 3: Financial Ratios & Cash Flow (Lectures: 12/10 – 27/10/2026)
│   └── formula_reference.tex                      # Combined Multi-Chapter Formula Reference Sheet with "Where:" definitions (Boxes 1-20)
├── figures/                                       # Department & University logos
└── README.md                                      # Documentation & compilation instructions
```

---

## 🛠️ How to Compile

Run from inside `Financial Mathematics/latex`:
```bash
pdflatex main.tex
pdflatex main.tex  # Second run resolves TOC and cross-references
```
The compiled output is generated as **`main.pdf`**.
