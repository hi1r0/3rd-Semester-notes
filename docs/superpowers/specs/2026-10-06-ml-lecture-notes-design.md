# Technical Design Specification: Machine Learning Lecture Notes in LaTeX

**Date:** 2026-10-06  
**Status:** Approved  
**Course:** Machine Learning in Quantitative Finance (MSQF Semester III)  
**Institution:** Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University  
**Source Document:** `C:\Users\Hp\Downloads\DocScanner 6 Oct 2026 19-28.pdf` (61 scanned pages)

---

## 1. Executive Summary & Objective

The objective of this project is to create an authoritative, publication-quality LaTeX document of the handwritten lecture notes contained in `DocScanner 6 Oct 2026 19-28.pdf`.

Strict Fidelity Mandate:
- The content must strictly transcribe the definitions, algorithms, formulas, worked examples, tables, and diagrams from the handwritten manuscript without adding extraneous external topics or truncating any written material.
- The top-half calculation on Page 1 for "Double Exponential Smoothing" is omitted as approved, starting strictly with K-Nearest Neighbors on Page 1.
- Minor scratchwork and crossed-out arithmetic errors in the notebook are resolved to the author's final intended and corrected numerical values.
- All diagrams (decision trees, workflows, preprocessing pipelines) will be rendered natively using TikZ conforming strictly to the repository's visual symmetry and spacing invariants.
- A single consolidated "Comprehensive Formula Reference Sheet" is appended at the very end of the document, structured chapter-by-chapter with explicit parameter definitions.

---

## 2. Directory & Modular Architecture

The project will reside in `d:\MSQF\Semester III\ML\latex\`:

```
d:/MSQF/Semester III/ML/
├── latex/
│   ├── main.tex
│   ├── main.pdf                                   # Compiled distribution PDF
│   ├── preamble/
│   │   ├── packages.tex                           # Core packages, geometry, math, tikz, tcolorbox
│   │   ├── environments.tex                       # Theorem, definition, example, algorithm environments
│   │   ├── macros.tex                             # Vector notation, operators, colors
│   │   └── titlepage.tex                          # Formal title cover page
│   └── chapters/
│       ├── ch01_ml_foundations_and_preprocessing.tex  # Notes pp. 44–51
│       ├── ch02_knn.tex                               # Notes pp. 1–10 (from KNN onwards)
│       ├── ch03_naive_bayes.tex                       # Notes pp. 52–56
│       ├── ch04_logistic_regression.tex               # Notes pp. 56–61
│       ├── ch05_decision_trees.tex                    # Notes pp. 11–30
│       ├── ch06_svm.tex                               # Notes pp. 31–43
│       └── formula_reference.tex                      # Combined Formula Reference Sheet
└── README.md                                      # Subject overview & chapter synchronization
```

---

## 3. Chapter-by-Chapter Content & Mapping

### Chapter 1: Machine Learning Foundations & Data Preprocessing (pp. 44–51)
1. **Machine Learning Challenges in Finance**: Need for large clean data, risk of overfitting, interpretability issues ("black box" dilemma), and regulatory/ethical constraints.
2. **Types of Variables**: Numerical (Continuous, Discrete) and Categorical (Nominal, Ordinal).
3. **Data Preprocessing Pipeline (TikZ Flowchart)**: Raw Data $\to$ Cleaning $\to$ Transformation $\to$ Normalization/Scaling $\to$ Categorical Encoding $\to$ Model-Ready Data.
4. **Train-Validation-Test Splitting**: Purpose of evaluating generalization; split proportions (e.g. 70/15/15); chronological splitting requirements for financial and time-series data to prevent future-data leakage.
5. **Missingness Mechanisms**: Missing Completely at Random (MCAR), Missing at Random (MAR), Missing Not at Random (MNAR).
6. **Imputation Methods**: Comparison table of Mean/Median, Mode, KNN, Forward Fill with Advantages and Disadvantages.
7. **Class Imbalance**: High class imbalance in financial datasets (e.g., Credit Card Fraud: 99.9% Genuine vs. 0.1% Fraudulent); limitations of raw accuracy.
8. **Evaluation Metrics**: Precision ($\frac{TP}{TP+FP}$), Recall ($\frac{TP}{TP+FN}$), $F_1$-score ($2 \cdot \frac{\text{Precision}\cdot\text{Recall}}{\text{Precision}+\text{Recall}}$).
9. **Mistakes to Avoid & Key Takeaways**: Data leakage from global scaling before split, blind mean imputation on MNAR, ignoring class imbalance, uncontrolled one-hot encoding on high-cardinality features, failing to shuffle non-time-series data, and the 60–80% preprocessing rule.

### Chapter 2: K-Nearest Neighbors (KNN) (pp. 1–10)
1. **Foundations**: Supervised learning, classification and regression capability, distance-based metric method, lazy learning / instance-based algorithm.
2. **Algorithm Workflow (TikZ Flowchart)**: Training Data $\to$ Calculate Distance $\to$ Find $k$ Nearest Neighbors $\to$ Make Prediction (majority voting or average).
3. **Distance Metrics**:
   - Euclidean Distance: 2-D case $d(x,y) = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2}$, $p$-dimensional case $d(x,y) = \sqrt{\sum_{j=1}^p (x_j-y_j)^2}$.
   - Manhattan Distance: 2-D $d = |x_1-x_2| + |y_1-y_2|$, 3-D $d = |x_1-x_2| + |y_1-y_2| + |z_1-z_2|$, general $n$-D $d(x,y) = \sum_{i=1}^n |x_i-y_i|$.
   - Minkowski Distance: $d(x,y) = \left(\sum |x_i - y_i|^p\right)^{1/p}$ ($p=1$ Manhattan, $p=2$ Euclidean).
4. **Worked Example 2.1: Fruit Classification (Apple vs. Lemon)**:
   - Features: Sweetness, Crunchiness. Data points $A(7,7)$, $B(8,6)$, $C(3,8)$, $D(2,7)$, $E(6,8)$, $F(1,9)$.
   - Query point: $X = (5,7)$. Distance calculations, sorted distance ranking, majority voting for $k=3$ ($\{E, A, C\} \implies$ Apple: 2, Lemon: 1 $\implies$ Apple).
5. **Worked Example 2.2: Fintech Stock Recommendation (Buy, Hold, Avoid)**:
   - Three standardized financial indicators ($Z = \frac{x-\mu}{\sigma}$).
   - Standardized training dataset $S_1$ to $S_8$. Query point $X = (-0.559, -0.437, -0.531)$.
   - Sorted Euclidean distances table: $S_2 (0.527)$, $S_3 (0.939)$, $S_7 (1.002)$, etc. $k=3$ voting: Buy: 2, Hold: 1, Avoid: 0 $\implies$ Classify as Buy.
6. **Worked Example 2.3: Bank Loan Approval**:
   - Features: Credit score (scaled / 100), Annual Income ($\text{₹}$ Lakhs).
   - Applicant $(6.5, 5.5)$. Manhattan distance step-by-step evaluation across applicants $A_1$ to $A_5$.
7. **Worked Example 2.4: Real Estate House Price Prediction (KNN Regression)**:
   - Features: Area (hundreds of sq. ft.), Age (years). Target: Price.
   - Houses $H_1, H_2, H_4$. Sorted Manhattan distances. Price prediction via neighborhood aggregation.
8. **Parameter Selection: Small $k$ vs. Large $k$**:
   - Structured comparison table covering: Neighbourhood size, Sensitivity to noise, Variance, Bias, Decision boundary shape, Risk of Overfitting vs. Underfitting.
   - Balancing principle: Choose $k$ to balance bias and variance.

### Chapter 3: Naive Bayes Classification (pp. 52–56)
1. **Probability Foundations**: Sample space, complement $P(A^c) = 1 - P(A)$, union $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, joint probability, conditional probability $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
2. **Bayes' Theorem Formulation**: $P(C_k|X) = \frac{P(X|C_k) P(C_k)}{P(X)}$.
3. **Credit Risk Application Example**: Class $C_1$: Good credit, $C_2$: Default.
4. **Prior, Likelihood, and Marginal Evidence**:
   - Prior probability $P(C_k)$, Likelihood $P(X|C_k)$.
   - Total probability rule for evidence: $P(X) = \sum_{k=1}^K P(X|C_k) P(C_k)$.
5. **The Naive Assumption**: Conditional independence of features given the class:
   $$P(x_1, x_2, \dots, x_p | C_k) = \prod_{j=1}^p P(x_j | C_k)$$
6. **Classification Decision Rule**:
   $$\hat{c} = \arg\max_{C_k} P(C_k) \prod_{j=1}^p P(x_j | C_k)$$

### Chapter 4: Logistic Regression (pp. 56–61)
1. **Fundamentals & Activation Function**: Supervised binary classification; sigmoid/logistic curve mapping linear score $z = w^T x + b$ to probability:
   $$P(Y=1) = \frac{e^z}{1 + e^z} = \frac{1}{1 + e^{-z}}$$
2. **Odds and Log-Odds (Logit)**:
   $$\text{Odds} = \frac{P(Y=1)}{1 - P(Y=1)} = e^z, \quad \ln(\text{Odds}) = \beta_0 + \sum \beta_j x_j$$
3. **Coefficient Interpretation**:
   - Each $\beta_j$ represents the change in log-odds per one-unit increase in $x_j$.
   - Multiplicative odds effect: $e^{\beta_j}$. Worked example: if $\beta_j = 0.7$, $e^{0.7} \approx 2$, meaning a 1-unit increase doubles the odds.
4. **Model Training via MLE**: Parameter estimation using Maximum Likelihood Estimation; absence of closed-form analytical solution; numerical optimization (Newton-Raphson / Gradient Descent).
5. **Assumptions**: Independence of observations, binary dependent variable, linear relationship between independent variables and log-odds, absence of extreme outliers, sufficiently large sample size, minimal multicollinearity.
6. **Variants of Logistic Regression**: Binomial, Multinomial (un-ordered categorical), Ordinal (ordered classes).
7. **Evaluation Metrics & Trade-offs**: Accuracy, Precision, Recall, $F_1$-score, ROC-AUC. Pros & Cons (interpretability vs. need to manually model interactions; complete separation issues).
8. **End-to-End Pipeline & Generalized Linear Models (GLM)**: Data prep $\to$ MLE fit $\to$ Odds interpretation $\to$ Probability prediction & thresholding $\to$ Evaluation; classification under the exponential dispersion GLM family.

### Chapter 5: Decision Trees (pp. 11–30)
1. **Foundations**: Recursive partitioning into homogeneous groups. Hierarchy: Root node, Decision / Internal node, Leaf node.
2. **Common Algorithms**:
   - ID3: Entropy impurity, Information Gain split criterion.
   - C4.5: Entropy impurity, Gain Ratio split criterion.
   - CART: Gini impurity, Gini Gain / weighted Gini criterion.
3. **Impurity Formulations**:
   - Shannon Entropy: $H(S) = -\sum_{i=1}^c p_i \log_2(p_i)$.
   - Gini Impurity: $\text{Gini}(S) = 1 - \sum_{i=1}^c p_i^2$. Two-class formula: $1 - (p_1^2 + p_2^2) = 2 p_1 p_2$.
   - Comparison table: Gini vs. Entropy on metric measured, minimum value (0 at pure node), maximum value (0.5 for Gini, 1.0 for Entropy in binary split), and computational behavior.
4. **Comprehensive Solved Problem 5.1: Play Tennis Dataset (15 Instances)**:
   - Attributes: Outlook ($S, O, R$), Temp ($H, M, C$), Humidity ($H, N$), Wind ($W, S$). Target: Tennis? ($Y, N$).
   - Full dataset entropy: $P(Y) = 9/15, P(N) = 6/15 \implies H = 0.9709$.
   - Attribute split entropies and information gain:
     - Outlook: Weighted entropy $= 0.69088 \implies \text{Gain} = 0.28002$.
     - Temp: Weighted entropy $= 0.9072 \implies \text{Gain} = 0.0637$.
     - Humidity: Weighted entropy $= 0.7850 \implies \text{Gain} = 0.1694$.
     - Wind: Gain calculation.
   - Root node selection: Outlook has maximum information gain.
   - Sub-branch expansion: Rain branch (Wind test $\implies$ Weak: Yes, Strong: No); Sunny branch analysis.
5. **Comprehensive Solved Problem 5.2: Credit Loan Approval Dataset (15 Instances)**:
   - Attributes: Location ($U, S, R$), Income ($H, M, L$), Credit Score ($G, P$), Employment ($FT, PT$). Target: Approved? ($Y, N$).
   - Dataset entropy calculation: $P(Y) = 9/15, P(N) = 6/15 \implies H = 0.9709$.
   - Step-by-step weighted entropy calculations for each feature: Location, Employment, Credit Score, Income.
   - Information gain ranking: $\text{Employment} > \text{Credit Score} > \text{Income} > \text{Location}$.
6. **Comprehensive Solved Problem 5.3: Candidate Evaluation Dataset (14 Instances)**:
   - Attributes: Experience (Junior, Mid, Senior), Certified (Yes, No), Rating (Fair, Excellent). Target: Hired? ($Y, N$).
   - Overall entropy: $P(Y) = 9/14, P(N) = 5/14 \implies H_S = -\frac{9}{14}\log_2(\frac{9}{14}) - \frac{5}{14}\log_2(\frac{5}{14})$.
   - Certified branch entropy, Junior branch calculations, Senior branch calculations.
   - Final Decision Tree TikZ Diagram: Complete tree representation with symmetrical branch geometry and explicit leaf outcomes.

### Chapter 6: Support Vector Machines (SVM) (pp. 31–43)
1. **Foundations**: Supervised learning algorithm for classification and regression; optimal separating hyperplane with maximal geometric margin; support vectors.
2. **Margin Mathematical Formulation**:
   - Functional margin: $\hat{\gamma}_i = y_i(w^T x_i + b)$.
   - Hard-margin condition for correctly scaled hyperplanes: $y_i(w^T x_i + b) \ge 1$ for all $i=1,\dots,N$, with equality holding for support vectors.
   - Geometric margin and width: $M = \frac{2}{\|w\|}$, distance of points from boundary $d = \frac{|w^T x + b|}{\|w\|}$.
3. **Geometric Boundary Orientations**:
   - Vertical separation: boundary $x_1 = c$.
   - Diagonal separation: boundary forms linear combination $x_2 - x_1 = c$ or $x_2 + x_1 = c$.
4. **Numerical Problem 6.1: Linearly Separable Point Sets**:
   - Class $+1$ points: $(7,1), (8,2), (7,3), (9,2), (8,1), (7,2)$.
   - Class $-1$ points: $(3,1), (2,2), (3,3), (1,2), (2,1), (3,2)$.
   - Identification of support vectors: $+ve$ vectors at $x_1 = 7$, $-ve$ vectors at $x_1 = 3$.
   - Solving for correctly scaled $w$ and $b$: $w = [0.5, 0]^T$, $b = -2.5$. Margin $M = \frac{2}{\|w\|} = 4$.
   - Classification of query point $(5,2)$: decision function value $f(5,2) = 0.5(5) - 2.5 = 0$ (lies exactly on the separating hyperplane).
5. **Numerical Problem 6.2: Diagonal Separating Hyperplane**:
   - Boundary form $x_2 - x_1 + 0 = 0 \implies -x_1 + x_2 + 0 = 0$.
   - Determining scale factor $s$: $w^T = s[-1, 1], b=0$.
   - Closest positive point $(1,3)$: $w^T x_i = s(-1\cdot 1 + 1\cdot 3) = 2s$. Condition $1(2s + 0) = 1 \implies s = 0.5$.
   - Resulting hyperplane parameters: $w = [-0.5, 0.5]^T$, $b = 0$.
   - Complete verification table: Checking $y_i(w^T x_i + b) \ge 1$ across all positive points $(1,3), (1,4), (2,4)$ and negative points $(3,1), (4,1), (4,2), (5,2)$.
   - Classification of new query point $(3,4)$: $y(3,4) = 0.5(4-3) = 0.5 > 0 \implies$ Class $+1$.

### Comprehensive Formula Reference Sheet (Document End)
Strictly mathematical summary formatted into individual `tcolorbox` blocks grouped by chapter, each containing formulas, validity conditions, and a mandatory structured **Where:** parameter definition block.

---

## 4. Formatting & Style Invariants

1. **LaTeX Packages & Typography**:
   - Document class: `report` (11pt, a4paper).
   - Fonts & Microtypography: `lmodern`, `microtype`, `amsmath`, `amssymb`, `mathtools`.
   - Visual boxes: `tcolorbox` with `skins`, `breakable`, `theorems`.
   - Tables: `booktabs`, `tabularx`, `array`, `colortbl`.
2. **Numbering Standards**:
   - `number within=section` for all definition, example, theorem, and formula boxes.
   - Clean section headings without manual duplicate serial numbers.
3. **TikZ Visual Standards**:
   - Flowcharts and Decision Trees must use uniform box geometry across parallel tiers.
   - Clear connector spacing of $\ge 0.8\,\text{cm}$ between connected nodes.
   - High-contrast arrow strokes ($\ge 1.2\,\text{pt}$) in theme palette colors (`navyblue`, `teal`).
4. **Git Workflow Invariant**:
   - Stage all new and modified files (`git add`).
   - Commit with descriptive message detailing chapters added.
   - Push to `origin main`.

---

## 5. Verification Plan

1. **Syntax & Compilability**:
   - Compile using `pdflatex -interaction=nonstopmode main.tex` (two passes to resolve table of contents, citations, and references).
   - Verify zero fatal compilation errors and produce `ML/latex/main.pdf`.
2. **Mathematical & Numerical Verification**:
   - Cross-check all entropy values (e.g. $-\frac{9}{15}\log_2\frac{9}{15} - \frac{6}{15}\log_2\frac{6}{15} = 0.97095$), Gini indices, Euclidean/Manhattan distances, and SVM vector coordinates against original notebook scans.
3. **Completeness Verification**:
   - Verify that all 61 pages of notes are represented with zero missing examples or formulas.
4. **Documentation & Git Sync**:
   - Update `ML/README.md` and repository root `README.md`.
   - Verify `git status` shows clean working tree after push.
