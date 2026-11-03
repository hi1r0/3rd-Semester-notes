# MSQF Semester III Notes & Official Curriculum

Comprehensive course notes, lecture materials, presentations, empirical research monographs, and LaTeX documents for M.Sc. Quantitative Finance (Semester III) at Pondicherry University (Ramanujan School of Mathematical Sciences, Department of Statistics).

---

## 📜 Official Curriculum & Syllabus References

- **Master Standalone PDF:** [`Semester_III_Syllabus.pdf`](./Semester_III_Syllabus.pdf) — Direct 8-page lossless page extraction from the official Pondicherry University M.Sc. Quantitative Finance curriculum (AY 2025–26 onwards), comprising the CBCS Semester III Scheme Matrix (p. 6), 6 Hard Core courses (pp. 27–32), and registered Soft Core Elective MSQF 542 (p. 46).
- **Master Markdown Syllabus:** [`SYLLABUS.md`](./SYLLABUS.md) — Comprehensive, verbatim markdown reference documenting Course Objectives, Course Outcomes (CO1–CO5), unit-by-unit syllabus outlines, complete reference book bibliographies, and CO-PO mapping matrices for all 7 active courses, with an appendix of all CBCS soft-core electives.
- **Subject-Specific Syllabus Files:** Individual `syllabus.md` files are maintained in each course folder.

---

## 📚 Repository Structure

```text
├── Semester_III_Syllabus.pdf       # Official extracted 8-page university syllabus PDF
├── SYLLABUS.md                     # Comprehensive master syllabus markdown reference
├── Corporate Internship/           # MSQF 534: Summer corporate internship guidelines & viva
│   └── syllabus.md                 # Verbatim 6-week internship regulations & CO-PO matrix
├── Financial Engineering & Derivatives/ # MSQF 542: Financial Engineering & Derivatives
│   ├── Derivatives_Trading_FAQs.pdf
│   ├── financial derivatives_module1.pptx
│   ├── Hull J.C.-Options, Futures and Other Derivatives_9th edition.pdf
│   ├── MSQF_542_Financial_Engineering_Derivatives_Unit1.pdf
│   ├── MSQF_542_Financial_Engineering_Derivatives_UNIT 3.pdf
│   ├── Unit_2_Derivatives_and_Market_Instruments-2-23.pdf
│   └── syllabus.md                 # Verbatim course syllabus, objectives & CO-PO matrix
├── Financial Mathematics/          # MSQF 532: Financial Mathematics
│   ├── Assignment/                 # FMCG Equity Valuation Assignment (Monochrome LaTeX, 8 pages, main.pdf)
│   ├── latex/                      # Modular LaTeX lecture notes (Units I, II, III & IV, 104 pages, main.pdf)
│   ├── notes.docx                  # Comprehensive course notes Word document
│   ├── syllabus.md                 # Verbatim course syllabus, objectives & CO-PO matrix
│   └── README.md                   # Subject overview and directory index
├── Financial Risk Management/      # MSQF 533: Financial Risk Management
│   ├── latex/                      # Modular LaTeX lecture notes (Units I & II, TikZ architectures, 29-page main.pdf)
│   ├── MSQF_533_Unit_I_Financial_Risk_Management.pdf # Unit I lecture slides (Dr. Kamalakkannan Adhisekar)
│   ├── MSQF-Introduction_to_Risk_Management-Class.pptx # 150-slide class deck grounded in Indian markets (Prof. D. Lazar)
│   ├── syllabus.md                 # Verbatim course syllabus, objectives & CO-PO matrix
│   └── README.md                   # Comprehensive curriculum roadmap and lecture index
├── Global Financial Management/    # MSQF 535: Global Financial Management
│   ├── assignment/                 # Swiss FDI Empirical Analysis (13-page monochrome monograph, main.pdf)
│   │   └── swiss_fdi_data/         # Official Swiss National Bank (SNB) data cubes (2015–2024) & Python fetcher
│   ├── latex/                      # Modular LaTeX lecture notes (Units I, II, III & IV, TikZ architectures, 72-page main.pdf)
│   ├── notes (GFM).docx            # GFM lecture notes Word document
│   ├── syllabus.md                 # Verbatim course syllabus, objectives & CO-PO matrix
│   └── README.md                   # Subject roadmap and lecture index
├── ML/                             # MSQF 536: Machine Learning Techniques
│   ├── latex/                      # Publication-grade LaTeX lecture notes book (63 pages with syllabus, main.pdf)
│   ├── Assignment/                 # Machine learning pair trading assignment & pipeline
│   ├── Cluster Analysis/           # Unsupervised learning notes & handouts
│   ├── Data Preprocessing/         # Notes, exercises, and U1E1 Loan Data assignment
│   ├── Decision Tree/              # Tree-based models (ID3, C4.5, CART) and exercise sets
│   ├── KNN/                        # K-Nearest Neighbors theory slides and assignment questions
│   ├── Naive Bayes/                # Probabilistic classification slides and numerical questions
│   ├── Neural Network/             # Neural networks notes & architectures
│   ├── Regression/                 # Logistic Regression lecture notes
│   ├── Supervised Learning/        # Unit 1 & Unit 2 presentation slide decks
│   ├── SVM/                        # Support Vector Machines theory, kernels & exercise sets
│   ├── syllabus.md                 # Verbatim course syllabus, objectives & CO-PO matrix
│   └── README.md                   # Machine learning course roadmap and pipeline architecture
├── Time Series/                    # MSQF 531: Applied Time Series Analysis and Forecasting
│   ├── latex/                      # Modular LaTeX lecture notes (Unit I, forecasting taxonomy flowchart, main.pdf)
│   ├── notes/                      # Scanned and handwritten lecture note archives
│   ├── assignment.xlsx             # Empirical time series problem sets
│   ├── moving_average.xlsx         # Excel workbook for moving average smoothing calculations
│   ├── syllabus.md                 # Verbatim course syllabus, objectives & CO-PO matrix
│   └── README.md                   # Subject summary and resource index
├── pondicherry_university_logo.png  # Institutional crest
└── README.md                       # Global master documentation
```

---

## 📖 Subjects Covered

1. **Applied Time Series Analysis and Forecasting (MSQF 531 — Hard Core, 4 Credits)**
   - Chronological series decomposition (Additive, Multiplicative, Logarithmic transformations) into trend ($T$), seasonality ($S$), cyclical ($C$), and irregular ($I$) components.
   - Forecasting methodologies: Quantitative vs. qualitative taxonomy, planning horizons, and annual trend models (linear, quadratic, exponential, $\AR(p)$).
   - Smoothing techniques, moving average models, Box-Jenkins ARIMA methodology, unit root tests (ADF), cointegration, VAR/VECM, ARCH/GARCH volatility modeling, and practical spreadsheet / R implementations.
   - Reference: [`Time Series/syllabus.md`](./Time%20Series/syllabus.md) | LaTeX: [`Time Series/latex/main.pdf`](./Time%20Series/latex/main.pdf)

2. **Financial Mathematics (MSQF 532 — Hard Core, 4 Credits)**
   - Simple and compound interest, effective interest rates, doubling periods (Rule of 72, Rule of 69), present value schedules, growing annuities, and perpetuities.
   - Equity valuation frameworks: Going concern vs. liquidation book value floor, Dividend Discount Models (Gordon Model under growth, normal, and declining regimes), Walter's Model, Modigliani-Miller (MM) dividend irrelevance theorem, Bond YTC, and Loan Amortization.
   - Financial ratio analysis: Profitability margins and fundamental invariance identity, operational asset turnover velocity cycles, short-term liquidity & solvency ratios (Current, Quick, Cash Position).
   - Dynamic flow statements: Funds Flow Statement (Net Working Capital) vs. Cash Flow Statement (Cash & Cash Equivalents), Funds from Operations ($\FFO$), Cash from Operations ($\CFO$).
   - Cost-Volume-Profit (CVP) and Break-Even Analysis: Contribution margin, P/V ratio, Break-Even Point (units and sales value), Margin of Safety ($\MOS$), Angle of Incidence ($\theta$), Sensitivity Analysis, and native vector TikZ/pgfplots Break-Even charts.
   - Risk, Return, and Portfolio Mathematics (Unit IV): Axiomatic risk-return foundations, measures of central tendency ($\AM, \GM, \HM$), classical mean inequality ($\AM \ge \GM \ge \HM$), portfolio expected return linear additivity vs. non-linear risk subadditivity, dispersion & Coefficient of Variation ($\CV$), Karl Pearson bivariate correlation ($r_{XY}$), foreign exchange exposure sensitivity ($\beta_{\text{FX}}$), and Sharpe Single-Index optimal portfolio construction (cut-off rate $C^*$, optimal asset weights $w_i$).
   - Unified Multi-Chapter Formula Reference Sheet: 23 high-density self-contained formula cards across Chapters 1 to 4 with structured parameter definitions.
   - Empirical Course Assignment: Comprehensive Tri-Partite Equity Valuation on the Indian FMCG sector (10 firms, sensitivity analysis, break-even growth $g^*$).
   - Reference: [`Financial Mathematics/syllabus.md`](./Financial%20Mathematics/syllabus.md) | LaTeX: [`Financial Mathematics/latex/main.pdf`](./Financial%20Mathematics/latex/main.pdf)

3. **Financial Risk Management (MSQF 533 — Hard Core, 4 Credits)**
   - Foundations of risk and uncertainty (Knightian uncertainty vs. financial risk), systematic vs. unsystematic decomposition ($\sigma_i^2 = \beta_i^2 \sigma_m^2 + \sigma_{\epsilon_i}^2$), enterprise risk taxonomy, and the Three Lines of Defence governance architecture.
   - Asset-class specific risk profiles: Commodity cost of carry ($F_0 = S_0 e^{(r + u - y)T}$), contango vs. backwardation, equity portfolio beta on NSE Nifty 50, fixed income duration ($D^*$) and convexity ($C$) under RBI repo shocks, and Covered Interest Parity (CIP) currency hedging.
   - Value at Risk ($\VaR$) and Expected Shortfall ($\ES$ / CVaR): Formal definitions, horizon scaling ($\sqrt{T}$ rule), subadditivity violations, and tail blindness.
   - Estimation methodologies: Local valuation (Delta-Normal parametric covariance matrix $\sigma_P^2 = \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}$) vs. Full valuation (Historical Simulation empirical percentiles and Monte Carlo Cholesky decomposition $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^T$).
   - Hedging strategies: Linear risk hedging, basis risk ($b_t = S_t - F_t$), optimal minimum-variance hedge ratio derivation ($h^* = \rho \frac{\sigma_S}{\sigma_F}$) via OLS regression, contract sizing ($N^*$), and non-linear option Delta-Gamma dynamic immunization.
   - **Modular LaTeX Monograph (`Financial Risk Management/latex/main.pdf`):** 29-page publication-grade reference with full front matter, 8 high-density TikZ architectures, 9 worked numerical examples, and a consolidated multi-chapter formula sheet.
   - Reference: [`Financial Risk Management/syllabus.md`](./Financial%20Risk%20Management/syllabus.md) | LaTeX: [`Financial Risk Management/latex/main.pdf`](./Financial%20Risk%20Management/latex/main.pdf)

4. **Corporate Internship and Viva (MSQF 534 — Hard Core, 6 Credits)**
   - 6-week summer corporate internship undertaken in leading banks, financial institutions, stock markets, investment banks, insurance companies, or merchant banking firms under academic and corporate guidance.
   - Practical integration of quantitative finance coursework with real-world financial tasks, industry protocols, structured documentation, and departmental viva presentation.
   - Reference: [`Corporate Internship/syllabus.md`](./Corporate%20Internship/syllabus.md)

5. **Global Financial Management (MSQF 535 — Hard Core, 4 Credits)**
   - International financial architecture: World Bank Group, IMF, Balance of Payments (BOP) disequilibrium, Special Drawing Rights (SDR) valuation basket, and ADB.
   - Foreign exchange markets: Two-tier structure, spot vs. forward delivery, SWIFT/CHIPS telecommunications, Covered Interest Parity (CIP), and FEDAI Indian merchant rates (TT/Bill Buying and Selling) with accounting ledgers.
   - Cross-rate quotation mechanics, draft cancellations, forward cross rates with dual-leg covering, and FEDAI Rule 7 forward contract delivery horizons.
   - Theories of Foreign Exchange Rate: Law of One Price, Absolute & Relative PPP, the Fisher Effect, Macroeconomic Parity Web architecture, and Covered Interest Arbitrage mechanics.
   - Foreign Exchange Exposure and Management (Unit-III Scope): Translation exposure (Current Rate vs. Temporal method), Transaction exposure (Multilateral netting, matching, forward/money market hedges), and Economic exposure sensitivity.
   - Financial Management of the Multinational Firm (Unit-IV): MNC definitions, wealth maximization, agency challenges, centralized treasury governance, and international trade cash flows.
   - **Modular LaTeX Monograph (`Global Financial Management/latex/main.pdf`):** 72-page publication-grade reference with 4 units, 12 high-density TikZ architectures, worked FEDAI merchant rate problems, and a consolidated multi-chapter formula sheet.
   - Empirical Monograph: Swiss Foreign Direct Investment (2015–2024) analyzing SNB capital stocks, flows, UBO conduit tracing, and MNE global labor multipliers.
   - Reference: [`Global Financial Management/syllabus.md`](./Global%20Financial%20Management/syllabus.md) | LaTeX: [`Global Financial Management/latex/main.pdf`](./Global%20Financial%20Management/latex/main.pdf)

6. **Machine Learning Techniques (MSQF 536 — Hard Core, 4 Credits)**
   - End-to-end data preprocessing pipelines: Missing value handling, categorical encoding, standardization, SMOTE class balancing, and train/validation/test splits.
   - Algorithmic foundations and mathematical derivations: Logistic Regression, K-Nearest Neighbors (KNN), Naive Bayes Classifiers, Decision Trees/Ensembles (Random Forest, XGBoost), Support Vector Machines (SVM), and Artificial Neural Networks (MLP, CNN, RNN).
   - **Modular LaTeX Lecture Notes Book (`ML/latex/main.pdf`):** 63-page publication-grade reference with official syllabus front-matter, 6 chapters, and a consolidated comprehensive formula reference sheet.
   - Reference: [`ML/syllabus.md`](./ML/syllabus.md) | LaTeX: [`ML/latex/main.pdf`](./ML/latex/main.pdf)

7. **Financial Engineering and Derivatives (MSQF 542 — Soft Core Elective, 3 Credits)**
   - Theoretical foundation and practical mechanics of derivative contracts: forward, futures, options, and swap structures in Indian and international markets.
   - Pricing models: Cost of carry, Binomial trees, and Black-Scholes analytical option pricing.
   - Option trading strategies: Covered calls, protective puts, bull/bear spreads, butterfly spreads, calendar spreads, straddles, strangles, and put-call parity arbitrage.
   - Interest rate and currency swaps, valuation dynamics, and counterparty credit risk mitigation.
   - Reference: [`Financial Engineering & Derivatives/syllabus.md`](./Financial%20Engineering%20%26%20Derivatives/syllabus.md)

---

## 🛠️ Building & Running Documents

### 1. Compile Lecture Notes
To compile the lecture notes in any of the subject `latex` directories:

```bash
cd "ML/latex"                          # or "Financial Mathematics/latex" or "Financial Risk Management/latex" or "Global Financial Management/latex" or "Time Series/latex"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex  # Second run resolves TOC and cross-references
```

### 2. Compile Empirical Research Assignments
To compile the assignment research monographs:

```bash
cd "Financial Mathematics/Assignment"  # or "Global Financial Management/assignment"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
