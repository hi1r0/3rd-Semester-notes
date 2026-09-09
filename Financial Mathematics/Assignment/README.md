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
1. **Liquidation Value (Breakdown Value)**: Evaluates the hard tangible balance-sheet floor of each corporation, deducting recorded goodwill and senior liabilities.
2. **Dividend Yield Analysis (Cost-of-Equity Hurdle Criterion)**: Measures direct cash distributions against a uniform $14.0\%$ cost-of-equity hurdle ($K_e$), establishing that zero firms satisfy current income requirements.
3. **Dividend Discount Model (Gordon Growth Model)**: Estimates intrinsic value under perpetual dividend growth, enforcing a conservative $12.0\%$ growth ceiling for supernormal growth enterprises.
4. **HUL Sensitivity Analysis**: Analytically derives the break-even perpetual growth threshold ($g^* \approx 11.46\%$) for Hindustan Unilever Ltd, demonstrating the extreme fragility of its apparent undervaluation.
5. **Consolidated Decision Matrix**: Synthesizes the three models under a majority-rule (2-out-of-3) consensus engine, classifying nine firms as **Overvalued** and Hindustan Unilever as **Mixed / Neutral**.

---

## Consolidated Valuation Decision Matrix

| Company Name | Market Price (₹) | Liquidation Value (₹) | Current Yield (%) | DDM Intrinsic Value (₹) | Final Classification |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Hindustan Unilever** | ₹ 1,973 | ₹ 201 | 2.27% | ₹ 2,512 | **Mixed / Neutral** |
| **ITC Ltd** | ₹ 264 | ₹ 59 | 4.45% | ₹ 206 | **Overvalued** |
| **Nestle India** | ₹ 1,409 | ₹ 33 | 0.91% | ₹ 388 | **Overvalued** |
| **Varun Beverages** | ₹ 204 | ₹ 26 | 1.55% | ₹ 178 | **Overvalued** |
| **Britannia Industries** | ₹ 5,120 | ₹ 154 | 1.44% | ₹ 4,144 | **Overvalued** |
| **Marico Ltd** | ₹ 814 | ₹ 32 | 1.20% | ₹ 245 | **Overvalued** |
| **Tata Consumer Products** | ₹ 1,010 | ₹ 204 | 1.08% | ₹ 421 | **Overvalued** |
| **Godrej Consumer Products** | ₹ 881 | ₹ 47 | 1.18% | ₹ 78 | **Overvalued** |
| **Dabur India** | ₹ 382 | ₹ 56 | 1.93% | ₹ 61 | **Overvalued** |
| **Colgate-Palmolive India** | ₹ 1,843 | ₹ 73 | 1.86% | ₹ 415 | **Overvalued** |

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
│   ├── sec01_assumptions_framework.tex           # Assumptions, limits & TikZ consensus flowchart
│   ├── sec02_liquidation_value.tex               # Liquidation value theory & Table 1
│   ├── sec03_dividend_yield.tex                  # Yield analysis, cost-of-equity hurdle & Table 2
│   ├── sec04_dividend_discount_model.tex         # Gordon DDM, 12% cap logic & Table 3
│   ├── sec05_sensitivity_analysis.tex            # HUL break-even derivation & Pgfplots sensitivity curve
│   └── sec06_consensus_and_conclusion.tex       # Table 4 (Consensus), Conclusion & Table 5 (Master formulas)
├── main.tex                                      # Master LaTeX compilation document
├── main.pdf                                      # Generated high-resolution monochrome PDF (8 pages)
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
