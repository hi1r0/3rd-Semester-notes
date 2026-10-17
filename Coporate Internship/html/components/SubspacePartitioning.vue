<script setup lang="ts">
import { ref, computed } from 'vue'

// --- 2D Dataset: Financial Ratio Subspace ---
// Dimension X: Operating Margin (-20% to +50%)
// Dimension Y: Operating Cash Flow / Total Assets (-25% to +35%)
interface DataPoint {
  id: string
  name: string
  margin: number // x in percent
  ocfAssets: number // y in percent
  isOutlier: boolean
  isTargetPeer?: boolean
}

// 32 Normal Peers tightly clustered in profitable cash-generative space
const peerCluster: DataPoint[] = [
  { id: 'TCS', name: 'TCS Ltd', margin: 25.2, ocfAssets: 19.4, isOutlier: false, isTargetPeer: true },
  { id: 'INFY', name: 'Infosys Ltd', margin: 21.4, ocfAssets: 16.5, isOutlier: false },
  { id: 'HCLTECH', name: 'HCL Tech', margin: 18.6, ocfAssets: 14.2, isOutlier: false },
  { id: 'WIPRO', name: 'Wipro', margin: 16.2, ocfAssets: 12.0, isOutlier: false },
  { id: 'LTIM', name: 'LTIMindtree', margin: 17.5, ocfAssets: 15.1, isOutlier: false },
  { id: 'TECHM', name: 'Tech Mahindra', margin: 12.8, ocfAssets: 9.8, isOutlier: false },
  { id: 'PERSISTENT', name: 'Persistent', margin: 15.2, ocfAssets: 14.0, isOutlier: false },
  { id: 'COFORGE', name: 'Coforge', margin: 17.8, ocfAssets: 15.3, isOutlier: false },
  { id: 'MPHASIS', name: 'Mphasis', margin: 15.4, ocfAssets: 13.2, isOutlier: false },
  { id: 'TATAELXSI', name: 'Tata Elxsi', margin: 28.4, ocfAssets: 21.5, isOutlier: false },
  { id: 'KPIT', name: 'KPIT Tech', margin: 20.1, ocfAssets: 16.8, isOutlier: false },
  { id: 'CYIENT', name: 'Cyient', margin: 16.0, ocfAssets: 11.5, isOutlier: false },
  { id: 'ZENSAR', name: 'Zensar', margin: 14.8, ocfAssets: 12.4, isOutlier: false },
  { id: 'BIRLA', name: 'Birlasoft', margin: 15.7, ocfAssets: 13.0, isOutlier: false },
  { id: 'LTTS', name: 'L&T Tech', margin: 17.1, ocfAssets: 14.8, isOutlier: false },
  { id: 'SONATA', name: 'Sonata Soft', margin: 24.0, ocfAssets: 18.2, isOutlier: false },
  { id: 'HAPPSTMNDS', name: 'Happiest Minds', margin: 18.0, ocfAssets: 15.0, isOutlier: false },
  { id: 'INTELLECT', name: 'Intellect', margin: 21.5, ocfAssets: 16.2, isOutlier: false },
  { id: 'RATEGAIN', name: 'RateGain', margin: 19.8, ocfAssets: 17.1, isOutlier: false },
  { id: 'NEWGEN', name: 'Newgen', margin: 20.5, ocfAssets: 16.0, isOutlier: false },
  { id: 'TANLA', name: 'Tanla', margin: 22.3, ocfAssets: 18.0, isOutlier: false },
  { id: 'BSOSOFT', name: 'BSE Soft', margin: 14.2, ocfAssets: 10.5, isOutlier: false },
  { id: 'KAYNES', name: 'Kaynes', margin: 13.5, ocfAssets: 11.2, isOutlier: false },
  { id: 'DATAPATT', name: 'Data Patterns', margin: 26.5, ocfAssets: 19.8, isOutlier: false },
  { id: 'LATENT', name: 'LatentView', margin: 23.1, ocfAssets: 17.5, isOutlier: false },
  { id: 'NETWEB', name: 'Netweb Tech', margin: 15.9, ocfAssets: 12.8, isOutlier: false },
  { id: 'PEER_A', name: 'Peer Group A', margin: 19.0, ocfAssets: 14.5, isOutlier: false },
  { id: 'PEER_B', name: 'Peer Group B', margin: 22.0, ocfAssets: 15.8, isOutlier: false },
  { id: 'PEER_C', name: 'Peer Group C', margin: 16.8, ocfAssets: 13.5, isOutlier: false },
  { id: 'PEER_D', name: 'Peer Group D', margin: 24.5, ocfAssets: 20.1, isOutlier: false },
  // Noise point in lower region
  { id: 'CYCLIC_NOISE', name: 'Distressed Asset', margin: -5.0, ocfAssets: -14.0, isOutlier: false },
]

// Single severe anomaly in sparse periphery
const outlierPoint: DataPoint = {
  id: 'ROGUE_CORP',
  name: 'ROGUE_TECH (Aggressive Revenue Trap)',
  margin: 44.0, // High operating margin
  ocfAssets: -18.0, // Negative operating cash flow
  isOutlier: true,
}

const allPoints = [...peerCluster, outlierPoint]

// Coordinate System Bounds: X: [-20, 50], Y: [-25, 35]
// SVG Canvas: width=420, height=230, plot area: left=35, top=15, width=370, height=195
const plotLeft = 35
const plotTop = 15
const plotWidth = 370
const plotHeight = 195

function toSvgX(val: number): number {
  return plotLeft + ((val - (-20)) / (50 - (-20))) * plotWidth
}

function toSvgY(val: number): number {
  return plotTop + ((35 - val) / (35 - (-25))) * plotHeight
}

// Partition Hyperplanes Definition (Progressive Cuts 1 to 8)
interface HyperplaneCut {
  id: number
  axis: 'x' | 'y'
  value: number // in ratio unit
  label: string
  subspaceScope: { xMin: number; xMax: number; yMin: number; yMax: number }
  description: string
  isolatesOutlier: boolean
}

const hyperplaneCuts: HyperplaneCut[] = [
  {
    id: 1,
    axis: 'y',
    value: -6.0,
    label: 'Cut 1 (Horizontal): OCF/Assets = -6.0%',
    subspaceScope: { xMin: -20, xMax: 50, yMin: -25, yMax: 35 },
    description: 'First random hyperplane slices along OCF/Assets at -6.0%. Separates sparse cash-negative space (2 firms) from dense peer cluster (31 firms).',
    isolatesOutlier: false,
  },
  {
    id: 2,
    axis: 'x',
    value: 30.0,
    label: 'Cut 2 (Vertical): Margin = +30.0%',
    subspaceScope: { xMin: -20, xMax: 50, yMin: -25, yMax: -6.0 },
    description: 'Second random hyperplane bisects lower quadrant along Margin at +30.0%. ROGUE_TECH is completely isolated into a solitary cell at h = 2!',
    isolatesOutlier: true,
  },
  {
    id: 3,
    axis: 'x',
    value: 20.0,
    label: 'Cut 3 (Vertical): Margin = +20.0%',
    subspaceScope: { xMin: -20, xMax: 50, yMin: -6.0, yMax: 35 },
    description: 'Bisects upper cluster into sub-cohorts [Margin < 20%] (14 firms) and [Margin >= 20%] (17 firms). High density persists.',
    isolatesOutlier: false,
  },
  {
    id: 4,
    axis: 'y',
    value: 15.0,
    label: 'Cut 4 (Horizontal): OCF/Assets = +15.0%',
    subspaceScope: { xMin: 20.0, xMax: 50, yMin: -6.0, yMax: 35 },
    description: 'Bisects upper-right cohort into cells with 9 and 8 peers. Nominal firms remain shielded in dense neighborhood.',
    isolatesOutlier: false,
  },
  {
    id: 5,
    axis: 'x',
    value: 16.0,
    label: 'Cut 5 (Vertical): Margin = +16.0%',
    subspaceScope: { xMin: -20, xMax: 20.0, yMin: -6.0, yMax: 35 },
    description: 'Fifth bisection subdivides mid-cap cluster. 7 peers remain grouped together.',
    isolatesOutlier: false,
  },
  {
    id: 6,
    axis: 'y',
    value: 18.0,
    label: 'Cut 6 (Horizontal): OCF/Assets = +18.0%',
    subspaceScope: { xMin: 20.0, xMax: 50, yMin: 15.0, yMax: 35 },
    description: 'Sixth bisection in Tier-1 IT core. TCS still shares cell with 3 peers (INFY, TATAELXSI, SONATA).',
    isolatesOutlier: false,
  },
  {
    id: 7,
    axis: 'x',
    value: 26.0,
    label: 'Cut 7 (Vertical): Margin = +26.0%',
    subspaceScope: { xMin: 20.0, xMax: 50, yMin: 18.0, yMax: 35 },
    description: 'Seventh cut separates TATAELXSI (Margin 28.4%). TCS and INFY remain together.',
    isolatesOutlier: false,
  },
  {
    id: 8,
    axis: 'x',
    value: 23.0,
    label: 'Cut 8 (Vertical): Margin = +23.0%',
    subspaceScope: { xMin: 20.0, xMax: 26.0, yMin: 18.0, yMax: 35 },
    description: 'Eighth bisection finally isolates TCS at h = 8! Dense cluster points require 4x more hyperplanes to be isolated than outliers.',
    isolatesOutlier: false,
  },
]

// Interactive Cut State
const activeCutStep = ref<number>(2) // default shows Cut 2 where outlier is isolated
const isAutoRunning = ref<boolean>(false)
const hoveredPoint = ref<DataPoint | null>(null)

// Step Control
function nextCut() {
  if (activeCutStep.value < 8) {
    activeCutStep.value++
  }
}

function prevCut() {
  if (activeCutStep.value > 0) {
    activeCutStep.value--
  }
}

function resetCuts() {
  activeCutStep.value = 0
}

function setToStep(step: number) {
  activeCutStep.value = step
}

// Auto-play timer
let autoTimer: any = null
function toggleAuto() {
  if (isAutoRunning.value) {
    clearInterval(autoTimer)
    isAutoRunning.value = false
  } else {
    isAutoRunning.value = true
    if (activeCutStep.value >= 8) activeCutStep.value = 0
    autoTimer = setInterval(() => {
      if (activeCutStep.value < 8) {
        activeCutStep.value++
      } else {
        clearInterval(autoTimer)
        isAutoRunning.value = false
      }
    }, 1100)
  }
}

// Current cuts applied up to activeCutStep
const currentCuts = computed(() => {
  return hyperplaneCuts.slice(0, activeCutStep.value)
})

// Current Status Description
const currentCutInfo = computed(() => {
  if (activeCutStep.value === 0) {
    return {
      title: 'Initial Subspace (h = 0)',
      detail: 'Whole ℝ² subspace unpartitioned. 32 nominal peer firms cluster tightly, while ROGUE_TECH sits isolated in sparse bottom-right periphery.',
      outlierIsolated: false,
      tcsIsolated: false,
    }
  }
  const last = hyperplaneCuts[activeCutStep.value - 1]
  return {
    title: last.label,
    detail: last.description,
    outlierIsolated: activeCutStep.value >= 2,
    tcsIsolated: activeCutStep.value >= 8,
  }
})
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Control Bar -->
    <div class="flex items-center justify-between gap-3 bg-[#071411]/90 p-2 rounded-xl border border-emerald-500/20 mb-2">
      <!-- Step Controls -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Partition Cut:
        </span>
        <button
          v-for="step in [0, 1, 2, 3, 4, 6, 8]"
          :key="step"
          @click="setToStep(step)"
          class="px-2 py-0.5 rounded text-[10px] font-mono font-semibold transition-all border"
          :class="activeCutStep === step
            ? step === 2
              ? 'bg-rose-500/30 text-rose-300 border-rose-500/60 shadow-[0_0_10px_rgba(244,63,94,0.4)]'
              : 'bg-emerald-500/30 text-emerald-300 border-emerald-500/60 shadow-[0_0_10px_rgba(52,211,153,0.3)]'
            : 'bg-[#0d211b] text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          {{ step === 0 ? 'Init' : `Cut ${step}` }}
          <span v-if="step === 2" class="text-[8px] text-rose-300 font-bold ml-0.5">★</span>
        </button>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-2">
        <button
          @click="prevCut"
          :disabled="activeCutStep <= 0"
          class="px-2 py-1 rounded text-[10px] font-mono border bg-[#0d211b] text-slate-300 border-emerald-500/20 hover:border-emerald-500/40 disabled:opacity-40"
        >
          ◀ Prev
        </button>

        <button
          @click="nextCut"
          :disabled="activeCutStep >= 8"
          class="px-2 py-1 rounded text-[10px] font-mono font-bold border bg-emerald-500/20 text-emerald-300 border-emerald-500/40 hover:bg-emerald-500/30 disabled:opacity-40"
        >
          Next Cut ▶
        </button>

        <button
          @click="toggleAuto"
          class="px-2.5 py-1 rounded text-[10px] font-mono font-semibold border flex items-center gap-1"
          :class="isAutoRunning ? 'bg-amber-500/25 text-amber-300 border-amber-500/40' : 'bg-teal-500/20 text-teal-300 border-teal-500/30 hover:bg-teal-500/30'"
        >
          <span>{{ isAutoRunning ? '⏸ Pause' : '⚡ Auto-Partition' }}</span>
        </button>

        <button
          @click="resetCuts"
          class="px-2 py-1 rounded text-[10px] font-mono text-slate-400 hover:text-white"
        >
          Reset
        </button>
      </div>
    </div>

    <!-- Main Dual-View Stage: 12-Column Grid -->
    <div class="grid grid-cols-12 gap-2.5 flex-1 min-h-0 mb-2">
      <!-- Left Panel: 2D Coordinate Subspace Cuts (Col 7) -->
      <div class="col-span-7 glass-card p-2.5 flex flex-col justify-between overflow-hidden">
        <div>
          <!-- Panel Header -->
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/20">
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">
                2D Financial Ratio Subspace (ℝ²)
              </span>
              <span
                v-if="currentCutInfo.outlierIsolated"
                class="text-[9px] px-1.5 py-0.2 rounded font-mono font-bold bg-rose-500/20 text-rose-300 border border-rose-500/50 animate-pulse"
              >
                ✓ Outlier Isolated at h=2
              </span>
            </div>
            <div class="text-[9px] font-mono text-slate-400">
              Active Cuts: <strong class="text-white">{{ activeCutStep }}</strong> / 8
            </div>
          </div>

          <!-- 2D Coordinate Space SVG -->
          <div class="w-full bg-[#071411]/90 rounded-lg p-1.5 border border-emerald-500/15 relative">
            <svg viewBox="0 0 420 230" class="w-full h-[180px]">
              <defs>
                <!-- Isolated Outlier Cell Gradient -->
                <radialGradient id="outlierCellGlow" cx="70%" cy="70%" r="60%">
                  <stop offset="0%" stop-color="rgba(244, 63, 94, 0.35)" />
                  <stop offset="100%" stop-color="rgba(244, 63, 94, 0.04)" />
                </radialGradient>
                <filter id="glowPointRose" x="-40%" y="-40%" width="180%" height="180%">
                  <feGaussianBlur stdDeviation="3" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
                <filter id="glowPointMint" x="-40%" y="-40%" width="180%" height="180%">
                  <feGaussianBlur stdDeviation="2.5" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              <!-- Grid Background Lines -->
              <!-- X grid ticks: -10, 0, 10, 20, 30, 40 -->
              <line
                v-for="xVal in [-10, 0, 10, 20, 30, 40]"
                :key="'xgrid_' + xVal"
                :x1="toSvgX(xVal)"
                y1="15"
                :x2="toSvgX(xVal)"
                y2="210"
                stroke="rgba(52, 211, 153, 0.08)"
                stroke-dasharray="2,2"
              />
              <!-- Y grid ticks: -20, -10, 0, 10, 20, 30 -->
              <line
                v-for="yVal in [-20, -10, 0, 10, 20, 30]"
                :key="'ygrid_' + yVal"
                x1="35"
                :y1="toSvgY(yVal)"
                x2="405"
                :y2="toSvgY(yVal)"
                stroke="rgba(52, 211, 153, 0.08)"
                stroke-dasharray="2,2"
              />

              <!-- Axes: Zero Lines -->
              <!-- Zero Margin (x = 0) -->
              <line
                :x1="toSvgX(0)"
                y1="15"
                :x2="toSvgX(0)"
                y2="210"
                stroke="rgba(148, 163, 184, 0.25)"
                stroke-width="1"
              />
              <!-- Zero OCF/Assets (y = 0) -->
              <line
                x1="35"
                :y1="toSvgY(0)"
                x2="405"
                :y2="toSvgY(0)"
                stroke="rgba(148, 163, 184, 0.25)"
                stroke-width="1"
              />

              <!-- HIGHLIGHT ISOLATED CELL: Cut 2 isolates Outlier in [x >= 30%, y <= -6%] -->
              <rect
                v-if="activeCutStep >= 2"
                :x="toSvgX(30.0)"
                :y="toSvgY(-6.0)"
                :width="toSvgX(50.0) - toSvgX(30.0)"
                :height="toSvgY(-25.0) - toSvgY(-6.0)"
                fill="url(#outlierCellGlow)"
                stroke="#FB7185"
                stroke-width="1.5"
                stroke-dasharray="3,3"
                class="transition-all duration-500 animate-pulse"
              />

              <!-- HYPERPLANE PARTITION CUT LINES -->
              <!-- Cut 1: Horizontal at y = -6.0% (across full width) -->
              <g v-if="activeCutStep >= 1">
                <line
                  :x1="toSvgX(-20)"
                  :y1="toSvgY(-6.0)"
                  :x2="toSvgX(50)"
                  :y2="toSvgY(-6.0)"
                  stroke="#38BDF8"
                  stroke-width="2"
                  stroke-dasharray="4,3"
                  class="transition-all duration-300"
                />
                <rect :x="toSvgX(-18)" :y="toSvgY(-6.0) - 8" width="46" height="13" rx="2" fill="#0369A1" opacity="0.9" />
                <text :x="toSvgX(-18) + 23" :y="toSvgY(-6.0) + 1.5" text-anchor="middle" fill="#FFFFFF" font-size="7.5" font-family="monospace" font-weight="bold">
                  Cut 1 (y)
                </text>
              </g>

              <!-- Cut 2: Vertical at x = +30.0% (in lower space y <= -6%) -->
              <g v-if="activeCutStep >= 2">
                <line
                  :x1="toSvgX(30.0)"
                  :y1="toSvgY(-6.0)"
                  :x2="toSvgX(30.0)"
                  :y2="toSvgY(-25.0)"
                  stroke="#FB7185"
                  stroke-width="2"
                  stroke-dasharray="4,3"
                  class="transition-all duration-300"
                />
                <rect :x="toSvgX(30.0) - 22" :y="toSvgY(-16.0)" width="44" height="13" rx="2" fill="#BE123C" opacity="0.9" />
                <text :x="toSvgX(30.0)" :y="toSvgY(-16.0) + 9.5" text-anchor="middle" fill="#FFFFFF" font-size="7.5" font-family="monospace" font-weight="bold">
                  Cut 2 (x)
                </text>
              </g>

              <!-- Cut 3: Vertical at x = +20.0% (in upper space y > -6%) -->
              <g v-if="activeCutStep >= 3">
                <line
                  :x1="toSvgX(20.0)"
                  :y1="toSvgY(35.0)"
                  :x2="toSvgX(20.0)"
                  :y2="toSvgY(-6.0)"
                  stroke="#34D399"
                  stroke-width="1.5"
                  stroke-dasharray="3,3"
                />
                <rect :x="toSvgX(20.0) - 20" :y="toSvgY(32.0)" width="40" height="11" rx="2" fill="#047857" opacity="0.9" />
                <text :x="toSvgX(20.0)" :y="toSvgY(32.0) + 8" text-anchor="middle" fill="#FFFFFF" font-size="7" font-family="monospace">
                  Cut 3
                </text>
              </g>

              <!-- Cut 4: Horizontal at y = +15.0% (for x > 20%) -->
              <g v-if="activeCutStep >= 4">
                <line
                  :x1="toSvgX(20.0)"
                  :y1="toSvgY(15.0)"
                  :x2="toSvgX(50.0)"
                  :y2="toSvgY(15.0)"
                  stroke="#10B981"
                  stroke-width="1.2"
                  stroke-dasharray="3,3"
                />
              </g>

              <!-- Cut 5: Vertical at x = 16.0% (for x < 20%) -->
              <g v-if="activeCutStep >= 5">
                <line
                  :x1="toSvgX(16.0)"
                  :y1="toSvgY(35.0)"
                  :x2="toSvgX(16.0)"
                  :y2="toSvgY(-6.0)"
                  stroke="#10B981"
                  stroke-width="1.2"
                  stroke-dasharray="3,3"
                />
              </g>

              <!-- Cut 6: Horizontal at y = 18.0% (for x in [20, 50], y > 15) -->
              <g v-if="activeCutStep >= 6">
                <line
                  :x1="toSvgX(20.0)"
                  :y1="toSvgY(18.0)"
                  :x2="toSvgX(50.0)"
                  :y2="toSvgY(18.0)"
                  stroke="#059669"
                  stroke-width="1.2"
                  stroke-dasharray="3,3"
                />
              </g>

              <!-- Cut 7: Vertical at x = 26.0% -->
              <g v-if="activeCutStep >= 7">
                <line
                  :x1="toSvgX(26.0)"
                  :y1="toSvgY(35.0)"
                  :x2="toSvgX(26.0)"
                  :y2="toSvgY(18.0)"
                  stroke="#059669"
                  stroke-width="1"
                  stroke-dasharray="2,2"
                />
              </g>

              <!-- Cut 8: Vertical at x = 23.0% (Finally isolates TCS!) -->
              <g v-if="activeCutStep >= 8">
                <line
                  :x1="toSvgX(23.0)"
                  :y1="toSvgY(35.0)"
                  :x2="toSvgX(23.0)"
                  :y2="toSvgY(18.0)"
                  stroke="#FBBF24"
                  stroke-width="1.5"
                  stroke-dasharray="3,3"
                />
                <rect :x="toSvgX(23.0) - 22" :y="toSvgY(25.0)" width="44" height="12" rx="2" fill="#B45309" opacity="0.9" />
                <text :x="toSvgX(23.0)" :y="toSvgY(25.0) + 9" text-anchor="middle" fill="#FFFFFF" font-size="7" font-family="monospace" font-weight="bold">
                  Cut 8 (TCS)
                </text>
              </g>

              <!-- PLOTTED DATA POINTS -->
              <!-- Normal Peer Points (Emerald dots) -->
              <circle
                v-for="pt in peerCluster"
                :key="pt.id"
                :cx="toSvgX(pt.margin)"
                :cy="toSvgY(pt.ocfAssets)"
                :r="pt.isTargetPeer ? 5 : 3"
                :fill="pt.isTargetPeer ? '#34D399' : '#10B981'"
                :stroke="pt.isTargetPeer ? '#FFFFFF' : 'rgba(52, 211, 153, 0.4)'"
                :stroke-width="pt.isTargetPeer ? 1.5 : 0.8"
                :filter="pt.isTargetPeer ? 'url(#glowPointMint)' : 'none'"
                class="cursor-pointer hover:r-5 transition-all"
                @mouseenter="hoveredPoint = pt"
                @mouseleave="hoveredPoint = null"
              />

              <!-- Target Peer Label (TCS) -->
              <text
                :x="toSvgX(25.2) + 7"
                :y="toSvgY(19.4) - 4"
                fill="#34D399"
                font-size="8"
                font-family="monospace"
                font-weight="bold"
              >
                TCS (Peer Core)
              </text>

              <!-- Distressed Noise Point in lower region -->
              <circle
                :cx="toSvgX(-5.0)"
                :cy="toSvgY(-14.0)"
                r="3.5"
                fill="#94A3B8"
                stroke="#64748B"
                stroke-width="1"
              />
              <text
                :x="toSvgX(-5.0) + 6"
                :y="toSvgY(-14.0) + 3"
                fill="#94A3B8"
                font-size="7"
                font-family="monospace"
              >
                Distressed Asset
              </text>

              <!-- ANOMALOUS OUTLIER POINT (ROGUE_CORP) -->
              <!-- Glowing Pulsing Ring -->
              <circle
                :cx="toSvgX(outlierPoint.margin)"
                :cy="toSvgY(outlierPoint.ocfAssets)"
                r="11"
                fill="none"
                stroke="#FB7185"
                stroke-width="1.2"
                stroke-dasharray="3,3"
                class="animate-spin"
              />
              <!-- Center Diamond/Dot -->
              <circle
                :cx="toSvgX(outlierPoint.margin)"
                :cy="toSvgY(outlierPoint.ocfAssets)"
                r="5.5"
                fill="#F43F5E"
                stroke="#FFFFFF"
                stroke-width="1.8"
                filter="url(#glowPointRose)"
                class="cursor-pointer"
                @mouseenter="hoveredPoint = outlierPoint"
                @mouseleave="hoveredPoint = null"
              />
              <!-- Outlier Label Badge -->
              <rect
                :x="toSvgX(outlierPoint.margin) - 95"
                :y="toSvgY(outlierPoint.ocfAssets) - 18"
                width="90"
                height="15"
                rx="3"
                fill="#E11D48"
                opacity="0.95"
              />
              <text
                :x="toSvgX(outlierPoint.margin) - 50"
                :y="toSvgY(outlierPoint.ocfAssets) - 7"
                text-anchor="middle"
                fill="#FFFFFF"
                font-size="7.5"
                font-family="monospace"
                font-weight="bold"
              >
                ROGUE_TECH (h=2)
              </text>

              <!-- Axis Titles & Tick Labels -->
              <!-- X-Axis Labels -->
              <text x="35" y="222" fill="#64748B" font-size="7.5" font-family="monospace">-20%</text>
              <text :x="toSvgX(0)" y="222" text-anchor="middle" fill="#94A3B8" font-size="7.5" font-family="monospace">0%</text>
              <text :x="toSvgX(20)" y="222" text-anchor="middle" fill="#94A3B8" font-size="7.5" font-family="monospace">+20%</text>
              <text :x="toSvgX(40)" y="222" text-anchor="middle" fill="#94A3B8" font-size="7.5" font-family="monospace">+40%</text>
              <text x="405" y="222" text-anchor="end" fill="#34D399" font-size="8" font-family="monospace" font-weight="bold">
                Operating Margin (%) ➔
              </text>

              <!-- Y-Axis Labels -->
              <text x="8" :y="toSvgY(30)" fill="#94A3B8" font-size="7" font-family="monospace">+30%</text>
              <text x="14" :y="toSvgY(0)" fill="#94A3B8" font-size="7" font-family="monospace">0%</text>
              <text x="8" :y="toSvgY(-20)" fill="#94A3B8" font-size="7" font-family="monospace">-20%</text>
              <text x="38" y="12" fill="#38BDF8" font-size="8" font-family="monospace" font-weight="bold">
                ↑ OCF / Total Assets (%)
              </text>
            </svg>
          </div>
        </div>

        <!-- Dynamic Partition Commentary Strip -->
        <div class="mt-1.5 p-1.5 rounded bg-[#071411]/90 border border-emerald-500/20 text-[9px] font-mono flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="text-emerald-400 font-bold">Cut {{ activeCutStep }}:</span>
            <span class="text-slate-300 leading-tight">
              {{ currentCutInfo.detail }}
            </span>
          </div>
        </div>
      </div>

      <!-- Right Panel: Synchronized Binary iTree Growth (Col 5) -->
      <div class="col-span-5 glass-card p-2.5 flex flex-col justify-between overflow-hidden">
        <div>
          <!-- Panel Header -->
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/20">
            <span class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Binary iTree Expansion
            </span>
            <span
              class="text-[9px] px-2 py-0.5 rounded font-mono font-bold"
              :class="activeCutStep >= 2 ? 'bg-rose-500/20 text-rose-300 border border-rose-500/50' : 'bg-slate-800 text-slate-400'"
            >
              {{ activeCutStep >= 2 ? 'Outlier Isolated (h=2)' : 'Tree Growing...' }}
            </span>
          </div>

          <!-- Dynamic SVG iTree -->
          <div class="w-full bg-[#071411]/90 rounded-lg p-1.5 border border-emerald-500/15 relative">
            <svg viewBox="0 0 320 180" class="w-full h-[180px]">
              <!-- Edges -->
              <!-- Level 0 to Level 1 -->
              <g v-if="activeCutStep >= 1">
                <!-- Left Branch to Outlier Subspace (x=90, y=65) -->
                <line
                  x1="160" y1="26" x2="90" y2="65"
                  stroke="#FB7185" stroke-width="2"
                  class="transition-all duration-300"
                />
                <!-- Right Branch to Peer Cluster (x=230, y=65) -->
                <line
                  x1="160" y1="26" x2="230" y2="65"
                  stroke="#34D399" stroke-width="2"
                  class="transition-all duration-300"
                />
              </g>

              <!-- Level 1 to Level 2 (Cut 2) -->
              <g v-if="activeCutStep >= 2">
                <!-- Left-Left Branch to Outlier Leaf (x=50, y=120) -->
                <line
                  x1="90" y1="75" x2="50" y2="120"
                  stroke="#F43F5E" stroke-width="2.5"
                  class="transition-all duration-300"
                />
                <!-- Left-Right Branch to Distressed Asset (x=115, y=120) -->
                <line
                  x1="90" y1="75" x2="115" y2="120"
                  stroke="#64748B" stroke-width="1.2" stroke-dasharray="2,2"
                />
              </g>

              <!-- Level 1 to Level 2 (Right side, Cuts 3 & 4) -->
              <g v-if="activeCutStep >= 3">
                <line
                  x1="230" y1="75" x2="195" y2="115"
                  stroke="#10B981" stroke-width="1.5"
                />
                <line
                  x1="230" y1="75" x2="265" y2="115"
                  stroke="#10B981" stroke-width="1.5"
                />
              </g>

              <!-- Level 2 to Level 3 (Cuts 5 to 8) -->
              <g v-if="activeCutStep >= 5">
                <line
                  x1="265" y1="123" x2="250" y2="155"
                  stroke="#059669" stroke-width="1.2" stroke-dasharray="2,2"
                />
                <line
                  x1="265" y1="123" x2="285" y2="155"
                  :stroke="activeCutStep >= 8 ? '#FBBF24' : '#059669'"
                  :stroke-width="activeCutStep >= 8 ? 2 : 1.2"
                />
              </g>

              <!-- NODES -->
              <!-- Root Node [h = 0] -->
              <g transform="translate(160, 18)">
                <rect x="-65" y="-10" width="130" height="20" rx="10" fill="#0d211b" stroke="#34D399" stroke-width="1.2" />
                <text x="0" y="3.5" text-anchor="middle" fill="#FFFFFF" font-size="8" font-family="monospace" font-weight="bold">
                  Root [N=33, h=0]
                </text>
              </g>

              <!-- Left Node Level 1 [h = 1] -->
              <g v-if="activeCutStep >= 1" transform="translate(90, 68)">
                <rect x="-48" y="-9" width="96" height="18" rx="9" fill="#2A1118" stroke="#FB7185" stroke-width="1.2" />
                <text x="0" y="3" text-anchor="middle" fill="#FECDD3" font-size="7.5" font-family="monospace">
                  OCF &lt; -6% [N=2]
                </text>
              </g>

              <!-- Right Node Level 1 [h = 1] -->
              <g v-if="activeCutStep >= 1" transform="translate(230, 68)">
                <rect x="-48" y="-9" width="96" height="18" rx="9" fill="#0d211b" stroke="#34D399" stroke-width="1.2" />
                <text x="0" y="3" text-anchor="middle" fill="#D1FAE5" font-size="7.5" font-family="monospace">
                  OCF ≥ -6% [N=31]
                </text>
              </g>

              <!-- Outlier Leaf [h = 2] (Terminating Leaf) -->
              <g v-if="activeCutStep >= 2" transform="translate(50, 126)">
                <!-- Halo pulse -->
                <circle r="15" fill="#F43F5E" opacity="0.25" class="animate-ping" />
                <circle r="16" fill="#BE123C" stroke="#FDA4AF" stroke-width="1.8" />
                <text x="0" y="-1" text-anchor="middle" fill="#FFFFFF" font-size="7.5" font-family="monospace" font-weight="bold">
                  h = 2
                </text>
                <text x="0" y="8" text-anchor="middle" fill="#FFE4E6" font-size="6.5" font-family="monospace">
                  N = 1
                </text>
                <!-- Terminal Badge -->
                <rect x="-40" y="20" width="80" height="13" rx="2" fill="#E11D48" />
                <text x="0" y="29.5" text-anchor="middle" fill="#FFFFFF" font-size="7" font-family="monospace" font-weight="bold">
                  ROGUE (Leaf)
                </text>
              </g>

              <!-- Sibling cell [h = 2, N=1] -->
              <g v-if="activeCutStep >= 2" transform="translate(115, 126)">
                <circle r="10" fill="#1e293b" stroke="#64748B" stroke-width="1" />
                <text x="0" y="3" text-anchor="middle" fill="#94A3B8" font-size="7" font-family="monospace">N=1</text>
              </g>

              <!-- Level 2 Sub-nodes (Right branch) -->
              <g v-if="activeCutStep >= 3" transform="translate(195, 118)">
                <rect x="-35" y="-8" width="70" height="16" rx="8" fill="#0d211b" stroke="#10B981" stroke-width="1" />
                <text x="0" y="3" text-anchor="middle" fill="#A7F3D0" font-size="7" font-family="monospace">
                  Margin &lt; 20%
                </text>
              </g>

              <g v-if="activeCutStep >= 3" transform="translate(265, 118)">
                <rect x="-35" y="-8" width="70" height="16" rx="8" fill="#0d211b" stroke="#10B981" stroke-width="1" />
                <text x="0" y="3" text-anchor="middle" fill="#A7F3D0" font-size="7" font-family="monospace">
                  Margin ≥ 20%
                </text>
              </g>

              <!-- Terminal Leaf for TCS (Cut 8) -->
              <g v-if="activeCutStep >= 8" transform="translate(285, 155)">
                <circle r="14" fill="#059669" stroke="#34D399" stroke-width="1.5" />
                <text x="0" y="-1" text-anchor="middle" fill="#FFFFFF" font-size="7.5" font-family="monospace" font-weight="bold">
                  h = 8
                </text>
                <text x="0" y="8" text-anchor="middle" fill="#D1FAE5" font-size="6.5" font-family="monospace">
                  N = 1
                </text>
              </g>
            </svg>
          </div>

          <!-- Comparison Metrics Table -->
          <div class="mt-2 space-y-1 bg-[#071411]/80 p-2 rounded border border-emerald-500/15 font-mono text-[9px]">
            <div class="flex justify-between border-b border-emerald-500/10 pb-0.5">
              <span class="text-slate-400">Outlier Isolation Cuts:</span>
              <strong class="text-rose-400 font-bold">h = 2 bisections</strong>
            </div>
            <div class="flex justify-between border-b border-emerald-500/10 pb-0.5">
              <span class="text-slate-400">Nominal Cluster Cuts (TCS):</span>
              <strong class="text-emerald-400 font-bold">h = 8 to 9 bisections</strong>
            </div>
            <div class="flex justify-between border-b border-emerald-500/10 pb-0.5">
              <span class="text-slate-400">Separation Path Differential:</span>
              <strong class="text-white">4.0x Deeper Traversal</strong>
            </div>
            <div class="flex justify-between pt-0.5">
              <span class="text-slate-400">Computational Scaling:</span>
              <strong class="text-emerald-300">O(t · ψ log ψ) Linear</strong>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Row: 3 Educational & Computational Scaling Cards (Col 12) -->
    <div class="grid grid-cols-12 gap-2.5">
      <!-- Card 1: Subspace Isolation Probability Mechanics -->
      <div class="col-span-4 glass-card p-2 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
            <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Hyperplane Isolation Theory
            </span>
            <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Mechanics
            </span>
          </div>

          <!-- Formula Box -->
          <div class="bg-[#071411]/90 p-1 rounded border border-emerald-500/20 font-mono text-[9px] text-emerald-200 leading-tight mb-1">
            <div class="text-emerald-300 font-semibold">Pr(Cut Isolates x) ∝ Bounding Cell Volume</div>
            <div class="text-[8px] text-slate-400 mt-0.5">
              Outliers inhabit low-density margins ⟹ Isolated in h ≪ c(n) cuts!
            </div>
          </div>

          <!-- Where: Parameter Block -->
          <div class="text-[8px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono">Where:</div>
            <ul class="space-y-0.2 text-slate-400">
              <li><strong class="text-white font-mono">Outliers:</strong> Few instances, high boundary margin ⟹ h = 2</li>
              <li><strong class="text-white font-mono">Nominals:</strong> Dense packing requires exponential bisections ⟹ h = 8+</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Card 2: Computational Complexity vs Distance Methods -->
      <div class="col-span-4 glass-card p-2 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
            <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Computational Complexity
            </span>
            <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Scaling
            </span>
          </div>

          <!-- Complexity Box -->
          <div class="bg-[#071411]/90 p-1 rounded border border-emerald-500/20 font-mono text-[9px] text-emerald-200 leading-tight mb-1">
            <div class="text-emerald-300 font-semibold">Time: O(t · ψ log ψ) | Memory: O(t · ψ)</div>
            <div class="text-[8px] text-slate-400 mt-0.5">
              Zero distance matrix calculation (Eliminates O(n²) bottlenecks)
            </div>
          </div>

          <!-- Where: Parameter Block -->
          <div class="text-[8px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono">Where:</div>
            <ul class="space-y-0.2 text-slate-400">
              <li><strong class="text-white font-mono">t:</strong> Number of trees (default t = 100)</li>
              <li><strong class="text-white font-mono">ψ:</strong> Sub-sampling size (ψ = 256; fixed sample budget)</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Card 3: 2D Projection of 16-Dimensional Space -->
      <div class="col-span-4 glass-card p-2 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
            <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Subspace Projection in ℝ¹⁶
            </span>
            <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Multivariate
            </span>
          </div>

          <!-- Projection Box -->
          <div class="space-y-1 font-mono text-[8.5px]">
            <div class="flex items-center justify-between bg-emerald-500/15 px-1.5 py-0.5 rounded border border-emerald-500/30">
              <span class="text-emerald-300 font-bold">16 Financial Dimensions</span>
              <span class="text-emerald-200">Profitability + Solvency + Cash Flow</span>
            </div>
            <div class="flex items-center justify-between bg-teal-500/15 px-1.5 py-0.5 rounded border border-teal-500/30">
              <span class="text-teal-300 font-bold">Orthogonal Random Cuts</span>
              <span class="text-teal-200">Uniform random dimension q ∈ ℝ¹⁶</span>
            </div>
          </div>

          <!-- Bottom Summary Note -->
          <div class="text-[7.5px] text-slate-400 mt-1 leading-tight">
            Immune to the curse of dimensionality because each tree cut selects a single feature dimension independently.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
