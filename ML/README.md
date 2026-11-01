# Machine Learning for Quantitative Finance (MSQF)

**Course:** Machine Learning in Quantitative Finance  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  

---

## 📂 Directory Architecture

```
ML/
├── Assignment/
│   ├── data/
│   │   └── market_data.csv                # Real daily market prices (2015-2024: 10 liquid tickers)
│   ├── src/                               # Modular quantitative pair trading & ML package
│   │   ├── market_data.py                 # Real market data ingestion & pair definition pipeline
│   │   ├── simulation.py                  # Backward-compatible pair loader bridge
│   │   ├── cointegration.py               # Rolling OLS hedge ratio & standardized Z-score engine
│   │   ├── features.py                    # 12-dimensional statistical quant feature extraction
│   │   ├── labeling.py                    # Triple-barrier meta-labeling with 10 bps friction
│   │   ├── models.py                      # 7 MSQF classifiers & Purged Walk-Forward CV
│   │   ├── backtest.py                    # Event-driven backtesting & financial risk engine
│   │   └── visualization.py               # Publication-grade plotting routines
│   ├── tests/
│   │   └── test_pipeline.py               # Automated unit tests (7 passing tests)
│   ├── build_notebook.py                  # Programmatic master notebook builder
│   ├── pair_trading_ml_assignment.ipynb   # Master executed Jupyter Notebook (1.74 MB)
│   ├── requirements.txt                   # Assignment dependencies
│   └── README.md                          # Comprehensive assignment documentation & benchmark results
├── Data Preprocessing/
│   ├── QF_ML_U1E1.pdf                     # Unit 1 Exercise 1 problem description
│   ├── QFS3U1 Note.pdf                    # Data preprocessing theoretical lecture notes
│   ├── QFS3U1E1.pdf                       # Exercise worksheet
│   └── U1E1_Assignment_Data/              # Implementation pipeline & datasets
│       ├── loan_data.csv                  # Raw credit loan dataset
│       ├── QF_ML_U1E1.py                  # End-to-end preprocessing script (cleaning, encoding, scaling, SMOTE)
│       ├── QF_ML_U1E1.ipynb               # Jupyter Notebook walkthrough
│       ├── QF_ML_U1E1_Answers.pdf         # Compiled solutions & evaluation metrics report
│       ├── main.pdf                       # Supplementary compiled report
│       └── *.npy                          # Processed train/validation/test split arrays
├── Decision Tree/
│   ├── DT Exercise.pdf                    # Decision Tree exercises & solved problems
│   └── QF_ML_U2_tree_based_models_note 1.pdf # Tree-based models (ID3, C4.5, CART, Random Forests)
├── KNN/
│   ├── ML_PPT_U1_KNN.pdf                  # K-Nearest Neighbors theory & distance metrics
│   └── QF_ML_U1_KNN_Ass_Q.pdf             # KNN assignment problems
├── Naive Bayes/
│   ├── QF_ML_Naive_bayes.pdf              # Probabilistic classification, Bayes' rule & Gaussian NB
│   └── QF_ML_Naive_bayes_Q1.pdf           # Naive Bayes problem set
├── Regression/
│   └── Logistic Regression.pdf            # Logistic Regression, odds ratio & sigmoid activation
├── Supervised Learning/
│   ├── QF_sem_3_ML_U1P1.pdf               # Unit 1 Part 1 Lecture Slides (Supervised Learning fundamentals)
│   └── QF_sem_3_ML_U2_PPT1.pdf            # Unit 2 Presentation Slides (Model selection & evaluation)
├── latex/                                 # Comprehensive LaTeX lecture notes book (62 pages, main.pdf)
│   ├── figures/                           # Institutional crest & graphics
│   ├── preamble/                          # Typography, packages, custom tcolorboxes & macros
│   ├── chapters/                          # Modular chapters 1–6 & comprehensive formula reference
│   ├── main.tex                           # Root master LaTeX file
│   ├── main.pdf                           # Publication-grade compiled PDF book (62 pages)
│   └── README.md                          # Detailed chapter overview & compilation guide
└── SVM/
    ├── QF_ML_SVM.pdf                      # Support Vector Machines, maximum margin hyperplanes
    ├── QF_ML_SVM_2 (1).pdf                # Kernel methods (RBF, Polynomial) & soft margin optimization
    └── QF_SVM_Question_2.pdf              # SVM problem set & numerical exercises
```

---

## 📑 Module Topics Covered

1. **Data Preprocessing & Feature Engineering**
   - Missing value imputation, categorical feature encoding (One-Hot, Target/Label encoding).
   - Feature normalization ($Z$-score standardization, Min-Max scaling).
   - Class imbalance handling (SMOTE oversampling, under-sampling).
   - Train / validation / test stratification pipelines on credit loan datasets (`loan_data.csv`).
2. **Supervised Learning Foundations**
   - Bias-variance tradeoff, cross-validation strategies ($k$-fold, stratified), and performance metrics (Precision, Recall, F1-score, ROC-AUC).
3. **K-Nearest Neighbors (KNN)**
   - Metric spaces (Euclidean, Manhattan, Minkowski distances), choice of $k$, distance weighting, and curse of dimensionality.
4. **Naive Bayes Classifiers**
   - Prior, likelihood, posterior calculation; conditional independence assumptions; Gaussian, Multinomial, and Bernoulli Naive Bayes.
5. **Linear & Logistic Regression**
   - Maximum likelihood estimation, log-odds transformation, decision boundaries, and regularization ($L_1$ Lasso, $L_2$ Ridge).
6. **Decision Trees & Ensemble Methods**
   - Information Gain, Entropy, Gini Impurity, tree pruning, classification and regression trees (CART).
7. **Support Vector Machines (SVM)**
   - Hard vs. soft margin optimization, slack variables ($C$), primal and dual formulations, kernel trick (Linear, Polynomial, RBF).
8. **End-to-End Capstone Project: Statistical Arbitrage & Pair Trading with Supervised ML (`Assignment/`)**
   - Historical daily market prices (2015–2024, 2,264 bars) across 10 liquid US equities and ETFs (`KO`, `PEP`, `XOM`, `CVX`, `JPM`, `BAC`, `BP`, `SHEL`, `GLD`, `SPY`).
   - Dynamic rolling cointegration, OLS hedge ratio estimation, and standardized spread $Z$-score triggers ($|Z| \ge 2.0$).
   - 12-dimensional quantitative feature engineering (Hurst exponent, OU half-life, ADF $p$-value, serial autocorrelations).
   - Triple-barrier meta-labeling with realistic transaction frictions (10 bps round-trip).
   - Purged Walk-Forward Time-Series Cross-Validation with horizon embargo buffers.
   - Comprehensive comparative benchmark across the full 7-model curriculum spectrum (Logistic Regression, Naive Bayes, KNN, Decision Tree, Random Forest, SVM RBF, MLP).
   - Event-driven backtesting contrasting Traditional vs. ML-Filtered statistical arbitrage strategies.
