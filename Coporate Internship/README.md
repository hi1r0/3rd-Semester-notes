# FinMetrics Suite: Corporate Internship Presentation

An executive-grade, 16-slide presentation suite for the Corporate Internship presentation in **M.Sc. Quantitative Finance** at **Pondicherry University (Ramanujan School of Mathematical Sciences, Department of Statistics)**.

The presentation presents **FinMetrics Suite: Algorithms and Architecture for Automated Ratio Benchmarking and Anomaly Detection for NSE Equities**, delivered in two synchronized, production-grade formats:
1. **Interactive Web Presentation Deck (Slidev + Vue 3)**: A modern, animated HTML5 presentation running on Slidev v51, Vite, UnoCSS, and 16 custom interactive Vue 3 components with Apple Keynote obsidian and jade aesthetics.
2. **Executive LaTeX Beamer PDF Deck (`main.pdf`)**: A publication-grade 16-slide PDF deck with custom native TikZ architecture diagrams, mathematical card containers, statistical plots, custom glowing jade bullets (zero triangles), and an Executive Dark Mode palette (0 overfull warnings).

---

## 1. Presentation Structure (16 Slides)

| Slide | Topic | Key Equations / Algorithmic Core | Primary Visual Components | Interactive Vue 3 Component |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **Title & Institutional Attribution** | Department of Statistics, Candidate, Faculty Guidance | University Crest, Centered Attribution Card | `TitleHero.vue` |
| **02** | **Analytical Motivations & Screening Latency** | Line-item variance, schema heterogeneity, manual screening lag | 4-card operational layout, animated latency comparison | `LatencyComparison.vue` |
| **03** | **Gaussian Breakdown & Outlier Masking** | $Z_i = \frac{x_i - \bar{\mu}}{\hat{\sigma}}$, Breakdown Point $\varepsilon^* = 0.0\%$, Masking Proof | Dynamic Gaussian bell curve vs. robust median, interactive perturbation slider | `GaussianBreakdown.vue` |
| **04** | **System Architecture & Data Pipeline** | Decoupled 4-stage execution flow with $\ge 1.0\,\text{cm}$ clearance | 4-stage interactive pipeline flow with step inspection & throughput stats | `SystemPipeline.vue` |
| **05** | **Ingestion Caching & Schema Harmonization** | Multi-tier Parquet caching ($>88.5\%$ hit rate), canonical aliases | Interactive caching tier inspector & singularity validation matrix | `CacheHarmonizer.vue` |
| **06** | **Ratio Engine Architecture** | 5 weighted pillars (16 ratios) \& $\text{safe\_divide}(a, b, \epsilon)$ | 5-pillar segmented hierarchy, live ratio weights, safe-divide guards | `RatioEnginePillars.vue` |
| **07** | **Financial Decomposition & DuPont Analysis** | 3-stage \& 5-stage DuPont identities: $\text{ROE} = \text{Tax} \times \text{Int} \times \text{Margin} \times \text{Turnover} \times \text{Lev}$ | Interactive 3-stage vs. 5-stage DuPont toggle with sector presets (IT vs. FMCG) | `DuPontDecomposition.vue` |
| **08** | **Non-Parametric Anomaly Detection** | Tukey IQR bounds: $\mathcal{F}_{\text{lower/upper}} = Q_{1/3} \mp 1.5\,\text{IQR}$ | Interactive boxplot with customizable multiplier $k$, quartile fences & outlier tags | `TukeyBoxplot.vue` |
| **09** | **Modified MAD Dispersion Engine** | $\text{MAD} = \text{median}(\|x_i - \text{Med}\|)$, $0.6745$ consistency factor, $50\%$ BP | Interactive Gaussian half-normal consistency scaling & Hoaglin rule demonstration | `MadDispersion.vue` |
| **10** | **Machine Learning Outlier Detection** | BST path length $c(n) = 2\ln(n-1) + 2\gamma - \frac{2(n-1)}{n}$, $s(x,n) = 2^{-\frac{\mathbb{E}(h)}{c(n)}}$ | Multivariate iForest in $\mathbb{R}^{16}$, path length calculator & tri-method consensus | `IsolationForestTree.vue` |
| **11** | **iForest Geometry & Subspace Partitioning** | 2D subspace cuts isolating anomalies in few bisections | Interactive 2D subspace hyperplane simulator with step-by-step bisection cuts | `SubspacePartitioning.vue` |
| **12** | **Peer Benchmarking & Sigmoid Normalization** | $S(x) = \frac{100}{1 + e^{-\kappa \frac{x-\text{Med}}{\text{IQR}}}}$, Dynamic NaN weights $w_i'$ | Interactive Sigmoid S-curve ($Q_1 \to 35$, Med $\to 50$, $Q_3 \to 65$) with steepness slider | `SigmoidCurve.vue` |
| **13** | **5-Tier Health Classification Matrix** | $\text{Composite} = \sum W_k \cdot \text{Pillar}_k \in [0, 100]$ | Interactive radial health gauge & complete credit risk classification matrix | `HealthGauge.vue` |
| **14** | **Portfolio Factor Attribution & Strategy** | Factor delta: $\Delta S_i = W_k \cdot w_{k,i}'(S(x_i) - 50.0)$ | Factor delta waterfall chart, quartile badges & L/S market-neutral alpha | `FactorAttribution.vue` |
| **15** | **AI Narration & Multi-Format Delivery** | Round-robin key rotation (`KEY_1..N`) | Interactive AI synthesis pipeline flow & 6-tab openpyxl Excel audit | `DeliveryPipeline.vue` |
| **16** | **Empirical Results & Research Roadmap** | 150+ NSE equities testing, GNN systemic debt contagion | Full-height comparative table & 3 interactive research horizons (No "Thank You") | `EmpiricalRoadmap.vue` |

---

## 2. Slidev Interactive Web Presentation (`html/`)

The `html/` directory houses an executive-grade interactive presentation powered by [Slidev](https://sli.dev/), [Vue 3](https://vuejs.org/), and [UnoCSS](https://unocss.dev/).

### Key Capabilities & Architectural Highlights
- **16 Custom Interactive Vue 3 Components**: Each slide is backed by a dedicated, animated Vue 3 component offering interactive mathematical simulations, real-time parameter manipulation, hover tooltips, and animated SVG transitions.
- **Apple Keynote Obsidian & Jade Design System**:
  - **Canvas Background**: Deep obsidian emerald (`#071411`)
  - **Elevated Glassmorphic Cards**: Dark container backgrounds (`#0D211B`), subtle border outlines (`#1E4E3F`), and soft backdrop blur
  - **Luminescent Accents**: Radiant mint (`#34D399`), glowing jade (`#10B981`), and deep emerald (`#059669`)
  - **Typography**: High-contrast platinum white (`#F8FAFC`) for body text, cool silver (`#94A3B8`) for secondary annotations, and JetBrains Mono for mathematical formulas and code
  - **Zero Gold Palette**: Pure emerald/mint/obsidian hierarchy adhering strictly to institutional aesthetic guidelines
- **Responsive Vector Graphics (SVG)**: Custom mathematical plots, boxplots, Gaussians, S-curves, and tree partitions rendered natively in high-DPI vector format.
- **Presenter Mode & Speaker Notes**: Comprehensive speaker notes embedded via markdown `<!-- notes -->` blocks for every slide.

### Interactive Components Catalogue

1. **`TitleHero.vue`** (Slide 1): Animated institutional crest, floating metadata badge pills, and glowing card borders.
2. **`LatencyComparison.vue`** (Slide 2): Interactive bar chart comparing manual audit latency (12–18 hrs) against automated FinMetrics execution (4.2 s, $99.96\%$ reduction).
3. **`GaussianBreakdown.vue`** (Slide 3): Interactive Gaussian bell curve vs. robust median with a live outlier perturbation slider demonstrating $0.0\%$ breakdown point and masking.
4. **`SystemPipeline.vue`** (Slide 4): Decoupled 4-stage horizontal pipeline with interactive stage tabs displaying latency, inputs, outputs, and validation rules.
5. **`CacheHarmonizer.vue`** (Slide 5): Tiered cache performance inspector showing memory vs. Parquet hit rates ($88.5\%$) and schema alias resolution table.
6. **`RatioEnginePillars.vue`** (Slide 6): 5-pillar weight breakdown (Profitability, Solvency, Liquidity, Efficiency, Valuation) with interactive ratio cards and safe-divide zero-denominator guards.
7. **`DuPontDecomposition.vue`** (Slide 7): Switchable 3-stage and 5-stage DuPont identity breakdown with sector benchmark presets (TCS vs. HUL vs. Tata Motors).
8. **`TukeyBoxplot.vue`** (Slide 8): Interactive non-parametric boxplot with dynamic IQR multiplier slider ($k \in [1.0, 3.0]$), quartile fences ($Q_1, Q_3$), and real-time outlier detection.
9. **`MadDispersion.vue`** (Slide 9): Interactive Modified MAD calculation visualizer comparing sample standard deviation distortion with median absolute deviation ($0.6745$ scaling consistency).
10. **`IsolationForestTree.vue`** (Slide 10): Interactive tree depth simulation displaying binary search tree (BST) average path length $c(n)$ and anomaly score $s(x,n)$ calculation across 100 estimators.
11. **`SubspacePartitioning.vue`** (Slide 11): 2D feature space bisection simulation showing how random axis-parallel cuts isolate anomalous data points in few splits compared to clustered inliers.
12. **`SigmoidCurve.vue`** (Slide 12): Interactive Sigmoid normalization S-curve with adjustable steepness factor $\kappa$, quartile anchor mappings ($Q_1 \to 35$, Med $\to 50$, $Q_3 \to 65$), and NaN weight redistribution.
13. **`HealthGauge.vue`** (Slide 13): Animated radial speedometer gauge displaying composite health score $[0, 100]$ alongside the 5-tier credit rating classification matrix.
14. **`FactorAttribution.vue`** (Slide 14): Interactive portfolio factor attribution waterfall showing individual ratio deltas $\Delta S_i$ and quartile positioning.
15. **`DeliveryPipeline.vue`** (Slide 15): Interactive multi-format delivery pipeline showing round-robin LLM key rotation and 6-tab openpyxl Excel workbook generator.
16. **`EmpiricalRoadmap.vue`** (Slide 16): Empirical findings from 150+ NSE equities with sector outlier benchmarks and interactive 3-pillar research roadmap (GNNs, intraday streaming, cross-border multi-currency).

### Running & Building the Slidev Deck

Navigate to the `html/` directory:

```powershell
cd "D:\MSQF\Semester III\Coporate Internship\html"
```

#### 1. Development Mode (Live Reload Server)
Starts the Slidev development server with hot-module replacement (HMR):

```powershell
npm run dev
```

The presentation is accessible at `http://localhost:3030`. Presenter mode is available at `http://localhost:3030/presenter`.

#### 2. Production Build (Static Single-Page App)
Compiles the complete presentation, Vue components, and UnoCSS styles into optimized static files:

```powershell
npm run build
```

The production output is generated in `html/dist/` with zero errors.

#### 3. Local Preview of Static Build
To preview the compiled `dist/` directory locally:

```powershell
npx serve dist
```

#### 4. Exporting to PDF / PNG
To export slides to PDF (requires Playwright/Chromium):

```powershell
npm run export
```

---

## 3. Executive LaTeX Beamer Deck (`main.tex` / `main.pdf`)

The root directory provides the production-grade LaTeX Beamer presentation compiled with `pdflatex`.

### Color Palette: Executive Dark Mode (Zero Gold)

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

### Compilation Instructions

Compile from PowerShell or terminal inside `D:\MSQF\Semester III\Coporate Internship`:

```powershell
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Two compilation passes resolve all cross-references, bounding boxes, and navigation counters. The output compiles with **zero overfull warnings** and exit code 0, generating exactly **16 pages** in `main.pdf`.

---

## 4. Directory Architecture

```text
D:\MSQF\Semester III\Coporate Internship\
|-- main.tex                         # Master Beamer document (aspectratio=169, 16 slides)
|-- main.pdf                         # Compiled 16-slide presentation deliverable (0 overfull warnings)
|-- README.md                        # Master documentation of presentation structure & execution
|-- figures/
|   `-- pondicherry_university_logo.png # Institutional crest for Beamer deck
|-- preamble/
|   |-- packages.tex                 # Core packages (beamer, tikz, tcolorbox, amsmath, tabularx)
|   |-- theme.tex                    # Executive Dark Mode palette, custom TikZ micro-dot bullets, empty footline
|   `-- macros.tex                   # Presenter metadata, mathematical operators, card macros
|-- slides/
|   |-- slide01_title.tex            # University branding & centered executive attribution card
|   |-- slide02_problem_statement.tex # Schema heterogeneity, line-item variance & manual audit latency
|   |-- slide03_gaussian_breakdown.tex # Gaussian 0.0% breakdown point, masking proof & TikZ bell curve
|   |-- slide04_system_architecture.tex # Full-width 4-stage horizontal pipeline with >= 1.0cm clearance
|   |-- slide05_ingestion_caching.tex # Parquet multi-tier cache (>88.5% hit rate) & schema normalization
|   |-- slide06_ratio_engine.tex     # 16 ratios, 5 analytical pillars & safe_divide guards
|   |-- slide07_dupont_decomposition.tex # 3-stage & 5-stage DuPont identities & cross-sector utility
|   |-- slide08_statistical_anomalies.tex # Native TikZ Tukey boxplot, fences & non-parametric bounds
|   |-- slide09_mad_dispersion.tex   # MAD derivation, 0.6745 normal consistency & 50% breakdown
|   |-- slide10_isolation_forest.tex # Multivariate iForest in R^16, BST path length & consensus
|   |-- slide11_iforest_geometry.tex # 2D subspace hyperplane bisections & iTree depth hierarchy
|   |-- slide12_benchmarking_sigmoid.tex # Sigmoid S-curve plot & dynamic NaN weight redistribution
|   |-- slide13_risk_classification.tex # 5-tier health gauge & credit health matrix (zero vertical overlap)
|   |-- slide14_portfolio_attribution.tex # Factor delta attribution, quartile badges & L/S equity factor
|   |-- slide15_ai_reporting_pipeline.tex # Round-robin LLM synthesis & 6-tab openpyxl Excel exports
|   `-- slide16_empirical_roadmap.tex # 150+ NSE empirical study & GNN contagion roadmap (full height)
`-- html/                            # Slidev Interactive Web Presentation
    |-- package.json                 # Slidev & Vue 3 dependencies and npm scripts
    |-- package-lock.json            # Deterministic lockfile
    |-- slides.md                    # Master 16-slide Slidev presentation markdown
    |-- uno.config.ts                # UnoCSS theme configurations & font mappings
    |-- vite.config.ts               # Vite bundler plugins and settings
    |-- dist/                        # Production build output (generated by npm run build)
    |-- public/
    |   `-- pondicherry_university_logo.png # Institutional crest asset
    |-- styles/
    |   `-- index.css                # Obsidian & jade CSS variables, keyframe animations, typography
    `-- components/                  # 16 Interactive animated Vue 3 presentation components
        |-- TitleHero.vue            # Slide 1: Animated crest & executive attribution
        |-- LatencyComparison.vue    # Slide 2: Manual vs. automated processing latency comparison
        |-- GaussianBreakdown.vue    # Slide 3: Interactive Gaussian curve with outlier perturbation slider
        |-- SystemPipeline.vue       # Slide 4: 4-stage pipeline flow with interactive step inspection
        |-- CacheHarmonizer.vue      # Slide 5: Parquet cache tier hit rate & alias harmonization table
        |-- RatioEnginePillars.vue   # Slide 6: 5-pillar weight breakdown & safe_divide calculation guards
        |-- DuPontDecomposition.vue  # Slide 7: Interactive 3-stage vs. 5-stage DuPont decomposition
        |-- TukeyBoxplot.vue         # Slide 8: Interactive non-parametric Tukey boxplot with k-multiplier slider
        |-- MadDispersion.vue        # Slide 9: Modified MAD dispersion engine & normal consistency scaling
        |-- IsolationForestTree.vue  # Slide 10: Machine learning outlier detection & BST path lengths
        |-- SubspacePartitioning.vue # Slide 11: 2D subspace hyperplanes & random bisection cuts
        |-- SigmoidCurve.vue         # Slide 12: Sigmoid S-curve normalization with steepness parameter tuning
        |-- HealthGauge.vue          # Slide 13: Radial 5-tier health gauge & credit risk matrix
        |-- FactorAttribution.vue    # Slide 14: Portfolio factor attribution waterfall & L/S alpha badges
        |-- DeliveryPipeline.vue     # Slide 15: Round-robin LLM synthesis & 6-tab Excel report generator
        `-- EmpiricalRoadmap.vue     # Slide 16: Empirical test findings & 3-pillar quantitative research roadmap
```

---

## 5. Presenter & Institutional Metadata

Configured in `preamble/macros.tex` and `html/slides.md`:

- **Project Title:** FinMetrics Suite: Algorithms and Architecture for Automated Ratio Benchmarking and Anomaly Detection for NSE Equities
- **Presentation Type:** Corporate Internship Presentation
- **Candidate:** N Rohit Vedhanandh
- **Register Number:** 25MSQUFPY0002
- **Faculty Guidance:** Dr. Kiruthika
- **Department:** Department of Statistics
- **School:** Ramanujan School of Mathematical Sciences
- **University:** Pondicherry University
- **Program:** M.Sc. Quantitative Finance (MSQF)

---

## 6. Primary References & Source Code

- **GitHub Repository**: [`https://github.com/hi1r0/finmetrics-PU`](https://github.com/hi1r0/finmetrics-PU)
- **Tukey, J. W. (1977)**: *Exploratory Data Analysis*, Addison-Wesley.
- **Iglewicz, B. & Hoaglin, D. C. (1993)**: *How to Detect and Handle Outliers*, ASQC Basic References in Quality Control.
- **Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008)**: *Isolation Forest*, IEEE ICDM, pp. 413–422.
