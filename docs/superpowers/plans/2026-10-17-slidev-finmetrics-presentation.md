# FinMetrics Suite: Apple-Grade Slidev Presentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an Apple-grade, animation-rich Slidev presentation in `D:\MSQF\Semester III\Coporate Internship\html` reproducing the 16 slides of `main.pdf` with custom interactive Vue 3 components, KaTeX mathematical formulas, and deep quantitative analytical insights.

**Architecture:** Initialize a standalone Slidev project with custom UnoCSS configuration and Apple-keynote glassmorphic theme styles (`#071411` obsidian emerald, frosted glass cards, `#34D399` radiant mint accents). Implement 16 custom Vue 3 components embodying the quantitative algorithms (Gaussian breakdown, 4-stage pipeline, DuPont decomposition, Tukey boxplot, MAD dispersion, iForest trees and 2D hyperplanes, Sigmoid normalization, 5-tier health gauge, factor attribution, etc.). Author the master `slides.md` deck with synchronized split card layout, KaTeX equations, parameter definitions, and progressive `v-click` animation reveals.

**Tech Stack:** Slidev (`@slidev/cli`), Vue 3, UnoCSS, KaTeX, Vite, CSS Animations.

## Global Constraints

- Working Directory: `D:\MSQF\Semester III\Coporate Internship\html`
- Canvas Background: `#071411` (Deep obsidian emerald)
- Glass Card: `rgba(13, 33, 27, 0.70)` with `backdrop-filter: blur(16px)` and `border: 1px solid rgba(52, 211, 153, 0.18)`
- Accent Colors: `#34D399` (Radiant Mint), `#10B981` (Glowing Jade), `#00E599` (Hyper Accent)
- Text Colors: `#F8FAFC` (Platinum White headings), `#94A3B8` (Slate Silver secondary)
- Math: KaTeX (`$...$` inline, `$$...$$` display) with explicit "Where:" parameter blocks
- Slide Aspect Ratio: 16:9 widescreen stage
- Git Tracking: Stage, commit, and push upon task verification per `git_and_formatting_standards.md`

---

### Task 1: Project Scaffolding & Configuration

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\package.json`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\uno.config.ts`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\vite.config.ts`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\styles\index.css`
- Copy: `D:\MSQF\Semester III\Coporate Internship\figures\pondicherry_university_logo.png` $\to$ `D:\MSQF\Semester III\Coporate Internship\html\public\pondicherry_university_logo.png`

**Interfaces:**
- Produces: Runnable npm environment with `@slidev/cli`, `@slidev/theme-default`, Vue 3, and UnoCSS custom glassmorphic utilities.

- [ ] **Step 1: Write `package.json`**

```json
{
  "name": "finmetrics-slidev-deck",
  "type": "module",
  "private": true,
  "scripts": {
    "dev": "slidev --port 3030 --open=false",
    "build": "slidev build",
    "export": "slidev export"
  },
  "dependencies": {
    "@slidev/cli": "^51.6.0",
    "@slidev/theme-default": "latest",
    "vue": "^3.5.13"
  },
  "devDependencies": {
    "@unocss/reset": "latest",
    "unocss": "latest"
  }
}
```

- [ ] **Step 2: Create `uno.config.ts` and `styles/index.css`**
Configure Apple-style obsidian/emerald palette, frosted glass utilities (`glass-card`, `glass-inset`), glowing borders, and animations.

- [ ] **Step 3: Copy logo into `public/` directory**
Copy `figures/pondicherry_university_logo.png` into `html/public/pondicherry_university_logo.png`.

- [ ] **Step 4: Install dependencies via npm**
Run: `npm install` inside `D:\MSQF\Semester III\Coporate Internship\html`.
Verify: `node_modules` exists and `@slidev/cli` is installed.

- [ ] **Step 5: Commit**
`git add html/package.json html/uno.config.ts html/styles/ html/public/`
`git commit -m "feat(slidev): initialize project scaffolding and Apple glassmorphism styling"`

---

### Task 2: Title and Problem Statement Components (Slides 01 & 02)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\TitleHero.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\LatencyComparison.vue`

**Interfaces:**
- Produces:
  - `<TitleHero />`: Animated pulsing emerald insignia, institutional attribution badge, and live status pill.
  - `<LatencyComparison />`: Animated bar/metric chart contrasting manual audit latency (12-24 hours) vs FinMetrics automated execution (<1.8 seconds) across 150+ NSE equities.

- [ ] **Step 1: Implement `TitleHero.vue`**
Include animated pulse ring, Pondicherry University branding, candidate metadata (N Rohit Vedhanandh, 25MSQUFPY0002), and Dr. Kiruthika attribution.

- [ ] **Step 2: Implement `LatencyComparison.vue`**
Include animated horizontal benchmark meters, schema error reduction metrics, and interactive play/replay button.

- [ ] **Step 3: Verify Vue components mount without compile errors**
Create minimal test slide in `slides.md` and test `npx slidev build --dry` or syntax check.

- [ ] **Step 4: Commit**
`git add html/components/TitleHero.vue html/components/LatencyComparison.vue`
`git commit -m "feat(components): add TitleHero and LatencyComparison animated components"`

---

### Task 3: Quantitative Breakdown & Pipeline Components (Slides 03-05)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\GaussianBreakdown.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\SystemPipeline.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\CacheHarmonizer.vue`

**Interfaces:**
- Produces:
  - `<GaussianBreakdown />`: Interactive SVG normal curve with draggable outlier injection showing mean $\bar{\mu} \to \infty$ vs median stability, proving breakdown point $\varepsilon^* = 0.0\%$.
  - `<SystemPipeline />`: Animated 4-stage data pipeline (Ingestion, Ratio Engine, Anomaly Detection, Delivery) with pulsing packet flow.
  - `<CacheHarmonizer />`: Animated cache hit rate radial gauge ($88.5\%$) and schema alias reconciler.

- [ ] **Step 1: Implement `GaussianBreakdown.vue`**
- [ ] **Step 2: Implement `SystemPipeline.vue`**
- [ ] **Step 3: Implement `CacheHarmonizer.vue`**
- [ ] **Step 4: Test & Commit**
`git add html/components/GaussianBreakdown.vue html/components/SystemPipeline.vue html/components/CacheHarmonizer.vue`
`git commit -m "feat(components): add GaussianBreakdown, SystemPipeline, and CacheHarmonizer"`

---

### Task 4: Financial Ratio Engine & DuPont Decomposition (Slides 06 & 07)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\RatioEnginePillars.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\DuPontDecomposition.vue`

**Interfaces:**
- Produces:
  - `<RatioEnginePillars />`: Interactive 5-pillar accordion (Profitability, Leverage, Liquidity, Efficiency, Valuation) displaying 16 ratios and $\safedivide(a, b, \epsilon)$ logic.
  - `<DuPontDecomposition />`: Animated interactive branching tree showing step-by-step multiplicative expansion: $\text{ROE} \to \text{Tax Burden} \times \text{Interest Burden} \times \text{Operating Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$.

- [ ] **Step 1: Implement `RatioEnginePillars.vue`**
- [ ] **Step 2: Implement `DuPontDecomposition.vue`**
- [ ] **Step 3: Test & Commit**
`git add html/components/RatioEnginePillars.vue html/components/DuPontDecomposition.vue`
`git commit -m "feat(components): add RatioEnginePillars and DuPontDecomposition"`

---

### Task 5: Non-Parametric Statistics & Dispersion Components (Slides 08 & 09)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\TukeyBoxplot.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\MadDispersion.vue`

**Interfaces:**
- Produces:
  - `<TukeyBoxplot />`: Animated SVG Tukey boxplot with interactive quartiles, dynamic whiskers at $\pm 1.5\,\IQR$, and flagged outlier dots.
  - `<MadDispersion />`: Side-by-side animated comparison demonstrating MAD stability at $50\%$ breakdown point vs standard deviation explosion.

- [ ] **Step 1: Implement `TukeyBoxplot.vue`**
- [ ] **Step 2: Implement `MadDispersion.vue`**
- [ ] **Step 3: Test & Commit**
`git add html/components/TukeyBoxplot.vue html/components/MadDispersion.vue`
`git commit -m "feat(components): add TukeyBoxplot and MadDispersion components"`

---

### Task 6: Machine Learning Isolation Forest Components (Slides 10 & 11)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\IsolationForestTree.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\SubspacePartitioning.vue`

**Interfaces:**
- Produces:
  - `<IsolationForestTree />`: Animated binary search tree traversal showing shallow path length $h(x) < \bar{h}$ for anomalous equities.
  - `<SubspacePartitioning />`: Interactive 2D coordinate space showcasing recursive hyperplane cuts isolating outliers in 2 cuts vs nominal points in 8+ cuts.

- [ ] **Step 1: Implement `IsolationForestTree.vue`**
- [ ] **Step 2: Implement `SubspacePartitioning.vue`**
- [ ] **Step 3: Test & Commit**
`git add html/components/IsolationForestTree.vue html/components/SubspacePartitioning.vue`
`git commit -m "feat(components): add IsolationForestTree and SubspacePartitioning components"`

---

### Task 7: Benchmarking, Health Matrix & Portfolio Attribution (Slides 12-14)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\SigmoidCurve.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\HealthGauge.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\FactorAttribution.vue`

**Interfaces:**
- Produces:
  - `<SigmoidCurve />`: Interactive S-curve plot with adjustable $\kappa$ parameter slider and dynamic quartile reference points ($Q_1 \to 35$, $\text{Med} \to 50$, $Q_3 \to 65$).
  - `<HealthGauge />`: Semicircular Apple-style speedometer gauge indicating AAA to D health ratings with glowing needle.
  - `<FactorAttribution />`: Animated factor delta waterfall $\Delta S_i = W_k \cdot w_{k,i}'(S(x_i) - 50.0)$ and Long/Short quintile portfolio spread visualizer.

- [ ] **Step 1: Implement `SigmoidCurve.vue`**
- [ ] **Step 2: Implement `HealthGauge.vue`**
- [ ] **Step 3: Implement `FactorAttribution.vue`**
- [ ] **Step 4: Test & Commit**
`git add html/components/SigmoidCurve.vue html/components/HealthGauge.vue html/components/FactorAttribution.vue`
`git commit -m "feat(components): add SigmoidCurve, HealthGauge, and FactorAttribution components"`

---

### Task 8: AI Narration & Empirical Roadmap Components (Slides 15 & 16)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\DeliveryPipeline.vue`
- Create: `D:\MSQF\Semester III\Coporate Internship\html\components\EmpiricalRoadmap.vue`

**Interfaces:**
- Produces:
  - `<DeliveryPipeline />`: Animated round-robin LLM synthesis router into 6-tab openpyxl Excel audit report generation.
  - `<EmpiricalRoadmap />`: Live quantitative metrics counter (150+ NSE equities, $88.5\%$ cache hit rate, $<1.8\text{s}$ latency) and 3-phase research roadmap (Dynamic GNN Contagion, Copula Joint Defaults, Intraday Microstructure).

- [ ] **Step 1: Implement `DeliveryPipeline.vue`**
- [ ] **Step 2: Implement `EmpiricalRoadmap.vue`**
- [ ] **Step 3: Test & Commit**
`git add html/components/DeliveryPipeline.vue html/components/EmpiricalRoadmap.vue`
`git commit -m "feat(components): add DeliveryPipeline and EmpiricalRoadmap components"`

---

### Task 9: Master Presentation Deck (`slides.md`)

**Files:**
- Create: `D:\MSQF\Semester III\Coporate Internship\html\slides.md`

**Content Requirements:**
- 16 Slides complete with Frontmatter metadata (theme: default, aspect ratio 16:9, high-contrast typography).
- Synchronized Split Architecture on every slide (`grid grid-cols-2 gap-6 items-center`).
- Exact mathematical rigor from `main.tex` with KaTeX formulations and parameter definition blocks ("Where:").
- Deep analytical takeaways with quantitative intuition.
- Progressive `v-click` reveals on cards and formulas for Apple Keynote pacing.

- [ ] **Step 1: Author `slides.md` with complete 16 slides**
- [ ] **Step 2: Verify all KaTeX equations render correctly**
- [ ] **Step 3: Commit**
`git add html/slides.md`
`git commit -m "feat(slidev): author master 16-slide presentation deck with synchronized split architecture"`

---

### Task 10: Build Verification, Preview Validation & Git Push

**Files:**
- Verify: `D:\MSQF\Semester III\Coporate Internship\html\dist` (via `npm run build`)
- Update: `D:\MSQF\Semester III\Coporate Internship\README.md` (documenting Slidev presentation commands)

- [ ] **Step 1: Run production build**
Execute `npm run build` inside `html/` and ensure 0 errors.

- [ ] **Step 2: Update documentation in `README.md`**
Add instructions for running Slidev dev server (`npm run dev`) and viewing static build.

- [ ] **Step 3: Verify git status, commit, and push to remote**
Execute `git add .`, commit with descriptive message, and push to `origin main`.
