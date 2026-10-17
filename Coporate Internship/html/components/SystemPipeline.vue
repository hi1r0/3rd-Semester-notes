<script setup lang="ts">
import { ref, onUnmounted } from 'vue'

interface StageInfo {
  id: number
  key: string
  name: string
  module: string
  sla: string
  slaMs: number
  badge: string
  input: string
  output: string
  description: string
  highlights: string[]
  metrics: { label: string; value: string }[]
}

const stages: StageInfo[] = [
  {
    id: 1,
    key: 'ingestion',
    name: 'Ingestion & Cache',
    module: 'SectorLoader',
    sla: '< 220 ms',
    slaMs: 220,
    badge: 'Stage 1',
    input: '150+ NSE Tickers (.NS)',
    output: 'Snappy Parquet Tensors',
    description: 'Asynchronous multi-threaded ingestion engine with multi-tier caching (RAM LRU & Snappy Parquet disk). Bypasses public rate limits and guarantees 4-year financial statement continuity.',
    highlights: [
      'Asynchronous batch pull of 4-yr balance sheets & cash flows',
      'Dual-tier cache: RAM hash-map (<1ms) + Parquet columnar',
      'SHA-256 payload fingerprinting & deterministic TTL',
      '88.5% cache hit rate eliminating HTTP 429 rate limits',
    ],
    metrics: [
      { label: 'Ingestion Latency', value: '214 ms' },
      { label: 'Cache Hit Rate', value: '88.5%' },
      { label: 'Statements / Firm', value: '4 Years' },
    ],
  },
  {
    id: 2,
    key: 'parsing',
    name: 'Vectorized Ratio Engine',
    module: 'FinancialParser',
    sla: '< 310 ms',
    slaMs: 310,
    badge: 'Stage 2',
    input: 'Raw Filing Line-Items',
    output: '16 Canonical Ratios',
    description: 'Deterministic schema harmonization mapping disparate filing line-items to canonical accounting definitions. Computes 16 cross-sectional ratios across 5 financial pillars.',
    highlights: [
      'Deterministic regex alias resolver (e.g. NetSales ➔ rev)',
      'Singularity guardrail: safe_divide(a, b, ε) with IEEE NaNs',
      'Accounting identity validation: Assets ≈ Liabilities + Equity',
      'Negative book equity interceptor isolating insolvent firms',
    ],
    metrics: [
      { label: 'Ratio Computation', value: '302 ms' },
      { label: 'Canonical Pillars', value: '5 Pillars' },
      { label: 'Singularity Crashes', value: '0.00%' },
    ],
  },
  {
    id: 3,
    key: 'engines',
    name: 'Anomaly Detection',
    module: 'OutlierEngine',
    sla: '< 780 ms',
    slaMs: 780,
    badge: 'Stage 3',
    input: '16-D Feature Vectors',
    output: 'Tri-Model Outlier Flags',
    description: 'Multi-tiered outlier consensus combining non-parametric dispersion and machine learning geometry in ℝ¹⁶ to eliminate masking while isolating true distressed anomalies.',
    highlights: [
      'Non-parametric Tukey boxplot fences ([Q₁ - 1.5·IQR, Q₃ + 1.5·IQR])',
      'Modified MAD Z-score with 50% breakdown point resistance',
      'Isolation Forest ensemble (100 trees) in ℝ¹⁶ feature space',
      'Consensus voting suppresses false-positive swamping',
    ],
    metrics: [
      { label: 'Detection Latency', value: '768 ms' },
      { label: 'Breakdown Point', value: 'ε* = 50%' },
      { label: 'ML Vector Space', value: 'ℝ¹⁶' },
    ],
  },
  {
    id: 4,
    key: 'delivery',
    name: 'Reporting Suite',
    module: 'SynthesisEngine',
    sla: '< 430 ms',
    slaMs: 430,
    badge: 'Stage 4',
    input: 'Consensus Anomaly Scores',
    output: 'LLM Memo & 6-Tab Excel',
    description: 'Automated executive delivery pipeline transforming raw anomaly vectors into human-readable strategic memos, 5-tier credit radars, and audit-grade financial workbooks.',
    highlights: [
      'Sigmoid peer score normalization calibrated from 0 to 100',
      '5-tier credit health radar (Prime, Strong, Stable, Watch, Distressed)',
      'Gemini LLM executive narration with financial reasoning',
      '6-tab openpyxl formatted audit workbook generated dynamically',
    ],
    metrics: [
      { label: 'Workbook Generation', value: '416 ms' },
      { label: 'Audit Workbook', value: '6 Tabs' },
      { label: 'Delivery Channels', value: 'Excel + Web' },
    ],
  },
]

const selectedStageId = ref<number>(1)
const isSimulating = ref<boolean>(false)
const activeSimStage = ref<number>(0)
const simulatedTimeMs = ref<number>(1740)
const activeTicker = ref<string>('ALL EQUITIES READY')

let simulationTimer: ReturnType<typeof setInterval> | null = null

const tickers = ['TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'ITC.NS', 'LT.NS', 'SBIN.NS']

function runPipelineSimulation() {
  if (isSimulating.value) return
  isSimulating.value = true
  activeSimStage.value = 1
  selectedStageId.value = 1
  simulatedTimeMs.value = 0

  const startTime = Date.now()
  const totalDuration = 1740 // 1.74s

  simulationTimer = setInterval(() => {
    const elapsed = Date.now() - startTime
    simulatedTimeMs.value = Math.min(elapsed, totalDuration)

    // Stage 1: 0 - 220ms
    if (elapsed < 220) {
      activeSimStage.value = 1
      selectedStageId.value = 1
      const tickerIdx = Math.floor((elapsed / 220) * tickers.length)
      activeTicker.value = `Caching ${tickers[tickerIdx % tickers.length]}...`
    }
    // Stage 2: 220 - 530ms
    else if (elapsed < 530) {
      activeSimStage.value = 2
      selectedStageId.value = 2
      activeTicker.value = 'Harmonizing Schema & Computing 16 Vector Ratios...'
    }
    // Stage 3: 530 - 1310ms
    else if (elapsed < 1310) {
      activeSimStage.value = 3
      selectedStageId.value = 3
      activeTicker.value = 'iForest Hyperplane Slicing + MAD Consensus (ℝ¹⁶)...'
    }
    // Stage 4: 1310 - 1740ms
    else if (elapsed < 1740) {
      activeSimStage.value = 4
      selectedStageId.value = 4
      activeTicker.value = 'Synthesizing Gemini Memo & 6-Tab Excel Workbook...'
    }
    // Complete
    else {
      activeSimStage.value = 0
      isSimulating.value = false
      simulatedTimeMs.value = 1740
      activeTicker.value = 'Pipeline Complete: 150+ NSE Equities Processed in 1.74s'
      if (simulationTimer) {
        clearInterval(simulationTimer)
        simulationTimer = null
      }
    }
  }, 30)
}

function selectStage(id: number) {
  selectedStageId.value = id
}

onUnmounted(() => {
  if (simulationTimer) {
    clearInterval(simulationTimer)
    simulationTimer = null
  }
})
</script>

<template>
  <div class="w-full flex flex-col gap-2.5 text-slate-100 select-none">
    <!-- Top Execution Control Bar & Telemetry -->
    <div class="glass-card px-3.5 py-2 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <button
          class="flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-bold transition-all duration-200"
          :class="isSimulating
            ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 cursor-wait'
            : 'bg-emerald-500/20 text-emerald-300 hover:bg-emerald-500/30 border border-emerald-400/40 shadow-[0_0_12px_rgba(52,211,153,0.25)] active:scale-95 cursor-pointer'"
          @click="runPipelineSimulation"
        >
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
            <polygon points="5 3 19 12 5 21 5 3" />
          </svg>
          <span>{{ isSimulating ? 'Executing Pipeline Stream...' : 'Stream End-to-End Pipeline' }}</span>
        </button>

        <div class="h-4 w-px bg-emerald-500/20 mx-1" />

        <div class="text-[11px] font-mono text-slate-300 flex items-center gap-1.5">
          <span class="text-slate-400">Status:</span>
          <span class="text-emerald-300 font-semibold">{{ activeTicker }}</span>
        </div>
      </div>

      <!-- Live Execution Clock KPI -->
      <div class="flex items-center gap-3">
        <div class="text-[11px] font-mono flex items-center gap-2">
          <span class="text-slate-400">Total Latency:</span>
          <span class="text-white font-bold bg-[#071411] px-2.5 py-0.5 rounded border border-emerald-500/30 text-emerald-300">
            {{ (simulatedTimeMs / 1000).toFixed(2) }}s
          </span>
          <span class="text-[10px] text-emerald-400/80 font-mono">(SLA: &lt; 1.80s)</span>
        </div>
      </div>
    </div>

    <!-- 4-Stage Horizontal Architectural Flow -->
    <div class="relative grid grid-cols-4 gap-3 items-stretch">
      <!-- Animated Pulsing Data Packet Overlay across Stages -->
      <div
        v-if="isSimulating"
        class="absolute -top-1.5 left-4 right-4 h-1 bg-gradient-to-r from-emerald-500/10 via-emerald-400 to-emerald-500/10 rounded-full z-10 pointer-events-none overflow-hidden"
      >
        <div
          class="h-full w-24 bg-gradient-to-r from-transparent via-[#00e599] to-transparent animate-pulse"
          :style="{
            transform: `translateX(${(simulatedTimeMs / 1740) * 850}%)`,
            transition: 'transform 0.05s linear',
          }"
        />
      </div>

      <!-- Stage Cards -->
      <div
        v-for="stg in stages"
        :key="stg.id"
        class="glass-card p-3 rounded-xl flex flex-col justify-between cursor-pointer transition-all duration-300 relative overflow-hidden"
        :class="[
          selectedStageId === stg.id ? 'border-emerald-400 shadow-[0_0_16px_rgba(52,211,153,0.22)] -translate-y-0.5' : 'hover:border-emerald-500/40',
          activeSimStage === stg.id ? 'ring-2 ring-emerald-400/80 bg-emerald-950/20' : '',
        ]"
        @click="selectStage(stg.id)"
      >
        <!-- Stage Card Header -->
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span
              class="px-2 py-0.5 rounded text-[10px] font-bold tracking-wider uppercase font-mono"
              :class="selectedStageId === stg.id ? 'bg-emerald-500/30 text-emerald-300 border border-emerald-400/40' : 'bg-slate-800 text-slate-400'"
            >
              [{{ stg.id }}] {{ stg.badge }}
            </span>
            <span class="text-[10px] font-mono text-emerald-400 font-bold bg-[#071411] px-1.5 py-0.5 rounded border border-emerald-500/20">
              {{ stg.sla }}
            </span>
          </div>

          <h3 class="text-xs font-bold text-white mb-0.5 tracking-tight flex items-center justify-between">
            <span>{{ stg.name }}</span>
            <span
              v-if="activeSimStage === stg.id"
              class="w-2 h-2 rounded-full bg-emerald-400 animate-ping inline-block"
            />
          </h3>

          <div class="text-[11px] font-mono text-emerald-300/90 font-medium mb-2">
            {{ stg.module }}
          </div>

          <div class="space-y-1 text-[10px] text-slate-300">
            <div class="flex items-center gap-1.5">
              <span class="text-slate-500 font-mono">In:</span>
              <span class="text-slate-200 truncate">{{ stg.input }}</span>
            </div>
            <div class="flex items-center gap-1.5">
              <span class="text-slate-500 font-mono">Out:</span>
              <span class="text-emerald-300 truncate">{{ stg.output }}</span>
            </div>
          </div>
        </div>

        <!-- Stage Card Footer: Mini Metric -->
        <div class="mt-2.5 pt-2 border-t border-emerald-500/15 flex items-center justify-between text-[10px]">
          <span class="text-slate-400">{{ stg.metrics[0].label }}</span>
          <span class="font-mono font-bold text-emerald-300">{{ stg.metrics[0].value }}</span>
        </div>
      </div>
    </div>

    <!-- Clickable Stage Drill-Down Inspector & Architecture Details -->
    <div class="glass-card p-3.5 border-emerald-500/25 relative overflow-hidden">
      <div v-for="stg in stages" :key="stg.id">
        <div v-if="selectedStageId === stg.id" class="grid grid-cols-12 gap-3.5 items-center">
          <!-- Left: Stage Description & Highlights -->
          <div class="col-span-8 flex flex-col justify-between">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="text-xs font-bold text-emerald-300 tracking-wide">
                Stage {{ stg.id }} Deep-Dive: {{ stg.name }} ({{ stg.module }})
              </span>
              <span class="text-[10px] text-slate-400 font-mono">Execution Budget: {{ stg.sla }}</span>
            </div>

            <p class="text-[11px] text-slate-300 leading-relaxed mb-2">
              {{ stg.description }}
            </p>

            <!-- Highlights Checklist -->
            <div class="grid grid-cols-2 gap-x-3 gap-y-1">
              <div
                v-for="(hl, idx) in stg.highlights"
                :key="idx"
                class="flex items-start gap-1.5 text-[10.5px] text-slate-200"
              >
                <span class="text-emerald-400 font-bold">✓</span>
                <span>{{ hl }}</span>
              </div>
            </div>
          </div>

          <!-- Right: Quantitative Telemetry Cards -->
          <div class="col-span-4 flex flex-col gap-2">
            <div class="p-2.5 rounded-lg bg-[#071411]/90 border border-emerald-500/25">
              <div class="text-[10px] uppercase font-bold text-slate-400 tracking-wider mb-2">
                Stage {{ stg.id }} Performance Invariants
              </div>
              <div class="grid grid-cols-3 gap-2">
                <div v-for="(m, mIdx) in stg.metrics" :key="mIdx" class="text-center">
                  <div class="text-[9px] text-slate-400 uppercase tracking-tight">{{ m.label }}</div>
                  <div class="text-xs font-mono font-bold text-emerald-300 mt-0.5">{{ m.value }}</div>
                </div>
              </div>
            </div>

            <div class="text-[10px] text-slate-400 bg-emerald-950/20 p-2 rounded border border-emerald-500/20 leading-tight">
              ⚡ <strong class="text-slate-200">Fail-Safe Isolation:</strong> Disjoint process memory prevents corrupted company filings from aborting concurrent peer evaluations.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Summary KPI Banner Underneath -->
    <div class="glass-inset px-3 py-2 border-emerald-500/20 flex items-center justify-between text-xs">
      <div class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
        <span class="font-bold text-white tracking-wide">Core Architectural Invariants:</span>
        <span class="text-slate-300 text-[11px]">Decoupled Fail-Safe Execution</span>
        <span class="text-slate-500">•</span>
        <span class="text-slate-300 text-[11px]">Sub-Two-Second Screening SLA</span>
      </div>

      <div class="flex items-center gap-4 text-[11px] font-mono">
        <span class="text-slate-300">
          Total SLA: <strong class="text-emerald-300">1.74s</strong> &lt;&lt; 18h Manual
        </span>
        <span class="text-slate-300">
          Coverage: <strong class="text-emerald-300">150+ Equities</strong>
        </span>
        <span class="text-slate-300">
          Singularity Crashes: <strong class="text-emerald-300">0.0%</strong>
        </span>
      </div>
    </div>
  </div>
</template>
