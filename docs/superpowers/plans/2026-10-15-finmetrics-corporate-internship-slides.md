# FinMetrics-PU Corporate Internship LaTeX Slide Deck Implementation Plan (Updated)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an executive-grade, 11-slide Beamer presentation deck with custom TikZ diagrams and mathematical cards in `D:\MSQF\Semester III\Coporate Internship`, compiled to a pristine `main.pdf`.

**Architecture:** A modular LaTeX Beamer deck with custom "Pure Monochromatic Emerald & Jade" styling (`#064E3B`, `#EBF5EE`, `#059669` - ZERO GOLD), strictly adhering to TikZ symmetry and clearance rules, with clean macro separation and standalone slide files.

**Tech Stack:** LaTeX Beamer (`aspectratio=169`), TikZ (`arrows.meta`, `positioning`, `calc`, `shapes.geometric`), `tcolorbox` (`skins`, `theorems`, `fitting`), `lmodern`, `amsmath`, `mathtools`, MiKTeX `pdflatex`.

## Global Constraints
- Target directory: `D:\MSQF\Semester III\Coporate Internship`.
- Aspect ratio: $16:9$ widescreen (`aspectratio=169`).
- Color palette: Deep Emerald (`#064E3B`), Soft Sage (`#EBF5EE`), Mint Border (`#A7F3D0`), Vibrant Jade (`#059669`), Dark Charcoal (`#0F172A`). ZERO GOLD.
- TikZ clearance invariant: Inter-node connector stems and card boundaries maintain $\ge 0.7\,\text{cm}$ to $1.0\,\text{cm}$ clearance; arrow strokes $\ge 1.3\,\text{pt}$.
- Card symmetry invariant: Parallel cards across a row must share identical width and height calibrations.
- Git Habit: Final clean compilation followed by `git add`, `git commit`, and `git push origin main`.

---

### Task 1: Scaffolding, Logo, and Core Preamble Configuration

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\figures\pondicherry_university_logo.png` (copied from root)
- Create: `D:\MSQF\Semester III\Coporate Internship\preamble\packages.tex`
- Create: `D:\MSQF\Semester III\Coporate Internship\preamble\theme.tex`
- Create: `D:\MSQF\Semester III\Coporate Internship\preamble\macros.tex`

**Interfaces:**
- Consumes: Root `pondicherry_university_logo.png`.
- Produces: Theme colors (monochromatic emerald & jade), custom tcolorbox environments (`quantcard`, `mathcard`, `alertcard`), Beamer head/footlines, and student metadata macros.

- [ ] **Step 1: Copy logo and create directory hierarchy**
  Create `preamble/`, `slides/`, and `figures/` directories in `D:\MSQF\Semester III\Coporate Internship` and copy `pondicherry_university_logo.png`.
- [ ] **Step 2: Write `preamble/packages.tex`**
  Import `inputenc`, `fontenc`, `lmodern`, `amsmath`, `amssymb`, `mathtools`, `bm`, `tikz`, `tcolorbox`, `booktabs`, `tabularx`, `xcolor`, `hyperref`.
- [ ] **Step 3: Write `preamble/theme.tex`**
  Define color palette (`deepemerald`, `forestgreen`, `lightsage`, `mintborder`, `jade`, `paperbg`, `darkcharcoal`, `slatygray` — no gold). Configure custom Beamer templates: remove navigation symbols, set background color, define clean custom `frametitle` banner, and construct corporate footer.
- [ ] **Step 4: Write `preamble/macros.tex`**
  Define presenter macros (`\StudentName`, `\RollNumber`, `\ProgramName`, `\CompanyName`, `\InternalGuide`, `\ExternalSupervisor`), mathematical operators ($\text{MAD}$, $\text{IQR}$, $\text{safe\_divide}$), and custom card environments using `tcolorbox` with `jade` and `deepemerald` framing.
- [ ] **Step 5: Verify preamble syntax**
  Check that color definitions, font settings, and tcolorbox styles are clean.

---

### Task 2: Master Compilation Framework & Title Slide

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\main.tex`
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide01_title.tex`

**Interfaces:**
- Consumes: `preamble/packages.tex`, `preamble/theme.tex`, `preamble/macros.tex`, `figures/pondicherry_university_logo.png`.
- Produces: Compilable `main.pdf` rendering Slide 1.

- [ ] **Step 1: Write `slides/slide01_title.tex`**
  Implement high-end title slide featuring university crest, department/program banner, project title, subtitle, and an executive presenter attribution card with all student and supervisor macros.
- [ ] **Step 2: Write `main.tex`**
  Configure documentclass `\documentclass[aspectratio=169, 10pt]{beamer}` and include preambles and Slide 1.
- [ ] **Step 3: Compile test slide 1**
  Run: `pdflatex -interaction=nonstopmode -output-directory="." main.tex` in `D:\MSQF\Semester III\Coporate Internship`.
  Expected: Successful exit code 0 producing `main.pdf`.

---

### Task 3: Problem Statement & Financial Screening Bottlenecks

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide02_problem_statement.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `quantcard` from `macros.tex`.
- Produces: Slide 2 presenting the 3 analytical bottlenecks.

- [ ] **Step 1: Write `slides/slide02_problem_statement.tex`**
  Construct 3 symmetrical parallel cards:
  1. *Schema Heterogeneity & Ingestion Bottlenecks*: yfinance API variances, missing balance sheet entries.
  2. *Statistical Vulnerabilities (Mean Distortion)*: Failure of Gaussian $\mu, \sigma$ under heavy-tailed fat distributions.
  3. *Enterprise Analytical Requirements*: Robust non-parametric consensus and automated executive synthesis.
- [ ] **Step 2: Add Slide 2 to `main.tex` and compile**
  Verify visual symmetry and text height balance.

---

### Task 4: End-to-End System Architecture TikZ Pipeline

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide03_system_architecture.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: TikZ libraries (`arrows.meta`, `positioning`, `calc`).
- Produces: Slide 3 rendering full-width system architecture pipeline.

- [ ] **Step 1: Write `slides/slide03_system_architecture.tex`**
  Implement 4-stage horizontal pipeline with uniform cards ($2.9\,\text{cm}$ width, $3.2\,\text{cm}$ height), bold connector arrows ($1.4\,\text{pt}$) with $\ge 0.7\,\text{cm}$ clearance in `deepemerald`, and architectural callout banner.
- [ ] **Step 2: Add Slide 3 to `main.tex` and compile**
  Verify that arrowheads are uncompressed and node borders align symmetrically.

---

### Task 5: Ratio Engine Mechanism & Mathematical Guardrails

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide04_ratio_engine.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: Mathematical environments and `mathcard` from `macros.tex`.
- Produces: Slide 4 detailing the 16 ratios, weights, and division-by-zero guards.

- [ ] **Step 1: Write `slides/slide04_ratio_engine.tex`**
  Implement 5-pillar weighting structure (Profitability $30\%$, Solvency $25\%$, Growth $15\%$, Liquidity $15\%$, Efficiency $15\%$) and mathematical safe division formula:
  $$\text{safe\_divide}(a, b, \epsilon) = \begin{cases} a/b & \text{if } |b| > \epsilon \\ \text{NaN} & \text{otherwise} \end{cases}$$
- [ ] **Step 2: Add Slide 4 to `main.tex` and compile**
  Verify mathematical alignment and tabular symmetry.

---

### Task 6: Statistical Anomaly Algorithms: Tukey IQR & MAD Z-Scores

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide05_statistical_anomalies.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `mathcard` and equation formatting.
- Produces: Slide 5 with non-parametric outlier math.

- [ ] **Step 1: Write `slides/slide05_statistical_anomalies.tex`**
  Implement dual-column mathematical cards for Tukey Fences ($\text{IQR} = Q_3 - Q_1$, cutoffs $Q_1 - 1.5\,\text{IQR}$) and MAD Z-score ($M_i = \frac{0.6745(x_i - \text{median})}{\text{MAD}}$) with asymptotic Gaussian consistency proof note ($\Phi^{-1}(0.75) \approx 0.6745$).
- [ ] **Step 2: Add Slide 5 to `main.tex` and compile**
  Verify formula clarity and KaTeX/LaTeX math rendering.

---

### Task 7: Machine Learning Anomaly Engine: Isolation Forests

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide06_isolation_forest.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `mathcard`, `quantcard`.
- Produces: Slide 6 detailing multivariate isolation math and composite consensus.

- [ ] **Step 1: Write `slides/slide06_isolation_forest.tex`**
  Implement multivariate isolation tree logic in $\mathbb{R}^{16}$, average path length equation $c(n) = 2\ln(n-1) + 2\gamma - \frac{2(n-1)}{n}$, anomaly score $s(x,n) = 2^{-\mathbb{E}(h(x))/c(n)}$, and tri-layer consensus scoring.
- [ ] **Step 2: Add Slide 6 to `main.tex` and compile**
  Verify equation layout and typography.

---

### Task 8: Cross-Sectional Peer Benchmarking & Sigmoid Normalization

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide07_benchmarking_sigmoid.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `mathcard`.
- Produces: Slide 7 detailing non-linear scaling and weight redistribution.

- [ ] **Step 1: Write `slides/slide07_benchmarking_sigmoid.tex`**
  Implement peer percentile matrix ($P_{10}, Q_1, \text{Med}, Q_3, P_{90}$), Sigmoid mapping $S(x) = \frac{100}{1 + e^{-\kappa \frac{x-\text{Med}}{\text{IQR}}}}$, inverted leverage transformation $S_{\text{inv}} = 100 - S(x)$, and dynamic weight renormalization $w_i' = \frac{w_i}{\sum_{j \in \mathcal{V}} w_j}$.
- [ ] **Step 2: Add Slide 7 to `main.tex` and compile**
  Verify card formatting and mathematical typography.

---

### Task 9: Composite Solvency & Health Classification Matrix

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide08_risk_classification.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `quantcard`, `tabularx`, `booktabs`.
- Produces: Slide 8 presenting composite index formula and 5-tier classification grid.

- [ ] **Step 1: Write `slides/slide08_risk_classification.tex`**
  Implement composite index equation $\sum W_k \cdot \text{Pillar}_k$, 5-tier health classification table (Excellent, Strong, Moderate, Weak, Distressed), and ratio contribution delta formula $\Delta S_i = w_i'(S(x_i) - 50)$.
- [ ] **Step 2: Add Slide 8 to `main.tex` and compile**
  Verify table alignment, row colors, and badge styling.

---

### Task 10: Generative AI Narration & Multi-Format Enterprise Delivery

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide09_ai_reporting_pipeline.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `quantcard`.
- Produces: Slide 9 presenting LLM key rotation, Excel engine, and Streamlit delivery.

- [ ] **Step 1: Write `slides/slide09_ai_reporting_pipeline.tex`**
  Implement 3-pillar enterprise delivery card:
  1. *Gemini Round-Robin Key Rotation*: Rate limit mitigation and quantitative-to-prose translation.
  2. *Six-Tab Automated Excel Artifact*: Scorecard, Percentiles, Outliers, Scores, Narrative, Meta.
  3. *Streamlit UI & PDF Engine*: Interactive charts, Plotly visual integration, automated PDF reporting.
- [ ] **Step 2: Add Slide 9 to `main.tex` and compile**
  Verify layout symmetry.

---

### Task 11: Empirical Results & Sector Benchmarking Insights (NSE Case Study)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide10_empirical_results.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `quantcard`, `mathcard`.
- Produces: Slide 10 presenting cross-sector empirical validation on NSE.

- [ ] **Step 1: Write `slides/slide10_empirical_results.tex`**
  Implement comparative empirical validation:
  1. *Gaussian vs. Non-Parametric Robustness*: Empirical demonstration of mean distortion avoidance in NSE Automobile and IT filings.
  2. *Multivariate Anomaly Yield*: Isolation Forest detecting subtle leverage-growth mismatches undetectable by 1D IQR.
  3. *Pipeline Performance*: Sub-second ratio computation, $85\%$ Parquet cache hit rate.
- [ ] **Step 2: Add Slide 10 to `main.tex` and compile**
  Verify card balance and metrics table.

---

### Task 12: Conclusion, Internship Learnings & Future Roadmap

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\slides\slide11_conclusion_roadmap.tex`
- Modify: `D:\MSQF\Semester III\Coporate Internship\main.tex`

**Interfaces:**
- Consumes: `quantcard`, `theme.tex`.
- Produces: Slide 11 providing thesis conclusion, future directions, and Q&A banner.

- [ ] **Step 1: Write `slides/slide11_conclusion_roadmap.tex`**
  Implement 3 strategic pillars:
  1. *Key Internship Achievements*: Production-grade robust anomaly architecture deployed for NSE equities.
  2. *Quant Finance Industry Value*: Instant screening, data-driven credit risk assessment, equity research acceleration.
  3. *Future Roadmap*: Dynamic concept drift tracking, streaming tick-level ingestion, graph-based systemic contagion.
  4. Closing banner with GitHub repository `github.com/hi1r0/finmetrics-PU` and thank you note.
- [ ] **Step 2: Add Slide 11 to `main.tex` and compile**
  Verify complete 11-slide compilation.

---

### Task 13: Project README Documentation & PDF Compilation Verification

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\README.md`
- Verify: `D:\MSQF\Semester III\Coporate Internship\main.pdf`

**Interfaces:**
- Consumes: All slide files and compilation artifacts.
- Produces: User-facing `README.md` and verified `main.pdf`.

- [ ] **Step 1: Write `README.md`**
  Document project overview, exact presentation structure, instructions to compile with `pdflatex`, macro customization guide for the student, and bibliography/references.
- [ ] **Step 2: Execute clean 2-pass compilation**
  Run: `pdflatex -interaction=nonstopmode -output-directory="." main.tex` twice.
  Verify: Exactly 11 pages in `main.pdf`, 0 errors, 0 undefined references.

---

### Task 14: Git Staging, Commit & Push Synchronization

**Files:**
- Stage: All files in `D:\MSQF\Semester III\Coporate Internship`, `docs/`, and `README.md`.

- [ ] **Step 1: Run `git status`**
  Inspect all modified and untracked files.
- [ ] **Step 2: Stage and commit**
  Run `git add "Coporate Internship" "docs/superpowers/plans" "docs/superpowers/specs"`
  Run `git commit -m "feat(internship): complete high-end LaTeX Beamer presentation for FinMetrics-PU defense (emerald/jade palette)"`
- [ ] **Step 3: Push to remote**
  Run `git push origin main`
- [ ] **Step 4: Verify working tree clean**
  Run `git status` to ensure a clean state.
