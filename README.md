# MSQF Semester III Notes

Comprehensive course notes, lecture materials, presentations, empirical research monographs, and LaTeX documents for M.Sc. Quantitative Finance (Semester III) at Pondicherry University (Ramanujan School of Mathematical Sciences, Department of Statistics).

---

## 📚 Repository Structure

```text
├── Financial Mathematics/
│   ├── Assignment/                # FMCG Equity Valuation Assignment (Monochrome LaTeX, 8 pages, main.pdf)
│   ├── latex/                     # Modular LaTeX lecture notes (Units I, II, & III, 83 pages, main.pdf)
│   ├── notes.docx                 # Comprehensive course notes Word document
│   └── README.md                  # Subject overview and directory index
├── Financial Risk Management/
│   ├── latex/                     # Modular LaTeX lecture notes (Units I & II, TikZ architectures, 29-page main.pdf)
│   ├── MSQF_533_Unit_I_Financial_Risk_Management.pdf # Unit I lecture slides (Dr. Kamalakkannan Adhisekar)
│   ├── MSQF-Introduction_to_Risk_Management-Class.pptx # 150-slide class deck grounded in Indian markets (Prof. D. Lazar)
│   └── README.md                  # Comprehensive curriculum roadmap and lecture index
├── Global Financial Management/
│   ├── assignment/                # Swiss FDI Empirical Analysis (13-page monochrome monograph, main.pdf)
│   │   └── swiss_fdi_data/        # Official Swiss National Bank (SNB) data cubes (2015–2024) & Python fetcher
│   ├── latex/                     # Modular LaTeX lecture notes (Unit I & Unit II, TikZ architectures, main.pdf)
│   ├── notes (GFM).docx           # GFM lecture notes Word document
│   └── README.md                  # Subject roadmap and lecture index
├── ML/
│   ├── latex/                     # Publication-grade LaTeX lecture notes book (59 pages, main.pdf)
│   ├── Data Preprocessing/        # Notes, exercises, and U1E1 Loan Data assignment (code, notebook & solutions)
│   ├── Decision Tree/             # Tree-based models (ID3, C4.5, CART) and exercise sets
│   ├── KNN/                       # K-Nearest Neighbors theory slides and assignment questions
│   ├── Naive Bayes/               # Probabilistic classification slides and numerical questions
│   ├── Regression/                # Logistic Regression lecture notes
│   ├── Supervised Learning/       # Unit 1 & Unit 2 presentation slide decks
│   ├── SVM/                       # Support Vector Machines theory, kernels & exercise sets
│   └── README.md                  # Machine learning course roadmap and pipeline architecture
├── Time Series/
│   ├── latex/                     # Modular LaTeX lecture notes (Unit I, forecasting taxonomy flowchart, main.pdf)
│   ├── notes/                     # Scanned and handwritten lecture note archives
│   ├── assignment.xlsx            # Empirical time series problem sets
│   ├── moving_average.xlsx        # Excel workbook for moving average smoothing calculations
│   └── README.md                  # Subject summary and resource index
├── pondicherry_university_logo.png # Institutional crest
└── README.md                      # Global master documentation
```

---

## 📖 Subjects Covered

1. **Financial Mathematics (MSQF 532)**
   - Simple and compound interest, effective interest rates, doubling periods (Rule of 72, Rule of 69), present value schedules, growing annuities, and perpetuities.
   - Equity valuation frameworks: Going concern vs. liquidation book value floor, Dividend Discount Models (Gordon Model under growth, normal, and declining regimes), Walter's Model, Modigliani-Miller (MM) dividend irrelevance theorem, Bond YTC, and Loan Amortization.
   - Financial ratio analysis: Profitability margins and fundamental invariance identity, operational asset turnover velocity cycles, short-term liquidity & solvency ratios (Current, Quick, Cash Position).
   - Dynamic flow statements: Funds Flow Statement (Net Working Capital) vs. Cash Flow Statement (Cash & Cash Equivalents), Funds from Operations ($\FFO$), Cash from Operations ($\CFO$).
   - Cost-Volume-Profit (CVP) and Break-Even Analysis: Contribution margin, P/V ratio, Break-Even Point (units and sales value), Margin of Safety ($\MOS$), Angle of Incidence ($\theta$), Sensitivity Analysis, and native vector TikZ/pgfplots Break-Even charts.
   - Empirical Course Assignment: Comprehensive Tri-Partite Equity Valuation on the Indian FMCG sector (10 firms, sensitivity analysis, break-even growth $g^*$).

2. **Financial Risk Management (MSQF 533)**
   - Foundations of risk and uncertainty (Knightian uncertainty vs. financial risk), systematic vs. unsystematic decomposition ($\sigma_i^2 = \beta_i^2 \sigma_m^2 + \sigma_{\epsilon_i}^2$), enterprise risk taxonomy, and the Three Lines of Defence governance architecture.
   - Asset-class specific risk profiles: Commodity cost of carry ($F_0 = S_0 e^{(r + u - y)T}$), contango vs. backwardation, equity portfolio beta on NSE Nifty 50, fixed income duration ($D^*$) and convexity ($C$) under RBI repo shocks, and Covered Interest Parity (CIP) currency hedging.
   - Value at Risk ($\VaR$) and Expected Shortfall ($\ES$ / CVaR): Formal definitions, horizon scaling ($\sqrt{T}$ rule), subadditivity violations, and tail blindness.
   - Estimation methodologies: Local valuation (Delta-Normal parametric covariance matrix $\sigma_P^2 = \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}$) vs. Full valuation (Historical Simulation empirical percentiles and Monte Carlo Cholesky decomposition $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^T$).
   - Hedging strategies: Linear risk hedging, basis risk ($b_t = S_t - F_t$), optimal minimum-variance hedge ratio derivation ($h^* = \rho \frac{\sigma_S}{\sigma_F}$) via OLS regression, contract sizing ($N^*$), and non-linear option Delta-Gamma dynamic immunization.
   - **Modular LaTeX Monograph (`Financial Risk Management/latex/main.pdf`):** 29-page publication-grade reference with full front matter, 8 high-density TikZ architectures, 9 worked numerical examples, and a consolidated multi-chapter formula sheet.

3. **Global Financial Management (MSQF 535)**
   - International financial architecture: World Bank Group, IMF, Balance of Payments (BOP) disequilibrium, Special Drawing Rights (SDR) valuation basket, and ADB.
   - Foreign exchange markets: Two-tier structure, spot vs. forward delivery, SWIFT/CHIPS telecommunications, Covered Interest Parity (CIP), and FEDAI Indian merchant rates (TT/Bill Buying and Selling) with accounting ledgers.
   - Cross-rate quotation mechanics, draft cancellations, and FEDAI Rule 7 forward contract delivery horizons.
   - Empirical Monograph: Swiss Foreign Direct Investment (2015–2024) analyzing SNB capital stocks, flows, UBO conduit tracing, and MNE global labor multipliers.

4. **Machine Learning for Quantitative Finance**
   - End-to-end data preprocessing pipelines: Missing value handling, categorical encoding, standardization, SMOTE class balancing, and train/validation/test splits.
   - Algorithmic foundations and mathematical derivations: Logistic Regression, K-Nearest Neighbors (KNN), Naive Bayes Classifiers, Decision Trees/Ensembles, and Support Vector Machines (SVM).
   - **Modular LaTeX Lecture Notes Book (`ML/latex/main.pdf`):** 59-page publication-grade reference with 6 chapters and a consolidated comprehensive formula reference sheet.

5. **Applied Time Series Analysis and Forecasting (MSQF 531)**
   - Chronological series decomposition (Additive, Multiplicative, Logarithmic transformations) into trend ($T$), seasonality ($S$), cyclical ($C$), and irregular ($I$) components.
   - Forecasting methodologies: Quantitative vs. qualitative taxonomy, planning horizons, and annual trend models (linear, quadratic, exponential, $\AR(p)$).
   - Smoothing techniques, moving average models, and practical spreadsheet implementations.

## 🛠️ Building & Running Documents

### 1. Compile Lecture Notes
To compile the lecture notes in any of the subject `latex` directories:

```bash
cd "ML/latex"                          # or "Financial Mathematics/latex" or "Global Financial Management/latex" or "Time Series/latex"
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
