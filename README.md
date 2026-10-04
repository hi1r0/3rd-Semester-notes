# MSQF Semester III Notes

Comprehensive course notes, lecture materials, presentations, empirical research monographs, and LaTeX documents for M.Sc. Quantitative Finance (Semester III) at Pondicherry University (Ramanujan School of Mathematical Sciences, Department of Statistics).

---

## 📚 Repository Structure

```text
.
├── Financial Mathematics/
│   ├── Assignment/                # FMCG Equity Valuation Assignment (Monochrome LaTeX, 8 pages, main.pdf)
│   ├── latex/                     # Modular LaTeX lecture notes (Unit I & Chapter 2, main.pdf)
│   ├── notes.docx                 # Comprehensive course notes Word document
│   └── README.md                  # Subject overview and directory index
├── Financial Risk Management/
│   ├── MSQF-Introduction_to_Risk_Management-Class.pptx # Risk management introductory lecture slides
│   └── README.md                  # Risk taxonomy and course overview
├── Global Financial Management/
│   ├── assignment/                # Swiss FDI Empirical Analysis (13-page monochrome monograph, main.pdf)
│   │   └── swiss_fdi_data/        # Official Swiss National Bank (SNB) data cubes (2015–2024) & Python fetcher
│   ├── latex/                     # Modular LaTeX lecture notes (Unit I & Unit II, TikZ architectures, main.pdf)
│   ├── notes (GFM).docx           # GFM lecture notes Word document
│   └── README.md                  # Subject roadmap and lecture index
├── ML/
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
   - Equity valuation frameworks: Going concern vs. liquidation book value floor, Dividend Discount Models (Gordon Model under growth, normal, and declining regimes), Walter's Model, and Modigliani-Miller (MM) dividend irrelevance theorem.
   - Empirical Course Assignment: Comprehensive Tri-Partite Equity Valuation on the Indian FMCG sector (10 firms, sensitivity analysis, break-even growth $g^*$).

2. **Financial Risk Management**
   - Taxonomy of financial risks: Market risk, credit risk, operational risk, and liquidity risk.
   - Value at Risk ($\VaR$), Expected Shortfall ($\ES$), Basel regulatory accords (Basel I, II, III), and financial derivative hedging strategies.

3. **Global Financial Management (MSQF 535)**
   - International financial architecture: World Bank Group, IMF, Balance of Payments (BOP) disequilibrium, Special Drawing Rights (SDR) valuation basket, and ADB.
   - Foreign exchange markets: Two-tier structure, spot vs. forward delivery, SWIFT/CHIPS telecommunications, Covered Interest Parity (CIP), and FEDAI Indian merchant rates (TT/Bill Buying and Selling) with accounting ledgers.
   - Cross-rate quotation mechanics, draft cancellations, and FEDAI Rule 7 forward contract delivery horizons.
   - Empirical Monograph: Swiss Foreign Direct Investment (2015–2024) analyzing SNB capital stocks, flows, UBO conduit tracing, and MNE global labor multipliers.

4. **Machine Learning for Quantitative Finance**
   - End-to-end data preprocessing pipelines: Missing value handling, categorical encoding, standardization, SMOTE class balancing, and train/validation/test splits.
   - Algorithmic foundations and mathematical derivations: Logistic Regression, K-Nearest Neighbors (KNN), Naive Bayes Classifiers, Decision Trees/Ensembles, and Support Vector Machines (SVM).

5. **Applied Time Series Analysis and Forecasting (MSQF 531)**
   - Chronological series decomposition (Additive, Multiplicative, Logarithmic transformations) into trend ($T$), seasonality ($S$), cyclical ($C$), and irregular ($I$) components.
   - Forecasting methodologies: Quantitative vs. qualitative taxonomy, planning horizons, and annual trend models (linear, quadratic, exponential, $\AR(p)$).
   - Smoothing techniques, moving average models, and practical spreadsheet implementations.

---

## 🛠️ Building LaTeX Documents

### 1. Compile Lecture Notes
To compile the lecture notes in any of the subject `latex` directories:

```bash
cd "Financial Mathematics/latex"       # or "Global Financial Management/latex" or "Time Series/latex"
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
