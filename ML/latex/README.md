# Machine Learning in Quantitative Finance — LaTeX Lecture Notes

**Course:** Machine Learning in Quantitative Finance  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Document:** `main.pdf` (62 pages, publication-grade compiled book)  
**Author / Scribe:** N Rohit Vedhanandh (Reg. No.: 25MSQUFPY0002)  

---

## 📖 Overview

This repository contains the publication-grade, fully transcribed and verified LaTeX lecture notes for **Machine Learning in Quantitative Finance**, converted directly and faithfully from handwritten lecture scans (`DocScanner 6 Oct 2026 19-28.pdf`).

The book adheres strictly to classroom lecture contents ("no extra, no little"), formatted with modern professional typography, custom `tcolorbox` theorem environments, standalone TikZ architectural diagrams and decision trees with sequential figure numbering (`Figures 1.1–1.2`, `2.1`, `4.1`, `5.1–5.4`, `6.1–6.3`), generous equation spacing, and a consolidated multi-chapter formula reference sheet.

---

## 📂 Directory Structure

```text
ML/latex/
├── figures/
│   └── pondicherry_university_logo.png     # Official institutional crest
├── preamble/
│   ├── packages.tex                        # Font, math, TikZ, caption, and geometry setup
│   ├── environments.tex                    # Custom tcolorboxes (definition, example, formulabox, etc.)
│   ├── macros.tex                          # Mathematical operators and notation shortcuts
│   └── titlepage.tex                       # Formal university front cover page
├── chapters/
│   ├── ch01_ml_foundations_and_preprocessing.tex  # Chapter 1 (pp. 44–51 of scans; Figs 1.1–1.2)
│   ├── ch02_knn.tex                               # Chapter 2 (pp. 1–10 of scans; Fig 2.1)
│   ├── ch03_naive_bayes.tex                       # Chapter 3 (pp. 52–56 of scans)
│   ├── ch04_logistic_regression.tex               # Chapter 4 (pp. 56–61 of scans; Fig 4.1)
│   ├── ch05_decision_trees.tex                    # Chapter 5 (pp. 11–30 of scans; Figs 5.1–5.4)
│   ├── ch06_svm.tex                               # Chapter 6 (pp. 31–43 of scans; Figs 6.1–6.3)
│   └── formula_reference.tex                      # Combined Multi-Chapter Formula Reference Sheet
├── main.tex                                # Root master document
└── main.pdf                                # 62-page compiled PDF book
```

---

## 📑 Chapter Outline & Covered Topics

### Chapter 1: Machine Learning Foundations & Data Preprocessing
- **Source Pages:** Scanned pages 44–51.
- **Topics Covered:**
  - Machine learning operational challenges (overfitting, high dimensionality, noisy/missing inputs).
  - Variable typology: Qualitative (Nominal, Ordinal) vs. Quantitative (Discrete, Continuous).
  - Scaler transformations: Z-Score Standardization, Min-Max Normalization, Robust Scaling (IQR).
  - Train-Test-Validation splitting strategies, $k$-fold cross-validation, and financial time-series data leakage prevention.
  - Missing data mechanisms (MCAR, MAR, MNAR) and statistical imputation decision framework.
  - Imbalanced categorical data handling (resampling, algorithmic weighting).
  - Supervised learning evaluation metrics (Accuracy, Precision, Recall, F1, ROC-AUC).
  - Pipeline pitfalls and best practices.

### Chapter 2: K-Nearest Neighbors (KNN)
- **Source Pages:** Scanned pages 1–10.
- **Topics Covered:**
  - Non-parametric instance-based lazy learning paradigm and workflow.
  - Mathematical distance metrics: Euclidean ($L_2$), Manhattan ($L_1$), and Minkowski ($L_p$) norms.
  - **Solved Example 2.3.1:** Fruit Classification via Euclidean Distance ($k=3$ majority voting).
  - **Solved Example 2.3.2:** Fintech Stock Recommendation with standardized financial indicators.
  - **Solved Example 2.3.3:** Bank Loan Approval via Manhattan Distance ($k=3$).
  - **Solved Example 2.3.4:** Real Estate House Price Prediction (continuous KNN regression).
  - Parameter selection: Bias-variance tradeoff across small $k$ vs. large $k$.

### Chapter 3: Naive Bayes Classification
- **Source Pages:** Scanned pages 52–56.
- **Topics Covered:**
  - Probability axioms, conditional probability, multiplication rule, and statistical independence.
  - Bayes' Theorem formulation for multiclass pattern recognition.
  - **Solved Numerical Example 3.3:** Credit Risk Default Classification (Good vs. Bad credit).
  - Theoretical Bayes optimal decision classifier.
  - Naive Bayes conditional independence assumption and high-dimensional tractability.
  - Maximum Likelihood Estimation (MLE) and Laplace ($\alpha = 1$) additive smoothing.

### Chapter 4: Logistic Regression
- **Source Pages:** Scanned pages 56–61.
- **Topics Covered:**
  - Theoretical limitations of Ordinary Least Squares (OLS) for binary targets.
  - Sigmoid activation function $\sigma(Z) = \frac{1}{1 + e^{-Z}} = \frac{e^Z}{1 + e^Z}$ and algebraic derivations.
  - Odds ratio, log-odds (logit transformation), and linear predictor matrix representations.
  - Econometric interpretation of logistic coefficients ($\beta_j$) and percentage change in odds.
  - Maximum Likelihood Estimation (MLE) and binary cross-entropy (log-loss) objective.
  - Core modeling assumptions, multinomial/ordinal extensions, and evaluation metrics (Confusion Matrix, ROC-AUC).
  - Membership in the Generalized Linear Model (GLM) family and 5-step implementation pipeline.

### Chapter 5: Decision Trees
- **Source Pages:** Scanned pages 11–30.
- **Topics Covered:**
  - Decision tree architecture (Root, Internal Decision Nodes, Terminal Leaf Nodes, Branching).
  - Recursive partitioning algorithms: ID3 (Entropy & Information Gain), C4.5 (Gain Ratio & Split Information), and CART (Gini Impurity).
  - Theoretical comparison: Shannon Entropy vs. Gini Impurity.
  - **Solved Problem 5.1:** Play Tennis Decision Tree ($n=15$ dataset, root split on Outlook, secondary splits on Rain/Wind and Sunny/Humidity, complete TikZ tree diagram).
  - **Solved Problem 5.2:** Credit Loan Approval Decision Tree ($n=15$ dataset, root split on Location, secondary splits on Income and Employment, complete TikZ tree diagram).
  - **Solved Problem 5.3:** Candidate Job Offer Decision Tree ($n=14$ dataset, root split on Experience, secondary splits on Certified and Salary, complete TikZ tree diagram).

### Chapter 6: Support Vector Machines (SVM)
- **Source Pages:** Scanned pages 31–43.
- **Topics Covered:**
  - Maximum-margin linear separating hyperplanes $\mathbf{w}^T \mathbf{x} + b = 0$, margin hyperplanes $\pm 1$, total margin width $M = \frac{2}{\|\mathbf{w}\|}$, and point-to-hyperplane perpendicular distance $d_i = \frac{|\mathbf{w}^T \mathbf{x}_i + b|}{\|\mathbf{w}\|}$.
  - Primal hard-margin feasibility constraints $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$ and support vector identification.
  - Diagnostic criteria and analytical solutions for Horizontal ($x_2 = c$), Vertical ($x_1 = c$), and Diagonal ($x_2 - x_1 = c$) separation.
  - **Solved Problem 6.1:** Horizontal Decision Boundary at $x_2 = 5$ ($\mathbf{w}=[0, 0.5]^T$, $b=-2.5$, margin $M=4$, verification table, query $(3,6) \to \text{Class } +1$, TikZ scatter plot).
  - **Solved Problem 6.2:** Vertical Decision Boundary at $x_1 = 5$ ($\mathbf{w}=[0.5, 0]^T$, $b=-2.5$, margin $M=4$, verification table, query $(5,2)$ boundary test, TikZ scatter plot).
  - **Solved Problem 6.3:** Diagonal Decision Boundary at $x_2 = x_1$ ($\mathbf{w}=[-0.5, 0.5]^T$, $b=0$, margin $M=2\sqrt{2} \approx 2.828$, point distance table, query $(3,4) \to \text{Class } +1$, TikZ scatter plot).

### Comprehensive Multi-Chapter Formula Reference Sheet
- **Document End Section:** Placed at pages 48–55.
- Structured chapter-by-chapter under `formulabox` environments.
- Strict formula-only presentation with mandatory, itemized `\textbf{Where:}` parameter blocks across all 6 chapters.

---

## 🛠️ Compilation Instructions

To build the complete document from source:

```bash
cd "d:/MSQF/Semester III/ML/latex"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The resulting `main.pdf` is fully indexed with roman numeral front matter, arabic numeral core chapters, and linked hyperref bookmarks.
