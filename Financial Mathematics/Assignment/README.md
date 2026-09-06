# Equity Valuation Assignment: Net Asset Value Method (FMCG Sector)

**Course:** MSQF 532 -- Financial Mathematics  
**Institution:** Pondicherry University, Ramanujan School of Mathematical Sciences, Department of Statistics  
**Course Instructor:** Dr. Venkatajalapathy  
**Student:** N Rohit Vedhanandh (Reg. No.: `25MSQUFPY0002`)  
**Date:** September 2026  
**Format:** Monochromatic / Academic Greyscale (LaTeX, TikZ, Booktabs, TColorBox)

---

## Executive Overview

This assignment performs an empirical and theoretical investigation into corporate equity valuation using the **Net Asset Value (Intrinsic Value / Liquidation Value) Method** applied across ten marquee Indian Fast-Moving Consumer Goods (FMCG) corporations.

Key findings demonstrate that every firm in the sample trades at significant premiums ($4.5\times$ to $42.7\times$) relative to its net tangible asset backing. The study details why the NAV method establishes the foundational **liquidation floor** for an enterprise, but systematically undervalues asset-light consumer franchises where earnings power is driven by uncapitalized intangible moats (brand equity, distribution reach, pricing power, and negative working capital cycles). The report further articulates alternative valuation paradigms, including the **Dividend Discount Model (DDM)**, **P/E Multiples**, and **Discounted Free Cash Flows (DCF)**.

---

## Sample Universe & Empirical Summary

| Company Name | Total Assets (₹ Cr) | Goodwill (₹ Cr) | Tangible Assets (₹ Cr) | Total Liabilities (₹ Cr) | Net Assets (₹ Cr) | Equity Shares (Cr) | Intrinsic Value (₹) | Market Price (₹) | Valuation Gap (₹) | Overvaluation Multiple |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ITC Ltd** | 93,637 | 2,399 | 91,238 | 16,981 | 74,257 | 1,253 | ₹ 59 | ₹ 264 | - ₹ 205 | **4.5×** |
| **Tata Consumer Products** | 34,279 | 2,820 | 31,459 | 11,264 | 20,195 | 99 | ₹ 204 | ₹ 1,010 | - ₹ 806 | **4.9×** |
| **Dabur India Ltd** | 17,480 | 1,287 | 16,193 | 6,238 | 9,955 | 177 | ₹ 56 | ₹ 382 | - ₹ 326 | **6.8×** |
| **Varun Beverages Ltd** | 25,541 | 0 | 25,541 | 7,639 | 17,902 | 676 | ₹ 26 | ₹ 204 | - ₹ 178 | **7.8×** |
| **Hindustan Unilever Ltd** | 79,738 | 1,478 | 78,260 | 30,999 | 47,261 | 235 | ₹ 201 | ₹ 1,973 | - ₹ 1,772 | **9.8×** |
| **Godrej Consumer Products** | 13,365 | 2,948 | 10,417 | 5,573 | 4,844 | 102 | ₹ 47 | ₹ 881 | - ₹ 834 | **18.7×** |
| **Colgate-Palmolive India** | 3,408 | 47 | 3,361 | 1,394 | 1,967 | 27 | ₹ 73 | ₹ 1,843 | - ₹ 1,770 | **25.3×** |
| **Marico Ltd** | 9,950 | 557 | 9,393 | 5,183 | 4,210 | 130 | ₹ 32 | ₹ 814 | - ₹ 782 | **25.4×** |
| **Britannia Industries Ltd** | 9,730 | 1,380 | 8,350 | 4,648 | 3,702 | 24 | ₹ 154 | ₹ 5,120 | - ₹ 4,966 | **33.2×** |
| **Nestle India Ltd** | 13,357 | 444 | 12,913 | 6,641 | 6,272 | 193 | ₹ 33 | ₹ 1,409 | - ₹ 1,376 | **42.7×** |

---

## Directory Architecture

```
Financial Mathematics/Assignment/
├── figures/
│   └── pondicherry_university_logo_bw.png        # Grayscale university crest
├── preamble/
│   ├── packages.tex                              # Package suite & grayscale config
│   ├── environments.tex                          # Custom tcolorbox theorem environments
│   ├── macros.tex                                # Mathematical & valuation shortcuts
│   └── titlepage.tex                             # Pondicherry University cover page
├── sections/
│   ├── sec01_methodology.tex                     # Theory, Goodwill, Net Assets, TikZ Flowchart
│   ├── sec02_empirical_valuation.tex             # Valuation tables & worked case studies
│   ├── sec03_comparative_analysis.tex            # TikZ Overvaluation chart & Tier cards
│   ├── sec04_limitations_alternative_models.tex  # Liquidation floor vs DDM, PE, DCF models
│   └── sec05_conclusion.tex                      # Strategic investor synthesis & Master formulas
├── main.tex                                      # Master LaTeX compilation document
├── main.pdf                                      # Generated high-resolution monochrome PDF
└── README.md                                     # Project and assignment documentation
```

---

## Build & Compilation Instructions

To build the assignment PDF from source:
```bash
cd "D:\MSQF\Semester III\Financial Mathematics\Assignment"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
*(Two compilation passes ensure correct resolution of hyperref links, figure cross-references, and table counters).*
