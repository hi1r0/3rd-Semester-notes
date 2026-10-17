<script setup lang="ts">
import { ref, computed, watch } from 'vue'

// --- Mathematical Constants & Formulas ---
const GAMMA = 0.5772156649 // Euler-Mascheroni constant

// Theoretical Average BST Path Length c(n)
function calculateCN(sampleSize: number): number {
  if (sampleSize <= 1) return 1
  if (sampleSize === 2) return 1
  return 2 * (Math.log(sampleSize - 1) + GAMMA) - (2 * (sampleSize - 1)) / sampleSize
}

// Interactive State
const sampleSize = ref<number>(256) // standard iForest sub-sample size
const selectedFirmKey = ref<'outlier' | 'nominal' | 'borderline' | 'manual'>('outlier')
const manualDepth = ref<number>(2) // Depth h slider when in manual mode
const traversalStep = ref<number>(2) // Active step in tree visualization (0 = root, 1 = node, 2 = leaf)
const isAutoPlaying = ref<boolean>(false)

// Firm Profiles
interface FirmProfile {
  key: 'outlier' | 'nominal' | 'borderline'
  ticker: string
  name: string
  sector: string
  depth: number
  archetype: string
  severity: 'critical' | 'nominal' | 'watch'
  ratios: {
    margin: string
    ocfAssets: string
    de: string
    roce: string
  }
  anomalyReason: string
  pathDecisions: Array<{
    level: number
    feature: string
    operator: string
    threshold: string
    actual: string
    conditionMet: boolean
    subspaceDesc: string
  }>
}

const firmProfiles: Record<'outlier' | 'nominal' | 'borderline', FirmProfile> = {
  outlier: {
    key: 'outlier',
    ticker: 'ROGUE_TECH',
    name: 'Rogue Cloud Solutions',
    sector: 'Enterprise Software',
    depth: 2,
    archetype: 'Divergent Cash Flow Trap',
    severity: 'critical',
    ratios: {
      margin: '+46.8%',
      ocfAssets: '-18.5%',
      de: '2.84x',
      roce: '+32.4%',
    },
    anomalyReason: 'Extreme contradiction: 46.8% Operating Margin paired with -18.5% OCF/Assets. Isolated in 2 hyperplanes!',
    pathDecisions: [
      {
        level: 0,
        feature: 'OCF / Total Assets',
        operator: '<',
        threshold: '-0.08',
        actual: '-0.185',
        conditionMet: true,
        subspaceDesc: 'Left Branch ➔ Sparse Negative Cash Flow Subspace (n = 12)',
      },
      {
        level: 1,
        feature: 'Operating Margin',
        operator: '>',
        threshold: '+0.35',
        actual: '+0.468',
        conditionMet: true,
        subspaceDesc: 'Left Leaf ➔ Isolated Outlier Cell (n = 1) at h = 2',
      },
    ],
  },
  nominal: {
    key: 'nominal',
    ticker: 'TCS',
    name: 'Tata Consultancy Services',
    sector: 'Tier-1 IT Services',
    depth: 9,
    archetype: 'Cluster Core Benchmark',
    severity: 'nominal',
    ratios: {
      margin: '+25.2%',
      ocfAssets: '+19.4%',
      de: '0.08x',
      roce: '+48.2%',
    },
    anomalyReason: 'Dense cluster centroid. Requires 9 recursive bisections across ℝ¹⁶ to separate from peer cluster.',
    pathDecisions: [
      {
        level: 0,
        feature: 'OCF / Total Assets',
        operator: '<',
        threshold: '-0.08',
        actual: '+0.194',
        conditionMet: false,
        subspaceDesc: 'Right Branch ➔ Normal Cash Flow Domain (n = 244)',
      },
      {
        level: 1,
        feature: 'ROCE',
        operator: '<',
        threshold: '+0.15',
        actual: '+0.482',
        conditionMet: false,
        subspaceDesc: 'Right Branch ➔ High Return Peer Region (n = 188)',
      },
      {
        level: 2,
        feature: 'Asset Turnover',
        operator: '<',
        threshold: '1.10x',
        actual: '1.24x',
        conditionMet: false,
        subspaceDesc: 'Deep Sub-tree ➔ Successive cuts down to h = 9 (n = 1)',
      },
    ],
  },
  borderline: {
    key: 'borderline',
    ticker: 'CYCLIC_INFRA',
    name: 'Cyclic Heavy Infra Ltd',
    sector: 'Capital Goods & EPC',
    depth: 6,
    archetype: 'Cyclical Working Capital Lag',
    severity: 'watch',
    ratios: {
      margin: '+12.4%',
      ocfAssets: '+2.1%',
      de: '2.15x',
      roce: '+11.8%',
    },
    anomalyReason: 'Modest debt overhang and thin cash flows. Traverses to intermediate depth h = 6.',
    pathDecisions: [
      {
        level: 0,
        feature: 'OCF / Total Assets',
        operator: '<',
        threshold: '-0.08',
        actual: '+0.021',
        conditionMet: false,
        subspaceDesc: 'Right Branch ➔ Positive Cash Flow Subspace (n = 244)',
      },
      {
        level: 1,
        feature: 'ROCE',
        operator: '<',
        threshold: '+0.15',
        actual: '+0.118',
        conditionMet: true,
        subspaceDesc: 'Left Branch ➔ Moderate Return Cohort (n = 56)',
      },
      {
        level: 2,
        feature: 'Debt-to-Equity (D/E)',
        operator: '>',
        threshold: '1.80x',
        actual: '2.15x',
        conditionMet: true,
        subspaceDesc: 'Intermediate Leaf ➔ Isolated at h = 6 after 6 bisections',
      },
    ],
  },
}

// Current Active Depth
const activeDepth = computed(() => {
  if (selectedFirmKey.value === 'manual') return manualDepth.value
  return firmProfiles[selectedFirmKey.value].depth
})

// Live BST Normalization Factor c(n)
const cN = computed(() => calculateCN(sampleSize.value))

// Path Length Ratio: h / c(n)
const pathRatio = computed(() => activeDepth.value / cN.value)

// Exponential Anomaly Score: s(x, n) = 2^(-h / c(n))
const anomalyScore = computed(() => Math.pow(2, -pathRatio.value))

// Score Classification & Interpretation
const scoreInterpretation = computed(() => {
  const s = anomalyScore.value
  if (s >= 0.70) {
    return {
      tier: 'Tier 3: Critical Alert',
      label: 'Definitive Subspace Anomaly',
      badgeClass: 'bg-rose-500/20 text-rose-300 border-rose-500/50',
      description: 'Extremely shallow path (h << c(n)). High probability of artificial accounting distortion or multi-metric stress.',
      color: '#F43F5E',
    }
  } else if (s >= 0.55) {
    return {
      tier: 'Tier 2: Elevated Watch',
      label: 'Marginal Subspace Outlier',
      badgeClass: 'bg-amber-500/20 text-amber-300 border-amber-500/50',
      description: 'Intermediate path length (h ≈ c(n)). Structural boundary firm requiring forensic cash reconciliation.',
      color: '#F59E0B',
    }
  } else {
    return {
      tier: 'Tier 1: Nominal Cohort',
      label: 'Dense Peer Cluster Interior',
      badgeClass: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50',
      description: 'Deep path traversal (h > c(n)). Firm shares joint multivariate distribution with healthy sector peers.',
      color: '#34D399',
    }
  }
})

// Preset Selection
function selectFirm(key: 'outlier' | 'nominal' | 'borderline' | 'manual') {
  selectedFirmKey.value = key
  if (key !== 'manual') {
    traversalStep.value = firmProfiles[key].depth
  } else {
    traversalStep.value = manualDepth.value
  }
}

// Traversal Animation Control
let autoPlayTimer: any = null
function toggleAutoPlay() {
  if (isAutoPlaying.value) {
    clearInterval(autoPlayTimer)
    isAutoPlaying.value = false
  } else {
    isAutoPlaying.value = true
    traversalStep.value = 0
    autoPlayTimer = setInterval(() => {
      const targetMax = activeDepth.value
      if (traversalStep.value < targetMax) {
        traversalStep.value++
      } else {
        clearInterval(autoPlayTimer)
        isAutoPlaying.value = false
      }
    }, 900)
  }
}

watch(selectedFirmKey, () => {
  if (isAutoPlaying.value) {
    clearInterval(autoPlayTimer)
    isAutoPlaying.value = false
  }
})
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Action & Selection Bar -->
    <div class="flex items-center justify-between gap-3 bg-[#071411]/90 p-2 rounded-xl border border-emerald-500/20 mb-2">
      <!-- Scenario Selector Tabs -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Scenario:
        </span>
        <button
          @click="selectFirm('outlier')"
          class="px-2.5 py-1 rounded-lg text-xs font-semibold font-mono transition-all flex items-center gap-1.5 border"
          :class="selectedFirmKey === 'outlier'
            ? 'bg-rose-500/25 text-rose-300 border-rose-500/60 shadow-[0_0_12px_rgba(244,63,94,0.35)]'
            : 'bg-[#0d211b]/80 text-slate-300 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span>
          Outlier (h=2, s=0.86)
        </button>

        <button
          @click="selectFirm('borderline')"
          class="px-2.5 py-1 rounded-lg text-xs font-semibold font-mono transition-all flex items-center gap-1.5 border"
          :class="selectedFirmKey === 'borderline'
            ? 'bg-amber-500/25 text-amber-300 border-amber-500/60 shadow-[0_0_12px_rgba(245,158,11,0.35)]'
            : 'bg-[#0d211b]/80 text-slate-300 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
          Borderline (h=6, s=0.63)
        </button>

        <button
          @click="selectFirm('nominal')"
          class="px-2.5 py-1 rounded-lg text-xs font-semibold font-mono transition-all flex items-center gap-1.5 border"
          :class="selectedFirmKey === 'nominal'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 shadow-[0_0_12px_rgba(52,211,153,0.35)]'
            : 'bg-[#0d211b]/80 text-slate-300 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          Nominal (h=9, s=0.50)
        </button>

        <button
          @click="selectFirm('manual')"
          class="px-2 py-1 rounded-lg text-xs font-semibold font-mono transition-all border"
          :class="selectedFirmKey === 'manual'
            ? 'bg-teal-500/25 text-teal-300 border-teal-500/60 shadow-[0_0_12px_rgba(20,184,166,0.35)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          Custom Simulator
        </button>
      </div>

      <!-- Sample Size & Traversal Controls -->
      <div class="flex items-center gap-3">
        <!-- Sample Size n Pill Selector -->
        <div class="flex items-center gap-1 text-[10px] font-mono">
          <span class="text-slate-400">Sub-sample (ψ):</span>
          <div class="flex bg-[#0d211b] p-0.5 rounded border border-emerald-500/20">
            <button
              v-for="size in [64, 128, 256, 512]"
              :key="size"
              @click="sampleSize = size"
              class="px-1.5 py-0.5 rounded text-[9.5px] transition-all font-mono"
              :class="sampleSize === size ? 'bg-emerald-500/30 text-emerald-300 font-bold' : 'text-slate-400 hover:text-white'"
            >
              {{ size }}
            </button>
          </div>
        </div>

        <!-- Traversal Animator Button -->
        <button
          @click="toggleAutoPlay"
          class="px-2.5 py-1 rounded-lg text-[10.5px] font-mono font-semibold transition-all border flex items-center gap-1 bg-emerald-500/15 text-emerald-300 border-emerald-500/30 hover:bg-emerald-500/25"
        >
          <span>{{ isAutoPlaying ? '⏸ Pause' : '▶ Animate Traversal' }}</span>
        </button>
      </div>
    </div>

    <!-- Main Content Stage: 12-Column Grid -->
    <div class="grid grid-cols-12 gap-2.5 flex-1 min-h-0 mb-2">
      <!-- Left Column: iTree Binary Graph Visualizer (Col 7) -->
      <div class="col-span-7 glass-card p-2.5 flex flex-col justify-between overflow-hidden">
        <div>
          <!-- Title & Subspace Header -->
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/20">
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">
                Multivariate iTree Traversal (ℝ¹⁶)
              </span>
              <span class="text-[9px] px-1.5 py-0.2 rounded font-mono bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                100 Trees Ensemble
              </span>
            </div>
            <div class="text-[9.5px] font-mono text-slate-400">
              Active Path: <strong class="text-emerald-300">h = {{ activeDepth }}</strong>
              <span class="text-slate-500"> / c({{ sampleSize }}) = {{ cN.toFixed(2) }}</span>
            </div>
          </div>

          <!-- SVG iTree Traversal Visualization -->
          <div class="w-full bg-[#071411]/90 rounded-lg p-2 border border-emerald-500/15 relative overflow-hidden">
            <svg viewBox="0 0 510 200" class="w-full h-[180px]">
              <defs>
                <linearGradient id="gradOutlier" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#FB7185" />
                  <stop offset="100%" stop-color="#E11D48" />
                </linearGradient>
                <linearGradient id="gradNominal" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#34D399" />
                  <stop offset="100%" stop-color="#059669" />
                </linearGradient>
                <filter id="glowRose" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="4" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
                <filter id="glowMint" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="3" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              <!-- Level 0: Root Node -->
              <!-- Edges from Root (x=255, y=20) -->
              <!-- Left Edge (to x=120, y=70) -->
              <line
                x1="255" y1="26" x2="120" y2="70"
                stroke-width="2.5"
                :stroke="selectedFirmKey === 'outlier' ? '#FB7185' : 'rgba(52, 211, 153, 0.25)'"
                :stroke-dasharray="selectedFirmKey === 'outlier' ? 'none' : '3,3'"
                class="transition-all duration-300"
              />
              <!-- Right Edge (to x=390, y=70) -->
              <line
                x1="255" y1="26" x2="390" y2="70"
                stroke-width="2.5"
                :stroke="(selectedFirmKey === 'nominal' || selectedFirmKey === 'borderline') ? '#34D399' : 'rgba(52, 211, 153, 0.25)'"
                class="transition-all duration-300"
              />

              <!-- Level 1: Left Node (Sparse region, x=120, y=70) -->
              <!-- Edge to Outlier Leaf (x=60, y=140) -->
              <line
                x1="120" y1="78" x2="60" y2="140"
                stroke-width="2.5"
                :stroke="selectedFirmKey === 'outlier' ? '#FB7185' : 'rgba(52, 211, 153, 0.20)'"
                :filter="selectedFirmKey === 'outlier' ? 'url(#glowRose)' : 'none'"
                class="transition-all duration-300"
              />
              <!-- Edge to empty sibling (x=175, y=130) -->
              <line
                x1="120" y1="78" x2="175" y2="130"
                stroke-width="1.2"
                stroke="rgba(148, 163, 184, 0.25)"
                stroke-dasharray="2,2"
              />

              <!-- Level 1: Right Node (Dense cluster, x=390, y=70) -->
              <!-- Edge to Mid Node Left (x=330, y=120) -->
              <line
                x1="390" y1="78" x2="330" y2="120"
                stroke-width="2"
                :stroke="selectedFirmKey === 'borderline' ? '#F59E0B' : 'rgba(52, 211, 153, 0.35)'"
                class="transition-all duration-300"
              />
              <!-- Edge to Deep Cluster Right (x=450, y=120) -->
              <line
                x1="390" y1="78" x2="450" y2="120"
                stroke-width="2"
                :stroke="selectedFirmKey === 'nominal' ? '#34D399' : 'rgba(52, 211, 153, 0.35)'"
                class="transition-all duration-300"
              />

              <!-- Level 2: Sub-edges for Deep Cluster (x=450, y=120 to x=430, y=165 and x=475, y=165) -->
              <line
                x1="450" y1="126" x2="430" y2="165"
                stroke-width="1.5"
                stroke="rgba(52, 211, 153, 0.30)"
                stroke-dasharray="2,2"
              />
              <line
                x1="450" y1="126" x2="475" y2="165"
                stroke-width="2"
                :stroke="selectedFirmKey === 'nominal' ? '#34D399' : 'rgba(52, 211, 153, 0.30)'"
                :filter="selectedFirmKey === 'nominal' ? 'url(#glowMint)' : 'none'"
              />

              <!-- Level 2: Sub-edges for Borderline (x=330, y=120 to x=315, y=165) -->
              <line
                x1="330" y1="126" x2="315" y2="165"
                stroke-width="1.8"
                :stroke="selectedFirmKey === 'borderline' ? '#F59E0B' : 'rgba(148, 163, 184, 0.30)'"
              />

              <!-- NODES -->
              <!-- Root Node [h = 0] -->
              <g transform="translate(255, 20)">
                <rect
                  x="-85" y="-12" width="170" height="24" rx="12"
                  fill="#0d211b" stroke="#34D399" stroke-width="1.5"
                />
                <text x="0" y="4" text-anchor="middle" fill="#F8FAFC" font-size="9.5" font-family="monospace" font-weight="bold">
                  q₀: OCF/Assets &lt; -0.08
                </text>
              </g>

              <!-- Node Left 1 [h = 1] -->
              <g transform="translate(120, 70)">
                <rect
                  x="-75" y="-11" width="150" height="22" rx="11"
                  :fill="selectedFirmKey === 'outlier' ? '#2A1118' : '#0d211b'"
                  :stroke="selectedFirmKey === 'outlier' ? '#FB7185' : '#34D399'"
                  stroke-width="1.5"
                />
                <text x="0" y="3.5" text-anchor="middle" :fill="selectedFirmKey === 'outlier' ? '#FECDD3' : '#F8FAFC'" font-size="9" font-family="monospace">
                  q₁: Margin &gt; 35.0%
                </text>
              </g>

              <!-- Outlier Leaf [h = 2] -->
              <g transform="translate(60, 142)">
                <circle
                  r="20"
                  fill="url(#gradOutlier)"
                  :filter="selectedFirmKey === 'outlier' ? 'url(#glowRose)' : 'none'"
                />
                <text x="0" y="-3" text-anchor="middle" fill="#FFFFFF" font-size="8.5" font-family="monospace" font-weight="bold">
                  h = 2
                </text>
                <text x="0" y="8" text-anchor="middle" fill="#FFE4E6" font-size="7.5" font-family="monospace">
                  Leaf (n=1)
                </text>
                <!-- Badge below leaf -->
                <rect x="-48" y="24" width="96" height="15" rx="3" fill="#E11D48" opacity="0.9" />
                <text x="0" y="34.5" text-anchor="middle" fill="#FFFFFF" font-size="7.5" font-family="monospace" font-weight="bold">
                  ROGUE_TECH (s=0.86)
                </text>
              </g>

              <!-- Sibling empty leaf -->
              <g transform="translate(175, 130)">
                <circle r="8" fill="#1e293b" stroke="#475569" stroke-width="1" />
                <text x="0" y="3" text-anchor="middle" fill="#94A3B8" font-size="7" font-family="monospace">n=11</text>
              </g>

              <!-- Node Right 1 [h = 1] -->
              <g transform="translate(390, 70)">
                <rect
                  x="-70" y="-11" width="140" height="22" rx="11"
                  fill="#0d211b" stroke="#34D399" stroke-width="1.5"
                />
                <text x="0" y="3.5" text-anchor="middle" fill="#F8FAFC" font-size="9" font-family="monospace">
                  q₁: ROCE &lt; 15.0%
                </text>
              </g>

              <!-- Borderline Leaf [h = 6] -->
              <g transform="translate(315, 165)">
                <circle
                  r="16"
                  :fill="selectedFirmKey === 'borderline' ? '#F59E0B' : '#1e293b'"
                  :stroke="selectedFirmKey === 'borderline' ? '#FDE68A' : '#64748B'"
                  stroke-width="1.5"
                />
                <text x="0" y="-1" text-anchor="middle" fill="#FFFFFF" font-size="8" font-family="monospace" font-weight="bold">
                  h = 6
                </text>
                <text x="0" y="9" text-anchor="middle" fill="#FEF3C7" font-size="7" font-family="monospace">
                  n=1
                </text>
                <text x="0" y="26" text-anchor="middle" fill="#FBBF24" font-size="7" font-family="monospace" font-weight="bold">
                  CYCLIC (s=0.63)
                </text>
              </g>

              <!-- Intermediate Right Node [h = 2] -->
              <g transform="translate(450, 120)">
                <rect
                  x="-45" y="-10" width="90" height="20" rx="10"
                  fill="#0d211b" stroke="#10B981" stroke-width="1.2"
                />
                <text x="0" y="3" text-anchor="middle" fill="#CBD5E1" font-size="8" font-family="monospace">
                  Sub-tree (h=2..8)
                </text>
              </g>

              <!-- Nominal Core Leaf [h = 9] -->
              <g transform="translate(475, 165)">
                <circle
                  r="18"
                  fill="url(#gradNominal)"
                  :filter="selectedFirmKey === 'nominal' ? 'url(#glowMint)' : 'none'"
                />
                <text x="0" y="-2" text-anchor="middle" fill="#042F2E" font-size="8.5" font-family="monospace" font-weight="bold">
                  h = 9
                </text>
                <text x="0" y="8" text-anchor="middle" fill="#064E3B" font-size="7" font-family="monospace">
                  Leaf (n=1)
                </text>
                <!-- Badge below leaf -->
                <rect x="-40" y="22" width="80" height="14" rx="3" fill="#059669" opacity="0.9" />
                <text x="0" y="32" text-anchor="middle" fill="#FFFFFF" font-size="7.5" font-family="monospace" font-weight="bold">
                  TCS (s=0.50)
                </text>
              </g>
            </svg>
          </div>
        </div>

        <!-- Traversal Logic Log Strip -->
        <div class="mt-1.5 p-1.5 rounded bg-[#071411]/90 border border-emerald-500/20 text-[9px] font-mono flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-emerald-400 font-bold">Partition Mechanism:</span>
            <span class="text-slate-300">
              Random dimension <strong class="text-white">q ∈ ℝ¹⁶</strong>, random split value <strong class="text-white">p ∈ [min, max]</strong>.
            </span>
          </div>
          <div class="text-slate-400">
            Ensemble: <span class="text-emerald-300 font-semibold">t = 100 Trees</span>
          </div>
        </div>
      </div>

      <!-- Right Column: Live Anomaly Score & Context (Col 5) -->
      <div class="col-span-5 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-1 mb-2 border-b border-emerald-500/20">
            <span class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Anomaly Score Engine
            </span>
            <span
              class="text-[9px] px-2 py-0.5 rounded font-mono font-bold border"
              :class="scoreInterpretation.badgeClass"
            >
              {{ scoreInterpretation.tier }}
            </span>
          </div>

          <!-- Dynamic Anomaly Score Display Card -->
          <div class="bg-[#071411]/90 p-2 rounded-lg border border-emerald-500/25 mb-2">
            <div class="flex items-baseline justify-between mb-1">
              <span class="text-[9.5px] text-slate-400 font-mono">Score s(x, {{ sampleSize }}):</span>
              <span class="text-xl font-extrabold font-mono" :style="{ color: scoreInterpretation.color }">
                {{ anomalyScore.toFixed(3) }}
              </span>
            </div>

            <!-- Visual Gradient Score Progress Bar -->
            <div class="w-full bg-slate-800/80 rounded-full h-2 mb-1.5 relative overflow-hidden">
              <div
                class="h-full rounded-full transition-all duration-500"
                :style="{
                  width: `${Math.min(100, anomalyScore * 100)}%`,
                  backgroundColor: scoreInterpretation.color,
                }"
              ></div>
            </div>

            <!-- Score Boundaries Marker Guide -->
            <div class="flex justify-between text-[7.5px] font-mono text-slate-400 px-0.5">
              <span>0.0 (Nominal Core)</span>
              <span>0.50 (c(n) Threshold)</span>
              <span>0.70 (Alert)</span>
              <span>1.0 (Outlier)</span>
            </div>
          </div>

          <!-- Live Variables Computation Table -->
          <div class="space-y-1 mb-2 bg-[#071411]/80 p-2 rounded border border-emerald-500/15 font-mono text-[9px]">
            <div class="flex justify-between border-b border-emerald-500/10 pb-0.5">
              <span class="text-slate-400">Ensemble Path Depth E[h(x)]:</span>
              <strong class="text-white">{{ activeDepth }} edges</strong>
            </div>
            <div class="flex justify-between border-b border-emerald-500/10 pb-0.5">
              <span class="text-slate-400">BST Normalization c({{ sampleSize }}):</span>
              <strong class="text-emerald-300">{{ cN.toFixed(3) }} edges</strong>
            </div>
            <div class="flex justify-between border-b border-emerald-500/10 pb-0.5">
              <span class="text-slate-400">Path Ratio E[h(x)] / c(n):</span>
              <strong class="text-white">{{ pathRatio.toFixed(3) }}</strong>
            </div>
            <div class="flex justify-between pt-0.5">
              <span class="text-slate-400">Exponential Power (2^-ratio):</span>
              <strong :style="{ color: scoreInterpretation.color }">{{ anomalyScore.toFixed(3) }}</strong>
            </div>
          </div>

          <!-- Manual Depth Slider (When in Custom Mode) -->
          <div v-if="selectedFirmKey === 'manual'" class="bg-[#071411] p-1.5 rounded border border-teal-500/30 mb-2">
            <div class="flex justify-between text-[9px] font-mono text-teal-300 mb-1">
              <span>Simulate Depth h:</span>
              <strong>h = {{ manualDepth }}</strong>
            </div>
            <input
              type="range"
              min="1"
              max="14"
              step="1"
              v-model.number="manualDepth"
              class="w-full accent-emerald-400 cursor-pointer h-1 bg-slate-700 rounded"
            />
          </div>

          <!-- Diagnostic Archetype Insight -->
          <div class="text-[9px] text-slate-300 leading-tight bg-slate-900/60 p-1.5 rounded border border-slate-700/50">
            <div class="font-bold text-emerald-300 font-mono mb-0.5">
              {{ selectedFirmKey === 'outlier' ? '🚨 ROGUE_TECH Forensic Diagnostic:' : selectedFirmKey === 'nominal' ? '✓ TCS Benchmark Diagnostic:' : '⚠️ CYCLIC Diagnostic:' }}
            </div>
            <p class="text-slate-400">
              {{ firmProfiles[selectedFirmKey === 'manual' ? 'outlier' : selectedFirmKey].anomalyReason }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Row: 3 Mathematical & Consensus Architecture Cards (Col 12) -->
    <div class="grid grid-cols-12 gap-2.5">
      <!-- Card 1: BST Average Path-Length Formula c(n) -->
      <div class="col-span-4 glass-card p-2 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
            <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              BST Path Expectation c(n)
            </span>
            <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Normalizer
            </span>
          </div>

          <!-- Formula Box -->
          <div class="bg-[#071411]/90 p-1 rounded border border-emerald-500/20 font-mono text-[9px] text-emerald-200 leading-tight mb-1">
            <div class="text-emerald-300 font-semibold">c(n) = 2·ln(n - 1) + 2γ - 2(n - 1)/n</div>
            <div class="text-[8px] text-slate-400 mt-0.5">
              At n={{ sampleSize }}: c({{ sampleSize }}) = 2·ln({{ sampleSize - 1 }}) + 1.1544 - {{ ((2*(sampleSize-1))/sampleSize).toFixed(2) }} = <strong class="text-emerald-300">{{ cN.toFixed(2) }}</strong>
            </div>
          </div>

          <!-- Where: Parameter Block -->
          <div class="text-[8px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono">Where:</div>
            <ul class="space-y-0.2 text-slate-400">
              <li><strong class="text-white font-mono">n:</strong> Sub-sample instances (ψ = 256; prevents masking)</li>
              <li><strong class="text-white font-mono">γ:</strong> Euler-Mascheroni constant ≈ 0.5772156649</li>
              <li><strong class="text-white font-mono">c(n):</strong> Average path of unsuccessful searches in BST</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Card 2: Exponential Anomaly Score Definition -->
      <div class="col-span-4 glass-card p-2 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
            <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Exponential Score s(x, n)
            </span>
            <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Metric
            </span>
          </div>

          <!-- Formula Box -->
          <div class="bg-[#071411]/90 p-1 rounded border border-emerald-500/20 font-mono text-[9px] text-emerald-200 leading-tight mb-1">
            <div class="text-emerald-300 font-semibold">s(x, n) = 2^(-E[h(x)] / c(n))</div>
            <div class="text-[8px] text-slate-400 mt-0.5">
              h ➔ 0 ⟹ s ➔ 1.0 (Alert) | h ➔ c(n) ⟹ s ➔ 0.50
            </div>
          </div>

          <!-- Where: Parameter Block -->
          <div class="text-[8px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono">Where:</div>
            <ul class="space-y-0.2 text-slate-400">
              <li><strong class="text-white font-mono">h(x):</strong> Path length to terminating external leaf node</li>
              <li><strong class="text-white font-mono">E[h(x)]:</strong> Average depth across ensemble of t=100 iTrees</li>
              <li><strong class="text-white font-mono">s &gt; 0.60:</strong> Definite multi-attribute anomaly flag</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Card 3: Tri-Method Consensus Matrix -->
      <div class="col-span-4 glass-card p-2 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
            <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Tri-Method Consensus Matrix
            </span>
            <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Consensus
            </span>
          </div>

          <!-- Consensus Matrix Tiers -->
          <div class="space-y-1 font-mono text-[8.5px]">
            <div class="flex items-center justify-between bg-rose-500/15 px-1.5 py-0.5 rounded border border-rose-500/30">
              <span class="text-rose-300 font-bold">Tier 3: Critical Alert</span>
              <span class="text-rose-200">3/3 (IQR + MAD + iForest)</span>
            </div>
            <div class="flex items-center justify-between bg-amber-500/15 px-1.5 py-0.5 rounded border border-amber-500/30">
              <span class="text-amber-300 font-bold">Tier 2: Elevated Watch</span>
              <span class="text-amber-200">2/3 Flagged (Joint Subspace)</span>
            </div>
            <div class="flex items-center justify-between bg-emerald-500/15 px-1.5 py-0.5 rounded border border-emerald-500/30">
              <span class="text-emerald-300 font-bold">Tier 1: Marginal Watch</span>
              <span class="text-emerald-200">1/3 Flagged (Marginal 1D)</span>
            </div>
          </div>

          <!-- Bottom Summary Note -->
          <div class="text-[7.5px] text-slate-400 mt-1 leading-tight">
            iForest isolates multivariate combinations in <strong class="text-emerald-300">ℝ¹⁶</strong> invisible to 1D univariate Tukey/MAD filters!
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
