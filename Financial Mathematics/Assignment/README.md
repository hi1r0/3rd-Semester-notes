# Equity Valuation Assignment: Indian FMCG Sector (Tri-Partite Framework)

**Course:** MSQF 532 -- Financial Mathematics  
**Institution:** Pondicherry University, Ramanujan School of Mathematical Sciences, Department of Statistics  
**Course Instructor:** Dr. Venkatajalapathy  
**Student:** N Rohit Vedhanandh (Reg. No.: `25MSQUFPY0002`)  
**Date:** September 2026  
**Format:** Monochromatic / Academic Greyscale (LaTeX, TikZ, Pgfplots, Booktabs, TColorBox)

---

## Executive Overview

This report conducts a comprehensive cross-sectional equity valuation of ten premier Indian Fast-Moving Consumer Goods (FMCG) corporations using a **tri-partite valuation architecture**:
1. **Liquidation Value (Breakdown Value / Tangible Book Value Floor)**: Evaluates the hard tangible balance-sheet floor of each corporation, deducting recorded goodwill and senior liabilities.
2. **Dividend Yield Analysis & Market-Implied Growth ($g^*$)**: Measures direct cash distributions against a uniform $14.0\%$ cost-of-equity hurdle ($K_e$), establishing that zero firms satisfy current income requirements, and inverts the Gordon model to derive the perpetual growth priced into secondary market shares ($g^* = \frac{P_0 \cdot K_e - D_0}{P_0 + D_0}$).
3. **Dividend Discount Model (Gordon Growth Model)**: Estimates intrinsic value under perpetual dividend growth, enforcing a conservative $12.0\%$ growth ceiling for supernormal growth enterprises ($K_e > g$).
4. **Cross-Sectional Growth Gap & Sensitivity Dynamics**: Analytically derives the break-even perpetual growth threshold ($g^* \approx 11.46\%$) for Hindustan Unilever Ltd, and evaluates the multi-firm growth gap ($g - g^*$). While HUL holds a $+0.53\,\text{pp}$ growth cushion, Varun Beverages ($-0.26\,\text{pp}$) and Britannia Industries ($-0.38\,\text{pp}$) operate on razor-thin overvaluation boundaries and flip to Undervalued if $K_e$ is adjusted by 100 bps to $13.0\%$. Consequently, only seven of the ten overvaluations are structurally robust.
5. **Consolidated Decision Matrix**: Synthesizes the three models under a majority-rule (2-out-of-3) consensus engine, classifying nine firms as **Overvalued** and Hindustan Unilever as **Mixed / Neutral**.

---

## Consolidated Valuation Decision Matrix

| Company Name | Market Price (₹) | Tangible BV Floor (₹) | Current Yield (%) | Implied $g^*$ (%) | DDM Intrinsic Value (₹) | Final Classification |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hindustan Unilever** | ₹ 1,973 | ₹ 201 | 2.27% | 11.47% | ₹ 2,512 | **Mixed / Neutral** |
| **ITC Ltd** | ₹ 264 | ₹ 59 | 4.45% | 9.15% | ₹ 206 | **Overvalued** |
| **Nestle India** | ₹ 1,409 | ₹ 33 | 0.91% | 12.97% | ₹ 388 | **Overvalued** |
| **Varun Beverages** | ₹ 204 | ₹ 26 | 1.55% | 12.26% | ₹ 178 | **Overvalued** |
| **Britannia Industries** | ₹ 5,120 | ₹ 154 | 1.44% | 12.38% | ₹ 4,144 | **Overvalued** |
| **Marico Ltd** | ₹ 814 | ₹ 32 | 1.20% | 12.65% | ₹ 245 | **Overvalued** |
| **Tata Consumer Products** | ₹ 1,010 | ₹ 204 | 1.08% | 12.78% | ₹ 421 | **Overvalued** |
| **Godrej Consumer Products** | ₹ 881 | ₹ 47 | 1.18% | 12.67% | ₹ 78 | **Overvalued** |
| **Dabur India** | ₹ 382 | ₹ 56 | 1.93% | 11.84% | ₹ 61 | **Overvalued** |
| **Colgate-Palmolive India** | ₹ 1,843 | ₹ 73 | 1.86% | 11.91% | ₹ 415 | **Overvalued** |

---

## Key Empirical Findings & Analytical Takeaways

1. **Severe Tangible Floor Disconnect**: All ten corporations trade at substantial premiums ($4.5\times$ to $43.4\times$) above tangible book value floors. FMCG equity valuations are heavily driven by off-balance-sheet intangible moats (brand brand equity, negative working capital cycles, extensive distribution reach) rather than liquidation asset recovery.
2. **Universal Current Income Deficit**: Dividend yields range from $0.91\%$ (Nestle India) to $4.45\%$ (ITC Ltd), failing the $14.0\%$ cost-of-equity hurdle universally across the sector.
3. **Market-Implied Growth Hurdles ($g^*$)**: Current equity prices demand sustained long-term earnings compounding between $9.15\%$ (ITC) and $12.97\%$ (Nestle India).
4. **Knife-Edge Valuation Frontiers**:
   - Hindustan Unilever trades at an implied growth rate of $11.47\%$. At the assumed $12.0\%$ sustainable growth ceiling, its DDM intrinsic value of ₹2,512 commands a $+27.3\%$ premium over the secondary market quotation of ₹1,973.
   - Varun Beverages ($g^* = 12.26\%$) and Britannia ($g^* = 12.38\%$) miss the $12.0\%$ growth ceiling by only $0.26\,\text{pp}$ and $0.38\,\text{pp}$ respectively. Under a modest 100 bps cost-of-equity stress test ($K_e = 13.0\%$), their implied hurdles drop to $11.27\%$ and $11.39\%$, flipping both firms into the Undervalued tier.
   - The remaining seven companies suffer large structural growth deficits ($g - g^* \le -1.28\,\text{pp}$), confirming their overvaluation across all reasonable discount rate scenarios.

---

## Academic References

- Damodaran, A. (2012). *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset* (3rd ed.). John Wiley \& Sons.
- Gordon, M. J. (1959). Dividends, Dilution, and the Cost of Capital. *The Review of Economics and Statistics*, 41(2), 99–105.
- Sharpe, W. F. (1964). Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk. *The Journal of Finance*, 19(3), 425–442.

---

## Directory Architecture

```
Financial Mathematics/Assignment/
├── figures/
│   └── pondicherry_university_logo_bw.png        # Grayscale university crest
├── preamble/
│   ├── packages.tex                              # Package suite, titlesec & grayscale config
│   ├── environments.tex                          # Custom tcolorbox theorem & formula environments
│   ├── macros.tex                                # Mathematical & valuation shortcuts
│   └── titlepage.tex                             # Pondicherry University cover page
├── sections/
│   ├── sec01_assumptions_framework.tex           # Assumptions, Sharpe/Gordon citations & TikZ flowchart
│   ├── sec02_liquidation_value.tex               # Tangible BV floor theory & Table 1 (exact multiples)
│   ├── sec03_dividend_yield.tex                  # Yield analysis, algebraic Implied g* derivation & Table 2
│   ├── sec04_dividend_discount_model.tex         # Gordon DDM, 12% ceiling rationale & Table 3
│   ├── sec05_sensitivity_analysis.tex            # HUL break-even derivation, Figure 2 curve & Sec 5.3 multi-firm stress test
│   └── sec06_consensus_and_conclusion.tex       # Table 4 (Consensus), Strategic synthesis, Table 5 & References
├── main.tex                                      # Master LaTeX compilation document
├── main.pdf                                      # Generated high-resolution monochrome PDF (strict 8 pages)
└── README.md                                     # Project and assignment documentation
```

---

## Build & Compilation Instructions

To build the assignment PDF from source:
```bash
cd "D:\MSQF\Semester III\Financial Mathematics\Assignment"
pdflatex --disable-installer -interaction=nonstopmode main.tex
pdflatex --disable-installer -interaction=nonstopmode main.tex
```
*(Two compilation passes ensure correct resolution of hyperref links, figure cross-references, and table counters).*
