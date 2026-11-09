# Machine Learning Techniques (MSQF 536) — LaTeX Lecture Notes

**Course:** MSQF 536: Machine Learning Techniques  
**Credits:** 4  
**Nature of Course:** Hard Core (Compulsory)  
**Degree:** M.Sc. Quantitative Finance (Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Document:** main.pdf (101 pages, publication-grade compiled book with official syllabus)  
**Author / Scribe:** N Rohit Vedhanandh (Reg. No.: 25MSQUFPY0002)  
**Official Syllabus Reference:** [../syllabus.md](../syllabus.md) | Master Curriculum: [../../SYLLABUS.md](../../SYLLABUS.md) | Official PDF: [../../Semester_III_Syllabus.pdf](../../Semester_III_Syllabus.pdf) (Page 7)  

---

## 📖 Overview

This repository contains the publication-grade, fully transcribed and verified LaTeX lecture notes for **Machine Learning in Quantitative Finance**, converted directly and faithfully from handwritten lecture scans (`DocScanner 6 Oct 2026 19-28.pdf` and `ml 09-11-2026.pdf`).

The book adheres strictly to classroom lecture contents ("no extra, no little"), formatted with modern professional typography, custom `tcolorbox` theorem environments, standalone TikZ architectural diagrams and decision trees with chapter-scoped sequential figure numbering (`Figures 1.1–1.2`, `2.1`, `4.1`, `5.1–5.4`, `6.1–6.3`, `7.1–7.5`, `8.1–8.2`, `9.1–9.2`, `10.1–10.2`), generous equation spacing, and a consolidated multi-chapter formula reference sheet.

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
│   ├── titlepage.tex                       # Formal university front cover page
│   └── syllabus.tex                        # Official course syllabus (Roman numeral page i)
├── chapters/
│   ├── ch01_ml_foundations_and_preprocessing.tex  # Chapter 1: ML Foundations & Preprocessing (Figs 1.1–1.2)
│   ├── ch02_knn.tex                               # Chapter 2: K-Nearest Neighbors (Fig 2.1)
│   ├── ch03_naive_bayes.tex                       # Chapter 3: Naive Bayes Classification
│   ├── ch04_logistic_regression.tex               # Chapter 4: Logistic Regression (Fig 4.1)
│   ├── ch05_decision_trees.tex                    # Chapter 5: Decision Trees (Figs 5.1–5.4)
│   ├── ch06_svm.tex                               # Chapter 6: Support Vector Machines (Figs 6.1–6.3)
│   ├── ch07_unsupervised_and_clustering.tex       # Chapter 7: Unsupervised Learning & Clustering (Figs 7.1–7.5)
│   ├── ch08_dimensionality_reduction_pca_svd.tex  # Chapter 8: Dimensionality Reduction: PCA & SVD (Figs 8.1–8.2)
│   ├── ch09_reinforcement_learning.tex            # Chapter 9: Reinforcement Learning & Trading (Figs 9.1–9.2)
│   ├── ch10_ensemble_learning.tex                 # Chapter 10: Ensemble Learning & XGBoost (Figs 10.1–10.2)
│   └── formula_reference.tex                      # Combined Multi-Chapter Formula Reference Sheet (Ch 1–10)
├── main.tex                                # Root master document
└── main.pdf                                # 101-page compiled PDF book
```

---

## 📑 Chapter Outline & Covered Topics

### Chapter 1: Machine Learning Foundations & Data Preprocessing
- **Source Pages:** Scanned pages 44–51 (`DocScanner 6 Oct 2026 19-28.pdf`).
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
- **Source Pages:** Scanned pages 1–10 (`DocScanner 6 Oct 2026 19-28.pdf`).
- **Topics Covered:**
  - Non-parametric instance-based lazy learning paradigm and workflow.
  - Mathematical distance metrics: Euclidean ($L_2$), Manhattan ($L_1$), and Minkowski ($L_p$) norms.
  - **Solved Example 2.3.1:** Fruit Classification via Euclidean Distance ($k=3$ majority voting).
  - **Solved Example 2.3.2:** Fintech Stock Recommendation with standardized financial indicators.
  - **Solved Example 2.3.3:** Bank Loan Approval via Manhattan Distance ($k=3$).
  - **Solved Example 2.3.4:** Real Estate House Price Prediction (continuous KNN regression).
  - Parameter selection: Bias-variance tradeoff across small $k$ vs. large $k$.

### Chapter 3: Naive Bayes Classification
- **Source Pages:** Scanned pages 52–56 (`DocScanner 6 Oct 2026 19-28.pdf`).
- **Topics Covered:**
  - Probability axioms, conditional probability, multiplication rule, and statistical independence.
  - Bayes' Theorem formulation for multiclass pattern recognition.
  - **Solved Numerical Example 3.3:** Credit Risk Default Classification (Good vs. Bad credit).
  - Theoretical Bayes optimal decision classifier.
  - Naive Bayes conditional independence assumption and high-dimensional tractability.
  - Maximum Likelihood Estimation (MLE) and Laplace ($\alpha = 1$) additive smoothing.

### Chapter 4: Logistic Regression
- **Source Pages:** Scanned pages 56–61 (`DocScanner 6 Oct 2026 19-28.pdf`).
- **Topics Covered:**
  - Theoretical limitations of Ordinary Least Squares (OLS) for binary targets.
  - Sigmoid activation function $\sigma(Z) = \frac{1}{1 + e^{-Z}} = \frac{e^Z}{1 + e^Z}$ and algebraic derivations.
  - Odds ratio, log-odds (logit transformation), and linear predictor matrix representations.
  - Econometric interpretation of logistic coefficients ($\beta_j$) and percentage change in odds.
  - Maximum Likelihood Estimation (MLE) and binary cross-entropy (log-loss) objective.
  - Core modeling assumptions, multinomial/ordinal extensions, and evaluation metrics (Confusion Matrix, ROC-AUC).
  - Membership in the Generalized Linear Model (GLM) family and 5-step implementation pipeline.

### Chapter 5: Decision Trees
- **Source Pages:** Scanned pages 11–30 (`DocScanner 6 Oct 2026 19-28.pdf`).
- **Topics Covered:**
  - Decision tree architecture (Root, Internal Decision Nodes, Terminal Leaf Nodes, Branching).
  - Recursive partitioning algorithms: ID3 (Entropy & Information Gain), C4.5 (Gain Ratio & Split Information), and CART (Gini Impurity).
  - Theoretical comparison: Shannon Entropy vs. Gini Impurity.
  - **Solved Problem 5.1:** Play Tennis Decision Tree ($n=15$ dataset, root split on Outlook, secondary splits on Rain/Wind and Sunny/Humidity, complete TikZ tree diagram).
  - **Solved Problem 5.2:** Credit Loan Approval Decision Tree ($n=15$ dataset, root split on Location, secondary splits on Income and Employment, complete TikZ tree diagram).
  - **Solved Problem 5.3:** Candidate Job Offer Decision Tree ($n=14$ dataset, root split on Experience, secondary splits on Certified and Salary, complete TikZ tree diagram).

### Chapter 6: Support Vector Machines (SVM)
- **Source Pages:** Scanned pages 31–43 (`DocScanner 6 Oct 2026 19-28.pdf`).
- **Topics Covered:**
  - Maximum-margin linear separating hyperplanes $\mathbf{w}^T \mathbf{x} + b = 0$, margin hyperplanes $\pm 1$, total margin width $M = \frac{2}{\|\mathbf{w}\|}$, and point-to-hyperplane perpendicular distance $d_i = \frac{|\mathbf{w}^T \mathbf{x}_i + b|}{\|\mathbf{w}\|}$.
  - Primal hard-margin feasibility constraints $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$ and support vector identification.
  - Diagnostic criteria and analytical solutions for Horizontal ($x_2 = c$), Vertical ($x_1 = c$), and Diagonal ($x_2 - x_1 = c$) separation.
  - **Solved Problem 6.1:** Horizontal Decision Boundary at $x_2 = 5$ ($\mathbf{w}=[0, 0.5]^T$, $b=-2.5$, margin $M=4$, verification table, query $(3,6) \to \text{Class } +1$, TikZ scatter plot).
  - **Solved Problem 6.2:** Vertical Decision Boundary at $x_1 = 5$ ($\mathbf{w}=[0.5, 0]^T$, $b=-2.5$, margin $M=4$, verification table, query $(5,2)$ boundary test, TikZ scatter plot).
  - **Solved Problem 6.3:** Diagonal Decision Boundary at $x_2 = x_1$ ($\mathbf{w}=[-0.5, 0.5]^T$, $b=0$, margin $M=2\sqrt{2} \approx 2.828$, point distance table, query $(3,4) \to \text{Class } +1$, TikZ scatter plot).

### Chapter 7: Unsupervised Learning & Cluster Analysis
- **Source Pages:** Scanned pages 1–16 (`ml 09-11-2026.pdf`).
- **Topics Covered:**
  - Taxonomy of ML paradigms: Supervised vs. Unsupervised Learning.
  - Variable typology (Nominal, Binary, Ordinal, Interval, Ratio) and metric proximity measures.
  - Mathematical metric axioms (Non-Negativity, Identity of Indiscernibles, Symmetry, Triangle Inequality).
  - Proximity metrics: Euclidean ($L_2$), Manhattan ($L_1$), Minkowski ($L_r$), Mahalanobis, SMC, and Jaccard similarity.
  - Hierarchical Clustering: Dendrogram structure, horizontal cutting threshold, Agglomerative vs. Divisive.
  - Inter-cluster linkage rules: Single (Min), Complete (Max), Average (Mean), Centroid, and Ward's Minimum Variance.
  - Divisive splitting strategies: Monothetic vs. Polythetic partitioning.
  - Non-hierarchical partitioning: $K$-Means Lloyd-Forgy iterative optimization, assignment/update cycle (TikZ flowchart), WCSS objective.
  - Density-based methods: DBSCAN local point typology (Core, Border, Noise points TikZ schematic), reachability, HDBSCAN, and OPTICS.

### Chapter 8: Dimensionality Reduction: PCA & SVD
- **Source Pages:** Scanned pages 16–26 (`ml 09-11-2026.pdf`).
- **Topics Covered:**
  - Curse of Dimensionality: Volume explosion, spatial sparsity, distance convergence, computational burden.
  - Feature Selection (Filter, Wrapper, Embedded) vs. Feature Extraction (PCA, LDA, Kernel PCA, QDA).
  - Principal Component Analysis (PCA): Maximum variance projection, orthogonal decorrelation, mathematical derivation.
  - **Solved Numerical Example 8.2.1:** Step-by-Step PCA Eigendecomposition on 4-Point Dataset $\{(4,11), (8,4), (13,5), (7,14)\}$ (mean centering, sample covariance matrix $\mathbf{S}$, characteristic polynomial $\lambda^2 - 37\lambda + 201 = 0$, eigenvalues $\lambda_1 = 30.3844, \lambda_2 = 6.6151$, eigenvectors, subspace projection).
  - Singular Value Decomposition (SVD): Factorization $\mathbf{A} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^T$, singular values vs. Gram matrix eigenvalues $\sigma_i = \sqrt{\lambda_i}$.
  - Eckart-Young Theorem: Optimal low-rank approximation $\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^T$.
  - **Solved Numerical Example 8.3.1:** Step-by-Step SVD of $2 \times 2$ Matrix $\mathbf{A} = \begin{pmatrix}1 & 2\\ 1 & 1\end{pmatrix}$ ($\mathbf{A}^T\mathbf{A}$, eigenvalues $\lambda_1 \approx 6.854, \lambda_2 \approx 0.146$, singular values $\sigma_1 \approx 2.618, \sigma_2 \approx 0.382$, singular vectors $\mathbf{u}_i, \mathbf{v}_i$).
  - Systematic comparison: PCA vs. SVD input structures, mean centering requirements, and algebraic equivalence.

### Chapter 9: Reinforcement Learning & Financial Trading
- **Source Pages:** Scanned pages 27–32 (`ml 09-11-2026.pdf`).
- **Topics Covered:**
  - Reinforcement learning principles: Trial-and-error, agent-environment interaction loop (TikZ schematic).
  - Discounted cumulative returns $G_t = \sum_{k=0}^\infty \gamma^k r_{t+k+1}$, discount factor $\gamma \in [0, 1]$.
  - Core RL terminology: Agent, Environment, State, Action, Reward, Policy $\pi(s)$, Value $V(s)$, Action-Value $Q(s, a)$.
  - Recurrent Reinforcement Learning (RRL) in Financial Trading: Direct policy optimization vs. value-function limitations.
  - Overcoming Markovianity: Modeling transaction cost friction memory $|F_t - F_{t-1}|$.
  - Recurrent policy model: Continuous position sizing $F_t = \tanh(\mathbf{w}^T \mathbf{x}_t + u F_{t-1} + b) \in [-1, +1]$.
  - Objective utilities: Cumulative net wealth, differential Sharpe ratio $S_T = \frac{A}{\sqrt{B - A^2}}$, and Gradient Ascent BPTT optimization.
  - Action selection: Exploration vs. Exploitation dilemma, $\epsilon$-greedy action selection mechanism.
  - Tabular $Q$-Learning: $Q$-table structure, Bellman optimality equation update, TD Target, and TD Error.
  - Systematic comparison matrices: Supervised vs. Unsupervised vs. RL; $Q$-Learning vs. RRL.

### Chapter 10: Ensemble Learning: Bagging, Boosting, & XGBoost
- **Source Pages:** Scanned pages 32–37 (`ml 09-11-2026.pdf`).
- **Topics Covered:**
  - Principles of ensemble learning: Wisdom of the crowd, Condorcet jury theorem intuition.
  - Bias-variance error decomposition: Target ensemble remediation (Bagging for high variance, Boosting for high bias).
  - Bootstrap Aggregating (Bagging): Random resampling with replacement ($63.2\%$ in-bag, $36.8\%$ out-of-bag validation).
  - Parallel Bagging workflow (TikZ architecture), majority voting / averaging aggregation.
  - Random Forests: De-correlating ensembles via random feature subsampling ($m = \lfloor\sqrt{p}\rfloor$ for classification, $m = \lfloor p/3 \rfloor$ for regression).
  - Boosting paradigms: Sequential error-focusing philosophy (TikZ architecture), weak learners.
  - Adaptive Boosting (AdaBoost): Exponential loss, sample weight updates $w_i^{(m+1)}$, learner importance $\alpha_m = \frac{1}{2}\ln\left(\frac{1 - \epsilon_m}{\epsilon_m}\right)$.
  - Gradient Boosting: Pseudo-residual optimization, shrinkage learning rate $\eta \in (0, 1]$.
  - Systematic comparison: Bagging vs. Boosting architecture, base learner complexity, and overfitting risk.
  - XGBoost (Extreme Gradient Boosting): Regularized objective $\operatorname{Obj}^{(t)} = \sum l(y_i, \hat{y}_i) + \sum \Omega(f_k)$, structural complexity penalty $\Omega(f) = \gamma T + \frac{1}{2}\lambda \sum w_j^2$.
  - XGBoost innovations: Sparsity-aware split finding, parallel block column growth, tree pruning via $\gamma$, early stopping.

### Comprehensive Multi-Chapter Formula Reference Sheet
- **Document End Section:** Placed at pages 89–102 (`chapters/formula_reference.tex`).
- Structured chapter-by-chapter (Chapters 1 to 10) under `formulabox` environments.
- Strict formula-only presentation with mandatory, itemized `\textbf{Where:}` parameter blocks across all 10 chapters.

---

## 🛠️ Compilation Instructions

To build the complete document from source:

```bash
cd "d:/MSQF/Semester III/ML/latex"
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The resulting `main.pdf` is fully indexed with roman numeral front matter, arabic numeral core chapters, and linked hyperref bookmarks.
