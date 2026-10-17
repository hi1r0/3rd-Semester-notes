<script setup lang="ts">
import { ref, computed } from 'vue'

// Base peer sample of 24 corporate ratios (e.g. Current Ratio or Interest Coverage)
// Includes normal cluster around 1.0, plus one genuinely distressed firm at x = -1.80
const baseSample = [
  0.82, 0.86, 0.90, 0.94, 0.97, 1.00, 1.02, 1.05, 1.08, 1.11,
  1.15, 1.19, 1.22, 1.26, 1.30, 0.76, 0.79, 1.35, 1.40, 1.03,
  0.98, 1.07, 1.12, -1.80, // distressed firm index 23
]

const outlierVal = ref<number>(1.0) // slider range [1.0, 20.0]
const activePreset = ref<'clean' | 'moderate' | 'severe' | 'fatal'>('clean')

function setPreset(preset: 'clean' | 'moderate' | 'severe' | 'fatal') {
  activePreset.value = preset
  if (preset === 'clean') outlierVal.value = 1.0
  else if (preset === 'moderate') outlierVal.value = 6.0
  else if (preset === 'severe') outlierVal.value = 12.0
  else if (preset === 'fatal') outlierVal.value = 19.5
}

// Current dataset including the single contaminated outlier
const fullData = computed(() => {
  return [...baseSample, outlierVal.value]
})

// Parametric Sample Mean \bar{\mu}
const sampleMean = computed(() => {
  const sum = fullData.value.reduce((acc, v) => acc + v, 0)
  return sum / fullData.value.length
})

// Clean ground truth mean
const cleanMean = computed(() => {
  const clean = [...baseSample, 1.0]
  return clean.reduce((acc, v) => acc + v, 0) / clean.length
})

// Parametric Standard Deviation \hat{\sigma}
const sampleStd = computed(() => {
  const mean = sampleMean.value
  const variance = fullData.value.reduce((acc, v) => acc + Math.pow(v - mean, 2), 0) / (fullData.value.length - 1)
  return Math.sqrt(variance)
})

const cleanStd = computed(() => {
  const clean = [...baseSample, 1.0]
  const mean = cleanMean.value
  const variance = clean.reduce((acc, v) => acc + Math.pow(v - mean, 2), 0) / (clean.length - 1)
  return Math.sqrt(variance)
})

// Robust Sample Median (50% Breakdown Point)
const sampleMedian = computed(() => {
  const sorted = [...fullData.value].sort((a, b) => a - b)
  const mid = Math.floor(sorted.length / 2)
  if (sorted.length % 2 === 0) {
    return (sorted[mid - 1] + sorted[mid]) / 2
  }
  return sorted[mid]
})

// Robust Median Absolute Deviation (MAD)
const sampleMAD = computed(() => {
  const med = sampleMedian.value
  const absDevs = fullData.value.map(v => Math.abs(v - med)).sort((a, b) => a - b)
  const mid = Math.floor(absDevs.length / 2)
  const rawMad = absDevs.length % 2 === 0
    ? (absDevs[mid - 1] + absDevs[mid]) / 2
    : absDevs[mid]
  return rawMad
})

// Distressed Firm Analysis (x_k = -1.80)
const distressedVal = -1.80

// Classical Z-score: (x - \mu) / \sigma
const classicalZ = computed(() => {
  return (distressedVal - sampleMean.value) / sampleStd.value
})

// Robust Modified Z_MAD: (x - Median) / (1.4826 * MAD)
const robustZ = computed(() => {
  const scale = 1.4826 * sampleMAD.value
  return (distressedVal - sampleMedian.value) / (scale || 0.0001)
})

// Outlier Masking Status
const isMasked = computed(() => {
  return Math.abs(classicalZ.value) < 2.0
})

// SVG Curve generation parameters
const svgWidth = 490
const svgHeight = 175
const xMin = -3.5
const xMax = 7.5

function scaleX(x: number): number {
  return ((x - xMin) / (xMax - xMin)) * svgWidth
}

function normalDensity(x: number, mean: number, std: number): number {
  const exponent = -0.5 * Math.pow((x - mean) / std, 2)
  return (1 / (std * Math.sqrt(2 * Math.PI))) * Math.exp(exponent)
}

function scaleY(density: number, maxDensity: number = 0.9): number {
  const plotBottom = svgHeight - 25
  const plotHeight = svgHeight - 45
  const clamped = Math.min(density / maxDensity, 1.1)
  return plotBottom - clamped * plotHeight
}

// Generate SVG path for Clean Normal Distribution
const cleanPath = computed(() => {
  const points: string[] = []
  const steps = 70
  for (let i = 0; i <= steps; i++) {
    const x = xMin + (i / steps) * (xMax - xMin)
    const dens = normalDensity(x, cleanMean.value, cleanStd.value)
    const sx = scaleX(x)
    const sy = scaleY(dens)
    points.push(`${i === 0 ? 'M' : 'L'} ${sx.toFixed(1)} ${sy.toFixed(1)}`)
  }
  return points.join(' ')
})

// Generate SVG path for Contaminated Normal Distribution
const contaminatedPath = computed(() => {
  const points: string[] = []
  const steps = 70
  for (let i = 0; i <= steps; i++) {
    const x = xMin + (i / steps) * (xMax - xMin)
    const dens = normalDensity(x, sampleMean.value, sampleStd.value)
    const sx = scaleX(x)
    const sy = scaleY(dens)
    points.push(`${i === 0 ? 'M' : 'L'} ${sx.toFixed(1)} ${sy.toFixed(1)}`)
  }
  return points.join(' ')
})

// False safety bracket [mean - 2*std, mean + 2*std]
const bracketLeft = computed(() => Math.max(scaleX(sampleMean.value - 2 * sampleStd.value), 0))
const bracketRight = computed(() => Math.min(scaleX(sampleMean.value + 2 * sampleStd.value), svgWidth))
</script>

<template>
  <div class="w-full flex flex-col gap-2.5 text-slate-100 select-none">
    <!-- Top Interactive Control Bar: Outlier Contamination Injection -->
    <div class="glass-card px-3.5 py-2 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping" />
          <span class="text-xs font-bold text-amber-300">Contamination Injection:</span>
        </div>

        <!-- Slider -->
        <div class="flex items-center gap-2">
          <span class="text-[11px] font-mono text-slate-400">x₀ =</span>
          <input
            v-model.number="outlierVal"
            type="range"
            min="1.0"
            max="20.0"
            step="0.5"
            class="w-36 h-1.5 bg-slate-700/80 rounded-lg appearance-none cursor-pointer accent-emerald-400"
            @input="activePreset = 'clean'"
          >
          <span class="text-xs font-mono font-bold text-emerald-300 bg-[#071411] px-2 py-0.5 rounded border border-emerald-500/25 min-w-[50px] text-center">
            +{{ outlierVal.toFixed(1) }}σ
          </span>
        </div>
      </div>

      <!-- Quick Preset Triggers -->
      <div class="flex items-center gap-1.5 bg-[#071411]/90 p-0.5 rounded-lg border border-emerald-500/20">
        <button
          class="px-2 py-0.5 text-[11px] font-medium rounded transition"
          :class="outlierVal <= 2.0
            ? 'bg-emerald-500/30 text-emerald-300 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset('clean')"
        >
          Clean Baseline (x₀=1.0)
        </button>
        <button
          class="px-2 py-0.5 text-[11px] font-medium rounded transition"
          :class="outlierVal > 2.0 && outlierVal <= 8.0
            ? 'bg-amber-500/30 text-amber-300 shadow-[0_0_8px_rgba(245,158,11,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset('moderate')"
        >
          Moderate (x₀=6.0)
        </button>
        <button
          class="px-2 py-0.5 text-[11px] font-medium rounded transition"
          :class="outlierVal > 8.0 && outlierVal <= 15.0
            ? 'bg-rose-500/30 text-rose-300 shadow-[0_0_8px_rgba(244,63,94,0.3)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset('severe')"
        >
          Severe (x₀=12.0)
        </button>
        <button
          class="px-2 py-0.5 text-[11px] font-medium rounded transition"
          :class="outlierVal > 15.0
            ? 'bg-red-500/40 text-red-300 shadow-[0_0_10px_rgba(239,68,68,0.4)]'
            : 'text-slate-400 hover:text-slate-200'"
          @click="setPreset('fatal')"
        >
          Fatal Breakdown (x₀=19.5)
        </button>
      </div>
    </div>

    <!-- Main Content Grid: SVG Bell Curve vs Robust Metric Telemetry -->
    <div class="grid grid-cols-12 gap-3 items-stretch">
      <!-- Left Column: Dynamic Bell Curve with Masking Bracket -->
      <div class="col-span-7 glass-card p-3 flex flex-col justify-between relative overflow-hidden">
        <div class="flex items-center justify-between mb-1">
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold text-white tracking-wide">Dynamic Gaussian Density Shift</span>
            <span
              v-if="isMasked"
              class="px-2 py-0.5 text-[10px] font-extrabold uppercase rounded bg-rose-500/20 text-rose-300 border border-rose-500/40 animate-pulse"
            >
              ⚠️ Outlier Masking Active
            </span>
            <span
              v-else
              class="px-2 py-0.5 text-[10px] font-semibold uppercase rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
            >
              ✓ Distressed Firm Flagged
            </span>
          </div>

          <!-- Legend -->
          <div class="flex items-center gap-3 text-[10px] font-mono">
            <span class="flex items-center gap-1 text-emerald-400">
              <span class="w-2.5 h-0.5 bg-emerald-400 inline-block" /> Clean PDF
            </span>
            <span class="flex items-center gap-1 text-rose-400">
              <span class="w-2.5 h-0.5 bg-rose-400 inline-block border-t border-dashed" /> Contaminated
            </span>
          </div>
        </div>

        <!-- SVG Curve Canvas -->
        <div class="relative w-full h-[180px] bg-[#071411]/90 rounded-lg border border-emerald-500/15 overflow-hidden flex items-center justify-center">
          <svg :viewBox="`0 0 ${svgWidth} ${svgHeight}`" class="w-full h-full">
            <defs>
              <!-- Gradient for False Safety Bracket -->
              <linearGradient id="safetyBracketGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.18" />
                <stop offset="100%" stop-color="#f43f5e" stop-opacity="0.02" />
              </linearGradient>
              <linearGradient id="cleanFillGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#10b981" stop-opacity="0.25" />
                <stop offset="100%" stop-color="#10b981" stop-opacity="0.0" />
              </linearGradient>
            </defs>

            <!-- Coordinate baseline -->
            <line
              x1="10"
              :y1="svgHeight - 25"
              :x2="svgWidth - 10"
              :y2="svgHeight - 25"
              stroke="#334155"
              stroke-width="1.2"
            />

            <!-- Shaded False Safety Zone [mean - 2*std, mean + 2*std] -->
            <rect
              :x="bracketLeft"
              y="15"
              :width="Math.max(bracketRight - bracketLeft, 0)"
              :height="svgHeight - 40"
              fill="url(#safetyBracketGrad)"
              stroke="#f43f5e"
              stroke-width="0.8"
              stroke-dasharray="3,3"
            />
            <text
              :x="(bracketLeft + bracketRight) / 2"
              y="26"
              text-anchor="middle"
              fill="#fb7185"
              font-size="9"
              font-family="monospace"
              font-weight="bold"
            >
              False Safety Bracket [μ̄ ± 2σ̂]
            </text>

            <!-- Clean Ground Truth Bell Curve -->
            <path
              :d="cleanPath"
              fill="none"
              stroke="#34d399"
              stroke-width="1.8"
              stroke-dasharray="4,2"
              opacity="0.75"
            />

            <!-- Contaminated Bell Curve -->
            <path
              :d="contaminatedPath"
              fill="none"
              stroke="#f43f5e"
              stroke-width="2.2"
              class="transition-all duration-300"
            />

            <!-- Ground Truth Median Line (Green, Rock Solid) -->
            <line
              :x1="scaleX(sampleMedian)"
              y1="32"
              :x2="scaleX(sampleMedian)"
              :y2="svgHeight - 25"
              stroke="#10b981"
              stroke-width="2"
            />
            <circle :cx="scaleX(sampleMedian)" :cy="32" r="3" fill="#10b981" />
            <text
              :x="scaleX(sampleMedian) - 6"
              y="44"
              text-anchor="end"
              fill="#34d399"
              font-size="9"
              font-weight="bold"
            >
              Median (50% BP)
            </text>

            <!-- Skewed Sample Mean Line (Rose/Red, Drifting) -->
            <line
              :x1="scaleX(sampleMean)"
              y1="40"
              :x2="scaleX(sampleMean)"
              :y2="svgHeight - 25"
              stroke="#f43f5e"
              stroke-width="2"
              stroke-dasharray="3,2"
            />
            <circle :cx="scaleX(sampleMean)" :cy="40" r="3" fill="#f43f5e" />
            <text
              :x="scaleX(sampleMean) + 6"
              y="52"
              text-anchor="start"
              fill="#fb7185"
              font-size="9"
              font-weight="bold"
            >
              Skewed μ̄
            </text>

            <!-- Distressed Firm Dot at x = -1.80 -->
            <circle
              :cx="scaleX(distressedVal)"
              :cy="svgHeight - 25"
              r="4.5"
              fill="#ef4444"
              stroke="#ffffff"
              stroke-width="1.2"
            />
            <text
              :x="scaleX(distressedVal)"
              :y="svgHeight - 10"
              text-anchor="middle"
              fill="#f87171"
              font-size="8.5"
              font-family="monospace"
              font-weight="bold"
            >
              Distressed (xk)
            </text>

            <!-- Injected Outlier Dot at x_0 -->
            <g v-if="outlierVal <= xMax">
              <circle
                :cx="scaleX(outlierVal)"
                :cy="svgHeight - 25"
                r="5"
                fill="#fbbf24"
                stroke="#f59e0b"
                stroke-width="2"
              />
              <circle
                :cx="scaleX(outlierVal)"
                :cy="svgHeight - 25"
                r="8"
                fill="none"
                stroke="#fbbf24"
                stroke-width="1"
                class="animate-ping"
              />
              <text
                :x="scaleX(outlierVal)"
                :y="svgHeight - 10"
                text-anchor="middle"
                fill="#fbbf24"
                font-size="8.5"
                font-family="monospace"
                font-weight="bold"
              >
                Outlier (x₀)
              </text>
            </g>
            <g v-else>
              <!-- Arrow pointing offscreen for extreme outlier -->
              <text
                :x="svgWidth - 12"
                :y="svgHeight - 32"
                text-anchor="end"
                fill="#fbbf24"
                font-size="9"
                font-family="monospace"
                font-weight="bold"
              >
                x₀ = {{ outlierVal.toFixed(1) }} ➔
              </text>
            </g>
          </svg>
        </div>

        <!-- Annotation Footer -->
        <div class="text-[10.5px] text-slate-300 mt-2 bg-[#071411]/70 p-2 rounded border border-emerald-500/10 flex items-center justify-between">
          <div class="leading-tight">
            <strong class="text-white">Masking Proof:</strong>
            As single outlier <span class="text-amber-300 font-mono">x₀ → ∞</span>, sample variance explodes as <span class="text-amber-300 font-mono">x₀²/n</span>.
            The distressed firm's $Z$-score collapses:
            <span class="text-emerald-300 font-mono">Zₖ ≈ -1/√n → 0</span>.
          </div>
          <div class="font-mono text-[10px] text-slate-400 ml-2 whitespace-nowrap">
            n = 25 Filings
          </div>
        </div>
      </div>

      <!-- Right Column: Quantitative Telemetry & Breakdown Comparison -->
      <div class="col-span-5 flex flex-col justify-between gap-2.5">
        <!-- Distressed Firm Detection Card: Classical vs Robust -->
        <div class="glass-card p-3 border-emerald-500/25">
          <div class="text-[11px] font-bold text-white mb-2 flex items-center justify-between">
            <span>Detection of Truly Distressed Firm (x = -1.80)</span>
            <span class="text-[10px] font-mono text-slate-400">Cutoff: |Z| &gt; 2.0</span>
          </div>

          <!-- Classical Gaussian Z-Score -->
          <div class="p-2 rounded bg-[#071411]/85 border mb-2" :class="isMasked ? 'border-rose-500/40 bg-rose-950/20' : 'border-slate-700/60'">
            <div class="flex items-center justify-between text-xs mb-1">
              <span class="font-medium text-slate-300">Classical Gaussian Z-Score:</span>
              <span
                class="font-mono font-bold text-sm"
                :class="isMasked ? 'text-rose-400' : 'text-emerald-400'"
              >
                {{ classicalZ.toFixed(2) }}
              </span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-[10px] text-slate-400">Z = (x - μ̄) / σ̂</span>
              <span
                class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wide"
                :class="isMasked
                  ? 'bg-rose-500/30 text-rose-300 border border-rose-500/50'
                  : 'bg-emerald-500/25 text-emerald-300 border border-emerald-500/40'"
              >
                {{ isMasked ? 'MASKED (FALSE SAFE)' : 'FLAGGED' }}
              </span>
            </div>
          </div>

          <!-- Robust Modified Z_MAD -->
          <div class="p-2 rounded bg-[#071411]/85 border border-emerald-500/35 bg-emerald-950/10">
            <div class="flex items-center justify-between text-xs mb-1">
              <span class="font-medium text-emerald-200">Robust Modified Z_MAD:</span>
              <span class="font-mono font-bold text-sm text-emerald-300">
                {{ robustZ.toFixed(2) }}
              </span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-[10px] text-slate-400">Z_MAD = (x - Med) / (1.4826·MAD)</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wide bg-emerald-500/30 text-emerald-300 border border-emerald-500/50">
                FLAGGED (SAFE)
              </span>
            </div>
          </div>
        </div>

        <!-- Estimator Breakdown Point Invariant Comparison -->
        <div class="glass-card p-3 border-emerald-500/25 flex-1 flex flex-col justify-between">
          <div class="text-[11px] font-bold text-white mb-2 flex items-center justify-between">
            <span>Estimator Breakdown Comparison</span>
            <span class="text-[10px] font-mono text-emerald-400">ε* = min(m/n)</span>
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs">
            <!-- Classical Estimator -->
            <div class="p-2 rounded bg-[#071411]/90 border border-rose-500/30">
              <div class="text-[10px] font-bold uppercase tracking-wider text-rose-400 mb-1">
                Classical Sample
              </div>
              <div class="text-[11px] text-slate-300">
                Mean μ̄: <strong class="text-white font-mono">{{ sampleMean.toFixed(2) }}</strong>
                <span class="text-[10px] text-rose-400 ml-1">({{ ((sampleMean - cleanMean) / cleanMean * 100).toFixed(0) }}%)</span>
              </div>
              <div class="text-[11px] text-slate-300">
                Std σ̂: <strong class="text-white font-mono">{{ sampleStd.toFixed(2) }}</strong>
                <span class="text-[10px] text-rose-400 ml-1">({{ (sampleStd / cleanStd).toFixed(1) }}x)</span>
              </div>
              <div class="mt-1.5 pt-1 border-t border-rose-500/20 text-[10px] font-bold text-rose-300">
                Breakdown Point: ε* = 0.0%
              </div>
            </div>

            <!-- Robust Median & MAD -->
            <div class="p-2 rounded bg-[#071411]/90 border border-emerald-500/35">
              <div class="text-[10px] font-bold uppercase tracking-wider text-emerald-400 mb-1">
                Robust Non-Parametric
              </div>
              <div class="text-[11px] text-slate-300">
                Median: <strong class="text-white font-mono">{{ sampleMedian.toFixed(2) }}</strong>
                <span class="text-[10px] text-emerald-400 ml-1">(±0.0%)</span>
              </div>
              <div class="text-[11px] text-slate-300">
                MAD: <strong class="text-white font-mono">{{ sampleMAD.toFixed(2) }}</strong>
                <span class="text-[10px] text-emerald-400 ml-1">(Stable)</span>
              </div>
              <div class="mt-1.5 pt-1 border-t border-emerald-500/20 text-[10px] font-bold text-emerald-300">
                Breakdown Point: ε* = 50.0%
              </div>
            </div>
          </div>

          <div class="mt-2 text-[10px] text-slate-400 leading-tight">
            💡 <strong class="text-slate-200">Key Finding:</strong> A single aberrant line-item destroys classical parametric screening ($\varepsilon^* = 0\%$), whereas median-based dispersion withstands up to $50\%$ contamination.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
