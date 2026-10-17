<script setup lang="ts">
import { ref, computed } from 'vue'

// Metric Preset Profiles
interface MetricProfile {
  name: string
  code: string
  median: number
  iqr: number
  unit: string
  isInverted: boolean
  description: string
  sampleValue: number
}

const metricProfiles: Record<string, MetricProfile> = {
  opMargin: {
    name: 'Operating Margin',
    code: 'OP_MARGIN',
    median: 18.0,
    iqr: 12.0,
    unit: '%',
    isInverted: false,
    description: 'Core operational profitability before interest and taxes',
    sampleValue: 24.0,
  },
  roe: {
    name: 'Return on Equity (ROE)',
    code: 'ROE',
    median: 15.0,
    iqr: 10.0,
    unit: '%',
    isInverted: false,
    description: 'Net income return generated on shareholders equity base',
    sampleValue: 21.5,
  },
  debtEquity: {
    name: 'Debt-to-Equity',
    code: 'DEBT_EQUITY',
    median: 0.80,
    iqr: 0.60,
    unit: 'x',
    isInverted: true,
    description: 'Capital structure gearing; lower debt rewards higher solvency score',
    sampleValue: 0.35,
  },
  interestCoverage: {
    name: 'Interest Coverage',
    code: 'INT_COVERAGE',
    median: 5.50,
    iqr: 4.20,
    unit: 'x',
    isInverted: false,
    description: 'EBIT multiples of annual finance costs; solvency safety buffer',
    sampleValue: 8.40,
  },
  currentRatio: {
    name: 'Current Ratio',
    code: 'CURRENT_RATIO',
    median: 1.60,
    iqr: 0.80,
    unit: 'x',
    isInverted: false,
    description: 'Short-term liquidity buffer for working capital obligations',
    sampleValue: 2.10,
  },
}

// Active State
const activeMetricKey = ref<string>('opMargin')
const kappa = ref<number>(1.386) // Calibrated default
const customValue = ref<number>(24.0)
const overrideInvert = ref<boolean | null>(null)

// Current active profile
const activeProfile = computed(() => metricProfiles[activeMetricKey.value])

// Effective inversion state
const isInverted = computed(() => {
  if (overrideInvert.value !== null) return overrideInvert.value
  return activeProfile.value.isInverted
})

// Normalized Quartile Distance: z = (x - Med) / IQR
const normalizedZ = computed(() => {
  const diff = customValue.value - activeProfile.value.median
  return diff / (activeProfile.value.iqr || 0.001)
})

// Sigmoid Score S(x) in [0, 100]
const rawSigmoidScore = computed(() => {
  const z = normalizedZ.value
  const k = kappa.value
  const s = 100 / (1 + Math.exp(-k * z))
  return s
})

// Directional Score (handling inverted solvency ratios)
const finalScore = computed(() => {
  if (isInverted.value) {
    return 100 - rawSigmoidScore.value
  }
  return rawSigmoidScore.value
})

// Score Tier Styling
const scoreTier = computed(() => {
  const s = finalScore.value
  if (s >= 80) return { label: 'EXCELLENT', color: '#34D399', badge: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50' }
  if (s >= 65) return { label: 'STRONG', color: '#10B981', badge: 'bg-teal-500/20 text-teal-300 border-teal-500/50' }
  if (s >= 50) return { label: 'MODERATE', color: '#059669', badge: 'bg-emerald-600/20 text-emerald-300 border-emerald-600/50' }
  if (s >= 35) return { label: 'WEAK', color: '#F59E0B', badge: 'bg-amber-500/20 text-amber-300 border-amber-500/50' }
  return { label: 'DISTRESSED', color: '#F43F5E', badge: 'bg-rose-500/20 text-rose-300 border-rose-500/50' }
})

// Switch Metric
function setMetric(key: string) {
  activeMetricKey.value = key
  customValue.value = metricProfiles[key].sampleValue
  overrideInvert.value = null
}

// Reset Kappa to Calibrated Default (1.386)
function resetKappa() {
  kappa.value = 1.386
}

// Jump to Quartile Preset Values
function jumpToQuartile(type: 'q1' | 'med' | 'q3' | 'outlier') {
  const prof = activeProfile.value
  if (type === 'q1') {
    customValue.value = Number((prof.median - 0.5 * prof.iqr).toFixed(2))
  } else if (type === 'med') {
    customValue.value = Number(prof.median.toFixed(2))
  } else if (type === 'q3') {
    customValue.value = Number((prof.median + 0.5 * prof.iqr).toFixed(2))
  } else if (type === 'outlier') {
    customValue.value = Number((prof.median + 2.5 * prof.iqr).toFixed(2))
  }
}

// ==========================================
// SVG Coordinate Mapping for Sigmoid Plot
// ==========================================
// SVG Dimensions
const svgW = 480
const svgH = 220
const padL = 46
const padR = 24
const padT = 20
const padB = 35

const plotW = svgW - padL - padR
const plotH = svgH - padT - padB

// z domain: [-3.5, +3.5]
const zMin = -3.5
const zMax = 3.5

function zToSvgX(z: number): number {
  const clamped = Math.max(zMin, Math.min(zMax, z))
  return padL + ((clamped - zMin) / (zMax - zMin)) * plotW
}

function scoreToSvgY(score: number): number {
  const clamped = Math.max(0, Math.min(100, score))
  return padT + plotH - (clamped / 100) * plotH
}

// Generate S-Curve SVG Path
const sigmoidPath = computed(() => {
  const points: string[] = []
  const steps = 90
  const k = kappa.value
  const inverted = isInverted.value

  for (let i = 0; i <= steps; i++) {
    const z = zMin + (i / steps) * (zMax - zMin)
    let s = 100 / (1 + Math.exp(-k * z))
    if (inverted) s = 100 - s
    const x = zToSvgX(z)
    const y = scoreToSvgY(s)
    points.push(`${i === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)}`)
  }
  return points.join(' ')
})

// Generate S-Curve Shaded Area Path
const sigmoidAreaPath = computed(() => {
  const baseCurve = sigmoidPath.value
  const botRightX = zToSvgX(zMax)
  const botLeftX = zToSvgX(zMin)
  const botY = scoreToSvgY(0)
  return `${baseCurve} L ${botRightX.toFixed(1)} ${botY.toFixed(1)} L ${botLeftX.toFixed(1)} ${botY.toFixed(1)} Z`
})

// Key Reference Coordinates
const q1Coord = computed(() => {
  const z = -0.5
  let s = 100 / (1 + Math.exp(-kappa.value * z))
  if (isInverted.value) s = 100 - s
  return { x: zToSvgX(z), y: scoreToSvgY(s), s }
})

const medCoord = computed(() => {
  const z = 0.0
  let s = 100 / (1 + Math.exp(-kappa.value * z))
  if (isInverted.value) s = 100 - s
  return { x: zToSvgX(z), y: scoreToSvgY(s), s }
})

const q3Coord = computed(() => {
  const z = 0.5
  let s = 100 / (1 + Math.exp(-kappa.value * z))
  if (isInverted.value) s = 100 - s
  return { x: zToSvgX(z), y: scoreToSvgY(s), s }
})

const probeCoord = computed(() => {
  return {
    x: zToSvgX(normalizedZ.value),
    y: scoreToSvgY(finalScore.value),
  }
})

// ==========================================
// Dynamic NaN Missing-Data Redistribution
// ==========================================
interface PillarMetricItem {
  id: string
  name: string
  baseWeight: number
  active: boolean
  rawScore: number
}

const pillarMetrics = ref<PillarMetricItem[]>([
  { id: 'm1', name: 'Operating Margin', baseWeight: 0.35, active: true, rawScore: 78.4 },
  { id: 'm2', name: 'Return on Equity (ROE)', baseWeight: 0.30, active: true, rawScore: 72.0 },
  { id: 'm3', name: 'EBITDA Margin', baseWeight: 0.20, active: true, rawScore: 66.5 },
  { id: 'm4', name: 'R&D / Revenue', baseWeight: 0.15, active: false, rawScore: 50.0 }, // Omitted disclosure
])

// Sum of valid weights
const validBaseSum = computed(() => {
  return pillarMetrics.value.reduce((acc, m) => acc + (m.active ? m.baseWeight : 0), 0)
})

// Dynamic renormalized weights w'_i = w_i / sum_{j in V} w_j
const renormalizedWeights = computed(() => {
  const sum = validBaseSum.value || 0.0001
  return pillarMetrics.value.map(m => {
    const reweighted = m.active ? m.baseWeight / sum : 0
    return {
      ...m,
      reweighted,
      pctDisplay: (reweighted * 100).toFixed(1),
      weightedContribution: (reweighted * m.rawScore).toFixed(1),
    }
  })
})

// Renormalized Pillar Score
const renormalizedPillarScore = computed(() => {
  return renormalizedWeights.value.reduce((acc, m) => acc + (m.active ? m.reweighted * m.rawScore : 0), 0)
})

// Naive Unnormalized Pillar Score (penalizing missing metrics as 0)
const naivePillarScore = computed(() => {
  return pillarMetrics.value.reduce((acc, m) => acc + (m.active ? m.baseWeight * m.rawScore : 0), 0)
})

function togglePillarMetric(id: string) {
  const target = pillarMetrics.value.find(m => m.id === id)
  if (target) {
    // Prevent unchecking all items
    const activeCount = pillarMetrics.value.filter(m => m.active).length
    if (activeCount === 1 && target.active) return
    target.active = !target.active
  }
}
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Action & Metric Selector Bar -->
    <div class="flex items-center justify-between gap-2 bg-[#071411]/90 px-3 py-1.5 rounded-xl border border-emerald-500/20 mb-2">
      <!-- Metric Selector Pills -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Metric:
        </span>
        <button
          v-for="(prof, key) in metricProfiles"
          :key="key"
          @click="setMetric(key)"
          class="px-2 py-0.8 rounded-lg text-[10px] font-semibold font-mono transition-all border flex items-center gap-1"
          :class="activeMetricKey === key
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 shadow-[0_0_12px_rgba(52,211,153,0.30)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40 hover:text-slate-200'"
        >
          <span>{{ prof.name }}</span>
          <span v-if="prof.isInverted" class="text-[8px] px-1 py-0.2 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40">INV</span>
        </button>
      </div>

      <!-- Inversion Toggle & Live Score Pill -->
      <div class="flex items-center gap-2">
        <button
          @click="overrideInvert = !isInverted"
          class="px-2 py-0.8 rounded text-[9.5px] font-mono border transition-all flex items-center gap-1"
          :class="isInverted
            ? 'bg-amber-500/20 text-amber-300 border-amber-500/50'
            : 'bg-emerald-500/15 text-emerald-300 border-emerald-500/35'"
          title="Toggle Directional Inversion (e.g. for Debt/Solvency metrics)"
        >
          <span>{{ isInverted ? 'Direction: Inverted (Lower is Better)' : 'Direction: Standard (Higher is Better)' }}</span>
        </button>

        <div class="flex items-center gap-1.5 px-2 py-0.8 rounded-lg bg-[#071411] border border-emerald-500/30">
          <span class="text-[9px] font-mono text-slate-400">Score S(x):</span>
          <span class="text-sm font-extrabold font-mono" :style="{ color: scoreTier.color }">
            {{ finalScore.toFixed(1) }}
          </span>
          <span class="text-[8px] font-bold px-1 py-0.2 rounded uppercase" :class="scoreTier.badge">
            {{ scoreTier.label }}
          </span>
        </div>
      </div>
    </div>

    <!-- Main Grid: Left Plot (7 Col) vs Right Mathematical & NaN Normalization Cards (5 Col) -->
    <div class="grid grid-cols-12 gap-2.5 mb-2">
      <!-- LEFT COLUMN: Interactive Sigmoid S-Curve SVG Plot -->
      <div class="col-span-7 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Plot Header -->
          <div class="flex items-center justify-between pb-1 mb-1 border-b border-emerald-500/15">
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-white font-mono flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#34D399]"></span>
                Calibrated Sigmoid Response Curve
              </span>
              <span class="text-[9px] font-mono text-emerald-400/90">
                κ = {{ kappa.toFixed(3) }}
              </span>
            </div>
            <!-- Quick Quartile Jump Buttons -->
            <div class="flex items-center gap-1">
              <span class="text-[8.5px] text-slate-400 font-mono">Anchor:</span>
              <button
                @click="jumpToQuartile('q1')"
                class="px-1.5 py-0.2 text-[8px] font-mono rounded bg-amber-500/15 text-amber-300 hover:bg-amber-500/30 border border-amber-500/30"
              >
                Q₁ (35)
              </button>
              <button
                @click="jumpToQuartile('med')"
                class="px-1.5 py-0.2 text-[8px] font-mono rounded bg-emerald-500/15 text-emerald-300 hover:bg-emerald-500/30 border border-emerald-500/30"
              >
                Med (50)
              </button>
              <button
                @click="jumpToQuartile('q3')"
                class="px-1.5 py-0.2 text-[8px] font-mono rounded bg-teal-500/15 text-teal-300 hover:bg-teal-500/30 border border-teal-500/30"
              >
                Q₃ (65)
              </button>
              <button
                @click="jumpToQuartile('outlier')"
                class="px-1.5 py-0.2 text-[8px] font-mono rounded bg-rose-500/15 text-rose-300 hover:bg-rose-500/30 border border-rose-500/30"
              >
                Outlier
              </button>
            </div>
          </div>

          <!-- SVG Plot Stage -->
          <div class="relative bg-[#071411]/95 rounded-lg border border-emerald-500/20 overflow-hidden py-1">
            <svg class="w-full h-44" viewBox="0 0 480 220" preserveAspectRatio="xMidYMid meet">
              <defs>
                <!-- Glowing Mint Filter -->
                <filter id="glowMintCurve" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="3" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
                <!-- Glowing Point Filter -->
                <filter id="glowPoint" x="-50%" y="-50%" width="200%" height="200%">
                  <feGaussianBlur stdDeviation="4" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
                <!-- Linear Gradient for Curve Stroke -->
                <linearGradient id="curveGradient" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#F43F5E" />
                  <stop offset="35%" stop-color="#F59E0B" />
                  <stop offset="50%" stop-color="#10B981" />
                  <stop offset="70%" stop-color="#34D399" />
                  <stop offset="100%" stop-color="#00E599" />
                </linearGradient>
                <!-- Area Fill Gradient -->
                <linearGradient id="curveAreaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="rgba(52, 211, 153, 0.22)" />
                  <stop offset="60%" stop-color="rgba(16, 185, 129, 0.08)" />
                  <stop offset="100%" stop-color="rgba(7, 20, 17, 0.0)" />
                </linearGradient>
              </defs>

              <!-- Coordinate Grid Lines -->
              <!-- Upper Asymptote (S = 100) -->
              <line
                :x1="padL" :y1="scoreToSvgY(100)"
                :x2="svgW - padR" :y2="scoreToSvgY(100)"
                stroke="#64748B" stroke-width="0.8" stroke-dasharray="3,3" opacity="0.6"
              />
              <text :x="padL - 6" :y="scoreToSvgY(100) + 3" text-anchor="end" fill="#94A3B8" font-size="8" font-family="monospace">100</text>
              <text :x="svgW - padR + 4" :y="scoreToSvgY(100) + 3" text-anchor="start" fill="#64748B" font-size="7.5" font-family="monospace">Asymptote</text>

              <!-- Score 65 Line (Q3) -->
              <line
                :x1="padL" :y1="scoreToSvgY(65)"
                :x2="svgW - padR" :y2="scoreToSvgY(65)"
                stroke="rgba(52, 211, 153, 0.25)" stroke-width="0.6" stroke-dasharray="2,3"
              />
              <text :x="padL - 6" :y="scoreToSvgY(65) + 3" text-anchor="end" fill="#34D399" font-size="8" font-family="monospace">65</text>

              <!-- Score 50 Line (Median) -->
              <line
                :x1="padL" :y1="scoreToSvgY(50)"
                :x2="svgW - padR" :y2="scoreToSvgY(50)"
                stroke="rgba(52, 211, 153, 0.45)" stroke-width="0.8" stroke-dasharray="3,3"
              />
              <text :x="padL - 6" :y="scoreToSvgY(50) + 3" text-anchor="end" fill="#34D399" font-size="8.5" font-weight="bold" font-family="monospace">50</text>

              <!-- Score 35 Line (Q1) -->
              <line
                :x1="padL" :y1="scoreToSvgY(35)"
                :x2="svgW - padR" :y2="scoreToSvgY(35)"
                stroke="rgba(245, 158, 11, 0.25)" stroke-width="0.6" stroke-dasharray="2,3"
              />
              <text :x="padL - 6" :y="scoreToSvgY(35) + 3" text-anchor="end" fill="#F59E0B" font-size="8" font-family="monospace">35</text>

              <!-- Lower Asymptote (S = 0) -->
              <line
                :x1="padL" :y1="scoreToSvgY(0)"
                :x2="svgW - padR" :y2="scoreToSvgY(0)"
                stroke="#64748B" stroke-width="0.8" opacity="0.7"
              />
              <text :x="padL - 6" :y="scoreToSvgY(0) + 3" text-anchor="end" fill="#94A3B8" font-size="8" font-family="monospace">0</text>

              <!-- Vertical Reference Axes -->
              <!-- z = 0 (Median) -->
              <line
                :x1="zToSvgX(0)" :y1="padT"
                :x2="zToSvgX(0)" :y2="svgH - padB"
                stroke="rgba(52, 211, 153, 0.35)" stroke-width="0.8" stroke-dasharray="3,3"
              />
              <text :x="zToSvgX(0)" :y="svgH - padB + 12" text-anchor="middle" fill="#34D399" font-size="8" font-weight="bold" font-family="monospace">Med (0)</text>

              <!-- z = -0.5 (Q1) -->
              <line
                :x1="zToSvgX(-0.5)" :y1="padT"
                :x2="zToSvgX(-0.5)" :y2="svgH - padB"
                stroke="rgba(245, 158, 11, 0.30)" stroke-width="0.6" stroke-dasharray="2,3"
              />
              <text :x="zToSvgX(-0.5)" :y="svgH - padB + 12" text-anchor="middle" fill="#F59E0B" font-size="7.5" font-family="monospace">Q₁ (-0.5)</text>

              <!-- z = +0.5 (Q3) -->
              <line
                :x1="zToSvgX(0.5)" :y1="padT"
                :x2="zToSvgX(0.5)" :y2="svgH - padB"
                stroke="rgba(52, 211, 153, 0.30)" stroke-width="0.6" stroke-dasharray="2,3"
              />
              <text :x="zToSvgX(0.5)" :y="svgH - padB + 12" text-anchor="middle" fill="#10B981" font-size="7.5" font-family="monospace">Q₃ (+0.5)</text>

              <!-- z = -2.0 and +2.0 -->
              <text :x="zToSvgX(-2)" :y="svgH - padB + 12" text-anchor="middle" fill="#64748B" font-size="7" font-family="monospace">-2.0</text>
              <text :x="zToSvgX(2)" :y="svgH - padB + 12" text-anchor="middle" fill="#64748B" font-size="7" font-family="monospace">+2.0</text>

              <!-- X Axis Label -->
              <text :x="svgW / 2 + 15" :y="svgH - 6" text-anchor="middle" fill="#94A3B8" font-size="8" font-family="monospace">
                Normalized Quartile Metric: z = (x - Med) / IQR
              </text>

              <!-- Shaded Area Under Sigmoid -->
              <path :d="sigmoidAreaPath" fill="url(#curveAreaGradient)" />

              <!-- Main Calibrated Sigmoid Curve -->
              <path
                :d="sigmoidPath"
                fill="none"
                stroke="url(#curveGradient)"
                stroke-width="2.6"
                stroke-linecap="round"
                stroke-linejoin="round"
                filter="url(#glowMintCurve)"
              />

              <!-- ANCHOR POINT 1: Q1 -->
              <g :transform="`translate(${q1Coord.x}, ${q1Coord.y})`">
                <circle r="4" fill="#F59E0B" stroke="#071411" stroke-width="1.5" />
                <rect x="5" y="-14" width="46" height="13" rx="3" fill="#071411" stroke="#F59E0B" stroke-width="0.8" />
                <text x="28" y="-5" text-anchor="middle" fill="#F59E0B" font-size="7" font-weight="bold" font-family="monospace">Q₁ ➔ 35</text>
              </g>

              <!-- ANCHOR POINT 2: Median -->
              <g :transform="`translate(${medCoord.x}, ${medCoord.y})`">
                <circle r="4.5" fill="#34D399" stroke="#071411" stroke-width="1.5" />
                <rect x="6" y="-14" width="52" height="13" rx="3" fill="#071411" stroke="#34D399" stroke-width="0.8" />
                <text x="32" y="-5" text-anchor="middle" fill="#34D399" font-size="7" font-weight="bold" font-family="monospace">Med ➔ 50</text>
              </g>

              <!-- ANCHOR POINT 3: Q3 -->
              <g :transform="`translate(${q3Coord.x}, ${q3Coord.y})`">
                <circle r="4" fill="#10B981" stroke="#071411" stroke-width="1.5" />
                <rect x="5" y="-14" width="46" height="13" rx="3" fill="#071411" stroke="#10B981" stroke-width="0.8" />
                <text x="28" y="-5" text-anchor="middle" fill="#10B981" font-size="7" font-weight="bold" font-family="monospace">Q₃ ➔ 65</text>
              </g>

              <!-- ACTIVE PROBE POINT -->
              <g>
                <!-- Probe Droplines to Axes -->
                <line
                  :x1="probeCoord.x" :y1="probeCoord.y"
                  :x2="probeCoord.x" :y2="svgH - padB"
                  stroke="#00E599" stroke-width="1.2" stroke-dasharray="2,2"
                />
                <line
                  :x1="padL" :y1="probeCoord.y"
                  :x2="probeCoord.x" :y2="probeCoord.y"
                  stroke="#00E599" stroke-width="1.2" stroke-dasharray="2,2"
                />

                <!-- Pulsing Probe Halo -->
                <circle
                  :cx="probeCoord.x"
                  :cy="probeCoord.y"
                  r="7"
                  fill="none"
                  stroke="#00E599"
                  stroke-width="1.5"
                  opacity="0.8"
                  class="animate-ping"
                />
                <circle
                  :cx="probeCoord.x"
                  :cy="probeCoord.y"
                  r="4.5"
                  fill="#00E599"
                  stroke="#071411"
                  stroke-width="1.5"
                  filter="url(#glowPoint)"
                />

                <!-- Probe Dynamic Tooltip Box -->
                <g :transform="`translate(${Math.max(60, Math.min(390, probeCoord.x))}, ${Math.max(30, probeCoord.y - 20)})`">
                  <rect
                    x="-55" y="-12" width="110" height="18" rx="4"
                    fill="#071411" stroke="#00E599" stroke-width="1.2"
                    filter="drop-shadow(0 2px 5px rgba(0,0,0,0.8))"
                  />
                  <text x="0" y="0.5" text-anchor="middle" fill="#F8FAFC" font-size="8" font-family="monospace" font-weight="bold">
                    z = {{ normalizedZ >= 0 ? '+' : '' }}{{ normalizedZ.toFixed(2) }} ➔ S = {{ finalScore.toFixed(1) }}
                  </text>
                </g>
              </g>
            </svg>
          </div>
        </div>

        <!-- Interactive Sliders Under Plot -->
        <div class="mt-2 grid grid-cols-2 gap-2 pt-1.5 border-t border-emerald-500/15 text-[9.5px] font-mono">
          <!-- Slider 1: Input Value x -->
          <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20">
            <div class="flex justify-between items-center mb-0.5">
              <span class="text-slate-400">Raw Input (x):</span>
              <strong class="text-emerald-300">
                {{ customValue.toFixed(2) }} {{ activeProfile.unit }}
              </strong>
            </div>
            <input
              type="range"
              :min="activeProfile.median - 2.5 * activeProfile.iqr"
              :max="activeProfile.median + 3.0 * activeProfile.iqr"
              :step="activeProfile.iqr / 40"
              v-model.number="customValue"
              class="w-full accent-emerald-400 cursor-pointer h-1 bg-slate-700 rounded"
            />
            <div class="flex justify-between text-[7.5px] text-slate-500 mt-0.5">
              <span>Med: {{ activeProfile.median }}{{ activeProfile.unit }}</span>
              <span>IQR: {{ activeProfile.iqr }}{{ activeProfile.unit }}</span>
            </div>
          </div>

          <!-- Slider 2: Kappa (Curvature Parameter) -->
          <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20">
            <div class="flex justify-between items-center mb-0.5">
              <span class="text-slate-400">Curvature (κ):</span>
              <div class="flex items-center gap-1">
                <strong class="text-emerald-300">κ = {{ kappa.toFixed(3) }}</strong>
                <button
                  v-if="kappa !== 1.386"
                  @click="resetKappa"
                  class="text-[7.5px] px-1 py-0.2 rounded bg-emerald-500/20 text-emerald-300 hover:bg-emerald-500/40"
                >
                  Reset
                </button>
              </div>
            </div>
            <input
              type="range"
              min="0.6"
              max="2.5"
              step="0.05"
              v-model.number="kappa"
              class="w-full accent-teal-400 cursor-pointer h-1 bg-slate-700 rounded"
            />
            <div class="flex justify-between text-[7.5px] text-slate-500 mt-0.5">
              <span>Gradual (0.60)</span>
              <span class="text-emerald-400">Calibrated (1.386)</span>
              <span>Steep (2.50)</span>
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Mathematical Formulation & NaN Dynamic Redistribution -->
      <div class="col-span-5 flex flex-col justify-between gap-2">
        <!-- CARD 1: Mathematical Formulation Card -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
              <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
                Sigmoid Transfer Formulation
              </span>
              <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
                Theoretical Model
              </span>
            </div>

            <!-- Mathematical Formula Box -->
            <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/25 font-mono text-[9.5px] text-emerald-200 leading-tight mb-1">
              <div class="text-emerald-300 font-semibold">
                S(xᵢ) = 100 / [ 1 + exp( -κ · (xᵢ - Med) / IQR ) ]
              </div>
              <div class="text-[8px] text-amber-300/90 mt-0.5">
                Inverted Solvency: S_inv(xᵢ) = 100 - S(xᵢ)
              </div>
            </div>

            <!-- Structured Where: Parameter Block -->
            <div class="text-[8px] leading-tight text-slate-300 bg-[#071411]/50 p-1.5 rounded border border-emerald-500/10">
              <div class="font-bold text-emerald-400 font-mono mb-0.5">Where:</div>
              <ul class="space-y-0.5 text-slate-400 font-mono">
                <li><strong class="text-white font-mono">xᵢ:</strong> Raw financial ratio for enterprise i</li>
                <li><strong class="text-white font-mono">Med:</strong> Sector robust median anchor point (50.0 pts)</li>
                <li><strong class="text-white font-mono">IQR:</strong> Interquartile dispersion scale (Q₃ - Q₁)</li>
                <li><strong class="text-white font-mono">κ ≈ 1.386:</strong> Calibrated curvature anchoring Q₁ ➔ 35, Q₃ ➔ 65</li>
                <li><strong class="text-white font-mono">[0, 100]:</strong> Asymptotically bounded saturation eliminate outlier distortion</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- CARD 2: Dynamic Missing-Data (NaN) Redistribution Simulator -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
              <span class="text-[10px] font-bold text-teal-300 uppercase tracking-wider font-mono">
                Dynamic Missing-Data Redistribution
              </span>
              <span class="text-[8px] px-1 py-0.2 bg-teal-500/15 text-teal-300 rounded font-mono">
                NaN Invariance
              </span>
            </div>

            <!-- Theory Callout -->
            <p class="text-[8px] text-slate-400 mb-1 leading-tight">
              Omitted line items (e.g. debt-free interest or tech R&amp;D) dynamically renormalize remaining reported metrics to preserve a strict 100-point scale:
            </p>

            <!-- Dynamic Redistribution Formula -->
            <div class="bg-[#071411]/90 px-1.5 py-1 rounded border border-teal-500/25 font-mono text-[9px] text-teal-200 leading-tight mb-1.5 flex justify-between items-center">
              <span>w'_{k,i} = w_{k,i} / ∑_{j ∈ 𝒱_k} w_{k,j}</span>
              <span class="text-[8px] text-emerald-400">∑ w'_{k,i} = 100.0%</span>
            </div>

            <!-- Interactive Metric Checklist Simulator -->
            <div class="space-y-1 mb-1.5">
              <div
                v-for="item in renormalizedWeights"
                :key="item.id"
                @click="togglePillarMetric(item.id)"
                class="flex items-center justify-between p-1 rounded border transition-all cursor-pointer font-mono text-[8.5px]"
                :class="item.active
                  ? 'bg-[#0d211b]/80 border-emerald-500/35 text-slate-200'
                  : 'bg-slate-900/40 border-slate-700/40 text-slate-500 line-through opacity-60'"
              >
                <div class="flex items-center gap-1.5">
                  <span
                    class="w-3 h-3 rounded flex items-center justify-center text-[7.5px] border"
                    :class="item.active ? 'bg-emerald-500/30 border-emerald-400 text-emerald-300' : 'bg-slate-800 border-slate-600 text-transparent'"
                  >
                    ✓
                  </span>
                  <span>{{ item.name }}</span>
                </div>

                <div class="flex items-center gap-2">
                  <span class="text-[7.5px] text-slate-400">
                    Base: {{ (item.baseWeight * 100).toFixed(0) }}%
                  </span>
                  <span
                    class="font-bold px-1 py-0.2 rounded text-[8px]"
                    :class="item.active ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-slate-800 text-slate-600'"
                  >
                    w' = {{ item.pctDisplay }}%
                  </span>
                </div>
              </div>
            </div>

            <!-- Score Comparison: Renormalized vs Naive Penalty -->
            <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20 text-[8.5px] font-mono">
              <div class="flex justify-between items-center">
                <span class="text-slate-400">Renormalized Pillar Score:</span>
                <strong class="text-emerald-300 text-[10px]">
                  {{ renormalizedPillarScore.toFixed(1) }} / 100.0
                </strong>
              </div>
              <div class="flex justify-between items-center text-slate-500 text-[7.5px] mt-0.5">
                <span>Naive Penalty Score (Un-normalized):</span>
                <span class="text-rose-400 line-through">{{ naivePillarScore.toFixed(1) }} pts</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Bar -->
    <div class="glass-card px-3 py-1 flex items-center justify-between text-[9px] font-mono">
      <div class="flex items-center gap-2 text-slate-300">
        <span class="text-emerald-400 font-bold">Bounded Saturation Guarantee:</span>
        <span class="text-slate-400">
          Heavy tails smoothly compress into asymptotes [0, 100] without parametric collapse, while NaN redistribution ensures debt-free and asset-light firms are evaluated objectively.
        </span>
      </div>
      <span class="text-emerald-300 text-[8px] bg-emerald-500/10 border border-emerald-500/25 px-1.5 py-0.5 rounded">
        Slide 12: Sigmoid Benchmark
      </span>
    </div>
  </div>
</template>

<style scoped>
/* Glassmorphism card utilities */
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
