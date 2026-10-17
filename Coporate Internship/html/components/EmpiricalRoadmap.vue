<script setup lang="ts">
import { ref, computed } from 'vue'

// Method Selection State for Comparative Validation Table
type MethodKey = 'gaussian' | 'tukey' | 'mad' | 'isoforest'
const activeMethodKey = ref<MethodKey>('isoforest')

// Sector Filter for 150+ Equities
type SectorFilter = 'all' | 'it' | 'auto' | 'fmcg' | 'banking' | 'infra'
const activeSectorFilter = ref<SectorFilter>('all')

// Research Roadmap Phase Selection
type RoadmapPhase = 'all' | 'phase1' | 'phase2' | 'phase3'
const activeRoadmapPhase = ref<RoadmapPhase>('all')

// Validation Matrix Models Data
interface ValidationModel {
  id: MethodKey
  name: string
  paradigm: string
  breakdownPoint: string
  breakdownVal: number
  outlierYield: string
  yieldCount: string
  primaryFinding: string
  formula: string
  whereBlock: string[]
  empiricalCaseStudy: string
  color: string
  badgeColor: string
}

const validationModels: Record<MethodKey, ValidationModel> = {
  gaussian: {
    id: 'gaussian',
    name: 'Gaussian Z-Score',
    paradigm: 'Parametric (μ, σ)',
    breakdownPoint: '0.0%',
    breakdownVal: 0.0,
    outlierYield: '2.1%',
    yieldCount: '3 / 150 equities',
    primaryFinding: 'Masked 8 troubled mid-caps via +32.4% mean displacement under fat tails.',
    formula: 'z_i = (x_i - μ) / σ',
    whereBlock: [
      'x_i = Observed corporate financial ratio',
      'μ = Sample mean (vulnerable to single extreme value)',
      'σ = Sample standard deviation (inflates quadratically)',
    ],
    empiricalCaseStudy: 'Catastrophic Mean Displacement: Two hyper-profitable IT giants inflated sector mean by +32.4% and quadrupled σ. Consequently, 8 distressed mid-caps with collapsing margins fell within |z| < 3.0, escaping detection entirely.',
    color: 'text-amber-300',
    badgeColor: 'bg-amber-500/20 text-amber-300 border-amber-500/40',
  },
  tukey: {
    id: 'tukey',
    name: 'Tukey IQR Fences',
    paradigm: 'Non-Parametric Quartiles',
    breakdownPoint: '25.0%',
    breakdownVal: 25.0,
    outlierYield: '4.8%',
    yieldCount: '7 / 150 equities',
    primaryFinding: 'Resisted fat tails, cleanly isolated univariate ratio spikes; missed multivariate decoupling.',
    formula: '[Q_1 - 1.5·IQR, Q_3 + 1.5·IQR]',
    whereBlock: [
      'Q_1, Q_3 = First and third sample quartiles (25th and 75th percentiles)',
      'IQR = Q_3 - Q_1 (Interquartile Range)',
      '1.5 = Standard Tukey fence multiplier',
    ],
    empiricalCaseStudy: 'Univariate Robustness: Resisted heavy-tailed distribution in Automobile ancillaries. Successfully identified 7 extreme leverage and operating margin outliers without skewing sector reference quartiles.',
    color: 'text-teal-300',
    badgeColor: 'bg-teal-500/20 text-teal-300 border-teal-500/40',
  },
  mad: {
    id: 'mad',
    name: 'Modified MAD Dispersion',
    paradigm: 'Median-Centered Dispersion',
    breakdownPoint: '50.0%',
    breakdownVal: 50.0,
    outlierYield: '5.2%',
    yieldCount: '8 / 150 equities',
    primaryFinding: 'Unshakable baseline stability (ΔMed < 1.2%); zero false positives in cyclical swings.',
    formula: 'M_i = 0.6745 · (x_i - Med(X)) / MAD',
    whereBlock: [
      'Med(X) = Sample median (50% breakdown resistance)',
      'MAD = Med(|x_i - Med(X)|) (Median Absolute Deviation)',
      '0.6745 = Consistency scale factor (1 / 1.4826) for Gaussian equivalence',
    ],
    empiricalCaseStudy: 'High Breakdown Proof: In volatile commodity and capital goods sectors, MAD preserved baseline median stability (drift < 1.2%), rejecting false-alarm penalties for cyclical earnings fluctuations.',
    color: 'text-emerald-300',
    badgeColor: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
  },
  isoforest: {
    id: 'isoforest',
    name: 'Isolation Forest (ℝ¹⁶)',
    paradigm: 'Ensemble Hyperplane Trees',
    breakdownPoint: 'Multivariate (Unbounded)',
    breakdownVal: 75.0,
    outlierYield: '8.4%',
    yieldCount: '13 / 150 equities',
    primaryFinding: 'Successfully flagged margin-cashflow decoupling and concealed distress invisible to 1D tests.',
    formula: 's(x, n) = 2^(-E(h(x)) / c(n))',
    whereBlock: [
      'h(x) = Tree traversal path length in ℝ¹⁶ feature space',
      'E(h(x)) = Expected average path length across 100 orthogonal isolation trees',
      'c(n) = Average path length of unsuccessful searches in binary search trees',
    ],
    empiricalCaseStudy: 'Multidimensional Anomaly Capture: Detected 13 equities where individual ratios looked normal in isolation, but joint combinations (e.g. rising accounting net income paired with negative operating cash flows and accelerating short-term debt) isolated in only h = 2.1 cuts.',
    color: 'text-cyan-300',
    badgeColor: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40',
  },
}

const currentMethod = computed(() => validationModels[activeMethodKey.value])

// Sector Distribution Counts
const sectorCounts = {
  all: { label: 'All Sectors', count: 150, hitRate: '88.5%', sla: '1.74s' },
  it: { label: 'IT Services', count: 32, hitRate: '91.2%', sla: '1.62s' },
  auto: { label: 'Automobile', count: 24, hitRate: '87.4%', sla: '1.81s' },
  fmcg: { label: 'FMCG & Retail', count: 28, hitRate: '89.6%', sla: '1.68s' },
  banking: { label: 'Banking & NBFC', count: 36, hitRate: '86.1%', sla: '1.92s' },
  infra: { label: 'Infra & Energy', count: 30, hitRate: '88.0%', sla: '1.79s' },
}

// Future Quantitative Research Roadmap Pillars
interface RoadmapPillar {
  id: string
  phaseKey: 'phase1' | 'phase2' | 'phase3'
  phaseNumber: string
  timeline: string
  title: string
  subtitle: string
  challenge: string
  methodology: string
  mathFormulation: string
  mathWhere: string[]
  milestones: string[]
  techStack: string[]
  color: string
  badgeColor: string
}

const roadmapPillars: RoadmapPillar[] = [
  {
    id: 'p1',
    phaseKey: 'phase1',
    phaseNumber: 'PILLAR 1',
    timeline: 'Phase 1 · Q1–Q2 2027',
    title: 'Dynamic Concept Drift Modeling',
    subtitle: 'Monetary Policy Cycle & Dynamic Sector Median Tracking',
    challenge: 'Financial ratio distributions are non-stationary. When central banks execute aggressive interest rate tightening cycles (e.g. RBI repo rate hikes from 4.0% to 6.5%), sector-wide median interest burdens and leverage ratios shift, causing static thresholds to generate false credit stress alarms.',
    methodology: 'Integrate continuous rolling-window state estimation via Bayesian Kalman Filtering. Recursively adjust baseline sector medians and IQR fences proportional to systemic credit velocity and macro regime state probabilities.',
    mathFormulation: 'θ_t = θ_(t-1) + K_t · (y_t - H · θ_(t-1)),  where K_t = P_t · H^T · (H · P_t · H^T + R)^(-1)',
    mathWhere: [
      'θ_t = Time-varying sector baseline median vector in ℝ¹⁶',
      'K_t = Optimal Kalman gain adapting to macro volatility shocks',
      'y_t = Current period cross-sectional ratio observation vector',
      'R = Measurement noise covariance calibrated to filing reporting variance',
    ],
    milestones: ['Macro Regime Classifier', 'Rolling Kalman Filter Engine', 'Adaptive Lookback Windows', 'RBI Policy Calibration'],
    techStack: ['Statsmodels', 'FilterPy', 'PyTorch', 'SciPy'],
    color: 'text-emerald-300',
    badgeColor: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
  },
  {
    id: 'p2',
    phaseKey: 'phase2',
    phaseNumber: 'PILLAR 2',
    timeline: 'Phase 2 · Q3–Q4 2027',
    title: 'Systemic Graph Contagion Networks',
    subtitle: 'Inter-Firm Counterparty Exposure & Default Cascade Topology',
    challenge: 'Corporate solvency failure is rarely an isolated phenomenon. Default by a major original equipment manufacturer (OEM) or real estate developer propagates downstream liquidity shocks across dozens of tier-1 and tier-2 supply chain vendors and creditor institutions.',
    methodology: 'Model the 150+ equity universe as a directed, edge-weighted Heterogeneous Graph G = (V, E). Nodes represent listed corporates, and edges quantify mutual trade payables/receivables and bank exposures. Deploy Graph Neural Networks (GNNs) to simulate liquidity stress propagation.',
    mathFormulation: 'h_v^(l+1) = σ( W_self · h_v^(l) + Σ_(u ∈ N(v)) α_(u,v) · W_edge · h_u^(l) )',
    mathWhere: [
      'h_v^(l) = Latent solvency stress embedding of firm v at layer l',
      'N(v) = Set of supplier and customer counterparties linked to firm v',
      'α_(u,v) = Contagion attention weight derived from balance sheet exposure magnitude',
      'W_edge = Shock transmission tensor modeling cash flow default pass-through',
    ],
    milestones: ['Inter-Firm Exposure Graph G=(V,E)', 'Heterogeneous Graph Transformer', 'Cascade Default Simulator', 'Systemic Centrality Ranking'],
    techStack: ['PyTorch Geometric (PyG)', 'DGL', 'NetworkX', 'CUDA'],
    color: 'text-teal-300',
    badgeColor: 'bg-teal-500/20 text-teal-300 border-teal-500/40',
  },
  {
    id: 'p3',
    phaseKey: 'phase3',
    phaseNumber: 'PILLAR 3',
    timeline: 'Phase 3 · Q1+ 2028',
    title: 'Alternative Textual ESG & MD&A Auditing',
    subtitle: 'Financial NLP Parsing of Footnotes & Auditor Qualifications',
    challenge: 'Stressed management teams frequently engineer optical accounting health through aggressive revenue recognition while concealing material credit overhangs inside dense annual report footnotes, contingent liability tables, and auditor qualifications.',
    methodology: 'Deploy specialized financial language models (FinBERT / RoBERTa) to parse unformatted annual report filings. Extract contingent liabilities, classify auditor remarks (Unqualified vs Qualified vs Adverse), and measure semantic sentiment-cashflow divergence.',
    mathFormulation: 'Divergence(Firm) = CosineSim(E_MD&A, E_CashFlow) · (1 + Σ Penalty_Qualifications)',
    mathWhere: [
      'E_MD&A = Dense transformer embedding of management discussion & analysis tone',
      'E_CashFlow = Objective numerical vector embedding of operating cash flow trajectory',
      'Penalty_Qualifications = Indicator penalty for "Emphasis of Matter" or going-concern doubts',
    ],
    milestones: ['Annual Report Footnote Extractor', 'FinBERT Audit Classifier', 'Contingent Liability NER', 'Sentiment-Cashflow Divergence Index'],
    techStack: ['HuggingFace', 'FinBERT', 'spaCy', 'LangChain'],
    color: 'text-cyan-300',
    badgeColor: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40',
  },
]

const filteredRoadmapPillars = computed(() => {
  if (activeRoadmapPhase.value === 'all') return roadmapPillars
  return roadmapPillars.filter(p => p.phaseKey === activeRoadmapPhase.value)
})
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Action & Sector Filter Bar -->
    <div class="flex items-center justify-between gap-2 bg-[#071411]/90 px-3 py-1.5 rounded-xl border border-emerald-500/20 mb-1.5">
      <!-- Sector Universe Selector -->
      <div class="flex items-center gap-1">
        <span class="text-[9.5px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Validation Universe:
        </span>
        <button
          @click="activeSectorFilter = 'all'"
          class="px-2 py-0.5 rounded text-[9px] font-mono transition border"
          :class="activeSectorFilter === 'all'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          150+ NSE Equities (All)
        </button>

        <button
          @click="activeSectorFilter = 'it'"
          class="px-2 py-0.5 rounded text-[9px] font-mono transition border"
          :class="activeSectorFilter === 'it'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          IT (32)
        </button>

        <button
          @click="activeSectorFilter = 'auto'"
          class="px-2 py-0.5 rounded text-[9px] font-mono transition border"
          :class="activeSectorFilter === 'auto'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          Auto (24)
        </button>

        <button
          @click="activeSectorFilter = 'fmcg'"
          class="px-2 py-0.5 rounded text-[9px] font-mono transition border"
          :class="activeSectorFilter === 'fmcg'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          FMCG (28)
        </button>

        <button
          @click="activeSectorFilter = 'banking'"
          class="px-2 py-0.5 rounded text-[9px] font-mono transition border"
          :class="activeSectorFilter === 'banking'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          Banking (36)
        </button>

        <button
          @click="activeSectorFilter = 'infra'"
          class="px-2 py-0.5 rounded text-[9px] font-mono transition border"
          :class="activeSectorFilter === 'infra'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          Infra (30)
        </button>
      </div>

      <!-- Roadmap Phase Toggle Filter -->
      <div class="flex items-center gap-1 font-mono text-[8.5px]">
        <span class="text-slate-400 mr-1">Roadmap Filter:</span>
        <div class="flex bg-[#071411] p-0.5 rounded border border-slate-800">
          <button
            @click="activeRoadmapPhase = 'all'"
            class="px-1.5 py-0.5 rounded transition"
            :class="activeRoadmapPhase === 'all' ? 'bg-emerald-500/30 text-emerald-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
          >
            All Pillars
          </button>
          <button
            @click="activeRoadmapPhase = 'phase1'"
            class="px-1.5 py-0.5 rounded transition"
            :class="activeRoadmapPhase === 'phase1' ? 'bg-emerald-500/30 text-emerald-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
          >
            1. Macro Drift
          </button>
          <button
            @click="activeRoadmapPhase = 'phase2'"
            class="px-1.5 py-0.5 rounded transition"
            :class="activeRoadmapPhase === 'phase2' ? 'bg-teal-500/30 text-teal-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
          >
            2. GNN Contagion
          </button>
          <button
            @click="activeRoadmapPhase = 'phase3'"
            class="px-1.5 py-0.5 rounded transition"
            :class="activeRoadmapPhase === 'phase3' ? 'bg-cyan-500/30 text-cyan-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
          >
            3. Textual NLP
          </button>
        </div>
      </div>
    </div>

    <!-- Production Engineering Performance Benchmarks (Banner) -->
    <div class="grid grid-cols-4 gap-2 mb-1.5 font-mono">
      <div class="glass-card px-2.5 py-1.5 flex items-center justify-between border-emerald-500/25">
        <div>
          <div class="text-[7.5px] uppercase tracking-wider text-slate-400">Sample Tested</div>
          <div class="text-base font-black text-emerald-300 leading-tight">150+ Equities</div>
          <div class="text-[6.8px] text-slate-500">5 Major Industrial Sectors</div>
        </div>
        <div class="w-7 h-7 rounded-lg bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center text-emerald-300 font-bold text-xs">
          NSE
        </div>
      </div>

      <div class="glass-card px-2.5 py-1.5 flex items-center justify-between border-teal-500/25">
        <div>
          <div class="text-[7.5px] uppercase tracking-wider text-slate-400">Cache Hit Rate</div>
          <div class="text-base font-black text-teal-300 leading-tight">88.5%</div>
          <div class="text-[6.8px] text-slate-500">Multi-Tier Parquet Storage</div>
        </div>
        <div class="w-7 h-7 rounded-lg bg-teal-500/15 border border-teal-500/30 flex items-center justify-center text-teal-300 font-bold text-xs">
          I/O
        </div>
      </div>

      <div class="glass-card px-2.5 py-1.5 flex items-center justify-between border-cyan-500/25">
        <div>
          <div class="text-[7.5px] uppercase tracking-wider text-slate-400">Processing Latency</div>
          <div class="text-base font-black text-cyan-300 leading-tight">&lt; 1.8s</div>
          <div class="text-[6.8px] text-slate-500">End-to-End Pipeline SLA</div>
        </div>
        <div class="w-7 h-7 rounded-lg bg-cyan-500/15 border border-cyan-500/30 flex items-center justify-center text-cyan-300 font-bold text-xs">
          SLA
        </div>
      </div>

      <div class="glass-card px-2.5 py-1.5 flex items-center justify-between border-emerald-500/25">
        <div>
          <div class="text-[7.5px] uppercase tracking-wider text-slate-400">Singularity Rate</div>
          <div class="text-base font-black text-emerald-400 leading-tight">0 Failures</div>
          <div class="text-[6.8px] text-slate-500">Across 10,000+ Calculations</div>
        </div>
        <div class="w-7 h-7 rounded-lg bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center text-emerald-300 font-bold text-xs">
          ε=0
        </div>
      </div>
    </div>

    <!-- Main Content: Left Column (Validation Matrix) & Right Column (Future Roadmap Full-Height Card) -->
    <div class="grid grid-cols-12 gap-2 flex-1 min-h-0 mb-1.5">
      <!-- LEFT COLUMN: Cross-Sectional Model Validation Matrix (Width: 6 Cols) -->
      <div class="col-span-6 flex flex-col gap-2">
        <!-- Comparative Matrix Table Card -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-1 mb-1 border-b border-emerald-500/15">
              <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-sm bg-emerald-400"></span>
                Cross-Sectional Model Validation (150+ NSE Equities)
              </span>
              <span class="text-[8px] font-mono px-1.5 py-0.2 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                Outlier Breakdown Comparison
              </span>
            </div>

            <!-- Matrix Table -->
            <table class="w-full text-left border-collapse font-mono text-[7.8px] mb-1">
              <thead>
                <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                  <th class="pb-0.5">Methodology</th>
                  <th class="pb-0.5 text-center">Breakdown Point</th>
                  <th class="pb-0.5 text-center">Yield</th>
                  <th class="pb-0.5">Empirical Diagnostic Assessment</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800/60">
                <tr
                  v-for="model in validationModels"
                  :key="model.id"
                  @click="activeMethodKey = model.id"
                  class="cursor-pointer transition hover:bg-slate-800/40"
                  :class="activeMethodKey === model.id ? 'bg-emerald-500/15' : ''"
                >
                  <td class="py-1 font-bold flex items-center gap-1" :class="model.color">
                    <span class="w-1.5 h-1.5 rounded-full" :class="activeMethodKey === model.id ? 'bg-emerald-400' : 'bg-slate-600'"></span>
                    <span>{{ model.name }}</span>
                  </td>
                  <td class="py-1 text-center font-bold text-slate-200">
                    {{ model.breakdownPoint }}
                  </td>
                  <td class="py-1 text-center font-bold text-slate-200">
                    {{ model.outlierYield }}
                  </td>
                  <td class="py-1 text-[7.2px] text-slate-300 leading-tight pr-1">
                    {{ model.primaryFinding }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Deep-Dive Diagnostic Inspector Box for Selected Method -->
          <div class="bg-[#071411] p-1.5 rounded-lg border border-emerald-500/25 font-mono text-[7.5px]">
            <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-slate-800">
              <span class="font-bold flex items-center gap-1.5" :class="currentMethod.color">
                <span>Method Inspector: {{ currentMethod.name }}</span>
                <span class="text-[6.5px] px-1 py-0.2 rounded border" :class="currentMethod.badgeColor">{{ currentMethod.paradigm }}</span>
              </span>
              <span class="text-[6.8px] text-slate-400">
                Outliers Flagged: <strong class="text-white">{{ currentMethod.yieldCount }}</strong>
              </span>
            </div>

            <!-- Formula Block -->
            <div class="bg-slate-900/90 p-1 rounded border border-slate-800 mb-1">
              <div class="text-[7.2px] text-emerald-400 font-bold">
                Formula: {{ currentMethod.formula }}
              </div>
              <div class="text-[6.5px] text-slate-400 space-y-0.2 mt-0.5">
                <div v-for="(item, idx) in currentMethod.whereBlock" :key="idx" class="truncate">
                  • {{ item }}
                </div>
              </div>
            </div>

            <!-- Case Study Finding -->
            <div class="text-[7.2px] text-slate-300 leading-tight">
              <strong class="text-teal-300">Empirical Validation Evidence: </strong>
              {{ currentMethod.empiricalCaseStudy }}
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Future Quantitative Research Roadmap (Full-Height Card, NO Thank You Banner!) -->
      <div class="col-span-6 flex flex-col">
        <div class="glass-card p-2 flex flex-col justify-between flex-1">
          <div>
            <!-- Header -->
            <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
              <div class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-sm bg-emerald-400"></span>
                <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
                  Future Quantitative Research Roadmap (Next Horizons)
                </span>
              </div>
              <span class="text-[7.5px] font-mono px-1.5 py-0.2 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                3 Strategic Pillars
              </span>
            </div>

            <!-- Roadmap Pillars Accordion / Card Deck -->
            <div class="space-y-1.5">
              <div
                v-for="pillar in filteredRoadmapPillars"
                :key="pillar.id"
                class="bg-[#071411]/90 p-2 rounded-lg border font-mono transition-all"
                :class="activeRoadmapPhase === pillar.phaseKey
                  ? 'border-emerald-400 bg-emerald-950/25 shadow-[0_0_12px_rgba(52,211,153,0.25)]'
                  : 'border-slate-800/80 hover:border-emerald-500/30'"
              >
                <!-- Pillar Header Line -->
                <div class="flex items-center justify-between mb-1 pb-0.5 border-b border-slate-800">
                  <div class="flex items-center gap-1.5">
                    <span class="text-[7.5px] px-1 py-0.2 rounded font-bold border" :class="pillar.badgeColor">
                      {{ pillar.phaseNumber }}
                    </span>
                    <span class="text-[9px] font-bold text-white tracking-tight">
                      {{ pillar.title }}
                    </span>
                  </div>
                  <span class="text-[7px] text-slate-400 font-bold">
                    {{ pillar.timeline }}
                  </span>
                </div>

                <!-- Subtitle / Concept -->
                <div class="text-[7.8px] font-bold mb-1" :class="pillar.color">
                  {{ pillar.subtitle }}
                </div>

                <!-- Challenge & Method Description -->
                <div class="text-[7.2px] text-slate-300 leading-relaxed mb-1 font-sans">
                  <span class="text-slate-400 font-mono font-bold">Methodological Architecture: </span>
                  {{ pillar.methodology }}
                </div>

                <!-- Mathematical Formulation (Shown when selected or in all) -->
                <div class="bg-slate-900/90 p-1 rounded border border-slate-800 mb-1 text-[6.8px]">
                  <div class="text-teal-300 font-bold mb-0.5">Formal Model: {{ pillar.mathFormulation }}</div>
                  <div class="text-[6.5px] text-slate-400 space-y-0.2">
                    <div v-for="(item, idx) in pillar.mathWhere.slice(0, 2)" :key="idx" class="truncate">
                      • {{ item }}
                    </div>
                  </div>
                </div>

                <!-- Milestone Tags & Tech Stack Chips -->
                <div class="flex items-center justify-between pt-0.5 text-[6.5px]">
                  <!-- Milestones -->
                  <div class="flex items-center gap-1 overflow-x-auto">
                    <span class="text-slate-500 font-bold">Milestones:</span>
                    <span
                      v-for="ms in pillar.milestones.slice(0, 3)"
                      :key="ms"
                      class="px-1 py-0.2 rounded bg-slate-800 text-slate-300 border border-slate-700 truncate"
                    >
                      {{ ms }}
                    </span>
                  </div>

                  <!-- Tech Stack Chips -->
                  <div class="flex items-center gap-1">
                    <span
                      v-for="tech in pillar.techStack.slice(0, 3)"
                      :key="tech"
                      class="px-1 py-0.2 rounded bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-bold"
                    >
                      {{ tech }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Bottom Quantitative Engineering Note -->
          <div class="text-[7.5px] text-slate-400 bg-[#071411]/90 p-1.5 rounded-lg border border-emerald-500/15 leading-tight font-mono mt-1">
            <strong class="text-emerald-300">Continuous Quantitative Innovation:</strong> Transitioning from cross-sectional factor estimation to temporal regime adaptation, systemic counterparty graph contagion, and automated NLP extraction establishes an end-to-end institutional financial intelligence infrastructure.
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Bar -->
    <div class="glass-card px-3 py-1 flex items-center justify-between text-[9px] font-mono">
      <div class="flex items-center gap-2 text-slate-300">
        <span class="text-emerald-400 font-bold">Empirical Synthesis:</span>
        <span class="text-slate-400">
          Validated across 150+ NSE equities with 88.5% cache hit rate and &lt;1.8s SLA, proving that non-parametric and multivariate anomaly models surpass classical Gaussian metrics in institutional financial screening.
        </span>
      </div>
      <span class="text-emerald-300 text-[8px] bg-emerald-500/10 border border-emerald-500/25 px-1.5 py-0.5 rounded">
        Slide 16: Empirical Validation &amp; Research Roadmap
      </span>
    </div>
  </div>
</template>

<style scoped>
.glass-card {
  background: rgba(13, 33, 27, 0.70);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(52, 211, 153, 0.18);
  border-radius: 12px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
}

.glass-card:hover {
  border-color: rgba(52, 211, 153, 0.35);
  box-shadow: 0 10px 36px 0 rgba(16, 185, 129, 0.15);
}
</style>
