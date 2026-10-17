<script setup lang="ts">
import { ref, computed } from 'vue'

// Active tab: 'pillars' (16 metrics explorer) or 'guardrails' (safe_divide & pathological lab)
const activeView = ref<'pillars' | 'guardrails'>('pillars')

// Five Weighted Pillars Data
interface MetricDefinition {
  id: string
  name: string
  formula: string
  description: string
  higherIsBetter: boolean
  benchmarks: {
    it: string
    auto: string
    fmcg: string
    utilities: string
  }
}

interface PillarDefinition {
  id: number
  key: string
  name: string
  weight: number
  color: string
  accentBorder: string
  badgeBg: string
  summary: string
  metrics: MetricDefinition[]
  guardrailNote: string
}

const pillars: PillarDefinition[] = [
  {
    id: 1,
    key: 'profitability',
    name: 'Profitability',
    weight: 30,
    color: '#34D399',
    accentBorder: 'border-emerald-400/40',
    badgeBg: 'bg-emerald-500/20 text-emerald-300',
    summary: 'Assesses earning power, capital return efficiency, and cost conversion margins across operational tiers.',
    guardrailNote: 'Negative income firms carry clamped zero scores; PAT floor avoids inverse ROE sign inversion.',
    metrics: [
      {
        id: 'gm',
        name: 'Gross Profit Margin',
        formula: '(Gross Profit / Sales) × 100%',
        description: 'Direct production margin after subtracting raw material & direct labor expenses (COGS).',
        higherIsBetter: true,
        benchmarks: { it: '42.5%', auto: '21.0%', fmcg: '48.5%', utilities: '28.0%' },
      },
      {
        id: 'om',
        name: 'Operating Margin (EBIT)',
        formula: '(EBIT / Sales) × 100%',
        description: 'Core operational profitability before debt servicing costs, corporate taxes, and exceptional items.',
        higherIsBetter: true,
        benchmarks: { it: '24.5%', auto: '10.5%', fmcg: '20.2%', utilities: '14.0%' },
      },
      {
        id: 'nm',
        name: 'Net Profit Margin (PAT)',
        formula: '(Net Income / Sales) × 100%',
        description: 'Bottom-line residual return available to equity shareholders after all operating, debt, and tax charges.',
        higherIsBetter: true,
        benchmarks: { it: '18.2%', auto: '6.8%', fmcg: '14.5%', utilities: '8.5%' },
      },
      {
        id: 'roe',
        name: 'Return on Equity (ROE)',
        formula: '(Net Income / Equity) × 100%',
        description: 'Efficiency of deploying shareholders equity capital; cross-analyzed via DuPont decomposition.',
        higherIsBetter: true,
        benchmarks: { it: '26.4%', auto: '16.2%', fmcg: '32.0%', utilities: '10.5%' },
      },
      {
        id: 'roa',
        name: 'Return on Assets (ROA)',
        formula: '(Net Income / Assets) × 100%',
        description: 'Overall capital productivity measuring net profit generated per unit of total enterprise asset base.',
        higherIsBetter: true,
        benchmarks: { it: '16.8%', auto: '7.5%', fmcg: '15.4%', utilities: '3.2%' },
      },
    ],
  },
  {
    id: 2,
    key: 'solvency',
    name: 'Solvency & Capital Structure',
    weight: 25,
    color: '#38BDF8',
    accentBorder: 'border-sky-400/40',
    badgeBg: 'bg-sky-500/20 text-sky-300',
    summary: 'Measures structural debt leverage, long-term solvency obligations, and fixed-charge interest coverage.',
    guardrailNote: 'Negative net worth intercepted immediately; zero-interest debt-free firms bypass division-by-zero.',
    metrics: [
      {
        id: 'de',
        name: 'Debt-to-Equity (D/E)',
        formula: 'Total Debt / Shareholders Equity',
        description: 'Ratio of external borrowed debt capital relative to net worth. Evaluates financial gearing risk.',
        higherIsBetter: false,
        benchmarks: { it: '0.04x', auto: '0.45x', fmcg: '0.12x', utilities: '2.15x' },
      },
      {
        id: 'dr',
        name: 'Debt Ratio',
        formula: 'Total Debt / Total Assets',
        description: 'Proportion of total firm assets funded through short-term and long-term interest-bearing debt.',
        higherIsBetter: false,
        benchmarks: { it: '3.2%', auto: '22.0%', fmcg: '7.5%', utilities: '52.0%' },
      },
      {
        id: 'icr',
        name: 'Interest Coverage Ratio',
        formula: 'EBIT / Finance Charges',
        description: 'Margin of safety for servicing debt interest; debt-free firms receive safe unlevered classification.',
        higherIsBetter: true,
        benchmarks: { it: 'Unlevered', auto: '9.8x', fmcg: '24.0x', utilities: '2.3x' },
      },
    ],
  },
  {
    id: 3,
    key: 'growth',
    name: 'Growth Trajectory',
    weight: 15,
    color: '#A855F7',
    accentBorder: 'border-purple-400/40',
    badgeBg: 'bg-purple-500/20 text-purple-300',
    summary: 'Evaluates top-line sales acceleration, bottom-line net profit compound growth, and cash conversion expansion.',
    guardrailNote: 'Sign-aware denominator formula prevents false positive growth when prior-year cash flows were negative.',
    metrics: [
      {
        id: 'rev_growth',
        name: 'YoY Revenue Growth',
        formula: '((Rev_t - Rev_{t-1}) / |Rev_{t-1}|) × 100%',
        description: 'Year-over-year operational expansion rate across continuous 4-year financial disclosure series.',
        higherIsBetter: true,
        benchmarks: { it: '12.4%', auto: '14.5%', fmcg: '9.8%', utilities: '7.2%' },
      },
      {
        id: 'ni_growth',
        name: 'Net Income Growth',
        formula: '((NI_t - NI_{t-1}) / |NI_{t-1}|) × 100%',
        description: 'Trailing bottom-line profit growth rate after accounting for cyclical tax and financing swings.',
        higherIsBetter: true,
        benchmarks: { it: '14.0%', auto: '18.2%', fmcg: '11.5%', utilities: '5.8%' },
      },
      {
        id: 'ocf_growth',
        name: 'Operating Cash Flow Growth',
        formula: '((OCF_t - OCF_{t-1}) / |OCF_{t-1}|) × 100%',
        description: 'True cash earnings momentum validating that reported earnings growth is backed by cash receipts.',
        higherIsBetter: true,
        benchmarks: { it: '15.2%', auto: '12.0%', fmcg: '13.4%', utilities: '4.5%' },
      },
    ],
  },
  {
    id: 4,
    key: 'liquidity',
    name: 'Liquidity Coverage',
    weight: 15,
    color: '#F59E0B',
    accentBorder: 'border-amber-400/40',
    badgeBg: 'bg-amber-500/20 text-amber-300',
    summary: 'Assesses short-term working capital buffers, liquid reserves, and immediate debt obligations due within 12 months.',
    guardrailNote: 'Working capital deficits flag liquidity stress regardless of high non-cash accrual revenue.',
    metrics: [
      {
        id: 'cr',
        name: 'Current Ratio',
        formula: 'Current Assets / Current Liabilities',
        description: 'Overall working capital adequacy buffer to cover short-term financial claims due within 1 year.',
        higherIsBetter: true,
        benchmarks: { it: '2.65x', auto: '1.25x', fmcg: '1.45x', utilities: '1.05x' },
      },
      {
        id: 'qr',
        name: 'Quick Ratio (Acid Test)',
        formula: '(CA - Inventory) / Current Liabilities',
        description: 'Strict liquidity buffer excluding illiquid raw materials, work-in-progress, and finished goods inventories.',
        higherIsBetter: true,
        benchmarks: { it: '2.65x', auto: '0.88x', fmcg: '1.02x', utilities: '0.82x' },
      },
      {
        id: 'cash_ratio',
        name: 'Cash Ratio',
        formula: 'Cash & Equivalents / Current Liabilities',
        description: 'Ultra-conservative solvency test measuring immediate cash and bank balances against all current debt.',
        higherIsBetter: true,
        benchmarks: { it: '1.75x', auto: '0.42x', fmcg: '0.58x', utilities: '0.22x' },
      },
    ],
  },
  {
    id: 5,
    key: 'efficiency',
    name: 'Operating Efficiency',
    weight: 15,
    color: '#10B981',
    accentBorder: 'border-teal-400/40',
    badgeBg: 'bg-teal-500/20 text-teal-300',
    summary: 'Analyzes velocity of asset utilization, revenue turnover cycles, and supply chain inventory throughput.',
    guardrailNote: 'Asset-light IT consulting firms without inventory bypass turnover calculations without metric penalties.',
    metrics: [
      {
        id: 'at',
        name: 'Total Asset Turnover',
        formula: 'Revenue / Total Assets',
        description: 'Operating velocity measuring how many rupees of sales are generated per single rupee of deployed assets.',
        higherIsBetter: true,
        benchmarks: { it: '1.05x', auto: '1.35x', fmcg: '2.10x', utilities: '0.45x' },
      },
      {
        id: 'it',
        name: 'Inventory Turnover',
        formula: 'COGS / Average Inventory',
        description: 'Frequency of inventory cycling and sales clearance; IT firms bypass this metric automatically.',
        higherIsBetter: true,
        benchmarks: { it: 'Bypassed', auto: '8.4x', fmcg: '11.2x', utilities: '5.1x' },
      },
    ],
  },
]

const selectedPillarIndex = ref(0)
const selectedPillar = computed(() => pillars[selectedPillarIndex.value])
const selectedMetricIndex = ref(0)
const selectedMetric = computed(() => selectedPillar.value.metrics[selectedMetricIndex.value] || selectedPillar.value.metrics[0])
const selectedSector = ref<'it' | 'auto' | 'fmcg' | 'utilities'>('it')

function selectPillar(idx: number) {
  selectedPillarIndex.value = idx
  selectedMetricIndex.value = 0
}

// -------------------------------------------------------------
// Interactive safe_divide(a, b, ε) Simulator
// -------------------------------------------------------------
const numA = ref<number>(1450)
const denomB = ref<number>(250)
const epsilonChoice = ref<'1e-6' | '1e-9'>('1e-6')
const epsilonVal = computed(() => (epsilonChoice.value === '1e-6' ? 1e-6 : 1e-9))
const isNegativeEquityTrap = ref<boolean>(false)

interface DivisionResult {
  status: 'safe' | 'zero_div' | 'negative_equity' | 'sub_epsilon'
  statusLabel: string
  statusBadgeClass: string
  computedValueText: string
  actionTaken: string
  riskPenalty: number
}

const safeDivideResult = computed<DivisionResult>(() => {
  const a = numA.value
  const b = denomB.value
  const eps = epsilonVal.value

  // Case 1: Negative Book Equity Trap
  if (isNegativeEquityTrap.value || (b < 0 && activePreset.value === 'distressed_equity')) {
    return {
      status: 'negative_equity',
      statusLabel: '🚨 Insolvent Capital Deficit Intercepted',
      statusBadgeClass: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
      computedValueText: 'INTERCEPTED [DEFICIT TRAP]',
      actionTaken: 'Suppressed negative denominator from producing falsely low D/E. Assigned maximum risk penalty (Score: 99.9).',
      riskPenalty: 99.9,
    }
  }

  // Case 2: Exact Zero or Sub-Epsilon Singularity
  if (Math.abs(b) <= eps) {
    if (b === 0) {
      return {
        status: 'zero_div',
        statusLabel: '⚠️ Singularity Guardrail: Zero Div Protected',
        statusBadgeClass: 'bg-amber-500/20 text-amber-300 border-amber-500/40',
        computedValueText: 'NaN [Debt-Free Unlevered]',
        actionTaken: 'Intercepted division by 0.00. Emits typed IEEE NaN and dynamically reweights pillar without crash.',
        riskPenalty: 0.0,
      }
    } else {
      return {
        status: 'sub_epsilon',
        statusLabel: 'ℹ️ Sub-Epsilon Floor Intercepted (|b| < ε)',
        statusBadgeClass: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40',
        computedValueText: 'NaN [Machine Precision Guard]',
        actionTaken: `Absolute denominator |${b}| is below machine threshold ε = ${epsilonChoice.value}. Clamped to safe NaN.`,
        riskPenalty: 15.0,
      }
    }
  }

  // Case 3: Normal Valid Division
  const val = a / b
  return {
    status: 'safe',
    statusLabel: '✓ Safe Finite IEEE Float Computed',
    statusBadgeClass: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
    computedValueText: `${val.toFixed(2)}x`,
    actionTaken: `Valid denominator (|b| = ${Math.abs(b)} > ε). Standard vectorized ratio calculated.`,
    riskPenalty: 0.0,
  }
})

// Simulator Presets
type PresetKey = 'standard_icr' | 'unlevered_it' | 'sub_epsilon' | 'distressed_equity' | 'negative_ocf'
const activePreset = ref<PresetKey>('standard_icr')

function applyPreset(preset: PresetKey) {
  activePreset.value = preset
  isNegativeEquityTrap.value = false
  if (preset === 'standard_icr') {
    numA.value = 1450 // EBIT ₹1,450 Cr
    denomB.value = 250 // Interest ₹250 Cr
  } else if (preset === 'unlevered_it') {
    numA.value = 8200 // EBIT ₹8,200 Cr
    denomB.value = 0 // Zero Interest
  } else if (preset === 'sub_epsilon') {
    numA.value = 500
    denomB.value = 0.00000001 // 1e-8
    epsilonChoice.value = '1e-6'
  } else if (preset === 'distressed_equity') {
    numA.value = 3500 // Total Debt ₹3,500 Cr
    denomB.value = -450 // Negative Equity Deficit -₹450 Cr
    isNegativeEquityTrap.value = true
  } else if (preset === 'negative_ocf') {
    numA.value = -50
    denomB.value = 120
  }
}
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between py-0.5 text-slate-100 select-none">
    <!-- Top Nav: View Switcher & Pillar Navigation -->
    <div class="flex items-center justify-between gap-3 px-3 py-1.5 glass-card">
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] font-mono uppercase tracking-wider text-emerald-400 font-bold mr-1">
          Framework:
        </span>
        <button
          v-for="(p, idx) in pillars"
          :key="p.key"
          class="flex items-center gap-1 px-2.5 py-1 rounded-md text-[11px] font-bold transition-all duration-200 cursor-pointer"
          :class="selectedPillarIndex === idx && activeView === 'pillars'
            ? 'bg-emerald-500/25 text-white border border-emerald-400/50 shadow-[0_0_10px_rgba(52,211,153,0.25)]'
            : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40 border border-transparent'"
          @click="activeView = 'pillars'; selectPillar(idx)"
        >
          <span>{{ p.id }}. {{ p.name }}</span>
          <span class="px-1 py-0.2 rounded text-[9px] font-mono bg-[#071411]/80 text-emerald-300">
            {{ p.weight }}%
          </span>
        </button>
      </div>

      <!-- Mode Toggle -->
      <div class="flex items-center gap-1 bg-[#071411]/80 p-0.5 rounded-lg border border-emerald-500/20">
        <button
          class="px-2.5 py-1 rounded text-[10px] font-bold transition cursor-pointer"
          :class="activeView === 'pillars'
            ? 'bg-emerald-500/30 text-emerald-300 shadow-sm'
            : 'text-slate-400 hover:text-slate-200'"
          @click="activeView = 'pillars'"
        >
          16 Ratios Explorer
        </button>
        <button
          class="px-2.5 py-1 rounded text-[10px] font-bold transition cursor-pointer flex items-center gap-1"
          :class="activeView === 'guardrails'
            ? 'bg-cyan-500/30 text-cyan-300 shadow-sm'
            : 'text-slate-400 hover:text-slate-200'"
          @click="activeView = 'guardrails'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />
          <span>safe_divide(a, b, ε) Lab</span>
        </button>
      </div>
    </div>

    <!-- MAIN BODY: TAB 1 (16 Core Metrics & Pillar Explorer) -->
    <div v-if="activeView === 'pillars'" class="grid grid-cols-12 gap-2.5 my-1.5 items-stretch">
      <!-- Left Column: Metrics List in Selected Pillar -->
      <div class="col-span-7 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Header for Selected Pillar -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-emerald-500/15">
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-white tracking-wide">
                {{ selectedPillar.id }}. {{ selectedPillar.name }} Framework
              </span>
              <span class="px-1.5 py-0.5 rounded text-[10px] font-mono font-bold" :class="selectedPillar.badgeBg">
                Weight: {{ selectedPillar.weight }}%
              </span>
            </div>
            <span class="text-[10px] text-slate-400 font-mono">
              {{ selectedPillar.metrics.length }} Core Metrics
            </span>
          </div>

          <!-- Description Summary -->
          <div class="text-[11px] text-slate-300 leading-tight mb-2 bg-[#071411]/60 p-1.5 rounded border border-emerald-500/10">
            {{ selectedPillar.summary }}
          </div>

          <!-- Metric Cards List -->
          <div class="space-y-1.5 max-h-[195px] overflow-y-auto pr-1">
            <div
              v-for="(m, mIdx) in selectedPillar.metrics"
              :key="m.id"
              class="p-2 rounded-lg border transition-all cursor-pointer"
              :class="selectedMetricIndex === mIdx
                ? 'bg-emerald-950/40 border-emerald-400/50 shadow-[0_0_8px_rgba(52,211,153,0.15)]'
                : 'bg-[#071411]/50 border-emerald-500/10 hover:border-emerald-500/25'"
              @click="selectedMetricIndex = mIdx"
            >
              <div class="flex items-center justify-between mb-0.5">
                <span class="text-[11px] font-bold text-white flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full" :style="{ backgroundColor: selectedPillar.color }" />
                  {{ m.name }}
                </span>
                <span class="text-[9px] font-mono px-1.5 py-0.2 rounded bg-slate-800 text-slate-300">
                  {{ m.higherIsBetter ? '▲ Higher is better' : '▼ Lower is better' }}
                </span>
              </div>
              <div class="flex items-center justify-between text-[10.5px]">
                <div class="font-mono text-emerald-300 text-[10px]">
                  {{ m.formula }}
                </div>
                <div class="text-[9.5px] text-slate-400">
                  Click to inspect
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Pillar Guardrail Alert Footer -->
        <div class="mt-1.5 text-[10px] bg-slate-900/80 p-1.5 rounded border border-amber-500/20 text-slate-300 flex items-start gap-1.5">
          <span class="text-amber-400 font-bold">🛡️ Guardrail:</span>
          <span>{{ selectedPillar.guardrailNote }}</span>
        </div>
      </div>

      <!-- Right Column: Detail Deep-Dive, Benchmarks & Where Parameter Block -->
      <div class="col-span-5 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Selected Metric Header -->
          <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-emerald-500/15">
            <span class="text-xs font-bold text-emerald-300">
              Metric Deep Dive: {{ selectedMetric.name }}
            </span>
            <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300">
              Pillar {{ selectedPillar.id }}
            </span>
          </div>

          <!-- Formula Box with KaTeX-Style Clear Block -->
          <div class="bg-[#071411]/90 p-2 rounded-lg border border-emerald-500/25 mb-2 text-center">
            <div class="text-[9.5px] text-slate-400 font-mono uppercase mb-0.5">
              Canonical Formulation
            </div>
            <div class="text-xs font-mono font-bold text-emerald-400">
              {{ selectedMetric.formula }}
            </div>
          </div>

          <!-- "Where:" Structured Parameter Definition Block -->
          <div class="bg-[#071411]/60 p-2 rounded border border-emerald-500/10 mb-2">
            <div class="text-[10px] font-bold text-slate-200 mb-1 flex items-center gap-1">
              <span class="text-emerald-400">Where:</span>
              <span class="text-[9px] text-slate-400 font-normal">Standardized MCA / Ind-AS Taxonomy</span>
            </div>
            <div class="text-[10px] text-slate-300 leading-tight">
              {{ selectedMetric.description }}
            </div>
          </div>

          <!-- Sector Benchmarks Grid -->
          <div class="mb-1">
            <div class="flex items-center justify-between mb-1">
              <span class="text-[10px] font-bold text-slate-300 uppercase tracking-wider">
                Cross-Sector Benchmarks (NSE Equities)
              </span>
              <span class="text-[9px] font-mono text-emerald-400">
                FY22–FY25 Median
              </span>
            </div>

            <div class="grid grid-cols-4 gap-1 text-center font-mono">
              <div class="bg-[#071411]/70 p-1.5 rounded border border-emerald-500/20">
                <div class="text-[8.5px] text-slate-400 uppercase">IT Services</div>
                <div class="text-[11px] font-bold text-emerald-300 mt-0.5">
                  {{ selectedMetric.benchmarks.it }}
                </div>
              </div>
              <div class="bg-[#071411]/70 p-1.5 rounded border border-sky-500/20">
                <div class="text-[8.5px] text-slate-400 uppercase">Automobile</div>
                <div class="text-[11px] font-bold text-sky-300 mt-0.5">
                  {{ selectedMetric.benchmarks.auto }}
                </div>
              </div>
              <div class="bg-[#071411]/70 p-1.5 rounded border border-amber-500/20">
                <div class="text-[8.5px] text-slate-400 uppercase">FMCG</div>
                <div class="text-[11px] font-bold text-amber-300 mt-0.5">
                  {{ selectedMetric.benchmarks.fmcg }}
                </div>
              </div>
              <div class="bg-[#071411]/70 p-1.5 rounded border border-purple-500/20">
                <div class="text-[8.5px] text-slate-400 uppercase">Utilities</div>
                <div class="text-[11px] font-bold text-purple-300 mt-0.5">
                  {{ selectedMetric.benchmarks.utilities }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Metric Attribution Status -->
        <div class="text-[9.5px] font-mono text-slate-400 flex items-center justify-between pt-1 border-t border-emerald-500/10">
          <span>Vectorized NumPy Implementation</span>
          <span class="text-emerald-400 font-bold">100% NaN-Safe</span>
        </div>
      </div>
    </div>

    <!-- MAIN BODY: TAB 2 (safe_divide Simulator & Pathological Lab) -->
    <div v-else class="grid grid-cols-12 gap-2.5 my-1.5 items-stretch">
      <!-- Left Column: Mathematical Definition & Scenarios -->
      <div class="col-span-6 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-cyan-500/20">
            <span class="text-xs font-bold text-white flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-cyan-400" />
              Singularity Guardrail: safe_divide(a, b, ε)
            </span>
            <span class="text-[10px] font-mono text-cyan-300">
              ε = {{ epsilonChoice }}
            </span>
          </div>

          <!-- Mathematical Formula Definition Card -->
          <div class="bg-[#071411]/90 p-2 rounded-lg border border-cyan-500/30 mb-2">
            <div class="text-[11px] font-mono text-cyan-300 text-center leading-relaxed">
              safe_divide(a, b, ε) = <br>
              <span class="text-emerald-300 font-bold">a / b</span> if |b| &gt; ε &nbsp;|&nbsp;
              <span class="text-rose-300 font-bold">NaN / Intercepted</span> if |b| ≤ ε or b &lt; 0 (Deficit)
            </div>
          </div>

          <!-- Where: Definition Block -->
          <div class="bg-[#071411]/70 p-1.5 rounded border border-cyan-500/15 mb-2 text-[10px] text-slate-300">
            <div class="font-bold text-slate-200 mb-0.5 text-[9.5px]">
              <span class="text-cyan-400">Where:</span>
            </div>
            <ul class="list-disc pl-3.5 space-y-0.5 text-[9.5px]">
              <li><strong>a:</strong> Numerator financial line-item (e.g. EBIT, Total Debt, Operating Cash Flow).</li>
              <li><strong>b:</strong> Denominator base (e.g. Finance Charges, Book Equity, Current Liabilities).</li>
              <li><strong>ε = 10⁻⁶:</strong> Machine precision zero-threshold preventing division-by-zero crashes.</li>
            </ul>
          </div>

          <!-- Interactive Test Preset Scenarios -->
          <div class="space-y-1">
            <div class="text-[10px] font-bold text-slate-300 uppercase tracking-wide">
              Select Pathological Test Scenario:
            </div>
            <div class="grid grid-cols-2 gap-1 text-[10px]">
              <button
                class="p-1.5 rounded border text-left transition cursor-pointer"
                :class="activePreset === 'standard_icr'
                  ? 'bg-emerald-500/25 border-emerald-400/50 text-white'
                  : 'bg-[#071411]/60 border-slate-700 text-slate-300 hover:border-slate-500'"
                @click="applyPreset('standard_icr')"
              >
                <div class="font-bold text-emerald-300">1. Nominal ICR</div>
                <div class="text-[9px] text-slate-400">EBIT ₹1450, Interest ₹250</div>
              </button>

              <button
                class="p-1.5 rounded border text-left transition cursor-pointer"
                :class="activePreset === 'unlevered_it'
                  ? 'bg-amber-500/25 border-amber-400/50 text-white'
                  : 'bg-[#071411]/60 border-slate-700 text-slate-300 hover:border-slate-500'"
                @click="applyPreset('unlevered_it')"
              >
                <div class="font-bold text-amber-300">2. Zero Interest (Debt-Free)</div>
                <div class="text-[9px] text-slate-400">EBIT ₹8200, Interest ₹0.00</div>
              </button>

              <button
                class="p-1.5 rounded border text-left transition cursor-pointer"
                :class="activePreset === 'sub_epsilon'
                  ? 'bg-cyan-500/25 border-cyan-400/50 text-white'
                  : 'bg-[#071411]/60 border-slate-700 text-slate-300 hover:border-slate-500'"
                @click="applyPreset('sub_epsilon')"
              >
                <div class="font-bold text-cyan-300">3. Sub-Epsilon Denominator</div>
                <div class="text-[9px] text-slate-400">|b| = 10⁻⁸ &lt; ε = 10⁻⁶</div>
              </button>

              <button
                class="p-1.5 rounded border text-left transition cursor-pointer"
                :class="activePreset === 'distressed_equity'
                  ? 'bg-rose-500/25 border-rose-400/50 text-white'
                  : 'bg-[#071411]/60 border-slate-700 text-slate-300 hover:border-slate-500'"
                @click="applyPreset('distressed_equity')"
              >
                <div class="font-bold text-rose-300">4. Negative Equity Deficit</div>
                <div class="text-[9px] text-slate-400">Debt ₹3500, Equity -₹450</div>
              </button>
            </div>
          </div>
        </div>

        <div class="text-[9px] font-mono text-slate-400 mt-2 bg-[#071411]/40 p-1 rounded">
          Status: Eliminates catastrophic IEEE-754 ZeroDivisionError across all batch runs.
        </div>
      </div>

      <!-- Right Column: Interactive Sandbox & Live Evaluation Output -->
      <div class="col-span-6 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2 pb-1 border-b border-cyan-500/20">
            <span class="text-xs font-bold text-cyan-300">
              Live Interactive Simulator Sandbox
            </span>
            <!-- Epsilon Toggle -->
            <div class="flex items-center gap-1 text-[9px] font-mono">
              <span class="text-slate-400">Threshold:</span>
              <button
                class="px-1.5 py-0.5 rounded transition cursor-pointer"
                :class="epsilonChoice === '1e-6' ? 'bg-cyan-500/30 text-cyan-300 font-bold' : 'text-slate-500'"
                @click="epsilonChoice = '1e-6'"
              >
                10⁻⁶
              </button>
              <button
                class="px-1.5 py-0.5 rounded transition cursor-pointer"
                :class="epsilonChoice === '1e-9' ? 'bg-cyan-500/30 text-cyan-300 font-bold' : 'text-slate-500'"
                @click="epsilonChoice = '1e-9'"
              >
                10⁻⁹
              </button>
            </div>
          </div>

          <!-- Controls: Sliders for Numerator and Denominator -->
          <div class="space-y-2 mb-2">
            <div>
              <div class="flex justify-between text-[10px] font-mono mb-0.5">
                <span class="text-slate-300">Numerator (a): ₹{{ numA }} Cr</span>
                <span class="text-slate-400">Range: -500 to +10,000</span>
              </div>
              <input
                v-model.number="numA"
                type="range"
                min="-500"
                max="10000"
                step="50"
                class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-emerald-400"
              >
            </div>

            <div>
              <div class="flex justify-between text-[10px] font-mono mb-0.5">
                <span class="text-slate-300">Denominator (b): {{ denomB }}</span>
                <span class="text-slate-400">Range: -500 to +2,000</span>
              </div>
              <input
                v-model.number="denomB"
                type="range"
                min="-500"
                max="2000"
                step="10"
                class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-400"
              >
            </div>
          </div>

          <!-- Result Card -->
          <div class="bg-[#071411]/90 p-2.5 rounded-lg border border-emerald-500/25 mb-2">
            <div class="flex items-center justify-between mb-1">
              <span class="text-[9.5px] font-mono uppercase text-slate-400">
                Evaluation Output
              </span>
              <span class="px-2 py-0.5 rounded text-[9.5px] font-bold border" :class="safeDivideResult.statusBadgeClass">
                {{ safeDivideResult.statusLabel }}
              </span>
            </div>

            <div class="flex items-baseline justify-between mt-1 pt-1 border-t border-slate-800">
              <span class="text-[10px] text-slate-400 font-mono">Calculated Ratio:</span>
              <span class="text-base font-extrabold font-mono tracking-tight" :class="safeDivideResult.status === 'safe' ? 'text-emerald-300' : 'text-amber-300'">
                {{ safeDivideResult.computedValueText }}
              </span>
            </div>
          </div>

          <!-- Action Taken Log -->
          <div class="bg-[#071411]/60 p-2 rounded border border-emerald-500/10 text-[9.5px] text-slate-300">
            <strong class="text-white">Execution Trace:</strong>
            <div class="mt-0.5 text-slate-300 leading-tight">
              {{ safeDivideResult.actionTaken }}
            </div>
          </div>
        </div>

        <div class="flex items-center justify-between text-[9px] font-mono text-slate-400 pt-1 border-t border-emerald-500/10">
          <span>Exception Interceptor</span>
          <span class="text-emerald-300 font-bold">Zero Crash Guarantee</span>
        </div>
      </div>
    </div>

    <!-- Bottom KPI Metric Cards Grid (4 Essential Metrics) -->
    <div class="grid grid-cols-4 gap-2.5 pt-0.5">
      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-emerald-400 uppercase tracking-wider">
          Analytical Pillars
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          5 Weighted Tiers
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          100% Normalized Weight
        </div>
      </div>

      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-sky-400 uppercase tracking-wider">
          Core Metrics Spanned
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          16 Ratios
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          Across 12 NSE Sectors
        </div>
      </div>

      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-amber-400 uppercase tracking-wider">
          Singularity Defense
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          ε = 10⁻⁶ Guard
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          Zero-Div Safe IEEE NaNs
        </div>
      </div>

      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-purple-400 uppercase tracking-wider">
          Negative Equity Defense
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          Insolvency Intercept
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          Suppresses Falsely Low D/E
        </div>
      </div>
    </div>
  </div>
</template>
