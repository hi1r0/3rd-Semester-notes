# Design Document: FinMetrics-PU Corporate Internship High-End LaTeX Slide Deck (Updated)

**Date:** 2026-10-15  
**Topic:** FinMetrics-PU High-End LaTeX Slides for Corporate Internship  
**Directory Target:** `D:\MSQF\Semester III\Coporate Internship`  
**Reference Material:** `FinMetrics_PU_Algorithms_and_Mechanism.pptx`, `https://github.com/hi1r0/finmetrics-PU`  
**Palette Revision:** Pure Monochromatic Emerald & Jade (Zero Gold)

---

## 1. Executive Summary & Objectives

The goal is to design, implement, and compile an executive-grade presentation slide deck in LaTeX Beamer for the Corporate Internship defense in M.Sc. Quantitative Finance at Pondicherry University. 

The deck is based on **FinMetrics-PU: Cross-Sectional Financial Outlier Detection and Sector Benchmarking System for NSE Equities**. It translates the high-level concepts from `FinMetrics_PU_Algorithms_and_Mechanism.pptx` into mathematically rigorous, publication-grade slides with custom TikZ architecture diagrams, balanced multi-pillar metric cards, and a cohesive, pure green quantitative color scheme.

---

## 2. Visual Aesthetic & Color Palette: "Pure Monochromatic Emerald & Jade"

Per explicit user direction, all warm gold/amber tones are replaced with a sophisticated monochromatic green-emerald spectrum:

- **Primary Brand / Structure (`deepemerald`):** `#064E3B` / `RGB(6, 78, 59)` — Slide titles, structural header bars, major framing borders.
- **Secondary Tone (`forestgreen`):** `#0D5C3A` / `RGB(13, 92, 58)` — Section banners, card title text, primary TikZ nodes.
- **Vibrant Accent / Badges (`jade`):** `#059669` / `RGB(5, 150, 105)` — Replaces gold entirely. Used for formula badges, active pipeline nodes, key mathematical variables, tags, and contrast markers.
- **Card Fill (`lightsage`):** `#EBF5EE` / `RGB(235, 245, 238)` — Soft, glare-free container background for content cards and formula boxes.
- **Card Border (`mintborder`):** `#A7F3D0` / `RGB(167, 243, 208)` — Subtle, crisp $0.8\,\text{pt}$ outline ensuring card definition without visual heaviness.
- **Slide Background (`paperbg`):** `#F7FBF9` / `RGB(247, 251, 249)` — Off-white soft mint parchment avoiding harsh screen glare.
- **Primary Typography (`darkcharcoal`):** `#0F172A` / `RGB(15, 23, 42)` — High-contrast dark slate body and formula text.
- **Muted Subtitles (`slatygray`):** `#475569` / `RGB(71, 85, 105)` — Slide subtitles, source tags, footnotes.

### Geometry & Typography
- **Aspect Ratio:** $16:9$ widescreen (`\documentclass[aspectratio=169, 10pt]{beamer}`).
- **Font Stack:** Latin Modern Sans (`lmodern`) paired with standard AMS math symbols (`amsmath`, `amssymb`, `mathtools`, `bm`).
- **Frametitle Banner:** Sleek header banner containing the topic title, section breadcrumb, and slide progress tracker.
- **Footline:** Minimalist footer displaying the author, institutional affiliation (Pondicherry University), project title, and page numbering ($n / N$).

---

## 3. Strict TikZ Invariants & Document Structuring Standards

All diagrams and parallel cards adhere strictly to the repository formatting invariants:
1. **Uniform Box Dimensions (Symmetry):** Parallel cards and horizontal workflow stages share identical width and height calibrations.
2. **Clearance & Arrow Spacing:** All inter-node connector stems maintain $\ge 0.7\,\text{cm}$ to $1.0\,\text{cm}$ clearance between card boundaries; arrowheads never squish against borders.
3. **High-Contrast Connectors:** Arrow strokes are rendered with bold stroke widths ($\ge 1.3\,\text{pt}$ to $1.5\,\text{pt}$) using `deepemerald` or `jade`.
4. **No Double-Numbering:** Headers rely entirely on Beamer's automatic framing.

---

## 4. Comprehensive 11-Slide Master Architecture

The deck comprises exactly 11 focused, high-density slides:

### Slide 1: Title Slide & Institutional Attribution
- University branding (`pondicherry_university_logo.png`).
- Presentation header: `PONDICHERRY UNIVERSITY | DEPARTMENT OF ECONOMICS | M.SC. QUANTITATIVE FINANCE`.
- Project Title: `FinMetrics-PU: NSE Financial Outlier Detective`.
- Subtitle: `Algorithms and Architecture for Automated Ratio Benchmarking and Anomaly Detection`.
- Presenter details card with dedicated LaTeX macros:
  - Student Name: `\StudentName`
  - Register / Roll Number: `\RollNumber`
  - Degree & Program: `\ProgramName`
  - Host Organization / Company: `\CompanyName`
  - Internal Academic Guide: `\InternalGuide`
  - External Industry Supervisor: `\ExternalSupervisor`
  - Presentation Date: `\PresentationDate`

### Slide 2: Problem Statement & Financial Screening Bottlenecks
- Three symmetrical vertical cards:
  1. *Schema Heterogeneity & Ingestion Bottlenecks*: Yahoo Finance API variance across NSE equities, missing values, asynchronous filing formats.
  2. *Statistical Vulnerabilities (Mean Distortion)*: Failure of Gaussian assumption $X \sim \mathcal{N}(\mu, \sigma^2)$ in heavy-tailed corporate ratios; skewness induced by single distressed firms.
  3. *Enterprise Analytical Requirements*: Non-parametric robust dispersion, multi-tier anomaly consensus, automated executive synthesis.

### Slide 3: End-to-End System Architecture (TikZ 4-Stage Horizontal Pipeline)
- Full-width 4-stage horizontal TikZ pipeline with $\ge 0.7\,\text{cm}$ connector clearance:
  - Stage 1: Data Acquisition (`SectorLoader` + `yfinance` + Parquet Cache)
  - Stage 2: Financial Parsing (`FinancialParser` + Canonical Alias Mapping)
  - Stage 3: Analytical Core (`RatioEngine` + `OutlierEngine` + `BenchmarkCore`)
  - Stage 4: Reporting & Delivery (`GeminiAIHandler` + `ReportGenerator` + Streamlit)
- Architectural summary container card underneath highlighting asynchronous caching, safe division, and decoupled micro-layers.

### Slide 4: Ratio Engine Mechanism & Mathematical Guardrails
- Five-Pillar analytical framework:
  - Profitability ($30\%$): Gross, Operating, Net margins, $\text{ROE} = \frac{\text{Net Income}}{\text{Equity}}$, $\text{ROA} = \frac{\text{Net Income}}{\text{Total Assets}}$.
  - Solvency & Growth ($40\%$): $\frac{D}{E}$, Debt Ratio, $\text{ICR} = \frac{\text{EBIT}}{\text{Interest}}$; CAGR growth.
  - Liquidity & Efficiency ($30\%$): Current, Quick, Cash ratios; Asset, Inventory, AR turnovers.
  - *Mathematical Guard Box*: Division-by-Zero & Singularity Guard:
    $$\text{safe\_divide}(a, b, \epsilon) = \begin{cases} a/b & \text{if } |b| > \epsilon \\ \text{NaN} & \text{otherwise} \end{cases}$$

### Slide 5: Statistical Anomaly Algorithms: Tukey IQR & MAD Z-Scores
- Comparative mathematical formulations:
  - *Tukey Fences (Non-Parametric Interquartile Dispersion)*:
    $$\text{IQR} = Q_3 - Q_1, \quad \mathcal{F}_{\text{lower}} = Q_1 - 1.5 \cdot \text{IQR}, \quad \mathcal{F}_{\text{upper}} = Q_3 + 1.5 \cdot \text{IQR}$$
    $$\text{Outlier Flag: } x_i \notin [\mathcal{F}_{\text{lower}}, \mathcal{F}_{\text{upper}}]$$
  - *Modified Z-Score via Median Absolute Deviation (MAD)*:
    $$\text{MAD} = \text{median}\left(|x_i - \text{median}(X)|\right)$$
    $$M_i = \frac{0.6745 \cdot (x_i - \text{median}(X))}{\text{MAD}}, \quad \text{Outlier if } |M_i| > 3.5$$
  - *Mathematical Rationale Note*: Why $0.6745$? Since $\Phi^{-1}(0.75) \approx 0.6745$, this normalizes MAD to match Gaussian standard deviation under normality.

### Slide 6: Machine Learning Anomaly Engine: Isolation Forests
- Multivariate anomaly isolation in $\mathbb{R}^{16}$:
  - Algorithm mechanics: Recursive random hyperplane partitioning, isolating outliers at shallow depths.
  - Average Path Length Equation:
    $$c(n) = 2 \ln(n - 1) + 2\gamma - \frac{2(n - 1)}{n}, \quad \gamma \approx 0.5772156649 \text{ (Euler-Mascheroni)}$$
  - Anomaly Score Formulation:
    $$s(x, n) = 2^{-\frac{\mathbb{E}(h(x))}{c(n)}}, \quad s \ge 0.6 \implies \text{Definite Anomaly}$$
  - Tri-Method Consensus Matrix: Combining Tukey IQR, MAD Z-Score, and iForest into a 3-tier severity score.

### Slide 7: Cross-Sectional Peer Benchmarking & Sigmoid Normalization
- Mathematical normalization cards:
  - Percentile Anchor Computation: $P_{10}, Q_1, \text{Median}, Q_3, P_{90}$ across sector peers.
  - Non-Linear Sigmoid Score Mapping ($0 \text{ to } 100$ scale):
    $$S(x) = \frac{100}{1 + \exp\left(-\kappa \cdot \frac{x - \text{Median}(X)}{\text{IQR}(X)}\right)}$$
  - Inverted Scale Transformation for Leverage/Risk ratios (Debt/Equity):
    $$S_{\text{inv}}(x) = 100 - S(x)$$
  - Dynamic Weight Redistribution (Handling missing/NaN filings):
    $$w_i' = \frac{w_i}{\sum_{j \in \mathcal{V}} w_j}$$

### Slide 8: Composite Solvency & Health Classification Matrix
- Hierarchical Composite Health Index:
  $$\text{Composite Score} = \sum_{k=1}^5 W_k \cdot \text{Pillar}_k = \sum_{k=1}^5 W_k \left( \sum_{i \in \text{Pillar}_k} w_{k,i}' \cdot S(x_i) \right)$$
- Five-Tier Classification Grid:
  - $\ge 80$: **Excellent** (Distinguished financial health)
  - $65 - 79$: **Strong** (Robust operational stability)
  - $50 - 64$: **Moderate** (Average peer standing)
  - $35 - 49$: **Weak** (Sub-par leverage/profitability)
  - $< 35$: **Distressed** (Imminent financial distress)
- Ratio Contribution Analysis: Quantifying marginal positive/negative point drag $\Delta S_i = w_i' (S(x_i) - 50)$.

### Slide 9: Generative AI Narration & Multi-Format Enterprise Delivery
- System Integration card:
  - *Automated LLM Synthesis*: Google Gemini API round-robin key rotation (`GEMINI_API_KEY_1..N`) to bypass rate limits; prompt engineering translating quantitative vectors into C-suite prose.
  - *Six-Tab Automated Excel Artifact*: Scorecard, Peer Percentiles, Outlier Register, Sigmoid Scores, Executive Narrative, Metadata.
  - *Interactive Streamlit & Automated PDF Engine*: Plotly radar & box plots, automated LaTeX/WeasyPrint report compilation.

### Slide 10: Empirical Results & Sector Benchmarking Insights (NSE Case Study)
- Comparative validation across NSE sectors (Automobile, IT, FMCG, Banking):
  - Robustness comparison: Gaussian Z-score vs. MAD Z-score under extreme skewness.
  - Empirical outlier discovery rates (univariate vs. multivariate isolation).
  - Production performance metrics: latency, caching hit rate ($>85\%$), zero-division safety.

### Slide 11: Conclusion, Internship Learnings & Future Roadmap
- Key technical contributions & quantitative achievements during the internship.
- Practical business impact for algorithmic screening and equity research.
- Future enhancements: Time-series dynamic drift detection, real-time tick streaming, graph neural network supply-chain risk propagation.
- Acknowledgments & Q&A banner with repository link `github.com/hi1r0/finmetrics-PU`.

---

## 5. File & Directory Layout

```
D:\MSQF\Semester III\Coporate Internship\
|-- main.tex                         # Master compilation document
|-- README.md                        # Documentation of presentation structure & compilation
|-- preamble\
|   |-- packages.tex                 # Core Beamer, TikZ, and tcolorbox imports
|   |-- theme.tex                    # Custom Beamer theme, Emerald/Jade palette, header/footer
|   |-- macros.tex                   # Presenter metadata, mathematical operators, card macros
|-- slides\
|   |-- slide01_title.tex
|   |-- slide02_problem_statement.tex
|   |-- slide03_system_architecture.tex
|   |-- slide04_ratio_engine.tex
|   |-- slide05_statistical_anomalies.tex
|   |-- slide06_isolation_forest.tex
|   |-- slide07_benchmarking_sigmoid.tex
|   |-- slide08_risk_classification.tex
|   |-- slide09_ai_reporting_pipeline.tex
|   |-- slide10_empirical_results.tex
|   |-- slide11_conclusion_roadmap.tex
|-- figures\
|   |-- pondicherry_university_logo.png
```

---

## 6. Verification and Compilation Strategy

1. **Compilation Engine:** `pdflatex` run via PowerShell:
   ```powershell
   pdflatex -interaction=nonstopmode -output-directory="." main.tex
   pdflatex -interaction=nonstopmode -output-directory="." main.tex
   ```
2. **Visual Verification:** Check output `main.pdf` page count (exactly 11 slides), inspect layout symmetry, verify zero LaTeX errors or missing reference warnings.
3. **Git Tracking & Synchronization:** Stage, commit with descriptive message, and push to remote `main` branch according to repository rules.
