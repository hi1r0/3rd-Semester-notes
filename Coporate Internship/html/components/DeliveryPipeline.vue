<script setup lang="ts">
import { ref, computed, onUnmounted } from 'vue'

// Entity Selection State
type EntityKey = 'tcs' | 'tatamotors' | 'distressed'
const activeEntityKey = ref<EntityKey>('tcs')

// Output Mode: Memo vs openpyxl Excel vs Split
type OutputMode = 'split' | 'memo' | 'excel'
const activeOutputMode = ref<OutputMode>('split')

// Excel Active Tab (1 to 6)
const activeExcelTab = ref<number>(1)

// Pipeline Simulation State
type PipelineState = 'idle' | 'routing' | 'injecting' | 'generating' | 'completed'
const pipelineState = ref<PipelineState>('idle')
const simulationProgress = ref<number>(0)
const activeKeyIndex = ref<number>(0)
const failoverTriggered = ref<boolean>(false)
const generationToast = ref<string | null>(null)

let simTimer: ReturnType<typeof setTimeout> | null = null
let intervalTimer: ReturnType<typeof setInterval> | null = null

onUnmounted(() => {
  if (simTimer) clearTimeout(simTimer)
  if (intervalTimer) clearInterval(intervalTimer)
})

// Dynamic API Key Pool (Stage 1)
interface ApiKeyInfo {
  id: string
  name: string
  label: string
  status: 'ACTIVE' | 'STANDBY' | 'COOLDOWN' | 'RATE_LIMITED'
  requestsServed: number
  rpm: number
  rpmMax: number
  tpmK: number
  tpmMaxK: number
  avgLatencyMs: number
}

const keyPool = ref<ApiKeyInfo[]>([
  { id: 'key_1', name: 'KEY_ALPHA', label: 'Primary LLM Cluster', status: 'ACTIVE', requestsServed: 412, rpm: 74, rpmMax: 100, tpmK: 38, tpmMaxK: 100, avgLatencyMs: 285 },
  { id: 'key_2', name: 'KEY_BETA', label: 'Failover Instance A', status: 'STANDBY', requestsServed: 388, rpm: 56, rpmMax: 100, tpmK: 29, tpmMaxK: 100, avgLatencyMs: 310 },
  { id: 'key_3', name: 'KEY_GAMMA', label: 'Failover Instance B', status: 'STANDBY', requestsServed: 435, rpm: 81, rpmMax: 100, tpmK: 44, tpmMaxK: 100, avgLatencyMs: 295 },
  { id: 'key_4', name: 'KEY_DELTA', label: 'Burst Reserve', status: 'COOLDOWN', requestsServed: 194, rpm: 98, rpmMax: 100, tpmK: 92, tpmMaxK: 100, avgLatencyMs: 840 },
])

// Entity Data Profiles
interface EntityData {
  ticker: string
  name: string
  sector: string
  compositeScore: number
  tier: string
  tierColor: string
  vector: {
    profitability: number
    solvency: number
    efficiency: number
    liquidity: number
    growth: number
  }
  factorDeltas: { metric: string; delta: string; detail: string; isPositive: boolean }[]
  anomalies: {
    gaussian: { status: string; detail: string; flagged: boolean }
    tukey: { status: string; detail: string; flagged: boolean }
    mad: { status: string; detail: string; flagged: boolean }
    isoForest: { status: string; detail: string; score: number; depth: number; flagged: boolean }
  }
  memo: {
    title: string
    headline: string
    commentary: string
    riskOverhang: string
    debtAssessment: string
    portfolioAction: string
    conviction: string
  }
}

const entityProfiles: Record<EntityKey, EntityData> = {
  tcs: {
    ticker: 'TCS',
    name: 'Tata Consultancy Services',
    sector: 'IT Services',
    compositeScore: 88.4,
    tier: 'EXCELLENT',
    tierColor: 'text-emerald-300 border-emerald-500/50 bg-emerald-500/20',
    vector: { profitability: 84.5, solvency: 98.0, efficiency: 81.5, liquidity: 91.0, growth: 87.2 },
    factorDeltas: [
      { metric: 'Operating Margin', delta: '+4.84 pts', detail: '26.8% vs 18.0% peer median', isPositive: true },
      { metric: 'Net Debt / Equity', delta: '+4.80 pts', detail: '0.00x (completely debt-free)', isPositive: true },
      { metric: 'Cash Flow Margin', delta: '+2.88 pts', detail: '22.4% vs 12.0% peer median', isPositive: true },
    ],
    anomalies: {
      gaussian: { status: 'CLEAN', detail: '|z| = 1.18 < 3.0', flagged: false },
      tukey: { status: 'CLEAN', detail: 'Within nominal IQR fences', flagged: false },
      mad: { status: 'CLEAN', detail: '|z_MAD| = 1.05 < 3.5', flagged: false },
      isoForest: { status: 'NOMINAL', detail: 's = 0.412, path depth h = 9.4', score: 0.412, depth: 9.4, flagged: false },
    },
    memo: {
      title: 'INSTITUTIONAL EQUITY AUDIT MEMO',
      headline: 'Top-Decile Capital Efficiency & Complete Balance Sheet Insulation',
      commentary: 'Tata Consultancy Services demonstrates stellar operational execution with an Operating Margin of 26.8%, contributing +4.84 pts of factor alpha against the peer baseline (18.0%). Zero debt obligations yield an elite Solvency score of 98.0, insulating the firm against monetary tightening.',
      riskOverhang: 'Negligible balance sheet overhang. Cash conversion cycle remains stable at 42 days, supported by resilient 22.4% free cash flow margin.',
      debtAssessment: 'Interest burden factor is 1.00 (debt-free). Zero solvency drag detected across 5-stage DuPont decomposition.',
      portfolioAction: 'Recommended Allocation: Overweight / Long (Quintile 5)',
      conviction: 'Strong Buy (98.4% Confidence Consensus)',
    },
  },
  tatamotors: {
    ticker: 'TATA MOTORS',
    name: 'Tata Motors Limited',
    sector: 'Automobile',
    compositeScore: 56.5,
    tier: 'MODERATE',
    tierColor: 'text-teal-300 border-teal-500/50 bg-teal-500/20',
    vector: { profitability: 56.0, solvency: 37.0, efficiency: 69.5, liquidity: 49.5, growth: 64.0 },
    factorDeltas: [
      { metric: 'Asset Turnover', delta: '+1.46 pts', detail: '1.40x vs 1.05x peer median', isPositive: true },
      { metric: 'Operating Margin', delta: '+0.60 pts', detail: '19.2% vs 18.0% peer median', isPositive: true },
      { metric: 'Net Debt / Equity', delta: '-1.30 pts', detail: '1.25x vs 0.80x peer median', isPositive: false },
    ],
    anomalies: {
      gaussian: { status: 'CLEAN', detail: '|z| = 0.82 < 3.0', flagged: false },
      tukey: { status: 'CLEAN', detail: 'Within nominal IQR fences', flagged: false },
      mad: { status: 'CLEAN', detail: '|z_MAD| = 0.94 < 3.5', flagged: false },
      isoForest: { status: 'MILD DRIFT', detail: 's = 0.582, path depth h = 5.8', score: 0.582, depth: 5.8, flagged: true },
    },
    memo: {
      title: 'INSTITUTIONAL EQUITY AUDIT MEMO',
      headline: 'Cyclical Turnaround Masked by Balance Sheet Gearing Drag',
      commentary: 'Tata Motors exhibits notable operational improvement driven by high asset velocity (1.40x vs sector median 1.05x). However, financial leverage of 1.25x Net Debt/Equity imposes a -1.30 pts drag on composite health, depressing Solvency to 37.0.',
      riskOverhang: 'Active interest service overhang. Interest coverage ratio of 3.4x is sensitive to input commodity cost spikes and rate hikes.',
      debtAssessment: '5-stage DuPont indicates Equity Multiplier of 3.2x artificially levitates headline ROE despite compressed interest retention (0.72).',
      portfolioAction: 'Recommended Allocation: Market Weight / Neutral (Quintile 3)',
      conviction: 'Hold (Balanced Operational Recovery vs Leverage)',
    },
  },
  distressed: {
    ticker: 'DISTRESSED INFRA',
    name: 'Stressed EPC Firm',
    sector: 'Infrastructure',
    compositeScore: 22.8,
    tier: 'DISTRESSED',
    tierColor: 'text-rose-400 border-rose-500/50 bg-rose-500/20',
    vector: { profitability: 22.5, solvency: 12.0, efficiency: 32.0, liquidity: 19.5, growth: 28.0 },
    factorDeltas: [
      { metric: 'Net Debt / Equity', delta: '-3.80 pts', detail: '3.80x (Severe default danger)', isPositive: false },
      { metric: 'Cash Flow Margin', delta: '-2.78 pts', detail: '-4.2% (Operating burn)', isPositive: false },
      { metric: 'Operating Margin', delta: '-2.75 pts', detail: '4.5% vs 18.0% peer median', isPositive: false },
    ],
    anomalies: {
      gaussian: { status: 'MASKED', detail: 'Displaced mean hides tail collapse', flagged: false },
      tukey: { status: 'FLAGGED', detail: 'Exceeds lower IQR cutoffs', flagged: true },
      mad: { status: 'FLAGGED', detail: '|z_MAD| = 4.12 > 3.5', flagged: true },
      isoForest: { status: 'CRITICAL', detail: 's = 0.748, path depth h = 2.1 cuts', score: 0.748, depth: 2.1, flagged: true },
    },
    memo: {
      title: 'INSTITUTIONAL EQUITY AUDIT MEMO',
      headline: 'Severe Credit Contraction & Acute Margin-Cashflow Decoupling',
      commentary: 'Stressed EPC Firm displays terminal balance sheet decay. Net Debt/Equity of 3.80x has crushed solvency to 12.0. While headline earnings show marginal accounting profits, operating cash flow is deeply negative (-4.2%), signaling aggressive unbilled revenue accruals.',
      riskOverhang: 'Severe insolvency overhang. Operating cash flows fail to service short-term debt repayments; debt rollover covenants at imminent risk of breach.',
      debtAssessment: 'Interest coverage ratio collapsed to 0.65x. Equity Multiplier exceeds 6.4x, triggering critical warning guards.',
      portfolioAction: 'Recommended Allocation: Strong Underweight / Short (Quintile 1)',
      conviction: 'High Conviction Short / Liquidation Watch',
    },
  },
}

const currentEntity = computed(() => entityProfiles[activeEntityKey.value])

// Trigger Simulation Cycle
function runSimulation() {
  if (pipelineState.value !== 'idle' && pipelineState.value !== 'completed') return

  pipelineState.value = 'routing'
  simulationProgress.value = 10
  generationToast.value = 'Stage 1: Round-Robin key pool evaluating health & quota...'

  // Advance key index round-robin
  activeKeyIndex.value = (activeKeyIndex.value + 1) % 3 // Rotate across healthy keys 0, 1, 2
  keyPool.value.forEach((k, idx) => {
    if (idx === activeKeyIndex.value) {
      k.status = 'ACTIVE'
      k.requestsServed += 1
      k.rpm = Math.min(k.rpmMax, k.rpm + 4)
    } else if (k.status !== 'COOLDOWN') {
      k.status = 'STANDBY'
    }
  })

  simTimer = setTimeout(() => {
    pipelineState.value = 'injecting'
    simulationProgress.value = 45
    generationToast.value = `Stage 2: Injecting 5-pillar vector [${currentEntity.value.vector.profitability}, ${currentEntity.value.vector.solvency}, ...] into prompt...`

    simTimer = setTimeout(() => {
      pipelineState.value = 'generating'
      simulationProgress.value = 80
      generationToast.value = 'Stage 3: LLM synthesis streaming memo & openpyxl workbook populating 6 audit tabs...'

      simTimer = setTimeout(() => {
        pipelineState.value = 'completed'
        simulationProgress.value = 100
        generationToast.value = `✓ Delivery Complete: Generated Executive Memo & 6-Tab openpyxl Excel Workbook for ${currentEntity.value.ticker}`

        simTimer = setTimeout(() => {
          generationToast.value = null
        }, 3500)
      }, 700)
    }, 650)
  }, 600)
}

// Simulate Automated 429 Failover Switch
function triggerFailoverSimulation() {
  failoverTriggered.value = true
  const prevActive = activeKeyIndex.value
  keyPool.value[prevActive].status = 'RATE_LIMITED'
  keyPool.value[prevActive].rpm = 100
  generationToast.value = `⚠️ 429 RateLimit on ${keyPool.value[prevActive].name}! Automatic failover initiating...`

  setTimeout(() => {
    activeKeyIndex.value = (prevActive + 1) % 3
    keyPool.value[activeKeyIndex.value].status = 'ACTIVE'
    keyPool.value[activeKeyIndex.value].requestsServed += 1
    generationToast.value = `✓ Failover Succeeded: Traffic routed to ${keyPool.value[activeKeyIndex.value].name} in 18ms SLA.`
    failoverTriggered.value = false
    setTimeout(() => {
      generationToast.value = null
    }, 3000)
  }, 900)
}
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Action & Pipeline Header Bar -->
    <div class="flex items-center justify-between gap-2 bg-[#071411]/90 px-3 py-1.5 rounded-xl border border-emerald-500/20 mb-1.5">
      <!-- Entity Selector -->
      <div class="flex items-center gap-1.5">
        <span class="text-[9.5px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Entity Profile:
        </span>
        <button
          @click="activeEntityKey = 'tcs'"
          class="px-2 py-0.5 rounded text-[9.5px] font-semibold font-mono transition-all border flex items-center gap-1"
          :class="activeEntityKey === 'tcs'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 shadow-[0_0_10px_rgba(52,211,153,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          <span>TCS (Score: 88.4)</span>
        </button>

        <button
          @click="activeEntityKey = 'tatamotors'"
          class="px-2 py-0.5 rounded text-[9.5px] font-semibold font-mono transition-all border flex items-center gap-1"
          :class="activeEntityKey === 'tatamotors'
            ? 'bg-teal-500/25 text-teal-300 border-teal-500/60 shadow-[0_0_10px_rgba(20,184,166,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-teal-400"></span>
          <span>Tata Motors (Score: 56.5)</span>
        </button>

        <button
          @click="activeEntityKey = 'distressed'"
          class="px-2 py-0.5 rounded text-[9.5px] font-semibold font-mono transition-all border flex items-center gap-1"
          :class="activeEntityKey === 'distressed'
            ? 'bg-rose-500/25 text-rose-300 border-rose-500/60 shadow-[0_0_10px_rgba(244,63,94,0.25)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span>
          <span>Distressed Infra (Score: 22.8)</span>
        </button>
      </div>

      <!-- Center Live Toast Notification -->
      <div v-if="generationToast" class="flex-1 max-w-[340px] text-[8.5px] font-mono text-center truncate px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-400/40 text-emerald-200 animate-pulse">
        {{ generationToast }}
      </div>
      <div v-else class="text-[8.5px] font-mono text-slate-400">
        Automated Synthesis & Multi-Format Delivery
      </div>

      <!-- Run Simulation Button -->
      <div class="flex items-center gap-2">
        <button
          @click="triggerFailoverSimulation"
          :disabled="pipelineState !== 'idle' && pipelineState !== 'completed'"
          class="px-2 py-0.8 rounded text-[8.5px] font-mono border border-amber-500/30 text-amber-300 bg-amber-500/10 hover:bg-amber-500/20 transition disabled:opacity-50"
          title="Simulate 429 quota exhaustion and watch automated failover"
        >
          ⚡ Test 429 Failover
        </button>

        <button
          @click="runSimulation"
          :disabled="pipelineState !== 'idle' && pipelineState !== 'completed'"
          class="px-2.5 py-0.8 rounded text-[9.5px] font-bold font-mono border flex items-center gap-1.5 transition-all shadow-[0_0_12px_rgba(52,211,153,0.25)]"
          :class="pipelineState === 'idle' || pipelineState === 'completed'
            ? 'bg-emerald-500/25 border-emerald-400 text-emerald-300 hover:bg-emerald-500/40 cursor-pointer'
            : 'bg-emerald-950/50 border-emerald-600/30 text-slate-400 cursor-not-allowed'"
        >
          <span class="w-2 h-2 rounded-full" :class="pipelineState === 'idle' || pipelineState === 'completed' ? 'bg-emerald-400' : 'bg-amber-400 animate-ping'"></span>
          <span>{{ pipelineState === 'idle' || pipelineState === 'completed' ? 'Run Synthesis Cycle' : 'Synthesizing...' }}</span>
        </button>
      </div>
    </div>

    <!-- Stepper Progress Tracker -->
    <div class="grid grid-cols-3 gap-2 mb-1.5 font-mono text-[8.5px]">
      <div
        class="px-2 py-1 rounded-lg border flex items-center justify-between transition-all"
        :class="pipelineState === 'routing'
          ? 'bg-emerald-500/20 border-emerald-400 text-emerald-200 shadow-[0_0_10px_rgba(52,211,153,0.3)]'
          : 'bg-[#0d211b]/60 border-emerald-500/15 text-slate-400'"
      >
        <span class="flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full" :class="pipelineState === 'routing' ? 'bg-emerald-400 animate-ping' : 'bg-slate-500'"></span>
          <strong>Stage 1:</strong> Round-Robin API Pool
        </span>
        <span class="text-[7.5px] px-1 py-0.2 rounded bg-[#071411]">Active: {{ keyPool[activeKeyIndex].name }}</span>
      </div>

      <div
        class="px-2 py-1 rounded-lg border flex items-center justify-between transition-all"
        :class="pipelineState === 'injecting'
          ? 'bg-teal-500/20 border-teal-400 text-teal-200 shadow-[0_0_10px_rgba(20,184,166,0.3)]'
          : 'bg-[#0d211b]/60 border-emerald-500/15 text-slate-400'"
      >
        <span class="flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full" :class="pipelineState === 'injecting' ? 'bg-teal-400 animate-ping' : 'bg-slate-500'"></span>
          <strong>Stage 2:</strong> Deterministic Context Injection
        </span>
        <span class="text-[7.5px] px-1 py-0.2 rounded bg-[#071411]">5-Pillar Vector Bound</span>
      </div>

      <div
        class="px-2 py-1 rounded-lg border flex items-center justify-between transition-all"
        :class="pipelineState === 'generating' || pipelineState === 'completed'
          ? 'bg-cyan-500/20 border-cyan-400 text-cyan-200 shadow-[0_0_10px_rgba(6,182,212,0.3)]'
          : 'bg-[#0d211b]/60 border-emerald-500/15 text-slate-400'"
      >
        <span class="flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full" :class="pipelineState === 'generating' ? 'bg-cyan-400 animate-ping' : pipelineState === 'completed' ? 'bg-emerald-400' : 'bg-slate-500'"></span>
          <strong>Stage 3:</strong> Dual Deliverables
        </span>
        <span class="text-[7.5px] px-1 py-0.2 rounded bg-[#071411]">Memo + 6-Tab openpyxl</span>
      </div>
    </div>

    <!-- Main Body: Two Columns (Left: Stages 1 & 2; Right: Stage 3 Dual Deliverables) -->
    <div class="grid grid-cols-12 gap-2 flex-1 min-h-0 mb-1.5">
      <!-- LEFT COLUMN: Stages 1 & 2 (Width: 5 Cols) -->
      <div class="col-span-5 flex flex-col gap-2">
        <!-- CARD 1: Stage 1 API Key Pool & Quota Protection -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-1 mb-1 border-b border-emerald-500/15">
              <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-sm bg-emerald-400"></span>
                Stage 1: Dynamic Round-Robin Key Pool
              </span>
              <span class="text-[8px] font-mono px-1.5 py-0.2 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                Quota Failover Router
              </span>
            </div>

            <!-- Key Pool Grid -->
            <div class="grid grid-cols-2 gap-1.5 mb-1.5">
              <div
                v-for="(key, idx) in keyPool"
                :key="key.id"
                class="p-1.5 rounded-lg border font-mono transition-all text-[8px]"
                :class="idx === activeKeyIndex
                  ? 'bg-emerald-500/20 border-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
                  : key.status === 'COOLDOWN' || key.status === 'RATE_LIMITED'
                    ? 'bg-rose-950/25 border-rose-500/30 opacity-75'
                    : 'bg-[#071411]/80 border-slate-700/60'"
              >
                <div class="flex items-center justify-between mb-0.5">
                  <span class="font-bold" :class="idx === activeKeyIndex ? 'text-emerald-300' : 'text-slate-300'">
                    {{ key.name }}
                  </span>
                  <span
                    class="text-[6.5px] px-1 py-0.2 rounded uppercase font-bold"
                    :class="idx === activeKeyIndex
                      ? 'bg-emerald-400/30 text-emerald-200'
                      : key.status === 'RATE_LIMITED'
                        ? 'bg-rose-500/30 text-rose-300 animate-pulse'
                        : key.status === 'COOLDOWN'
                          ? 'bg-amber-500/30 text-amber-300'
                          : 'bg-slate-800 text-slate-400'"
                  >
                    {{ idx === activeKeyIndex ? 'ACTIVE' : key.status }}
                  </span>
                </div>
                <div class="text-[7px] text-slate-400 truncate mb-1">{{ key.label }}</div>

                <!-- RPM & Latency Mini-Bars -->
                <div class="space-y-0.5">
                  <div class="flex justify-between text-[6.5px] text-slate-400">
                    <span>RPM Quota:</span>
                    <span :class="key.rpm > 85 ? 'text-amber-300 font-bold' : 'text-slate-300'">{{ key.rpm }} / {{ key.rpmMax }}</span>
                  </div>
                  <div class="w-full bg-slate-800 h-1 rounded overflow-hidden">
                    <div
                      class="h-full transition-all duration-300"
                      :class="key.rpm > 85 ? 'bg-amber-400' : 'bg-emerald-400'"
                      :style="{ width: `${(key.rpm / key.rpmMax) * 100}%` }"
                    ></div>
                  </div>
                  <div class="flex justify-between text-[6.5px] text-slate-400 pt-0.5">
                    <span>Latency: {{ key.avgLatencyMs }}ms</span>
                    <span>Served: {{ key.requestsServed }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Stage 1 Architectural Note -->
            <div class="text-[7.5px] text-slate-400 bg-[#071411]/90 p-1 rounded border border-emerald-500/15 leading-tight font-mono">
              <strong class="text-emerald-300">Resilient Router Architecture:</strong> Dynamic round-robin rotation distributes generation load across N authorized credentials. On HTTP 429 quota exhaustion, traffic automatically switches in &lt;20ms to the next standby instance without dropping active pipeline transactions.
            </div>
          </div>
        </div>

        <!-- CARD 2: Stage 2 Deterministic Context Injection -->
        <div class="glass-card p-2 flex flex-col justify-between flex-1">
          <div>
            <div class="flex items-center justify-between pb-1 mb-1 border-b border-teal-500/15">
              <span class="text-[10px] font-bold text-teal-300 uppercase tracking-wider font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-sm bg-teal-400"></span>
                Stage 2: Deterministic Context Injection
              </span>
              <span class="text-[8px] font-mono px-1.5 py-0.2 rounded bg-teal-500/15 text-teal-300 border border-teal-500/30">
                Anti-Hallucination Schema
              </span>
            </div>

            <!-- Structured JSON Prompt Injection Preview -->
            <div class="bg-[#071411] p-1.5 rounded-lg border border-teal-500/25 font-mono text-[7.5px] text-slate-300 leading-tight space-y-1 mb-1.5">
              <div class="text-teal-400/90 font-bold text-[8px] flex items-center justify-between border-b border-slate-800 pb-0.5">
                <span>SYSTEM_PROMPT_BINDINGS:</span>
                <span class="text-slate-500 text-[6.5px]">STRICT_GROUNDING = TRUE</span>
              </div>
              <div class="grid grid-cols-2 gap-1 text-[7px]">
                <div>
                  <span class="text-slate-500">TICKER:</span>
                  <span class="text-emerald-300 font-bold ml-1">{{ currentEntity.ticker }}</span>
                </div>
                <div>
                  <span class="text-slate-500">HEALTH_TIER:</span>
                  <span class="font-bold ml-1" :class="currentEntity.compositeScore >= 70 ? 'text-emerald-300' : currentEntity.compositeScore >= 45 ? 'text-amber-300' : 'text-rose-400'">
                    {{ currentEntity.tier }} ({{ currentEntity.compositeScore }})
                  </span>
                </div>
              </div>

              <!-- 5-Pillar Vector Readout -->
              <div class="bg-slate-900/80 p-1 rounded border border-slate-800 text-[6.8px]">
                <div class="text-slate-400 mb-0.5 font-bold">NORMALIZED 5-PILLAR VECTOR (0–100):</div>
                <div class="flex justify-between text-slate-200">
                  <span>Prof: <strong class="text-emerald-300">{{ currentEntity.vector.profitability }}</strong></span>
                  <span>Solv: <strong class="text-teal-300">{{ currentEntity.vector.solvency }}</strong></span>
                  <span>Eff: <strong class="text-sky-300">{{ currentEntity.vector.efficiency }}</strong></span>
                  <span>Liq: <strong class="text-cyan-300">{{ currentEntity.vector.liquidity }}</strong></span>
                  <span>Gro: <strong class="text-amber-300">{{ currentEntity.vector.growth }}</strong></span>
                </div>
              </div>

              <!-- Factor Deltas & Anomaly Consensus Flags -->
              <div class="grid grid-cols-2 gap-1 text-[6.8px]">
                <div class="bg-slate-900/80 p-1 rounded border border-slate-800">
                  <div class="text-slate-400 font-bold mb-0.5">TOP FACTOR DELTAS:</div>
                  <div v-for="delta in currentEntity.factorDeltas.slice(0, 2)" :key="delta.metric" class="truncate">
                    <span :class="delta.isPositive ? 'text-emerald-400' : 'text-rose-400'">{{ delta.delta }}</span>
                    <span class="text-slate-400 ml-1">{{ delta.metric }}</span>
                  </div>
                </div>

                <div class="bg-slate-900/80 p-1 rounded border border-slate-800">
                  <div class="text-slate-400 font-bold mb-0.5">ANOMALY CONSENSUS:</div>
                  <div class="truncate">
                    <span class="text-slate-400">Tukey/MAD:</span>
                    <span class="ml-1" :class="currentEntity.anomalies.tukey.flagged ? 'text-rose-400 font-bold' : 'text-emerald-400'">{{ currentEntity.anomalies.tukey.status }}</span>
                  </div>
                  <div class="truncate">
                    <span class="text-slate-400">IsoForest:</span>
                    <span class="ml-1" :class="currentEntity.anomalies.isoForest.flagged ? 'text-rose-400 font-bold' : 'text-emerald-400'">h={{ currentEntity.anomalies.isoForest.depth }}</span>
                  </div>
                </div>
              </div>

              <div class="text-slate-400 text-[6.5px] italic">
                Directive: "Synthesize quantitative findings using only provided vector. Never hallucinate unverified balance sheet items."
              </div>
            </div>

            <div class="text-[7.5px] text-slate-400 font-mono">
              <span class="text-teal-300 font-bold">Zero-Hallucination Bound:</span> Context injection guarantees that narrative memo statements map 1-to-1 to mathematical ratio engine derivations.
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Stage 3 Dual Deliverables (Width: 7 Cols) -->
      <div class="col-span-7 flex flex-col gap-2">
        <div class="glass-card p-2 flex flex-col justify-between flex-1">
          <!-- Stage 3 Header & Deliverable Switcher -->
          <div class="flex items-center justify-between pb-1 mb-1 border-b border-cyan-500/15">
            <div class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-sm bg-cyan-400"></span>
              <span class="text-[10px] font-bold text-cyan-300 uppercase tracking-wider font-mono">
                Stage 3: Dual Output Deliverables
              </span>
            </div>

            <!-- View Mode Switcher -->
            <div class="flex items-center gap-1 bg-[#071411] p-0.5 rounded border border-slate-800 font-mono text-[8px]">
              <button
                @click="activeOutputMode = 'split'"
                class="px-1.5 py-0.5 rounded transition"
                :class="activeOutputMode === 'split' ? 'bg-cyan-500/30 text-cyan-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
              >
                Split View
              </button>
              <button
                @click="activeOutputMode = 'memo'"
                class="px-1.5 py-0.5 rounded transition"
                :class="activeOutputMode === 'memo' ? 'bg-cyan-500/30 text-cyan-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
              >
                📄 AI Memo
              </button>
              <button
                @click="activeOutputMode = 'excel'"
                class="px-1.5 py-0.5 rounded transition"
                :class="activeOutputMode === 'excel' ? 'bg-emerald-500/30 text-emerald-200 font-bold' : 'text-slate-400 hover:text-slate-200'"
              >
                📊 openpyxl Excel (6 Tabs)
              </button>
            </div>
          </div>

          <!-- DELIVERABLE CONTENT CONTAINER -->
          <div class="flex-1 flex flex-col gap-2 min-h-0">
            <!-- VIEW A: Executive AI Analyst Memo -->
            <div
              v-show="activeOutputMode === 'split' || activeOutputMode === 'memo'"
              class="bg-[#071411]/95 p-2 rounded-lg border border-cyan-500/25 flex flex-col justify-between overflow-hidden"
              :class="activeOutputMode === 'split' ? 'h-[180px]' : 'flex-1'"
            >
              <div>
                <!-- Memo Header -->
                <div class="flex items-center justify-between pb-1 mb-1 border-b border-slate-800">
                  <div class="flex items-center gap-1.5">
                    <span class="text-[9px] font-bold text-white font-mono uppercase tracking-wide">
                      {{ currentEntity.memo.title }}
                    </span>
                    <span class="text-[7.5px] px-1 py-0.2 rounded font-mono border" :class="currentEntity.tierColor">
                      {{ currentEntity.tier }} · Score {{ currentEntity.compositeScore }}
                    </span>
                  </div>
                  <div class="text-[7.5px] font-mono text-slate-400">
                    Engine: FinMetrics-LLM-v2.4
                  </div>
                </div>

                <!-- Headline -->
                <div class="text-[8.5px] font-bold text-cyan-300 font-mono mb-1 leading-snug">
                  {{ currentEntity.memo.headline }}
                </div>

                <!-- Executive Commentary Paragraph -->
                <div class="text-[7.8px] text-slate-300 leading-relaxed mb-1 font-sans">
                  {{ currentEntity.memo.commentary }}
                </div>

                <!-- Structured Bullet Analysis -->
                <div class="grid grid-cols-2 gap-1 text-[7.2px] font-mono mb-1">
                  <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
                    <span class="text-amber-300 font-bold">Risk Overhangs: </span>
                    <span class="text-slate-300">{{ currentEntity.memo.riskOverhang }}</span>
                  </div>
                  <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
                    <span class="text-cyan-300 font-bold">Debt Serviceability: </span>
                    <span class="text-slate-300">{{ currentEntity.memo.debtAssessment }}</span>
                  </div>
                </div>
              </div>

              <!-- Recommendation Footer -->
              <div class="flex items-center justify-between pt-1 border-t border-slate-800 text-[7.5px] font-mono">
                <div class="flex items-center gap-1 text-slate-300">
                  <span class="text-emerald-400 font-bold">Action:</span>
                  <span>{{ currentEntity.memo.portfolioAction }}</span>
                </div>
                <div class="text-slate-400">
                  {{ currentEntity.memo.conviction }}
                </div>
              </div>
            </div>

            <!-- VIEW B: Interactive 6-Tab openpyxl Excel Audit Workbook -->
            <div
              v-show="activeOutputMode === 'split' || activeOutputMode === 'excel'"
              class="bg-[#0b1f19] rounded-lg border border-emerald-500/30 flex flex-col justify-between overflow-hidden shadow-lg"
              :class="activeOutputMode === 'split' ? 'h-[185px]' : 'flex-1'"
            >
              <!-- Excel Titlebar & Formula Bar -->
              <div class="bg-[#064e3b]/80 px-2 py-1 border-b border-emerald-600/40 flex items-center justify-between text-[8px] font-mono">
                <div class="flex items-center gap-1.5 text-emerald-100">
                  <span class="w-2.5 h-2.5 bg-emerald-500 text-black font-black text-[6.5px] flex items-center justify-center rounded-sm">X</span>
                  <span class="font-bold">FinMetrics_Institutional_Audit_{{ currentEntity.ticker }}.xlsx</span>
                  <span class="text-[6.5px] text-emerald-300 bg-emerald-900/60 px-1 rounded">[openpyxl Verified]</span>
                </div>
                <div class="text-[7px] text-emerald-300/80">
                  Workbook: 6 Worksheets · Read-Only
                </div>
              </div>

              <!-- Formula Bar Readout -->
              <div class="bg-[#071411] px-2 py-0.5 border-b border-slate-800 flex items-center gap-2 text-[7.5px] font-mono">
                <span class="text-slate-500 font-bold">fx</span>
                <span class="text-emerald-400 truncate">
                  <span v-if="activeExcelTab === 1">=FINMETRICS.EXECUTIVE_SUMMARY("{{ currentEntity.ticker }}", "Q3-2026")</span>
                  <span v-else-if="activeExcelTab === 2">=PILLAR_SCORECARD.WEIGHTED_SUM(W_k, S_xi, "5-PILLARS")</span>
                  <span v-else-if="activeExcelTab === 3">=DUPONT.5STAGE(TAX_BURDEN, INT_BURDEN, OP_MARGIN, ASSET_TURNOVER, LEV_MULT)</span>
                  <span v-else-if="activeExcelTab === 4">=ANOMALY_CONSENSUS.EVALUATE(GAUSSIAN, TUKEY, MAD, ISOFOREST_R16)</span>
                  <span v-else-if="activeExcelTab === 5">=SIGMOID.PERCENTILE_MAP(RAW_RATIO, MEDIAN_NSE, IQR_NSE, KAPPA=1.386)</span>
                  <span v-else>=PARQUET.RAW_INGEST("NSE_{{ currentEntity.ticker }}_FUNDAMENTALS")</span>
                </span>
              </div>

              <!-- Spreadsheet Grid View (Changes with activeExcelTab) -->
              <div class="p-1.5 flex-1 overflow-auto font-mono text-[7.5px]">
                <!-- TAB 1: Executive Summary -->
                <div v-if="activeExcelTab === 1" class="space-y-1">
                  <table class="w-full text-left border-collapse">
                    <thead>
                      <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                        <th class="pb-0.5">Cell</th>
                        <th class="pb-0.5">Parameter Field</th>
                        <th class="pb-0.5">Calculated Value</th>
                        <th class="pb-0.5">Benchmark / Status</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-200">
                      <tr>
                        <td class="text-slate-500">B2</td>
                        <td>Company Name / Ticker</td>
                        <td class="font-bold text-white">{{ currentEntity.name }} ({{ currentEntity.ticker }})</td>
                        <td class="text-emerald-400">Sector: {{ currentEntity.sector }}</td>
                      </tr>
                      <tr>
                        <td class="text-slate-500">B3</td>
                        <td>FinMetrics Composite Score</td>
                        <td class="font-bold text-emerald-300">{{ currentEntity.compositeScore }} / 100</td>
                        <td class="font-bold" :class="currentEntity.compositeScore >= 70 ? 'text-emerald-400' : currentEntity.compositeScore >= 45 ? 'text-amber-400' : 'text-rose-400'">{{ currentEntity.tier }}</td>
                      </tr>
                      <tr>
                        <td class="text-slate-500">B4</td>
                        <td>Rating Agency Equivalent</td>
                        <td>{{ currentEntity.compositeScore >= 80 ? 'CRISIL AAA / ICRA AAA' : currentEntity.compositeScore >= 50 ? 'CRISIL BBB+ / ICRA BBB' : 'CRISIL D / Default Risk' }}</td>
                        <td class="text-slate-400">2-Quarter Lead Warning</td>
                      </tr>
                      <tr>
                        <td class="text-slate-500">B5</td>
                        <td>Multivariate Health Consensus</td>
                        <td :class="currentEntity.anomalies.isoForest.flagged ? 'text-rose-400 font-bold' : 'text-emerald-400'">{{ currentEntity.anomalies.isoForest.status }}</td>
                        <td class="text-slate-400">IsoForest Path Depth: {{ currentEntity.anomalies.isoForest.depth }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- TAB 2: 5-Pillar Scorecard -->
                <div v-else-if="activeExcelTab === 2">
                  <table class="w-full text-left border-collapse">
                    <thead>
                      <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                        <th class="pb-0.5">Pillar Name</th>
                        <th class="pb-0.5 text-center">Macro Weight (W_k)</th>
                        <th class="pb-0.5 text-center">Normalized Score</th>
                        <th class="pb-0.5 text-right">Weighted Contribution</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-200">
                      <tr>
                        <td>1. Profitability</td>
                        <td class="text-center text-slate-400">25.0%</td>
                        <td class="text-center font-bold text-emerald-300">{{ currentEntity.vector.profitability }}</td>
                        <td class="text-right font-mono">{{ (currentEntity.vector.profitability * 0.25).toFixed(2) }} pts</td>
                      </tr>
                      <tr>
                        <td>2. Solvency &amp; Leverage</td>
                        <td class="text-center text-slate-400">25.0%</td>
                        <td class="text-center font-bold" :class="currentEntity.vector.solvency >= 50 ? 'text-teal-300' : 'text-rose-400'">{{ currentEntity.vector.solvency }}</td>
                        <td class="text-right font-mono">{{ (currentEntity.vector.solvency * 0.25).toFixed(2) }} pts</td>
                      </tr>
                      <tr>
                        <td>3. Operating Efficiency</td>
                        <td class="text-center text-slate-400">15.0%</td>
                        <td class="text-center font-bold text-sky-300">{{ currentEntity.vector.efficiency }}</td>
                        <td class="text-right font-mono">{{ (currentEntity.vector.efficiency * 0.15).toFixed(2) }} pts</td>
                      </tr>
                      <tr>
                        <td>4. Liquidity &amp; Cash Flow</td>
                        <td class="text-center text-slate-400">20.0%</td>
                        <td class="text-center font-bold text-cyan-300">{{ currentEntity.vector.liquidity }}</td>
                        <td class="text-right font-mono">{{ (currentEntity.vector.liquidity * 0.20).toFixed(2) }} pts</td>
                      </tr>
                      <tr>
                        <td>5. Structural Growth</td>
                        <td class="text-center text-slate-400">15.0%</td>
                        <td class="text-center font-bold text-amber-300">{{ currentEntity.vector.growth }}</td>
                        <td class="text-right font-mono">{{ (currentEntity.vector.growth * 0.15).toFixed(2) }} pts</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- TAB 3: DuPont Decomposition -->
                <div v-else-if="activeExcelTab === 3">
                  <table class="w-full text-left border-collapse">
                    <thead>
                      <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                        <th class="pb-0.5">DuPont Driver</th>
                        <th class="pb-0.5">Formula Line</th>
                        <th class="pb-0.5 text-center">Entity Factor</th>
                        <th class="pb-0.5 text-right">Diagnostic Signal</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-200">
                      <tr>
                        <td>Tax Retention</td>
                        <td class="text-slate-400">Net Income / EBT</td>
                        <td class="text-center font-mono font-bold">0.74x</td>
                        <td class="text-right text-emerald-400">Normal 26% Corp Rate</td>
                      </tr>
                      <tr>
                        <td>Interest Burden</td>
                        <td class="text-slate-400">EBT / EBIT</td>
                        <td class="text-center font-mono font-bold" :class="activeEntityKey === 'distressed' ? 'text-rose-400' : 'text-slate-200'">{{ activeEntityKey === 'tcs' ? '1.00x' : activeEntityKey === 'tatamotors' ? '0.72x' : '0.41x' }}</td>
                        <td class="text-right" :class="activeEntityKey === 'distressed' ? 'text-rose-400 font-bold' : 'text-slate-400'">{{ activeEntityKey === 'tcs' ? 'Debt Free' : activeEntityKey === 'tatamotors' ? 'Moderate Drag' : 'Critical Debt Drag' }}</td>
                      </tr>
                      <tr>
                        <td>Operating Margin</td>
                        <td class="text-slate-400">EBIT / Sales</td>
                        <td class="text-center font-mono font-bold text-emerald-300">{{ activeEntityKey === 'tcs' ? '26.8%' : activeEntityKey === 'tatamotors' ? '19.2%' : '4.5%' }}</td>
                        <td class="text-right text-slate-300">{{ activeEntityKey === 'distressed' ? 'Margin Collapse' : 'Healthy Core' }}</td>
                      </tr>
                      <tr>
                        <td>Asset Turnover</td>
                        <td class="text-slate-400">Sales / Assets</td>
                        <td class="text-center font-mono font-bold">{{ activeEntityKey === 'tcs' ? '1.45x' : activeEntityKey === 'tatamotors' ? '1.40x' : '0.55x' }}</td>
                        <td class="text-right text-teal-300">Capital Velocity</td>
                      </tr>
                      <tr>
                        <td>Equity Multiplier</td>
                        <td class="text-slate-400">Assets / Equity</td>
                        <td class="text-center font-mono font-bold" :class="activeEntityKey === 'distressed' ? 'text-rose-400 font-bold' : 'text-slate-200'">{{ activeEntityKey === 'tcs' ? '1.25x' : activeEntityKey === 'tatamotors' ? '3.20x' : '6.40x' }}</td>
                        <td class="text-right" :class="activeEntityKey === 'distressed' ? 'text-rose-400' : 'text-slate-400'">{{ activeEntityKey === 'distressed' ? 'Extreme Gearing' : 'Controlled Leverage' }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- TAB 4: Anomaly Consensus -->
                <div v-else-if="activeExcelTab === 4">
                  <table class="w-full text-left border-collapse">
                    <thead>
                      <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                        <th class="pb-0.5">Detection Engine</th>
                        <th class="pb-0.5">Threshold / Boundary</th>
                        <th class="pb-0.5 text-center">Score / Metric</th>
                        <th class="pb-0.5 text-right">Consensus Decision</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-200">
                      <tr>
                        <td>Gaussian Parametric (Z)</td>
                        <td class="text-slate-400">|z| &gt; 3.0 (Breakdown 0%)</td>
                        <td class="text-center font-mono">z = {{ activeEntityKey === 'distressed' ? '+1.94 (Masked)' : '1.18' }}</td>
                        <td class="text-right" :class="activeEntityKey === 'distressed' ? 'text-amber-400' : 'text-emerald-400'">{{ currentEntity.anomalies.gaussian.status }}</td>
                      </tr>
                      <tr>
                        <td>Tukey Non-Parametric (IQR)</td>
                        <td class="text-slate-400">[Q₁ - 1.5·IQR, Q₃ + 1.5·IQR]</td>
                        <td class="text-center font-mono">{{ activeEntityKey === 'distressed' ? 'Outer Fence Cutoff' : 'Within Bounds' }}</td>
                        <td class="text-right font-bold" :class="currentEntity.anomalies.tukey.flagged ? 'text-rose-400' : 'text-emerald-400'">{{ currentEntity.anomalies.tukey.status }}</td>
                      </tr>
                      <tr>
                        <td>Modified MAD Dispersion</td>
                        <td class="text-slate-400">|z_MAD| &gt; 3.5 (Breakdown 50%)</td>
                        <td class="text-center font-mono">{{ currentEntity.anomalies.mad.detail }}</td>
                        <td class="text-right font-bold" :class="currentEntity.anomalies.mad.flagged ? 'text-rose-400' : 'text-emerald-400'">{{ currentEntity.anomalies.mad.status }}</td>
                      </tr>
                      <tr>
                        <td>Isolation Forest (ℝ¹⁶)</td>
                        <td class="text-slate-400">E(h(x)) &lt; 4 cuts (Multivariate)</td>
                        <td class="text-center font-mono">h = {{ currentEntity.anomalies.isoForest.depth }} cuts (s={{ currentEntity.anomalies.isoForest.score }})</td>
                        <td class="text-right font-bold" :class="currentEntity.anomalies.isoForest.flagged ? 'text-rose-400 animate-pulse' : 'text-emerald-400'">{{ currentEntity.anomalies.isoForest.status }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- TAB 5: Peer Benchmarking -->
                <div v-else-if="activeExcelTab === 5">
                  <table class="w-full text-left border-collapse">
                    <thead>
                      <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                        <th class="pb-0.5">Benchmark Metric</th>
                        <th class="pb-0.5 text-center">Sector Q1 (35 pts)</th>
                        <th class="pb-0.5 text-center">Sector Med (50 pts)</th>
                        <th class="pb-0.5 text-center">Sector Q3 (65 pts)</th>
                        <th class="pb-0.5 text-right">Firm Reading</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-200">
                      <tr>
                        <td>Operating Margin (%)</td>
                        <td class="text-center text-slate-400">11.5%</td>
                        <td class="text-center text-slate-300 font-bold">18.0%</td>
                        <td class="text-center text-slate-400">22.4%</td>
                        <td class="text-right font-bold text-emerald-300">{{ activeEntityKey === 'tcs' ? '26.8% (Q4)' : activeEntityKey === 'tatamotors' ? '19.2% (Q3)' : '4.5% (<Q1)' }}</td>
                      </tr>
                      <tr>
                        <td>Net Debt / Equity (x)</td>
                        <td class="text-center text-slate-400">0.20x</td>
                        <td class="text-center text-slate-300 font-bold">0.80x</td>
                        <td class="text-center text-slate-400">1.40x</td>
                        <td class="text-right font-bold" :class="activeEntityKey === 'distressed' ? 'text-rose-400' : 'text-teal-300'">{{ activeEntityKey === 'tcs' ? '0.00x (Pristine)' : activeEntityKey === 'tatamotors' ? '1.25x' : '3.80x (Outlier)' }}</td>
                      </tr>
                      <tr>
                        <td>Asset Turnover (x)</td>
                        <td class="text-center text-slate-400">0.85x</td>
                        <td class="text-center text-slate-300 font-bold">1.05x</td>
                        <td class="text-center text-slate-400">1.35x</td>
                        <td class="text-right font-mono">{{ activeEntityKey === 'tcs' ? '1.45x' : activeEntityKey === 'tatamotors' ? '1.40x' : '0.55x' }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- TAB 6: Raw Fundamentals -->
                <div v-else-if="activeExcelTab === 6">
                  <table class="w-full text-left border-collapse">
                    <thead>
                      <tr class="text-slate-400 border-b border-slate-800 text-[6.8px] uppercase">
                        <th class="pb-0.5">Parquet Alias</th>
                        <th class="pb-0.5">Normalized Concept</th>
                        <th class="pb-0.5 text-center">Currency / Units</th>
                        <th class="pb-0.5 text-right">Raw Statement Value</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800/60 text-slate-200">
                      <tr>
                        <td class="text-slate-400 font-mono">REV_OPERATIONS</td>
                        <td>Total Revenue from Operations</td>
                        <td class="text-center text-slate-500">INR Crores</td>
                        <td class="text-right font-mono font-bold">{{ activeEntityKey === 'tcs' ? '240,893' : activeEntityKey === 'tatamotors' ? '437,928' : '18,450' }}</td>
                      </tr>
                      <tr>
                        <td class="text-slate-400 font-mono">OP_PROFIT_EBIT</td>
                        <td>Earnings Before Interest and Tax</td>
                        <td class="text-center text-slate-500">INR Crores</td>
                        <td class="text-right font-mono font-bold text-emerald-300">{{ activeEntityKey === 'tcs' ? '64,559' : activeEntityKey === 'tatamotors' ? '84,082' : '830' }}</td>
                      </tr>
                      <tr>
                        <td class="text-slate-400 font-mono">TOTAL_DEBT_NET</td>
                        <td>Short + Long Debt - Cash Equiv</td>
                        <td class="text-center text-slate-500">INR Crores</td>
                        <td class="text-right font-mono" :class="activeEntityKey === 'distressed' ? 'text-rose-400 font-bold' : 'text-slate-300'">{{ activeEntityKey === 'tcs' ? '0 (Net Cash +12,400)' : activeEntityKey === 'tatamotors' ? '54,200' : '48,900' }}</td>
                      </tr>
                      <tr>
                        <td class="text-slate-400 font-mono">CASH_FLOW_OPERATING</td>
                        <td>Cash Flow from Operating Activities</td>
                        <td class="text-center text-slate-500">INR Crores</td>
                        <td class="text-right font-mono font-bold" :class="activeEntityKey === 'distressed' ? 'text-rose-400' : 'text-cyan-300'">{{ activeEntityKey === 'tcs' ? '54,020' : activeEntityKey === 'tatamotors' ? '51,675' : '-775' }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Excel Sheet Tabs (6 Clickable Tabs at Bottom) -->
              <div class="bg-[#071411] border-t border-slate-800 px-1 py-0.5 flex items-center gap-0.5 overflow-x-auto text-[7px] font-mono">
                <span class="text-slate-500 px-1">Sheets:</span>
                <button
                  @click="activeExcelTab = 1"
                  class="px-1.5 py-0.5 rounded-t border-t border-x transition flex items-center gap-1"
                  :class="activeExcelTab === 1
                    ? 'bg-[#0b1f19] text-emerald-300 border-emerald-500/50 font-bold'
                    : 'bg-transparent text-slate-400 border-transparent hover:text-slate-200'"
                >
                  <span>1. Exec Summary</span>
                </button>
                <button
                  @click="activeExcelTab = 2"
                  class="px-1.5 py-0.5 rounded-t border-t border-x transition flex items-center gap-1"
                  :class="activeExcelTab === 2
                    ? 'bg-[#0b1f19] text-emerald-300 border-emerald-500/50 font-bold'
                    : 'bg-transparent text-slate-400 border-transparent hover:text-slate-200'"
                >
                  <span>2. 5-Pillar Scorecard</span>
                </button>
                <button
                  @click="activeExcelTab = 3"
                  class="px-1.5 py-0.5 rounded-t border-t border-x transition flex items-center gap-1"
                  :class="activeExcelTab === 3
                    ? 'bg-[#0b1f19] text-emerald-300 border-emerald-500/50 font-bold'
                    : 'bg-transparent text-slate-400 border-transparent hover:text-slate-200'"
                >
                  <span>3. DuPont Decomp</span>
                </button>
                <button
                  @click="activeExcelTab = 4"
                  class="px-1.5 py-0.5 rounded-t border-t border-x transition flex items-center gap-1"
                  :class="activeExcelTab === 4
                    ? 'bg-[#0b1f19] text-emerald-300 border-emerald-500/50 font-bold'
                    : 'bg-transparent text-slate-400 border-transparent hover:text-slate-200'"
                >
                  <span>4. Anomaly Consensus</span>
                </button>
                <button
                  @click="activeExcelTab = 5"
                  class="px-1.5 py-0.5 rounded-t border-t border-x transition flex items-center gap-1"
                  :class="activeExcelTab === 5
                    ? 'bg-[#0b1f19] text-emerald-300 border-emerald-500/50 font-bold'
                    : 'bg-transparent text-slate-400 border-transparent hover:text-slate-200'"
                >
                  <span>5. Peer Benchmarks</span>
                </button>
                <button
                  @click="activeExcelTab = 6"
                  class="px-1.5 py-0.5 rounded-t border-t border-x transition flex items-center gap-1"
                  :class="activeExcelTab === 6
                    ? 'bg-[#0b1f19] text-emerald-300 border-emerald-500/50 font-bold'
                    : 'bg-transparent text-slate-400 border-transparent hover:text-slate-200'"
                >
                  <span>6. Raw Fundamentals</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Bar -->
    <div class="glass-card px-3 py-1 flex items-center justify-between text-[9px] font-mono">
      <div class="flex items-center gap-2 text-slate-300">
        <span class="text-emerald-400 font-bold">Dual-Format Production Utility:</span>
        <span class="text-slate-400">
          Combines automated natural language LLM synthesis with an openpyxl-generated 6-tab institutional Excel workbook, strictly grounded against mathematical vectors to eliminate hallucinations.
        </span>
      </div>
      <span class="text-emerald-300 text-[8px] bg-emerald-500/10 border border-emerald-500/25 px-1.5 py-0.5 rounded">
        Slide 15: AI Narration &amp; Multi-Format Delivery
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
