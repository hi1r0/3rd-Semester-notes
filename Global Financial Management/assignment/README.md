# Foreign Direct Investment in Switzerland: Trends, Determinants and Economic Impact — An Empirical Analysis

**Course:** MSQF 535 -- Global Financial Management  
**Institution:** Pondicherry University, Ramanujan School of Mathematical Sciences, Department of Statistics  
**Course Instructor:** Dr. Venkatajalapathy  
**Student:** N Rohit Vedhanandh (Reg. No.: `25MSQUFPY0002`)  
**Date:** September 2026  
**Format:** Monochromatic / Academic Greyscale (LaTeX, TikZ, Pgfplots, Booktabs, TColorBox)

---

## Executive Overview

This empirical monograph provides a comprehensive investigation into the trends, institutional determinants, and macroeconomic spillovers of Foreign Direct Investment (FDI) in Switzerland across the decade spanning **2015 to 2024**. Utilizing official statistical time-series published by the **Swiss National Bank (SNB)**, this report evaluates direct investment capital stocks, cross-border financial transactions, sectoral allocations, bilateral geographic distributions (unmasking the "Phantom FDI" conduit effect), and the worldwide operational footprint of Swiss Multinational Enterprises (MNEs).

### Key Empirical Findings

1. **Structural Net Capital Exporter Status:** Switzerland maintains an outward FDI capital stock of $\CHF\,1,340.1\bn$ ($167.5\%$ of GDP) versus an inward FDI capital stock of $\CHF\,925.7\bn$ ($115.7\%$ of GDP), generating a permanent net capital export surplus of $+\CHF\,414.4\bn$.
2. **Post-2017 Inward FDI Contraction:** Inward capital stocks peaked in 2017 at $\CHF\,1,347.8\bn$ before contracting by $31.3\%$ to $\CHF\,925.7\bn$ in 2024, reflecting the implementation of the OECD/G20 BEPS framework, Swiss corporate tax reform (STAF/TRAF 2020), and currency translation deflation.
3. **High Equity Capital Concentration:** Over $95\%$ of direct investment capital in both directions is funded via equity instruments ($95.8\%$ inward, $97.2\%$ outward), signaling permanent corporate ownership rather than speculative debt.
4. **The Conduit / Phantom FDI Discrepancy:** While the Netherlands ($26.4\%$) and Luxembourg ($15.2\%$) lead immediate investor statistics, Ultimate Beneficial Owner (UBO) tracing establishes that the **United States** controls $40.0\%$ ($\CHF\,370.7\bn$) of total inward FDI in Switzerland.
5. **Sectoral Divergence:** Inward FDI is concentrated in tertiary services ($77.6\%$, led by wholesale commodity trading and holding companies), whereas Swiss outward FDI maintains a substantial advanced manufacturing base ($37.9\%$, led by the Basel life-sciences cluster).
6. **Massive Worldwide Employment Multiplier:** Non-resident affiliates of Swiss MNEs employed $2.48\mn$ personnel globally in 2024 across $21,265$ foreign subsidiaries, yielding a global-to-domestic labor multiplier of $4.43\times$.

---

## Consolidated Empirical Summary Table

| Investment Metric / Dimension | 2015 Baseline | 2017 Peak / Shift | 2024 Position | 10-Year Trajectory & Impact |
| :--- | :---: | :---: | :---: | :--- |
| **Inward FDI Capital Stock** | $\CHF\,937.1\bn$ | $\CHF\,1,347.8\bn$ | $\CHF\,925.7\bn$ | $-31.3\%$ contraction from 2017 peak (BEPS/Tax reforms) |
| **Outward FDI Capital Stock** | $\CHF\,1,130.7\bn$ | $\CHF\,1,398.1\bn$ | $\CHF\,1,340.1\bn$ | $+18.5\%$ expansion; resilient global asset accumulation |
| **Net Direct Investment Surplus** | $+\CHF\,193.6\bn$ | $+\CHF\,50.3\bn$ | $+\CHF\,414.4\bn$ | Net capital export surplus expanded by $>110\%$ |
| **US Inward FDI Share (UBO)** | $\sim 35\%$ | $\sim 38\%$ | $40.0\%$ | Dominant ultimate investor ($\CHF\,370.7\bn$) |
| **Foreign Operating Affiliates** | $17,923$ | $18,696$ | $21,265$ | $+18.7\%$ expansion ($+3,342$ new foreign entities) |
| **Global Workforce Abroad** | $2,033.6\text{k}$ | $2,101.6\text{k}$ | $2,483.5\text{k}$ | $+22.1\%$ growth ($+449,900$ overseas jobs created) |
| **Domestic Parent Staff** | $528.4\text{k}$ | $538.4\text{k}$ | $561.0\text{k}$ | $+6.2\%$ growth ($+32,520$ high-wage domestic jobs) |
| **FDI Contribution to GDP** | $\sim 2.0\%$ | $\sim 2.2\%$ | $1.5\text{--}3.0\%$ | Critical driver of Swiss productivity & capital formation |

---

## Directory Architecture

```
Global Financial Management/assignment/
├── figures/
│   └── pondicherry_university_logo_bw.png        # Grayscale university crest
├── preamble/
│   ├── packages.tex                              # Package suite, titlesec & grayscale config
│   ├── environments.tex                          # Custom tcolorbox theorem, definition & case environments
│   ├── macros.tex                                # Mathematical & currency shortcuts
│   └── titlepage.tex                             # Pondicherry University cover page
├── sections/
│   ├── sec00_executive_summary.tex               # Executive overview & key empirical findings
│   ├── sec01_introduction.tex                    # FDI theory, OLI paradigm & TikZ Figure 1.1
│   ├── sec02_overview_fdi_switzerland.tex        # 2024 stocks, 2024 flows & BOP accounting theorem
│   ├── sec03_trend_analysis.tex                  # 2015-2024 trends, Tables 3.1-3.2 & Pgfplots Figure 3.1
│   ├── sec04_sectorwise_analysis.tex             # Sector breakdown, Pgfplots Figure 4.1 & Basel case
│   ├── sec05_countrywise_analysis.tex            # Immediate vs UBO, Pgfplots Figure 5.1 & conduit analysis
│   ├── sec06_swiss_mnes_abroad.tex               # Subsidiaries, employment, Pgfplots Figure 6.1 & Nestlé case
│   ├── sec07_determinants_fdi.tex                # Macro/institutional/tax determinants & TikZ Figure 7.1
│   ├── sec08_economic_impact.tex                 # Labor, GFCF, productivity, trade & TikZ Figure 8.1
│   ├── sec09_major_findings.tex                  # Comprehensive findings & Table 9.1 synthesis matrix
│   ├── sec10_conclusion_references.tex           # SWOT outlook, policy recommendations & references
│   └── sec11_formula_reference.tex               # Appendix: Rule 5 formula reference sheet
├── swiss_fdi_data/                               # Official SNB raw datasets (2015-2024)
│   ├── fetch_swiss_fdi.py
│   ├── swiss_fdi_by_country_2015_2024.csv
│   ├── swiss_fdi_by_sector_2015_2024.csv
│   ├── swiss_mne_parents_in_switzerland_2015_2024.csv
│   └── swiss_mne_subsidiaries_abroad_2015_2024.csv
├── main.tex                                      # Master LaTeX compilation document
├── main.pdf                                      # Generated monochrome PDF report
└── README.md                                     # Project and assignment documentation
```

---

## Build & Compilation Instructions

To compile the LaTeX source into the final high-resolution monochrome PDF:
```powershell
cd "D:\MSQF\Semester III\Global Financial Management\assignment"
pdflatex --disable-installer -interaction=nonstopmode main.tex
pdflatex --disable-installer -interaction=nonstopmode main.tex
```
*(Running two compilation passes ensures proper resolution of the Table of Contents, hyperref links, figure cross-references, and section counters).*
