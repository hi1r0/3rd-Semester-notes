# FinMetrics Suite: Corporate Internship Presentation

An executive-grade, 16-slide presentation deck in LaTeX Beamer for the Corporate Internship presentation in **M.Sc. Quantitative Finance** at **Pondicherry University (Ramanujan School of Mathematical Sciences, Department of Statistics)**.

The deck presents **FinMetrics Suite: Algorithms and Architecture for Automated Ratio Benchmarking and Anomaly Detection for NSE Equities**, featuring custom native TikZ system architecture diagrams, mathematical card containers, statistical plots, custom glowing jade bullets (zero triangles), and an **Executive Dark Mode** palette (deep obsidian emerald `#071411` with glowing jade and radiant mint accents).

---

## 1. Presentation Structure (16 Slides)

| Slide | Topic | Key Equations / Algorithmic Core | Primary Visual Components |
| :---: | :--- | :--- | :--- |
| **01** | **Title & Institutional Attribution** | Department of Statistics, Candidate, Faculty Guidance | University Crest, Centered Executive Attribution Card |
| **02** | **Analytical Motivations & Screening Latency** | Line-item variance, schema heterogeneity, manual screening lag | 4-card decongested operational layout |
| **03** | **Gaussian Breakdown & Outlier Masking** | $Z_i = \frac{x_i - \bar{\mu}}{\hat{\sigma}}$, Breakdown Point $\varepsilon^* = 0.0\%$, Masking Proof | TikZ Gaussian mean displacement curve vs. robust median |
| **04** | **System Architecture & Data Pipeline** | Decoupled 4-stage execution flow with $\ge 1.0\,\text{cm}$ clearance | Native TikZ 4-stage pipeline \& high-contrast drop-lines |
| **05** | **Ingestion Caching & Schema Harmonization** | Multi-tier Parquet caching ($>88.5\%$ hit rate), canonical aliases | 4-card caching architecture \& singularity validation |
| **06** | **Ratio Engine Architecture** | 5 weighted pillars (16 ratios) \& $\safedivide(a, b, \epsilon)$ | TikZ 5-pillar segmented hierarchy \& safe-divide mathcard |
| **07** | **Financial Decomposition & DuPont Analysis** | 3-stage \& 5-stage DuPont identities: $\text{ROE} = \text{Tax} \times \text{Int} \times \text{Margin} \times \text{Turnover} \times \text{Lev}$ | DuPont mathematical derivations \& cross-sector insights |
| **08** | **Non-Parametric Anomaly Detection** | Tukey IQR bounds: $\mathcal{F}_{\text{lower/upper}} = Q_{1/3} \mp 1.5\,\IQR$ | Native TikZ Boxplot (quartiles, fences, outliers) \& mathcard |
| **09** | **Modified MAD Dispersion Engine** | $\MAD = \median(|x_i - \text{Med}|)$, $0.6745$ consistency factor, $50\%$ BP | Gaussian half-normal consistency derivation \& Hoaglin rule |
| **10** | **Machine Learning Outlier Detection** | BST path length $c(n) = 2\ln(n-1) + 2\gamma - \frac{2(n-1)}{n}$, $s(x,n) = 2^{-\frac{\mathbb{E}(h)}{c(n)}}$ | Multivariate iForest in $\mathbb{R}^{16}$ \& tri-method consensus |
| **11** | **iForest Geometry & Subspace Partitioning** | 2D subspace cuts isolating anomalies in few bisections | Native TikZ 2D hyperplanes \& iTree hierarchy diagram |
| **12** | **Peer Benchmarking & Sigmoid Normalization** | $S(x) = \frac{100}{1 + e^{-\kappa \frac{x-\text{Med}}{\IQR}}}$, Dynamic NaN weights $w_i'$ | Native TikZ Sigmoid S-curve plot ($Q_1 \to 35$, Med $\to 50$, $Q_3 \to 65$) |
| **13** | **5-Tier Health Classification Matrix** | $\text{Composite} = \sum W_k \cdot \text{Pillar}_k \in [0, 100]$ | Native TikZ 5-tier Health Meter gauge \& complete credit table |
| **14** | **Portfolio Factor Attribution & Strategy** | Factor delta: $\Delta S_i = W_k \cdot w_{k,i}'(S(x_i) - 50.0)$ | Factor delta mathcard, positioning badges \& L/S equity factor |
| **15** | **AI Narration & Multi-Format Delivery** | Round-robin key rotation (`KEY_1..N`) | Native TikZ synthesis flow, 6-tab openpyxl Excel details |
| **16** | **Empirical Results & Research Roadmap** | 150+ NSE equities testing, GNN systemic debt contagion | Full-height comparative table \& 3 research pillars (No "Thank You") |

---

## 2. Directory Architecture

```text
D:\MSQF\Semester III\Coporate Internship\
|-- main.tex                         # Master Beamer document (aspectratio=169, 16 slides)
|-- main.pdf                         # Compiled 16-slide presentation deliverable (0 overfull warnings)
|-- README.md                        # Documentation of presentation structure & compilation
|-- figures/
|   `-- pondicherry_university_logo.png
|-- preamble/
|   |-- packages.tex                 # Core packages (beamer, tikz, tcolorbox, amsmath, tabularx)
|   |-- theme.tex                    # Executive Dark Mode palette, custom TikZ micro-dot bullets, empty footline
|   `-- macros.tex                   # Presenter metadata, mathematical operators, card macros, empty sourcepill
`-- slides/
    |-- slide01_title.tex            # University branding & centered executive attribution card
    |-- slide02_problem_statement.tex # Schema heterogeneity, line-item variance & manual audit latency
    |-- slide03_gaussian_breakdown.tex # Gaussian 0.0% breakdown point, masking proof & TikZ bell curve
    |-- slide04_system_architecture.tex # Full-width 4-stage horizontal pipeline with >= 1.0cm clearance
    |-- slide05_ingestion_caching.tex # Parquet multi-tier cache (>88.5% hit rate) & schema normalization
    |-- slide06_ratio_engine.tex     # 16 ratios, 5 analytical pillars & safe_divide guards
    |-- slide07_dupont_decomposition.tex # 3-stage & 5-stage DuPont identities & cross-sector utility
    |-- slide08_statistical_anomalies.tex # Native TikZ Tukey boxplot, fences & non-parametric bounds
    |-- slide09_mad_dispersion.tex   # MAD derivation, 0.6745 normal consistency & 50% breakdown
    |-- slide10_isolation_forest.tex # Multivariate iForest in R^16, BST path length & consensus
    |-- slide11_iforest_geometry.tex # 2D subspace hyperplane bisections & iTree depth hierarchy
    |-- slide12_benchmarking_sigmoid.tex # Sigmoid S-curve plot & dynamic NaN weight redistribution
    |-- slide13_risk_classification.tex # 5-tier health gauge & credit health matrix (zero vertical overlap)
    |-- slide14_portfolio_attribution.tex # Factor delta attribution, quartile badges & L/S equity factor
    |-- slide15_ai_reporting_pipeline.tex # Round-robin LLM synthesis & 6-tab openpyxl Excel exports
    `-- slide16_empirical_roadmap.tex # 150+ NSE empirical study & GNN contagion roadmap (full height)
```

---

## 3. Presenter & Institutional Metadata

Configured in `preamble/macros.tex`:

- **Project Title:** FinMetrics Suite
- **Presentation Type:** Corporate Internship
- **Candidate:** N Rohit Vedhanandh
- **Register Number:** 25MSQUFPY0002
- **Faculty Guidance:** Dr. Kiruthika
- **Department:** Department of Statistics
- **School:** Ramanujan School of Mathematical Sciences
- **University:** Pondicherry University
- **Program:** M.Sc. Quantitative Finance (MSQF)

---

## 4. Color Palette: Executive Dark Mode (Zero Gold)

| Color Role | Name | Hex Code | Purpose |
| :--- | :--- | :--- | :--- |
| **Canvas Background** | `paperbg` | `#071411` | Deep obsidian emerald canvas |
| **Elevated Card Container**| `cardbg` | `#0D211B` | Elevated dark card background for content containers |
| **Inset Box / Formulas** | `cardinner` | `#132F26` | Inset mathcards and formula containers |
| **Border Outline** | `mintborder` | `#1E4E3F` | Subtle dark emerald outline for cards and dividers |
| **Titles & Frametitles** | `deepemerald` | `#34D399` | Radiant mint for high-contrast titles and headers |
| **Subtitles & Badges** | `forestgreen` | `#10B981` | Glowing jade for section subtitles and active badges |
| **Accent & Active Nodes** | `jade` | `#059669` | Vibrant accent for outliers, arrows, and key highlights |
| **Body Typography** | `darkcharcoal` | `#F8FAFC` | Platinum white high-contrast text |
| **Secondary Typography** | `slatygray` | `#94A3B8` | Cool silver for mathematical annotations and subheadings |

---

## 5. Compilation Instructions

Compile from PowerShell or terminal inside `D:\MSQF\Semester III\Coporate Internship`:

```powershell
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Two compilation passes resolve all cross-references, bounding boxes, and navigation counters. The output compiles with **zero overfull warnings** and exit code 0, generating exactly **16 pages** in `main.pdf`.

---

## 6. Primary References & Source Code

- **GitHub Repository**: [`https://github.com/hi1r0/finmetrics-PU`](https://github.com/hi1r0/finmetrics-PU)
- **Tukey, J. W. (1977)**: *Exploratory Data Analysis*, Addison-Wesley.
- **Iglewicz, B. & Hoaglin, D. C. (1993)**: *How to Detect and Handle Outliers*, ASQC Basic References in Quality Control.
- **Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008)**: *Isolation Forest*, IEEE ICDM, pp. 413–422.
