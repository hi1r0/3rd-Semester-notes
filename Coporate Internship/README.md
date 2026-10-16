# FinMetrics-PU: Corporate Internship Defense Presentation

An executive-grade, 11-slide presentation deck in LaTeX Beamer for the Corporate Internship defense in **M.Sc. Quantitative Finance** at **Pondicherry University (Department of Economics)**.

The deck presents **FinMetrics-PU: Cross-Sectional Financial Outlier Detection and Sector Benchmarking System for NSE Equities**, featuring custom TikZ system architecture pipelines, mathematical card containers, and an **Executive Monochromatic Emerald & Jade** color palette (zero gold).

---

## 1. Presentation Structure (11 Slides)

| Slide | Topic | Key Equations / Algorithmic Core | Primary Components |
| :---: | :--- | :--- | :--- |
| **01** | **Title & Institutional Attribution** | University Crest, Candidate, Guide, Supervisor metadata | `pondicherry_university_logo.png`, `quantcard` |
| **02** | **Problem Statement & Bottlenecks** | $Z_i = \frac{x_i - \bar{\mu}}{\hat{\sigma}}$ failure under heavy tails | 3 Symmetric Ingestion/Stats/Architecture Cards |
| **03** | **End-to-End System Architecture** | 4-Stage Horizontal Pipeline ($\ge 0.7\,\text{cm}$ clearance) | Custom TikZ chevron flow \& decoupled summary card |
| **04** | **Ratio Engine Mechanism** | 5 analytical pillars (16 ratios) \& $\safedivide(a, b, \epsilon)$ | Weighting matrix, DuPont decomposition card |
| **05** | **Statistical Anomaly Algorithms** | $\IQR = Q_3 - Q_1$, $M_i = \frac{0.6745(x_i - \median)}{\MAD}$ | Dual `mathcard` comparing Tukey vs. MAD $0.6745$ |
| **06** | **Machine Learning Anomaly Engine** | $c(n) = 2\ln(n-1) + 2\gamma - \frac{2(n-1)}{n}$, $s(x,n) = 2^{-\frac{\mathbb{E}(h(x))}{c(n)}}$ | Multivariate iForest in $\mathbb{R}^{16}$ \& consensus matrix |
| **07** | **Peer Benchmarking \& Sigmoid** | $S(x) = \frac{100}{1 + e^{-\kappa \frac{x-\text{Med}}{\IQR}}}$, $w_i' = \frac{w_i}{\sum w_j}$ | Non-linear Sigmoid scaling, dynamic NaN weights |
| **08** | **Risk Classification Matrix** | $\text{Composite} = \sum W_k \cdot \text{Pillar}_k$, $\Delta S_i = w_i'(S(x_i) - 50)$ | 5-tier credit health table (Excellent to Distressed) |
| **09** | **AI Narration \& Delivery** | Gemini round-robin rotation (`GEMINI_API_KEY_1..N`) | 6-tab automated Excel artifact, Streamlit UI |
| **10** | **Empirical Results (NSE Study)** | Gaussian breakdown ($+32.4\%$ distortion) vs. MAD stability | Cross-sectional validation table across 150+ stocks |
| **11** | **Conclusion \& Future Roadmap** | Technical contributions, credit early warnings, GNN roadmap | 3 strategic pillars \& Q&A discussion banner |

---

## 2. Directory Architecture

```
D:\MSQF\Semester III\Coporate Internship\
|-- main.tex                         # Master compilation document (aspectratio=169)
|-- main.pdf                         # Compiled 11-slide presentation deliverable
|-- README.md                        # Documentation of presentation structure & compilation
|-- figures\
|   |-- pondicherry_university_logo.png
|-- preamble\
|   |-- packages.tex                 # Core packages (beamer, tikz, tcolorbox, amsmath)
|   |-- theme.tex                    # Custom Beamer theme, Emerald/Jade palette, header/footer
|   |-- macros.tex                   # Presenter metadata, mathematical operators, card macros
|-- slides\
|   |-- slide01_title.tex            # University branding & attribution card
|   |-- slide02_problem_statement.tex # Schema variance & mean distortion
|   |-- slide03_system_architecture.tex # Full-width 4-stage horizontal TikZ pipeline
|   |-- slide04_ratio_engine.tex     # 16 ratios, 5 analytical pillars & safe divide
|   |-- slide05_statistical_anomalies.tex # Tukey Fences & MAD Z-Scores
|   |-- slide06_isolation_forest.tex # Multivariate iForest & path-length math
|   |-- slide07_benchmarking_sigmoid.tex # Sigmoid normalization & dynamic weights
|   |-- slide08_risk_classification.tex # 5-tier health classification matrix
|   |-- slide09_ai_reporting_pipeline.tex # Gemini LLM key rotation & 6-tab Excel
|   |-- slide10_empirical_results.tex # Cross-sector NSE empirical findings
|   |-- slide11_conclusion_roadmap.tex # Industry impact, future work & Q&A
```

---

## 3. Presenter Metadata Configuration

To personalize the title slide, edit the following macros in `preamble/macros.tex`:

```latex
\newcommand{\StudentName}{[Your Name]}
\newcommand{\RollNumber}{[Your Roll No]}
\newcommand{\ProgramName}{M.Sc. Quantitative Finance (MSQF)}
\newcommand{\DepartmentName}{Department of Economics}
\newcommand{\UniversityName}{Pondicherry University}
\newcommand{\CompanyName}{[Company Name]}
\newcommand{\InternalGuide}{[Faculty Name]}
\newcommand{\ExternalSupervisor}{[Supervisor Name]}
\newcommand{\PresentationDate}{Academic Year 2026--2027}
```

---

## 4. Color Palette: Pure Monochromatic Emerald & Jade

| Color Role | Name | Hex Code | RGB Values | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Structure** | `deepemerald` | `#064E3B` | `RGB(6, 78, 59)` | Slide titles, structural borders, main headers |
| **Secondary Accent** | `forestgreen` | `#0D5C3A` | `RGB(13, 92, 58)` | Section subtitles, card title text, subheadings |
| **Vibrant Highlight** | `jade` | `#059669` | `RGB(5, 150, 105)` | Formula badges, active nodes, contrast pills |
| **Card Fill** | `lightsage` | `#EBF5EE` | `RGB(235, 245, 238)` | Card background for high mathematical contrast |
| **Card Border** | `mintborder` | `#A7F3D0` | `RGB(167, 243, 208)` | Subtle 0.8pt outlines for card definition |
| **Slide Background** | `paperbg` | `#F7FBF9` | `RGB(247, 251, 249)` | Off-white soft mint canvas preventing screen glare |
| **Primary Text** | `darkcharcoal` | `#0F172A` | `RGB(15, 23, 42)` | High-contrast body text and equations |
| **Muted Annotation** | `slatygray` | `#475569` | `RGB(71, 85, 105)` | Footnotes, source pills, and secondary details |

---

## 5. Compilation Instructions

Compile from PowerShell or terminal inside `D:\MSQF\Semester III\Coporate Internship`:

```powershell
pdflatex -interaction=nonstopmode -output-directory="." main.tex
pdflatex -interaction=nonstopmode -output-directory="." main.tex
```

Two compilation passes are recommended to fully resolve page totals (`\inserttotalframenumber`) and navigation counters.

---

## 6. Primary References & Source Code

- **GitHub Repository**: [`https://github.com/hi1r0/finmetrics-PU`](https://github.com/hi1r0/finmetrics-PU)
- **Reference Deck**: `FinMetrics_PU_Algorithms_and_Mechanism.pptx`
- **Tukey, J. W. (1977)**: *Exploratory Data Analysis*, Addison-Wesley.
- **Iglewicz, B. & Hoaglin, D. C. (1993)**: *How to Detect and Handle Outliers*, ASQC Basic References in Quality Control.
- **Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008)**: *Isolation Forest*, IEEE ICDM, pp. 413–422.
