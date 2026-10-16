# FinMetrics Suite: Corporate Internship Presentation

An executive-grade, 11-slide presentation deck in LaTeX Beamer for the Corporate Internship presentation in **M.Sc. Quantitative Finance** at **Pondicherry University (Ramanujan School of Mathematical Sciences, Department of Statistics)**.

The deck presents **FinMetrics Suite: Algorithms and Architecture for Automated Ratio Benchmarking and Anomaly Detection for NSE Equities**, featuring custom native TikZ system architecture diagrams, mathematical card containers, statistical plots, and an **Executive Monochromatic Emerald & Jade** color palette (zero gold).

---

## 1. Presentation Structure (11 Slides)

| Slide | Topic | Key Equations / Algorithmic Core | Primary Visual Components |
| :---: | :--- | :--- | :--- |
| **01** | **Title & Institutional Attribution** | Department of Statistics, Candidate, Faculty Guidance | University Crest, Centered Executive Attribution Card |
| **02** | **Problem Statement & Bottlenecks** | $Z_i = \frac{x_i - \bar{\mu}}{\hat{\sigma}}$ failure under heavy tails ($0.0\%$ BP) | TikZ Gaussian mean displacement curve vs. robust median |
| **03** | **End-to-End System Architecture** | 4-stage execution flow with clean inter-node spacing | Native TikZ 4-stage pipeline \& decoupled summary card |
| **04** | **Ratio Engine Mechanism** | 5 analytical pillars (16 ratios) \& $\safedivide(a, b, \epsilon)$ | TikZ 5-pillar segmented hierarchy, DuPont decomposition card |
| **05** | **Statistical Anomaly Algorithms** | $\IQR = Q_3 - Q_1$, $M_i = \frac{0.6745(x_i - \median)}{\MAD}$ | Native TikZ Boxplot (quartiles, fences, outliers) \& MAD card |
| **06** | **Machine Learning Anomaly Engine** | $c(n) = 2\ln(n-1) + 2\gamma - \frac{2(n-1)}{n}$, $s(x,n) = 2^{-\frac{\mathbb{E}(h(x))}{c(n)}}$ | Native TikZ 2D hyperplanes \& isolation tree hierarchy |
| **07** | **Peer Benchmarking \& Sigmoid** | $S(x) = \frac{100}{1 + e^{-\kappa \frac{x-\text{Med}}{\IQR}}}$, $w_i' = \frac{w_i}{\sum w_j}$ | Native TikZ Sigmoid S-curve plot ($Q_1 \to 35$, Med $\to 50$, $Q_3 \to 65$) |
| **08** | **Risk Classification Matrix** | $\text{Composite} = \sum W_k \cdot \text{Pillar}_k$, $\Delta S_i = w_i'(S(x_i) - 50)$ | Native TikZ 5-tier Health Meter gauge \& classification table |
| **09** | **AI Narration \& Delivery** | Round-robin rotation (`GEMINI_API_KEY_1..N`) | Native TikZ synthesis flow, 6-tab Excel details \& Streamlit UI |
| **10** | **Empirical Results (NSE Study)** | Gaussian distortion ($+32.4\%$) vs. MAD stability | Cross-sectional validation table across 150+ NSE equities |
| **11** | **Conclusion \& Future Roadmap** | Production microservices, GNN systemic contagion modeling | 3 strategic pillars \& Department of Statistics closing banner |

---

## 2. Directory Architecture

```text
D:\MSQF\Semester III\Coporate Internship\
|-- main.tex                         # Master Beamer document (aspectratio=169, 11 slides)
|-- main.pdf                         # Compiled 11-slide presentation deliverable (0 overfull warnings)
|-- README.md                        # Documentation of presentation structure & compilation
|-- figures/
|   `-- pondicherry_university_logo.png
|-- preamble/
|   |-- packages.tex                 # Core packages (beamer, tikz, tcolorbox, amsmath, tabularx)
|   |-- theme.tex                    # Custom Beamer theme, Emerald/Jade palette, clean header (zero footline)
|   `-- macros.tex                   # Presenter metadata, mathematical operators, card macros
`-- slides/
    |-- slide01_title.tex            # University branding & centered executive attribution card
    |-- slide02_problem_statement.tex # Gaussian mean displacement plot & line-item variance
    |-- slide03_system_architecture.tex # 4-stage horizontal TikZ pipeline with bold connectors
    |-- slide04_ratio_engine.tex     # 16 ratios, 5 analytical pillars & safe-divide guards
    |-- slide05_statistical_anomalies.tex # Native TikZ boxplot, Tukey fences & MAD Z-Scores
    |-- slide06_isolation_forest.tex # Multivariate iForest, 2D hyperplanes & tree diagram
    |-- slide07_benchmarking_sigmoid.tex # Sigmoid S-curve plot & dynamic NaN weighting
    |-- slide08_risk_classification.tex # 5-tier health gauge & credit health matrix
    |-- slide09_ai_reporting_pipeline.tex # Round-robin LLM synthesis & 6-tab Excel exports
    |-- slide10_empirical_results.tex # Cross-sectional validation on NSE equities
    `-- slide11_conclusion_roadmap.tex # Industry impact, GNN roadmap & closing discussion banner
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

## 4. Color Palette: Pure Monochromatic Emerald & Jade (Zero Gold)

| Color Role | Name | Hex Code | RGB Values | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Structure** | `deepemerald` | `#064E3B` | `RGB(6, 78, 59)` | Slide titles, structural borders, main headers |
| **Secondary Accent** | `forestgreen` | `#0D5C3A` | `RGB(13, 92, 58)` | Section subtitles, card title text, subheadings |
| **Vibrant Highlight** | `jade` | `#059669` | `RGB(5, 150, 105)` | Formula badges, active nodes, contrast pills |
| **Card Fill** | `lightsage` | `#EBF5EE` | `RGB(235, 245, 238)` | Card background for high mathematical contrast |
| **Card Border** | `mintborder` | `#A7F3D0` | `RGB(167, 243, 208)` | Subtle 0.7pt outlines for card definition |
| **Slide Background** | `paperbg` | `#F7FBF9` | `RGB(247, 251, 249)` | Off-white soft mint canvas preventing screen glare |
| **Primary Text** | `darkcharcoal` | `#0F172A` | `RGB(15, 23, 42)` | High-contrast body text and equations |
| **Muted Annotation** | `slatygray` | `#475569` | `RGB(71, 85, 105)` | Section subtitles, source pills, and secondary details |

---

## 5. Compilation Instructions

Compile from PowerShell or terminal inside `D:\MSQF\Semester III\Coporate Internship`:

```powershell
pdflatex -interaction=nonstopmode -output-directory="." main.tex
pdflatex -interaction=nonstopmode -output-directory="." main.tex
```

Two compilation passes resolve all cross-references, bounding boxes, and navigation counters. The output compiles with **zero overfull warnings** and exit code 0.

---

## 6. Primary References & Source Code

- **GitHub Repository**: [`https://github.com/hi1r0/finmetrics-PU`](https://github.com/hi1r0/finmetrics-PU)
- **Reference Deck**: `FinMetrics_PU_Algorithms_and_Mechanism.pptx`
- **Tukey, J. W. (1977)**: *Exploratory Data Analysis*, Addison-Wesley.
- **Iglewicz, B. & Hoaglin, D. C. (1993)**: *How to Detect and Handle Outliers*, ASQC Basic References in Quality Control.
- **Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008)**: *Isolation Forest*, IEEE ICDM, pp. 413–422.
