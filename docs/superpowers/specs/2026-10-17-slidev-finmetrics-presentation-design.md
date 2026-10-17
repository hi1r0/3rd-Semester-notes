# Design Specification: FinMetrics Suite Slidev Presentation

**Document Date:** 2026-10-17  
**Target Path:** `D:\MSQF\Semester III\Coporate Internship\html`  
**Source Baseline:** `D:\MSQF\Semester III\Coporate Internship\main.pdf` (and `main.tex`)  
**Design Reference:** Apple Keynote / Product Page Aesthetic & `frontend-slides` Patterns

---

## 1. Executive Summary & Goals

The objective is to convert the 16-slide academic Beamer presentation for the Corporate Internship in M.Sc. Quantitative Finance at Pondicherry University (*FinMetrics Suite: Algorithms and Architecture for Automated Ratio Benchmarking and Anomaly Detection for NSE Equities*) into a presentation built on **Slidev** (`https://sli.dev`).

The presentation will live in `D:\MSQF\Semester III\Coporate Internship\html` and feature:
1. **Apple-Inspired Design Language:** Ultra-clean typography, deep obsidian dark canvas (`#071411`), translucent frosted glass cards (`backdrop-blur: 16px`), glowing jade/mint accents (`#34D399`, `#10B981`, `#00E599`), and platinum white hierarchy.
2. **Synchronized Split Architecture:** Every technical slide pairs rigorous mathematical formulas and deep financial analytical insights on the left with a dedicated, custom interactive animated Vue 3 component on the right.
3. **Hybrid Animation System:** Automated entry sequences synced to Slidev `v-click` progressive reveals, coupled with interactive controls (play/pause, step triggers, parameter sliders) for live demonstration.
4. **Complete 16-Slide Fidelity:** Complete coverage of all 16 slides from `main.pdf`, preserving candidate attribution, mathematical rigor, and empirical findings.

---

## 2. Technology Stack & Dependencies

- **Presentation Engine:** Slidev (`@slidev/cli`, `@slidev/theme-default`)
- **UI Framework:** Vue 3 Composition API (`<script setup>`)
- **Styling Engine:** UnoCSS / Tailwind-compatible styling with custom CSS variables and frosted glass utility classes
- **Mathematical Typesetting:** Built-in KaTeX (`$...$` inline, `$$...$$` display mode)
- **Animation Primitives:** CSS Keyframes, SVG morphing/transitions, and Vue reactive animation states inspired by the installed `frontend-slides` patterns
- **Package Management:** `npm` (Node.js v24.14.0, npm 11.9.0)

---

## 3. Visual Design System (Apple Keynote Aesthetic)

### 3.1 Color Palette
- **Canvas Base (`--color-bg-base`):** `#071411` (Deep obsidian emerald)
- **Glass Card Surface (`--color-card-bg`):** `rgba(13, 33, 27, 0.70)` with `backdrop-filter: blur(16px)`
- **Glass Border (`--color-card-border`):** `rgba(52, 211, 153, 0.18)`
- **Elevated Inset (`--color-card-inset`):** `rgba(19, 47, 38, 0.65)`
- **Primary Typography (`--color-text-primary`):** `#F8FAFC` (Platinum white)
- **Secondary Typography (`--color-text-secondary`):** `#94A3B8` (Cool slate silver)
- **Muted Caption (`--color-text-muted`):** `#86868B` (Apple graphite)
- **Accent - Radiant Mint (`--color-mint`):** `#34D399`
- **Accent - Glowing Jade (`--color-jade`):** `#10B981`
- **Accent - Hyper Accent (`--color-accent`):** `#00E599`
- **Anomaly Warning / Outlier Alert (`--color-alert`):** `#F43F5E` (Crimson rose) / `#F59E0B` (Amber)

### 3.2 Typography Hierarchy
- **Header Font:** `Plus Jakarta Sans`, `-apple-system`, `BlinkMacSystemFont`, `SF Pro Display`, `sans-serif`
- **Body Font:** `Inter`, `-apple-system`, `BlinkMacSystemFont`, `sans-serif`
- **Code & Numbers:** `JetBrains Mono`, `SF Mono`, `monospace`
- **Tracking & Leading:** Tight letter spacing on headers (`-0.02em`), generous line-height (`1.6`) on analytical descriptions.

---

## 4. Slide-by-Slide Specification & Animated Components

| Slide | Title | Left Card: Math & Analytical Insights | Right Card: Custom Animated Vue 3 Component |
| :---: | :--- | :--- | :--- |
| **01** | **FinMetrics Suite: Title & Attribution** | Pondicherry University, Department of Statistics, Candidate: N Rohit Vedhanandh (25MSQUFPY0002), Guide: Dr. Kiruthika. | `TitleHero.vue`: Animated pulsing executive emerald emblem, glowing title card, live status badge. |
| **02** | **Analytical Motivations & Screening Latency** | Line-item divergence across filings, schema heterogeneity, manual screening lag (hours $\to$ seconds). | `LatencyComparison.vue`: Interactive animated timeline & throughput bar comparing manual vs automated pipeline. |
| **03** | **Gaussian Breakdown & Outlier Masking** | Gaussian breakdown point $\varepsilon^* = 0.0\%$, sample mean shift $\bar{\mu} \to \infty$, masking proof under contamination. | `GaussianBreakdown.vue`: Interactive SVG normal curve with draggable outlier injection showing mean skew vs median stability. |
| **04** | **System Architecture & Data Pipeline** | 4-stage decoupled architecture: Ingestion, Ratio Engine, Anomaly Detection, Delivery. | `SystemPipeline.vue`: Animated 4-stage flow with traveling data packets, node status lights, and latency metrics. |
| **05** | **Ingestion Caching & Schema Harmonization** | Multi-tier Parquet caching ($>88.5\%$ hit rate), canonical aliasing, singularity validation. | `CacheHarmonizer.vue`: Animated cache gauge meter ($88.5\%$) and schema mapping reconciler. |
| **06** | **Ratio Engine Architecture** | 5 financial pillars (16 ratios), epsilon guard $\safedivide(a, b, \epsilon)$ preventing zero-division errors. | `RatioEnginePillars.vue`: Interactive 5-pillar selector revealing formulas and weights dynamically. |
| **07** | **Financial Decomposition & DuPont Analysis** | 3-stage and 5-stage multiplicative identities: $\text{ROE} = \text{Tax} \times \text{Int} \times \text{Margin} \times \text{Turnover} \times \text{Lev}$. | `DuPontDecomposition.vue`: Animated interactive branching tree showing multiplicative expansion from ROE into 5 factors. |
| **08** | **Non-Parametric Anomaly Detection** | Tukey IQR bounds: $\mathcal{F}_{\text{lower/upper}} = Q_{1/3} \mp 1.5\,\IQR$, quartile resistance. | `TukeyBoxplot.vue`: Interactive animated boxplot with dynamic whiskers, fences, and highlighted outlier points. |
| **09** | **Modified MAD Dispersion Engine** | $\MAD = \median(\|x_i - \text{Med}\|)$, 50% breakdown point, $0.6745$ Gaussian scale consistency derivation. | `MadDispersion.vue`: Side-by-side animated comparison of standard deviation explosion vs MAD resilience. |
| **10** | **Machine Learning Outlier Detection** | BST path length $c(n) = 2\ln(n-1) + 2\gamma - \frac{2(n-1)}{n}$, multivariate consensus scoring $s(x,n) = 2^{-\frac{\mathbb{E}(h)}{c(n)}}$. | `IsolationForestTree.vue`: Animated binary tree path traversal showing shallow anomaly termination ($h < \bar{h}$). |
| **11** | **iForest Geometry & Subspace Partitioning** | 2D subspace cuts isolating anomalies in few orthogonal bisections vs deep nominal clusters. | `SubspacePartitioning.vue`: Interactive 2D coordinate grid demonstrating recursive cut lines isolating an outlier. |
| **12** | **Peer Benchmarking & Sigmoid Normalization** | $S(x) = \frac{100}{1 + e^{-\kappa \frac{x-\text{Med}}{\IQR}}}$, dynamic NaN weight redistribution. | `SigmoidCurve.vue`: Interactive S-curve plot with adjustable $\kappa$ steepness slider and quartile reference points ($35, 50, 65$). |
| **13** | **5-Tier Health Classification Matrix** | Composite score $\sum W_k \cdot \text{Pillar}_k$, AAA to D credit risk tier boundaries. | `HealthGauge.vue`: Animated semicircular Apple-style health gauge with glowing tier needles and status pill. |
| **14** | **Portfolio Factor Attribution & Strategy** | Factor delta: $\Delta S_i = W_k \cdot w_{k,i}'(S(x_i) - 50.0)$, Long/Short equity quintile spreads. | `FactorAttribution.vue`: Animated factor delta waterfall chart and L/S equity portfolio spread visualizer. |
| **15** | **AI Narration & Multi-Format Delivery** | Multi-agent round-robin LLM synthesis, automated 6-tab openpyxl Excel audit report generation. | `DeliveryPipeline.vue`: Animated dispatch diagram showing multi-model routing into automated spreadsheet exports. |
| **16** | **Empirical Results & Research Roadmap** | 150+ NSE equities empirical validation, GNN systemic risk & debt contagion graph neural network roadmap. | `EmpiricalRoadmap.vue`: Animated quantitative metrics counter and 3-phase future research timeline card. |

---

## 5. Project Directory & File Layout

```text
D:\MSQF\Semester III\Coporate Internship\html\
├── package.json               # Slidev CLI, Vue 3, UnoCSS, KaTeX dependencies
├── slides.md                  # Master presentation file (16 slides, synchronized layout)
├── uno.config.ts              # Custom colors, frosted glass shortcuts, typography rules
├── vite.config.ts             # Vite configuration with auto-import and Vue support
├── styles/
│   ├── index.css              # Apple aesthetic variables, glassmorphism, animations
│   └── custom-katex.css       # Enhanced styling for high-contrast math blocks
├── components/                # Custom Vue 3 Interactive Animated Components
│   ├── TitleHero.vue
│   ├── LatencyComparison.vue
│   ├── GaussianBreakdown.vue
│   ├── SystemPipeline.vue
│   ├── CacheHarmonizer.vue
│   ├── RatioEnginePillars.vue
│   ├── DuPontDecomposition.vue
│   ├── TukeyBoxplot.vue
│   ├── MadDispersion.vue
│   ├── IsolationForestTree.vue
│   ├── SubspacePartitioning.vue
│   ├── SigmoidCurve.vue
│   ├── HealthGauge.vue
│   ├── FactorAttribution.vue
│   ├── DeliveryPipeline.vue
│   └── EmpiricalRoadmap.vue
└── public/
    └── pondicherry_university_logo.png
```

---

## 6. Verification & Quality Gates

1. **Compilation & Dev Server:** `npm run dev` starts without errors, runs on `http://localhost:3030`.
2. **Build Verification:** `npm run build` generates a standalone distribution in `dist/` with 0 build errors.
3. **Responsive Fixed 16:9 Stage:** Content scales correctly without overflow, vertical overlaps, or clipped formulas.
4. **Interactive Component Testing:** Each of the animated components mounts, executes its animation sequence, and responds to user interaction (buttons/sliders/hover).
5. **Git Tracking & Remote Push:** Comply with the project's git standards by staging, committing, and pushing all source files upon completion.
