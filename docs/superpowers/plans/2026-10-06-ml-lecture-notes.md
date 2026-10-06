# Machine Learning Lecture Notes LaTeX Conversion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transcribe and publish the 61 scanned handwritten lecture note pages from `DocScanner 6 Oct 2026 19-28.pdf` into a publication-grade modular LaTeX book under `d:\MSQF\Semester III\ML\latex`, compile `main.pdf`, update documentation, and push to Git.

**Architecture:** Modular LaTeX document structure matching `Financial Mathematics/latex` and `Global Financial Management/latex`, containing `main.tex`, `preamble/`, `chapters/`, and `formula_reference.tex`. All diagrams rendered natively in TikZ adhering to repository symmetry and connector spacing rules.

**Tech Stack:** LaTeX (`pdflatex`, `tcolorbox`, `tikz`, `booktabs`, `amsmath`, `hyperref`), Python (`fitz`/PyMuPDF for page inspection), Git.

## Global Constraints

- Source PDF: `C:\Users\Hp\Downloads\DocScanner 6 Oct 2026 19-28.pdf` (61 pages).
- Top-half calculation of Page 1 ("Double Exponential Smoothing") is omitted as approved; notes start strictly with KNN on Page 1.
- Strict content fidelity: Only include what is inside the notes—no external additions, no truncated content.
- Resolved corrections: Adopt author's final intended/corrected values for crossed-out handwriting.
- TikZ rules: Uniform box dimensions across parallel cards, $\ge 0.8\,\text{cm}$ connector clearance, bold $\ge 1.2\,\text{pt}$ arrow strokes.
- Formula reference rule: Single combined formula reference sheet at document end with chapter groupings and mandatory "Where:" parameter blocks.
- Git habit: Clean working tree, descriptive commit, push to `origin main`.

---

### Task 1: Scaffolding and LaTeX Preamble Setup

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\main.tex`
- Create: `d:\MSQF\Semester III\ML\latex\preamble\packages.tex`
- Create: `d:\MSQF\Semester III\ML\latex\preamble\environments.tex`
- Create: `d:\MSQF\Semester III\ML\latex\preamble\macros.tex`
- Create: `d:\MSQF\Semester III\ML\latex\preamble\titlepage.tex`

**Interfaces:**
- Consumes: Pondicherry University logo `pondicherry_university_logo.png`
- Produces: Base compilable LaTeX framework with `\lecturedate`, `\newtcbtheorem[number within=section]`, and color palette.

- [ ] **Step 1: Write `preamble/packages.tex`**
  Configure microtype, amsmath, amssymb, geometry, tcolorbox, tikz (shapes, arrows.meta, positioning), booktabs, tabularx, xcolor, hyperref.
- [ ] **Step 2: Write `preamble/macros.tex`**
  Define `\lecturedate`, colors (`navyblue`, `tealaccent`, `cardborder`, `softgray`), vector notation `\vect`, argmax operator.
- [ ] **Step 3: Write `preamble/environments.tex`**
  Configure section-scoped tcolorbox environments: `example`, `definition`, `theorem`, `note`, `formulatext`.
- [ ] **Step 4: Write `preamble/titlepage.tex`**
  Formal title page for Department of Statistics, Ramanujan School of Mathematical Sciences, Pondicherry University.
- [ ] **Step 5: Write `main.tex`**
  Include preambles and skeleton chapter inputs.
- [ ] **Step 6: Verify compilation**
  Run `pdflatex -interaction=nonstopmode main.tex` to confirm clean skeleton build.
- [ ] **Step 7: Commit scaffolding**

---

### Task 2: Transcribe Chapter 1: ML Foundations & Data Preprocessing (pp. 44–51)

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\ch01_ml_foundations_and_preprocessing.tex`

**Interfaces:**
- Consumes: Scanned pages 44 to 51 of `DocScanner 6 Oct 2026 19-28.pdf`
- Produces: Section-scoped Chapter 1 with TikZ Preprocessing Pipeline, Imputation Table, and Evaluation Metrics.

- [ ] **Step 1: Inspect pages 44–51 high-resolution images**
  Render pages 44–51 to disk at 200 DPI and inspect every formula and text note.
- [ ] **Step 2: Draft `ch01_ml_foundations_and_preprocessing.tex`**
  Include: Challenges in ML, Types of Variables, Preprocessing Pipeline TikZ diagram, Train-Validation-Test splitting, Missingness mechanisms (MCAR, MAR, MNAR), Imputation comparison table, Class Imbalance, Precision/Recall/F1-score formulas, Mistakes to be Avoided, and Key Takeaways.
- [ ] **Step 3: Compile and verify Chapter 1 in `main.tex`**
  Run `pdflatex main.tex` and inspect output.
- [ ] **Step 4: Commit Chapter 1**

---

### Task 3: Transcribe Chapter 2: K-Nearest Neighbors (KNN) (pp. 1–10)

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\ch02_knn.tex`

**Interfaces:**
- Consumes: Scanned pages 1 to 10 of `DocScanner 6 Oct 2026 19-28.pdf` (starting from KNN on p. 1)
- Produces: Section-scoped Chapter 2 with 4 worked numerical examples, TikZ workflow, distance metrics, and Small $k$ vs Large $k$ table.

- [ ] **Step 1: Inspect pages 1–10 high-resolution images**
  Render pages 1–10 to disk at 200 DPI and inspect distance calculations.
- [ ] **Step 2: Draft `ch02_knn.tex`**
  Include: KNN intro, distance-based, lazy learning, TikZ workflow diagram, Euclidean, Manhattan, Minkowski metrics, Worked Example 2.1 (Apple vs Lemon), Worked Example 2.2 (Stock Buy/Hold/Avoid with standardization), Worked Example 2.3 (Bank Loan Approval), Worked Example 2.4 (Real Estate KNN Regression), and Small $k$ vs Large $k$ comparison table.
- [ ] **Step 3: Compile and verify Chapter 2 in `main.tex`**
  Run `pdflatex main.tex` and verify calculations.
- [ ] **Step 4: Commit Chapter 2**

---

### Task 4: Transcribe Chapter 3: Naive Bayes Classification (pp. 52–56)

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\ch03_naive_bayes.tex`

**Interfaces:**
- Consumes: Scanned pages 52 to 56 of `DocScanner 6 Oct 2026 19-28.pdf`
- Produces: Section-scoped Chapter 3 with probability foundations, Bayes theorem, credit risk formulation, naive assumption, and decision rule.

- [ ] **Step 1: Inspect pages 52–56 high-resolution images**
  Render pages 52–56 at 200 DPI and inspect probability expressions.
- [ ] **Step 2: Draft `ch03_naive_bayes.tex`**
  Include: Key probability identities, Bayes theorem, credit risk classification application, prior, likelihood, marginal evidence, the Naive conditional independence assumption, and classification decision rule.
- [ ] **Step 3: Compile and verify Chapter 3 in `main.tex`**
  Run `pdflatex main.tex` and check equations.
- [ ] **Step 4: Commit Chapter 3**

---

### Task 5: Transcribe Chapter 4: Logistic Regression (pp. 56–61)

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\ch04_logistic_regression.tex`

**Interfaces:**
- Consumes: Scanned pages 56 to 61 of `DocScanner 6 Oct 2026 19-28.pdf`
- Produces: Section-scoped Chapter 4 with sigmoid derivation, odds ratio, MLE training, assumptions, types, metrics, pros & cons, and GLM family.

- [ ] **Step 1: Inspect pages 56–61 high-resolution images**
  Render pages 56–61 at 200 DPI and inspect derivations and tables.
- [ ] **Step 2: Draft `ch04_logistic_regression.tex`**
  Include: Supervised classification, sigmoid activation derivation, odds ratio definition, coefficient interpretation with multiplier $e^{\beta_j}$, MLE parameter estimation, model assumptions, variants (Binomial, Multinomial, Ordinal), evaluation metrics, pros & cons, and step-by-step overview pipeline.
- [ ] **Step 3: Compile and verify Chapter 4 in `main.tex`**
  Run `pdflatex main.tex`.
- [ ] **Step 4: Commit Chapter 4**

---

### Task 6: Transcribe Chapter 5: Decision Trees (pp. 11–30)

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\ch05_decision_trees.tex`

**Interfaces:**
- Consumes: Scanned pages 11 to 30 of `DocScanner 6 Oct 2026 19-28.pdf`
- Produces: Section-scoped Chapter 5 with ID3/C4.5/CART algorithms, Gini vs Entropy table, 3 complete solved datasets (Play Tennis, Loan Approval, Candidate Experience), and TikZ Decision Tree diagram.

- [ ] **Step 1: Inspect pages 11–30 high-resolution images**
  Render pages 11–30 at 200 DPI and verify dataset values and calculations.
- [ ] **Step 2: Draft `ch05_decision_trees.tex`**
  Include: Recursive partitioning, node hierarchy, ID3/C4.5/CART comparison, Gini and Shannon Entropy formulas, comparison table, Solved Problem 5.1 (Play Tennis 15 rows with attribute gains and branch expansion), Solved Problem 5.2 (Loan Approval 15 rows with weighted entropy ranking), Solved Problem 5.3 (Candidate Experience 14 rows), and high-contrast TikZ Decision Tree diagram.
- [ ] **Step 3: Compile and verify Chapter 5 in `main.tex`**
  Run `pdflatex main.tex`.
- [ ] **Step 4: Commit Chapter 5**

---

### Task 7: Transcribe Chapter 6: Support Vector Machines (SVM) (pp. 31–43)

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\ch06_svm.tex`

**Interfaces:**
- Consumes: Scanned pages 31 to 43 of `DocScanner 6 Oct 2026 19-28.pdf`
- Produces: Section-scoped Chapter 6 with maximum margin hyperplane, functional/geometric margin, vertical and diagonal separation cases, and complete numerical verifications.

- [ ] **Step 1: Inspect pages 31–43 high-resolution images**
  Render pages 31–43 at 200 DPI and verify vector algebra.
- [ ] **Step 2: Draft `ch06_svm.tex`**
  Include: Principles of SVM, hyperplane definition, functional and geometric margins, hard-margin condition $y_i(w^T x_i + b) \ge 1$, vertical separation case, diagonal separation case, margin width $M = 2/\|w\|$, Numerical Problem 6.1 (vertical support vectors, $w=[0.5, 0]^T$, query classification), Numerical Problem 6.2 (diagonal boundary $w=[-0.5, 0.5]^T$, complete verification table for all 7 points, query classification).
- [ ] **Step 3: Compile and verify Chapter 6 in `main.tex`**
  Run `pdflatex main.tex`.
- [ ] **Step 4: Commit Chapter 6**

---

### Task 8: Consolidate Comprehensive Formula Reference Sheet

**Files:**
- Create: `d:\MSQF\Semester III\ML\latex\chapters\formula_reference.tex`

**Interfaces:**
- Consumes: Formulas from Chapters 1 through 6
- Produces: Consolidated formula reference sheet grouped chapter by chapter with explicit "Where:" parameter blocks.

- [ ] **Step 1: Draft `formula_reference.tex`**
  Group by Chapter 1 to Chapter 6. Include all mathematical formulas, distance metrics, impurity measures, odds ratios, margins, and decision rules. Every box must include itemized parameter definitions.
- [ ] **Step 2: Include in `main.tex`**
- [ ] **Step 3: Compile and check formatting**
- [ ] **Step 4: Commit formula reference**

---

### Task 9: Two-Pass PDF Compilation & Quality Inspection

**Files:**
- Modify: `d:\MSQF\Semester III\ML\latex\main.tex`
- Output: `d:\MSQF\Semester III\ML\latex\main.pdf`

- [ ] **Step 1: Perform clean two-pass compilation**
  Run `pdflatex -interaction=nonstopmode main.tex` twice to resolve TOC, counters, and references.
- [ ] **Step 2: Inspect compiled PDF**
  Check page count, table of contents, absence of orphans, and visual symmetry.
- [ ] **Step 3: Commit final compiled artifacts**

---

### Task 10: Documentation Synchronization & Git Push

**Files:**
- Modify: `d:\MSQF\Semester III\ML\README.md`
- Modify: `d:\MSQF\Semester III\README.md`

- [ ] **Step 1: Update `ML/README.md`**
  Add `latex/` directory overview, chapter summary, and covered topics table.
- [ ] **Step 2: Update root `README.md`**
  Update ML section to include the newly compiled comprehensive LaTeX book.
- [ ] **Step 3: Run `git status`, stage all files, and commit**
- [ ] **Step 4: Run `git push origin main`**
- [ ] **Step 5: Verify clean Git working tree**
