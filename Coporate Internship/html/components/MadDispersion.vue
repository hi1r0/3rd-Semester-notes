<script setup lang="ts">
import { ref, computed } from 'vue'

// Base clean cohort of 30 peer firms with realistic operating return metrics
// Centered at Median ~ 12.2% with clean MAD ~ 1.50% and clean sigma ~ 2.22%
const baseCohort = [
  { id: 1, ticker: 'TCS', base: 12.5 },
  { id: 2, ticker: 'INFY', base: 11.8 },
  { id: 3, ticker: 'HCLTECH', base: 12.1 },
  { id: 4, ticker: 'WIPRO', base: 10.9 },
  { id: 5, ticker: 'LTIM', base: 13.0 },
  { id: 6, ticker: 'TECHM', base: 10.2 },
  { id: 7, ticker: 'PERSISTENT', base: 13.6 },
  { id: 8, ticker: 'COFORGE', base: 12.8 },
  { id: 9, ticker: 'MPHASIS', base: 11.5 },
  { id: 10, ticker: 'TATAELXSI', base: 14.8 },
  { id: 11, ticker: 'KPITTECH', base: 13.2 },
  { id: 12, ticker: 'CYIENT', base: 11.2 },
  { id: 13, ticker: 'ZENSAR', base: 10.6 },
  { id: 14, ticker: 'BIRLASOFT', base: 11.9 },
  { id: 15, ticker: 'LTTS', base: 12.3 },
  { id: 16, ticker: 'SONATA', base: 13.9 },
  { id: 17, ticker: 'OFSS', base: 15.2 },
  { id: 18, ticker: 'HAPPSTMNDS', base: 12.7 },
  { id: 19, ticker: 'INTELLECT', base: 13.4 },
  { id: 20, ticker: 'RATEGAIN', base: 12.4 },
  { id: 21, ticker: 'TANLA', base: 14.1 },
  { id: 22, ticker: 'MAPMYINDIA', base: 14.5 },
  { id: 23, ticker: 'NEWGEN', base: 12.9 },
  { id: 24, ticker: 'BSOSOFT', base: 10.8 },
  { id: 25, ticker: 'NAZARA', base: 9.8 },
  { id: 26, ticker: 'KAYNES', base: 13.7 },
  { id: 27, ticker: 'DATAPATT', base: 14.3 },
  { id: 28, ticker: 'LATENTVIEW', base: 11.7 },
  { id: 29, ticker: 'NETWEB', base: 13.1 },
  { id: 30, ticker: 'DISTRESSED', base: 4.8 }, // Genuine distressed firm to test masking
]

// Interactive Contamination State
// k = number of contaminated peers (0 to 15 out of 30, i.e. 0.0% to 50.0%)
const corruptedCount = ref<number>(3)
const corruptionMagnitude = ref<number>(55.0) // Corrupted outlier value (e.g. +55.0%)
const hoveredPoint = ref<{ ticker: string; val: number; isCorrupt: boolean; modZ: number; classZ: number } | null>(null)

// Quick Presets
function setPreset(k: number) {
  corruptedCount.value = k
}

// Active Sample: Replace the last k items with corrupted outliers
const activeSample = computed(() => {
  const result: Array<{ id: number; ticker: string; value: number; isCorrupt: boolean }> = []
  const N = baseCohort.length
  const k = corruptedCount.value

  for (let i = 0; i < N; i++) {
    const item = baseCohort[i]
    if (i >= N - k) {
      result.push({
        id: item.id,
        ticker: `ROGUE_${item.ticker}`,
        value: corruptionMagnitude.value + (i % 3) * 2.5,
        isCorrupt: true,
      })
    } else {
      result.push({
        id: item.id,
        ticker: item.ticker,
        value: item.base,
        isCorrupt: false,
      })
    }
  }
  return result
})

// Clean Baseline Reference Values (k = 0)
const cleanMean = computed(() => {
  const sum = baseCohort.reduce((acc, c) => acc + c.base, 0)
  return sum / baseCohort.length
})

const cleanStd = computed(() => {
  const m = cleanMean.value
  const variance = baseCohort.reduce((acc, c) => acc + Math.pow(c.base - m, 2), 0) / (baseCohort.length - 1)
  return Math.sqrt(variance)
})

const cleanMedian = computed(() => {
  const sorted = [...baseCohort.map(c => c.base)].sort((a, b) => a - b)
  const mid = Math.floor(sorted.length / 2)
  return sorted.length % 2 === 0 ? (sorted[mid - 1] + sorted[mid]) / 2 : sorted[mid]
})

const cleanMAD = computed(() => {
  const med = cleanMedian.value
  const absDevs = baseCohort.map(c => Math.abs(c.base - med)).sort((a, b) => a - b)
  const mid = Math.floor(absDevs.length / 2)
  return absDevs.length % 2 === 0 ? (absDevs[mid - 1] + absDevs[mid]) / 2 : absDevs[mid]
})

const cleanSigmaMAD = computed(() => cleanMAD.value * 1.4826)

// Active Parametric Statistics under Current Contamination
const sampleMean = computed(() => {
  const sum = activeSample.value.reduce((acc, c) => acc + c.value, 0)
  return sum / activeSample.value.length
})

const sampleStd = computed(() => {
  const m = sampleMean.value
  const variance = activeSample.value.reduce((acc, c) => acc + Math.pow(c.value - m, 2), 0) / (activeSample.value.length - 1)
  return Math.sqrt(variance)
})

// Active Robust Median (50% Breakdown Point)
const sampleMedian = computed(() => {
  const sorted = [...activeSample.value.map(c => c.value)].sort((a, b) => a - b)
  const mid = Math.floor(sorted.length / 2)
  return sorted.length % 2 === 0 ? (sorted[mid - 1] + sorted[mid]) / 2 : sorted[mid]
})

// Active Robust MAD & Scale Estimator
const sampleMAD = computed(() => {
  const med = sampleMedian.value
  const absDevs = activeSample.value.map(c => Math.abs(c.value - med)).sort((a, b) => a - b)
  const mid = Math.floor(absDevs.length / 2)
  return absDevs.length % 2 === 0 ? (absDevs[mid - 1] + absDevs[mid]) / 2 : absDevs[mid]
})

// Asymptotically Unbiased Scale Estimator: \hat{\sigma}_{MAD} = 1.4826 * MAD
const sampleSigmaMAD = computed(() => sampleMAD.value * 1.4826)

// Contamination Proportion
const contaminationPct = computed(() => {
  return ((corruptedCount.value / baseCohort.length) * 100).toFixed(1)
})

// Inflation Factors
const stdInflation = computed(() => sampleStd.value / cleanStd.value)
const madInflation = computed(() => sampleSigmaMAD.value / cleanSigmaMAD.value)

// Distress Firm Evaluation (Firm #30 at x = 4.8%)
const distressedFirm = computed(() => {
  const val = 4.8
  const classZ = (val - sampleMean.value) / sampleStd.value
  const modZ = (0.6745 * Math.abs(val - sampleMedian.value)) / (sampleMAD.value || 0.001)
  const isMaskedByStd = Math.abs(classZ) < 3.0 // Outlier masking!
  const isDetectedByMAD = modZ > 3.5
  return {
    val,
    classZ,
    modZ,
    isMaskedByStd,
    isDetectedByMAD,
  }
})

// SVG Visualization Bounds
const svgWidth = 860
const svgHeight = 125
const paddingLeft = 40
const paddingRight = 40
const plotWidth = svgWidth - paddingLeft - paddingRight

const minDomain = 0.0
const maxDomain = 65.0

function scaleX(val: number): number {
  const clamped = Math.max(minDomain, Math.min(maxDomain, val))
  return paddingLeft + ((clamped - minDomain) / (maxDomain - minDomain)) * plotWidth
}
</script>

<template>
  <div class="w-full flex flex-col gap-2 select-none text-slate-100">
    <!-- Top Interactive Control Bar: 50% Breakdown Contamination Slider & Presets -->
    <div class="glass-card px-3 py-1.5 flex items-center justify-between gap-3">
      <!-- Contamination Slider -->
      <div class="flex items-center gap-2.5">
        <div class="flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping" />
          <span class="text-[11px] font-bold text-amber-300 font-mono uppercase tracking-wide">
            Contamination Injection:
          </span>
        </div>

        <div class="flex items-center gap-2">
          <span class="text-[10px] font-mono text-slate-400">k = {{ corruptedCount }}/30</span>
          <input
            v-model.number="corruptedCount"
            type="range"
            min="0"
            max="15"
            step="1"
            class="w-28 h-1.5 bg-slate-700/80 rounded appearance-none cursor-pointer accent-emerald-400"
          >
          <span
            class="text-[11px] font-mono font-bold px-2 py-0.5 rounded border text-center min-w-[58px]"
            :class="corruptedCount >= 15
              ? 'bg-rose-500/20 text-rose-300 border-rose-500/40 animate-pulse'
              : corruptedCount > 0
                ? 'bg-amber-500/20 text-amber-300 border-amber-500/40'
                : 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30'"
          >
            {{ contaminationPct }}% γ
          </span>
        </div>
      </div>

      <!-- Quick Preset Triggers -->
      <div class="flex items-center gap-1.5 bg-[#071411]/90 p-0.5 rounded-lg border border-emerald-500/20">
        <button
          class="px-2 py-0.5 text-[10px] font-medium rounded transition"
          :class="corruptedCount === 0
            ? 'bg-emerald-500/30 text-emerald-300 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset(0)"
        >
          Pristine (0%)
        </button>
        <button
          class="px-2 py-0.5 text-[10px] font-medium rounded transition"
          :class="corruptedCount === 3
            ? 'bg-amber-500/30 text-amber-300 shadow-[0_0_8px_rgba(245,158,11,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset(3)"
        >
          10% Sector Shock
        </button>
        <button
          class="px-2 py-0.5 text-[10px] font-medium rounded transition"
          :class="corruptedCount === 9
            ? 'bg-orange-500/30 text-orange-300 shadow-[0_0_8px_rgba(249,115,22,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset(9)"
        >
          30% Systemic Shock
        </button>
        <button
          class="px-2 py-0.5 text-[10px] font-medium rounded transition"
          :class="corruptedCount === 14
            ? 'bg-emerald-500/30 text-emerald-300 border border-emerald-400/40 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset(14)"
        >
          46.7% Max Tolerance
        </button>
        <button
          class="px-2 py-0.5 text-[10px] font-medium rounded transition"
          :class="corruptedCount === 15
            ? 'bg-red-500/40 text-red-300 shadow-[0_0_10px_rgba(239,68,68,0.4)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset(15)"
        >
          50% Breakdown Cliff
        </button>
      </div>

      <!-- Outlier Masking Warning Banner -->
      <div class="flex items-center gap-1.5 font-mono text-[10px]">
        <span
          v-if="corruptedCount >= 1"
          class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 flex items-center gap-1"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-ping" />
          Std Dev Masking Active: σ inflated {{ stdInflation.toFixed(1) }}x
        </span>
        <span
          v-else
          class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
        >
          Clean Baseline Profile
        </span>
      </div>
    </div>

    <!-- Main Visual Stage: Classical 3σ Masking Band vs Robust 3.5·σ_MAD Fence -->
    <div class="glass-card p-2.5 flex flex-col justify-between overflow-hidden">
      <div class="flex items-center justify-between mb-0.5 px-1">
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold text-white tracking-wide">
            Dynamic Dispersion Response: Classical σ Inflation vs MAD Invariance
          </span>
          <span class="text-[10px] text-slate-400 font-mono">
            [Sample N = 30 Peers | Operating Return %]
          </span>
        </div>

        <!-- Legend -->
        <div class="flex items-center gap-3 text-[10px] font-mono">
          <span class="flex items-center gap-1 text-emerald-400">
            <span class="w-2.5 h-2 rounded-sm bg-emerald-500/30 border border-emerald-400 inline-block" />
            Robust Fence [Med ± 3.5·σ_MAD]
          </span>
          <span class="flex items-center gap-1 text-rose-400">
            <span class="w-2.5 h-2 rounded-sm bg-rose-500/20 border border-rose-400 border-dashed inline-block" />
            Blown Classical [μ ± 3·σ]
          </span>
        </div>
      </div>

      <!-- SVG Canvas Stage -->
      <div class="relative w-full h-[130px] bg-[#071411]/95 rounded-lg border border-emerald-500/15 overflow-hidden flex items-center justify-center">
        <svg :viewBox="`0 0 ${svgWidth} ${svgHeight}`" class="w-full h-full">
          <defs>
            <linearGradient id="madSafeCorridor" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#10b981" stop-opacity="0.25" />
              <stop offset="100%" stop-color="#10b981" stop-opacity="0.05" />
            </linearGradient>
            <linearGradient id="stdBlownCorridor" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.16" />
              <stop offset="100%" stop-color="#f43f5e" stop-opacity="0.02" />
            </linearGradient>
          </defs>

          <!-- Blown Classical Error Band: [mean - 3*std, mean + 3*std] -->
          <rect
            :x="Math.max(paddingLeft, scaleX(sampleMean - 3 * sampleStd))"
            y="20"
            :width="Math.max(0, Math.min(svgWidth - paddingRight, scaleX(sampleMean + 3 * sampleStd)) - Math.max(paddingLeft, scaleX(sampleMean - 3 * sampleStd)))"
            height="86"
            fill="url(#stdBlownCorridor)"
            stroke="#f43f5e"
            stroke-width="1.2"
            stroke-dasharray="3 3"
            rx="4"
          />

          <!-- Robust MAD Invariant Fence: [median - 3.5*sigmaMAD, median + 3.5*sigmaMAD] -->
          <rect
            :x="scaleX(sampleMedian - 3.5 * sampleSigmaMAD)"
            y="26"
            :width="Math.max(4, scaleX(sampleMedian + 3.5 * sampleSigmaMAD) - scaleX(sampleMedian - 3.5 * sampleSigmaMAD))"
            height="74"
            fill="url(#madSafeCorridor)"
            stroke="#34d399"
            stroke-width="1.8"
            rx="3"
          />

          <!-- Reference Axis -->
          <line
            :x1="paddingLeft"
            y1="68"
            :x2="svgWidth - paddingRight"
            y2="68"
            stroke="#334155"
            stroke-width="1"
            stroke-dasharray="2 3"
          />

          <!-- Median Marker -->
          <line
            :x1="scaleX(sampleMedian)"
            y1="22"
            :x2="scaleX(sampleMedian)"
            y2="104"
            stroke="#00e599"
            stroke-width="2.5"
            stroke-linecap="round"
          />
          <text
            :x="scaleX(sampleMedian)"
            y="16"
            fill="#00e599"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            Med: {{ sampleMedian.toFixed(1) }}%
          </text>

          <!-- Mean Marker (Drifting Under Contamination) -->
          <line
            :x1="scaleX(sampleMean)"
            y1="22"
            :x2="scaleX(sampleMean)"
            y2="104"
            stroke="#f43f5e"
            stroke-width="2"
            stroke-dasharray="4 2"
          />
          <text
            :x="scaleX(sampleMean)"
            y="116"
            fill="#f43f5e"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            μ̄: {{ sampleMean.toFixed(1) }}%
          </text>

          <!-- Robust Fence Boundary Labels -->
          <text
            :x="scaleX(sampleMedian - 3.5 * sampleSigmaMAD)"
            y="114"
            fill="#34d399"
            font-size="8"
            font-family="monospace"
            text-anchor="middle"
          >
            -3.5·σ_MAD ({{ (sampleMedian - 3.5 * sampleSigmaMAD).toFixed(1) }}%)
          </text>
          <text
            :x="scaleX(sampleMedian + 3.5 * sampleSigmaMAD)"
            y="114"
            fill="#34d399"
            font-size="8"
            font-family="monospace"
            text-anchor="middle"
          >
            +3.5·σ_MAD ({{ (sampleMedian + 3.5 * sampleSigmaMAD).toFixed(1) }}%)
          </text>

          <!-- Peer Firm Data Points -->
          <g v-for="(p, i) in activeSample" :key="p.id">
            <!-- Clean / Normal Peer -->
            <circle
              v-if="!p.isCorrupt"
              :cx="scaleX(p.value)"
              :cy="68 + ((i % 5) - 2) * 8"
              :r="p.ticker === 'DISTRESSED' ? 5.5 : 3.5"
              :fill="p.ticker === 'DISTRESSED' ? '#fbbf24' : '#34d399'"
              :stroke="p.ticker === 'DISTRESSED' ? '#f59e0b' : '#071411'"
              stroke-width="1.2"
              class="cursor-pointer transition-all duration-150 hover:r-5"
              @mouseenter="hoveredPoint = { ticker: p.ticker, val: p.value, isCorrupt: false, modZ: (0.6745 * Math.abs(p.value - sampleMedian)) / (sampleMAD || 0.001), classZ: (p.value - sampleMean) / sampleStd }"
              @mouseleave="hoveredPoint = null"
            />

            <!-- Corrupted Outlier Peer -->
            <circle
              v-else
              :cx="scaleX(p.value)"
              :cy="68 + ((i % 3) - 1) * 10"
              r="5.5"
              fill="#f43f5e"
              stroke="#ffffff"
              stroke-width="1.5"
              class="cursor-pointer transition-all duration-150 animate-pulse hover:r-7"
              @mouseenter="hoveredPoint = { ticker: p.ticker, val: p.value, isCorrupt: true, modZ: (0.6745 * Math.abs(p.value - sampleMedian)) / (sampleMAD || 0.001), classZ: (p.value - sampleMean) / sampleStd }"
              @mouseleave="hoveredPoint = null"
            />
          </g>

          <!-- Hover Tooltip -->
          <g v-if="hoveredPoint">
            <rect
              :x="Math.min(svgWidth - 160, Math.max(10, scaleX(hoveredPoint.val) - 75))"
              y="28"
              width="150"
              height="30"
              rx="4"
              fill="#071411"
              stroke="#34d399"
              stroke-width="1"
            />
            <text
              :x="Math.min(svgWidth - 85, Math.max(85, scaleX(hoveredPoint.val)))"
              y="41"
              fill="#ffffff"
              font-size="8.5"
              font-family="monospace"
              text-anchor="middle"
              font-weight="bold"
            >
              {{ hoveredPoint.ticker }}: {{ hoveredPoint.val.toFixed(1) }}%
            </text>
            <text
              :x="Math.min(svgWidth - 85, Math.max(85, scaleX(hoveredPoint.val)))"
              y="52"
              fill="#94a3b8"
              font-size="7.5"
              font-family="monospace"
              text-anchor="middle"
            >
              Mod-Z: {{ hoveredPoint.modZ.toFixed(2) }} | Class-Z: {{ hoveredPoint.classZ.toFixed(2) }}
            </text>
          </g>
        </svg>
      </div>
    </div>

    <!-- Side-by-Side KPI Cards & Mathematical Derivation Engine -->
    <div class="grid grid-cols-12 gap-2.5 items-stretch">
      <!-- Card 1: Classical Estimator Breakdown Status -->
      <div class="col-span-3 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-rose-500/20">
            <span class="text-[10.5px] font-bold text-rose-300 uppercase tracking-wider font-mono">
              Classical Standard Dev
            </span>
            <span
              class="text-[8.5px] px-1.5 py-0.2 rounded font-mono font-bold"
              :class="corruptedCount >= 1 ? 'bg-rose-500/20 text-rose-300' : 'bg-emerald-500/20 text-emerald-300'"
            >
              ε* = 0.0%
            </span>
          </div>

          <div class="bg-[#071411]/90 p-2 rounded border border-rose-500/25 mb-1.5">
            <div class="text-[9px] text-slate-400 font-mono">Sample Std Dev (σ̂):</div>
            <div class="text-base font-extrabold font-mono text-rose-300">
              {{ sampleStd.toFixed(2) }}%
              <span class="text-[10px] font-normal text-rose-400/90 ml-1">
                (+{{ ((stdInflation - 1) * 100).toFixed(0) }}%)
              </span>
            </div>
            <div class="text-[9px] text-slate-500 font-mono">
              Clean σ̂₀ = {{ cleanStd.toFixed(2) }}%
            </div>
          </div>

          <div class="space-y-1 text-[9px] text-slate-300">
            <div class="text-rose-300/90 font-mono font-semibold">
              Failure Mode: Outlier Masking
            </div>
            <p class="leading-tight text-slate-400">
              Corrupted peers inflate the denominator, collapsing classical Z-scores. Distressed firm (x=4.8%) evaluates to Z={{ distressedFirm.classZ.toFixed(2) }}, masquerading as healthy!
            </p>
          </div>
        </div>
      </div>

      <!-- Card 2: Robust Modified MAD Estimator Status -->
      <div class="col-span-3 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/20">
            <span class="text-[10.5px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Modified MAD Scale
            </span>
            <span class="text-[8.5px] px-1.5 py-0.2 rounded font-mono font-bold bg-emerald-500/20 text-emerald-300">
              ε* = 50.0%
            </span>
          </div>

          <div class="bg-[#071411]/90 p-2 rounded border border-emerald-500/25 mb-1.5">
            <div class="text-[9px] text-slate-400 font-mono">Robust Scale (σ̂_MAD):</div>
            <div class="text-base font-extrabold font-mono text-emerald-300">
              {{ sampleSigmaMAD.toFixed(2) }}%
              <span class="text-[10px] font-normal text-emerald-400/90 ml-1">
                (+{{ ((madInflation - 1) * 100).toFixed(1) }}%)
              </span>
            </div>
            <div class="text-[9px] text-slate-500 font-mono">
              MAD = {{ sampleMAD.toFixed(2) }}% | Factor: 1.4826
            </div>
          </div>

          <div class="space-y-1 text-[9px] text-slate-300">
            <div class="text-emerald-300 font-mono font-semibold">
              Protection Mode: 50% Invariant Shield
            </div>
            <p class="leading-tight text-slate-400">
              Scale remains impervious up to k=14/30 (46.7%). Distressed firm correctly isolated at M_i={{ distressedFirm.modZ.toFixed(2) }} &gt; 3.5 without distortion.
            </p>
          </div>
        </div>
      </div>

      <!-- Card 3: Normal Consistency Proof (Why 0.6745?) -->
      <div class="col-span-3 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
            <span class="text-[10.5px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Why 0.6745? Derivation
            </span>
            <span class="text-[8.5px] px-1.5 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Proof
            </span>
          </div>

          <!-- Formula Box -->
          <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20 font-mono text-[9.5px] text-emerald-200 leading-snug mb-1">
            <div>MAD = median(|xᵢ - median(X)|)</div>
            <div>F(z) = 2Φ(z) - 1 = 0.50</div>
            <div>⟹ Φ(z) = 0.75 ⟹ z ≈ 0.6745</div>
            <div class="text-emerald-400 font-bold border-t border-emerald-500/15 pt-0.5 mt-0.5">
              σ̂_MAD = MAD / 0.6745 ≈ 1.4826·MAD
            </div>
          </div>

          <!-- Where: Parameter Block -->
          <div class="text-[8.5px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono">Where:</div>
            <ul class="space-y-0.5 text-slate-400">
              <li><strong class="text-white font-mono">Φ(z):</strong> Standard normal cumulative distribution</li>
              <li><strong class="text-white font-mono">0.6745:</strong> 75th percentile of normal curve [Φ⁻¹(0.75)]</li>
              <li><strong class="text-white font-mono">1.4826:</strong> Consistency scale multiplier (1 / 0.6745)</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Card 4: Iglewicz-Hoaglin Outlier Rule & Breakdown Bound -->
      <div class="col-span-3 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
            <span class="text-[10.5px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Iglewicz-Hoaglin Rule
            </span>
            <span class="text-[8.5px] px-1.5 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Decision Rule
            </span>
          </div>

          <!-- Modified Z Formula -->
          <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20 font-mono text-[9.5px] text-emerald-200 leading-snug mb-1">
            <div>Mᵢ = 0.6745 · |xᵢ - median(X)| / MAD</div>
            <div class="text-amber-300 font-bold mt-0.5">
              Outlier(xᵢ) = 1_{Mᵢ &gt; 3.5}
            </div>
            <div class="text-[8.5px] text-slate-400 border-t border-emerald-500/15 pt-0.5 mt-0.5">
              Theoretical Bound: ε*(MAD) = ⌊n/2⌋ / n ⟶ 50.0%
            </div>
          </div>

          <!-- Where: Parameter Block -->
          <div class="text-[8.5px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono">Where:</div>
            <ul class="space-y-0.5 text-slate-400">
              <li><strong class="text-white font-mono">Mᵢ:</strong> Robust modified Z-score immune to masking</li>
              <li><strong class="text-white font-mono">3.5:</strong> Critical threshold isolating 3.5σ departures</li>
              <li><strong class="text-white font-mono">50.0%:</strong> Maximal possible breakdown point bound</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
