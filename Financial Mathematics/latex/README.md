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
    - *Solved Examples:* `1.3.1` to `1.3.6` (*Lectures: 18/08/2026, 24/08/2026, 25/08/2026, 27/08/2026*).
  - **1.3.2 Discounting & Present Value Techniques:**
    - Present Value of a Lump Sum & Series of Cash Flows.
    - Construction of Present Value Factor ($\text{PVF}$) schedules.
    - Present Value of Ordinary Annuities ($\PVAF$) and Annuities Due.
    - Constant Perpetuities ($C/R$) & Growing Perpetuities ($C_1/(R-G)$).
    - Finite Growing Annuity streams & Sinking Fund ($\text{S.F.}$) reserve accumulations (Ordinary & Annuity Due).
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
- **Comprehensive Multi-Chapter Formula Reference Sheet:**
  - Dedicated multi-page formula section at the end of the document, partitioned by Chapter 1 and Chapter 2.
  - Features high-density mathematical formula boxes with explicit itemized `Where:` parameter definitions for every variable, equation, and payout decision matrix.

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
│   ├── ch02_valuation_of_financial_instruments.tex # Chapter 2: Valuation of Instruments (Lectures: 07/09 – 16/09/2026)
│   └── formula_reference.tex                      # Combined Multi-Chapter Formula Reference Sheet with "Where:" definitions
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
