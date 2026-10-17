<script setup lang="ts">
import { ref, computed } from 'vue'

// Company Archetype Profiles
interface CompanyArchetype {
  id: string
  ticker: string
  name: string
  sector: string
  score: number
  tier: 'EXCELLENT' | 'STRONG' | 'MODERATE' | 'WEAK' | 'DISTRESSED'
  creditRating: string
  solvencySummary: string
  portfolioStrategy: string
  pillars: {
    profitability: number // W1 = 25%
    leverage: number // W2 = 25%
    liquidity: number // W3 = 20%
    efficiency: number // W4 = 15%
    valuation: number // W5 = 15%
  }
}

const archetypes: Record<string, CompanyArchetype> = {
  tcs: {
    id: 'tcs',
    ticker: 'TCS / INFY',
    name: 'Tata Consultancy Services',
    sector: 'IT Services & Consulting',
    score: 88.4,
    tier: 'EXCELLENT',
    creditRating: 'AAA / AA+',
    solvencySummary: 'Pristine zero net debt, >$5B cash reserves, elite operating margins and cash conversion.',
    portfolioStrategy: 'Overweight / Core Alpha Compounder',
    pillars: { profitability: 92.5, leverage: 98.0, liquidity: 85.0, efficiency: 84.0, valuation: 75.0 },
  },
  reliance: {
    id: 'reliance',
    ticker: 'RELIANCE',
    name: 'Reliance Industries',
    sector: 'Diversified Conglomerate',
    score: 72.1,
    tier: 'STRONG',
    creditRating: 'AA / A+',
    solvencySummary: 'Massive EBITDA generation comfortably covers multi-year telecom & green energy CapEx debt service.',
    portfolioStrategy: 'Long Factor Exposure / Core Hold',
    pillars: { profitability: 74.0, leverage: 62.5, liquidity: 68.0, efficiency: 78.5, valuation: 76.0 },
  },
  tatamotors: {
    id: 'tatamotors',
    ticker: 'TATA MOTORS',
    name: 'Tata Motors Limited',
    sector: 'Automotive & Commercial Vehicles',
    score: 56.5,
    tier: 'MODERATE',
    creditRating: 'BBB+ / BBB-',
    solvencySummary: 'Cyclical margin recovery, improving JLR free cash flow offset by substantial industrial debt.',
    portfolioStrategy: 'Sector-Neutral Market Weight',
    pillars: { profitability: 55.0, leverage: 51.0, liquidity: 58.0, efficiency: 62.0, valuation: 57.0 },
  },
  vodafone: {
    id: 'vodafone',
    ticker: 'VODAFONE IDEA',
    name: 'Vodafone Idea Limited',
    sector: 'Telecommunications Services',
    score: 41.2,
    tier: 'WEAK',
    creditRating: 'BB+ / BB-',
    solvencySummary: 'Severe AGR liability overhang, persistent EBITDA margin drag, continuous reliance on equity dilution.',
    portfolioStrategy: 'Underweight / Elevated Risk Watch',
    pillars: { profitability: 38.0, leverage: 32.0, liquidity: 44.0, efficiency: 48.0, valuation: 49.0 },
  },
  distressed: {
    id: 'distressed',
    ticker: 'DISTRESSED INFRA',
    name: 'Stressed Infrastructure EPC',
    sector: 'Heavy EPC & Power Transmission',
    score: 22.8,
    tier: 'DISTRESSED',
    creditRating: 'B / C / D',
    solvencySummary: 'Negative net worth, depleted liquidity, formal debt service default and IBC restructuring risk.',
    portfolioStrategy: 'Capital Preservation / Outright Avoid',
    pillars: { profitability: 18.0, leverage: 12.5, liquidity: 24.0, efficiency: 32.0, valuation: 35.0 },
  },
}

// Active State
const activeKey = ref<string>('tcs')
const isCustomMode = ref<boolean>(false)
const customScore = ref<number>(88.4)

// Current Score Value
const activeScore = computed(() => {
  if (isCustomMode.value) return customScore.value
  return archetypes[activeKey.value].score
})

// Active Tier Metadata
const currentTierMeta = computed(() => {
  const s = activeScore.value
  if (s >= 80) {
    return {
      tier: 'EXCELLENT',
      scoreRange: '≥ 80',
      color: '#34D399',
      borderClass: 'border-emerald-500/60 shadow-[0_0_15px_rgba(52,211,153,0.3)]',
      bgClass: 'bg-emerald-500/20 text-emerald-300',
      ratingEquiv: 'AAA / AA+',
      solvencyRisk: 'Negligible default risk; top-quartile liquidity buffers and pristine solvency.',
      strategy: 'Overweight / Core Alpha Compounder',
    }
  } else if (s >= 65) {
    return {
      tier: 'STRONG',
      scoreRange: '65–79',
      color: '#10B981',
      borderClass: 'border-teal-500/60 shadow-[0_0_15px_rgba(16,185,129,0.3)]',
      bgClass: 'bg-teal-500/20 text-teal-300',
      ratingEquiv: 'AA / A+',
      solvencyRisk: 'Robust interest coverage; resilient cash flows comfortably absorbing shocks.',
      strategy: 'Long Factor Exposure / Core Hold',
    }
  } else if (s >= 50) {
    return {
      tier: 'MODERATE',
      scoreRange: '50–64',
      color: '#059669',
      borderClass: 'border-emerald-600/60 shadow-[0_0_15px_rgba(5,150,105,0.3)]',
      bgClass: 'bg-emerald-600/20 text-emerald-300',
      ratingEquiv: 'BBB+ / BBB-',
      solvencyRisk: 'Median leverage; operations in-line with broader sector benchmarks.',
      strategy: 'Sector-Neutral Market Weight',
    }
  } else if (s >= 35) {
    return {
      tier: 'WEAK',
      scoreRange: '35–49',
      color: '#F59E0B',
      borderClass: 'border-amber-500/60 shadow-[0_0_15px_rgba(245,158,11,0.3)]',
      bgClass: 'bg-amber-500/20 text-amber-300',
      ratingEquiv: 'BB+ / BB-',
      solvencyRisk: 'Tightening liquidity; elevated debt load with significant margin compression.',
      strategy: 'Underweight / Elevated Risk Watch',
    }
  } else {
    return {
      tier: 'DISTRESSED',
      scoreRange: '< 35',
      color: '#F43F5E',
      borderClass: 'border-rose-500/60 shadow-[0_0_15px_rgba(244,63,94,0.3)]',
      bgClass: 'bg-rose-500/20 text-rose-300',
      ratingEquiv: 'B / C / D',
      solvencyRisk: 'Critical capital deficit; persistent cash drain and near-term default risk.',
      strategy: 'Capital Preservation / Outright Avoid',
    }
  }
})

// Current Pillar Scores (interpolated if in custom mode)
const activePillars = computed(() => {
  if (!isCustomMode.value) {
    return archetypes[activeKey.value].pillars
  }
  const s = customScore.value
  return {
    profitability: Math.min(100, Math.max(0, s * 1.05 - 3)),
    leverage: Math.min(100, Math.max(0, s * 1.10 - 8)),
    liquidity: Math.min(100, Math.max(0, s * 0.95 + 4)),
    efficiency: Math.min(100, Math.max(0, s * 0.92 + 5)),
    valuation: Math.min(100, Math.max(0, s * 0.90 + 6)),
  }
})

function selectArchetype(key: string) {
  isCustomMode.value = false
  activeKey.value = key
}

function enableCustom() {
  isCustomMode.value = true
}

// ==========================================
// SVG Semicircular Speedometer Arc Geometry
// ==========================================
// Center: (150, 130)
// Radius: Outer R=100, Inner R=78 (Thickness 22)
// Angle convention:
// Score 0: 180 deg (Left)
// Score 50: 90 deg (Top)
// Score 100: 0 deg (Right)
const cx = 150
const cy = 135
const rOut = 95
const rIn = 75
const needleLength = 80

function polarToCartesian(centerX: number, centerY: number, radius: number, angleInDegrees: number) {
  const angleInRadians = (angleInDegrees * Math.PI) / 180.0
  return {
    x: centerX + radius * Math.cos(angleInRadians),
    y: centerY - radius * Math.sin(angleInRadians),
  }
}

function describeArcSegment(startScore: number, endScore: number) {
  // Score to angle: angle = 180 - (score / 100) * 180
  // With 1 degree gap for visual elegance
  const startAngle = 180 - (startScore / 100) * 180 - 0.7
  const endAngle = 180 - (endScore / 100) * 180 + 0.7

  const p1 = polarToCartesian(cx, cy, rOut, startAngle)
  const p2 = polarToCartesian(cx, cy, rOut, endAngle)
  const p3 = polarToCartesian(cx, cy, rIn, endAngle)
  const p4 = polarToCartesian(cx, cy, rIn, startAngle)

  const largeArcFlag = Math.abs(endAngle - startAngle) > 180 ? 1 : 0

  return `M ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} A ${rOut} ${rOut} 0 ${largeArcFlag} 1 ${p2.x.toFixed(1)} ${p2.y.toFixed(1)} L ${p3.x.toFixed(1)} ${p3.y.toFixed(1)} A ${rIn} ${rIn} 0 ${largeArcFlag} 0 ${p4.x.toFixed(1)} ${p4.y.toFixed(1)} Z`
}

// 5 Arc Paths
const arcDistressed = computed(() => describeArcSegment(0, 35))
const arcWeak = computed(() => describeArcSegment(35, 50))
const arcModerate = computed(() => describeArcSegment(50, 65))
const arcStrong = computed(() => describeArcSegment(65, 80))
const arcExcellent = computed(() => describeArcSegment(80, 100))

// Needle Coordinates
const needleCoords = computed(() => {
  const score = Math.max(0, Math.min(100, activeScore.value))
  const angleDeg = 180 - (score / 100) * 180
  const tip = polarToCartesian(cx, cy, needleLength, angleDeg)

  // Shoulder width for tapered needle
  const perpAngle1 = angleDeg + 90
  const perpAngle2 = angleDeg - 90
  const shoulderRadius = 6

  const s1 = polarToCartesian(cx, cy, shoulderRadius, perpAngle1)
  const s2 = polarToCartesian(cx, cy, shoulderRadius, perpAngle2)

  // Counter-weight base behind pivot
  const basePoint = polarToCartesian(cx, cy, 14, angleDeg - 180)

  return {
    tip,
    s1,
    s2,
    basePoint,
    path: `M ${s1.x.toFixed(1)} ${s1.y.toFixed(1)} L ${tip.x.toFixed(1)} ${tip.y.toFixed(1)} L ${s2.x.toFixed(1)} ${s2.y.toFixed(1)} L ${basePoint.x.toFixed(1)} ${basePoint.y.toFixed(1)} Z`,
  }
})
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Action & Company Selector Bar -->
    <div class="flex items-center justify-between gap-2 bg-[#071411]/90 px-3 py-1.5 rounded-xl border border-emerald-500/20 mb-2">
      <!-- Company Selector Pills -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Profile:
        </span>
        <button
          v-for="(arch, key) in archetypes"
          :key="key"
          @click="selectArchetype(key)"
          class="px-2 py-0.8 rounded-lg text-[10px] font-semibold font-mono transition-all border flex items-center gap-1"
          :class="!isCustomMode && activeKey === key
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 shadow-[0_0_12px_rgba(52,211,153,0.30)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40 hover:text-slate-200'"
        >
          <span>{{ arch.ticker }}</span>
          <span class="text-[8px] opacity-75 font-normal">({{ arch.score.toFixed(0) }})</span>
        </button>

        <button
          @click="enableCustom"
          class="px-2 py-0.8 rounded-lg text-[10px] font-semibold font-mono transition-all border flex items-center gap-1"
          :class="isCustomMode
            ? 'bg-teal-500/25 text-teal-300 border-teal-500/60 shadow-[0_0_12px_rgba(20,184,166,0.30)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span>Custom Slider</span>
        </button>
      </div>

      <!-- Active Tier Status Badge -->
      <div class="flex items-center gap-2">
        <div class="flex items-center gap-1.5 px-2.5 py-0.8 rounded-lg bg-[#071411] border" :class="currentTierMeta.borderClass">
          <span class="w-2 h-2 rounded-full animate-pulse" :style="{ backgroundColor: currentTierMeta.color }"></span>
          <span class="text-[9px] font-mono text-slate-300">Grade:</span>
          <strong class="text-xs font-black font-mono tracking-wider" :style="{ color: currentTierMeta.color }">
            {{ currentTierMeta.tier }}
          </strong>
          <span class="text-[8.5px] font-mono text-slate-400 border-l border-emerald-500/20 pl-1.5">
            {{ currentTierMeta.ratingEquiv }}
          </span>
        </div>
      </div>
    </div>

    <!-- Main Content Grid: Speedometer Gauge & Pillars (5 Col) vs Credit Health Matrix (7 Col) -->
    <div class="grid grid-cols-12 gap-2.5 mb-2">
      <!-- LEFT COLUMN: Semicircular Speedometer Gauge & 5-Pillar Scores -->
      <div class="col-span-5 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-1 mb-1 border-b border-emerald-500/15">
            <span class="text-xs font-bold text-white font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#34D399]"></span>
              Semicircular Health Meter
            </span>
            <span class="text-[9px] font-mono text-emerald-400">
              Score: {{ activeScore.toFixed(1) }} / 100
            </span>
          </div>

          <!-- Apple-Style Speedometer SVG Stage -->
          <div class="relative bg-[#071411]/95 rounded-lg border border-emerald-500/20 p-1 flex flex-col items-center justify-center">
            <svg class="w-68 h-38" viewBox="30 20 240 135" preserveAspectRatio="xMidYMid meet">
              <defs>
                <!-- Glowing Filter -->
                <filter id="gaugeGlow" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="3" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
                <filter id="needleGlow" x="-30%" y="-30%" width="160%" height="160%">
                  <feGaussianBlur stdDeviation="3.5" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              <!-- Outer Guide Ring -->
              <path
                d="M 50 135 A 100 100 0 0 1 250 135"
                fill="none"
                stroke="rgba(52, 211, 153, 0.12)"
                stroke-width="1"
              />

              <!-- ARC SEGMENT 1: Distressed (< 35) -->
              <path
                :d="arcDistressed"
                fill="#F43F5E"
                :opacity="currentTierMeta.tier === 'DISTRESSED' ? 1.0 : 0.40"
                class="transition-opacity duration-300"
              />

              <!-- ARC SEGMENT 2: Weak (35 - 50) -->
              <path
                :d="arcWeak"
                fill="#F59E0B"
                :opacity="currentTierMeta.tier === 'WEAK' ? 1.0 : 0.40"
                class="transition-opacity duration-300"
              />

              <!-- ARC SEGMENT 3: Moderate (50 - 65) -->
              <path
                :d="arcModerate"
                fill="#059669"
                :opacity="currentTierMeta.tier === 'MODERATE' ? 1.0 : 0.40"
                class="transition-opacity duration-300"
              />

              <!-- ARC SEGMENT 4: Strong (65 - 80) -->
              <path
                :d="arcStrong"
                fill="#10B981"
                :opacity="currentTierMeta.tier === 'STRONG' ? 1.0 : 0.40"
                class="transition-opacity duration-300"
              />

              <!-- ARC SEGMENT 5: Excellent (>= 80) -->
              <path
                :d="arcExcellent"
                fill="#34D399"
                :opacity="currentTierMeta.tier === 'EXCELLENT' ? 1.0 : 0.40"
                class="transition-opacity duration-300"
              />

              <!-- Tick Marks & Numbers -->
              <text x="44" y="146" text-anchor="middle" fill="#94A3B8" font-size="7.5" font-family="monospace">0</text>
              <text x="82" y="66" text-anchor="middle" fill="#F59E0B" font-size="7.5" font-family="monospace">35</text>
              <text x="150" y="32" text-anchor="middle" fill="#34D399" font-size="8" font-weight="bold" font-family="monospace">50</text>
              <text x="218" y="66" text-anchor="middle" fill="#10B981" font-size="7.5" font-family="monospace">65</text>
              <text x="248" y="98" text-anchor="middle" fill="#34D399" font-size="7.5" font-family="monospace">80</text>
              <text x="256" y="146" text-anchor="middle" fill="#94A3B8" font-size="7.5" font-family="monospace">100</text>

              <!-- NEEDLE -->
              <g filter="url(#needleGlow)">
                <path
                  :d="needleCoords.path"
                  :fill="currentTierMeta.color"
                  stroke="#071411"
                  stroke-width="1.2"
                  class="transition-all duration-500 ease-out"
                />
              </g>

              <!-- Pivot Center Hub -->
              <circle :cx="cx" :cy="cy" r="9" fill="#071411" stroke="#34D399" stroke-width="1.8" />
              <circle :cx="cx" :cy="cy" r="4.5" :fill="currentTierMeta.color" />

              <!-- Digital Readout in center arc -->
              <text :x="cx" :y="cy - 16" text-anchor="middle" fill="#F8FAFC" font-size="14" font-family="monospace" font-weight="900">
                {{ activeScore.toFixed(1) }}
              </text>
              <text :x="cx" :y="cy - 31" text-anchor="middle" :fill="currentTierMeta.color" font-size="7" font-family="monospace" font-weight="bold">
                {{ currentTierMeta.tier }}
              </text>
            </svg>
          </div>

          <!-- Custom Slider (Active in Custom Mode) -->
          <div v-if="isCustomMode" class="mt-1.5 bg-[#071411] p-1.5 rounded border border-teal-500/30 font-mono text-[9px]">
            <div class="flex justify-between text-teal-300 mb-0.5">
              <span>Interactive Score Sweep:</span>
              <strong>{{ customScore.toFixed(1) }} pts</strong>
            </div>
            <input
              type="range"
              min="0"
              max="100"
              step="0.5"
              v-model.number="customScore"
              class="w-full accent-teal-400 cursor-pointer h-1 bg-slate-700 rounded"
            />
          </div>

          <!-- 5 Analytical Pillar Breakdown Bars -->
          <div class="mt-2 space-y-1 font-mono text-[8.5px]">
            <div class="text-[9px] font-bold text-slate-300 mb-0.5 flex justify-between">
              <span>Weighted Analytical Pillars (∑ Wₖ = 100%):</span>
              <span class="text-emerald-400">Score</span>
            </div>

            <!-- Pillar 1: Profitability (25%) -->
            <div>
              <div class="flex justify-between text-slate-400 text-[8px] mb-0.2">
                <span>Profitability (W₁ = 25%)</span>
                <span class="text-white">{{ activePillars.profitability.toFixed(1) }} pts</span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div class="h-full bg-emerald-400 rounded-full transition-all duration-500" :style="{ width: `${activePillars.profitability}%` }"></div>
              </div>
            </div>

            <!-- Pillar 2: Leverage & Solvency (25%) -->
            <div>
              <div class="flex justify-between text-slate-400 text-[8px] mb-0.2">
                <span>Solvency &amp; Leverage (W₂ = 25%)</span>
                <span class="text-white">{{ activePillars.leverage.toFixed(1) }} pts</span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div class="h-full bg-teal-400 rounded-full transition-all duration-500" :style="{ width: `${activePillars.leverage}%` }"></div>
              </div>
            </div>

            <!-- Pillar 3: Liquidity Buffer (20%) -->
            <div>
              <div class="flex justify-between text-slate-400 text-[8px] mb-0.2">
                <span>Liquidity Buffer (W₃ = 20%)</span>
                <span class="text-white">{{ activePillars.liquidity.toFixed(1) }} pts</span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div class="h-full bg-cyan-400 rounded-full transition-all duration-500" :style="{ width: `${activePillars.liquidity}%` }"></div>
              </div>
            </div>

            <!-- Pillar 4: Operating Efficiency (15%) -->
            <div>
              <div class="flex justify-between text-slate-400 text-[8px] mb-0.2">
                <span>Operating Efficiency (W₄ = 15%)</span>
                <span class="text-white">{{ activePillars.efficiency.toFixed(1) }} pts</span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div class="h-full bg-emerald-500 rounded-full transition-all duration-500" :style="{ width: `${activePillars.efficiency}%` }"></div>
              </div>
            </div>

            <!-- Pillar 5: Valuation Alignment (15%) -->
            <div>
              <div class="flex justify-between text-slate-400 text-[8px] mb-0.2">
                <span>Valuation Alignment (W₅ = 15%)</span>
                <span class="text-white">{{ activePillars.valuation.toFixed(1) }} pts</span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div class="h-full bg-emerald-600 rounded-full transition-all duration-500" :style="{ width: `${activePillars.valuation}%` }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Synchronized Credit Health Classification Matrix -->
      <div class="col-span-7 flex flex-col justify-between gap-2">
        <!-- Matrix Table Card -->
        <div class="glass-card p-2.5 flex flex-col justify-between">
          <div>
            <!-- Table Header -->
            <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
              <span class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">
                Credit Health Classification Matrix
              </span>
              <span class="text-[8px] px-1.5 py-0.5 bg-emerald-500/15 text-emerald-400 rounded font-mono">
                NSE Migration Calibration
              </span>
            </div>

            <!-- SYNCHRONIZED MATRIX TABLE -->
            <div class="overflow-hidden rounded-lg border border-emerald-500/20 font-mono text-[8.5px]">
              <table class="w-full border-collapse">
                <thead>
                  <tr class="bg-[#071411] text-emerald-400/90 border-b border-emerald-500/20 text-left text-[8px] uppercase">
                    <th class="py-1 px-1.5">Grade</th>
                    <th class="py-1 px-1.5">Score</th>
                    <th class="py-1 px-1.5">Agency Equiv</th>
                    <th class="py-1 px-2">Solvency Risk Profile</th>
                    <th class="py-1 px-2">Portfolio Strategy</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-emerald-500/10">
                  <!-- TIER 1: EXCELLENT -->
                  <tr
                    class="transition-colors duration-200"
                    :class="currentTierMeta.tier === 'EXCELLENT'
                      ? 'bg-emerald-500/20 font-bold border-l-3 border-emerald-400 text-white'
                      : 'hover:bg-slate-800/30 text-slate-300'"
                  >
                    <td class="py-1 px-1.5 text-emerald-300 flex items-center gap-1">
                      <span v-if="currentTierMeta.tier === 'EXCELLENT'" class="text-emerald-400">▶</span>
                      Excellent
                    </td>
                    <td class="py-1 px-1.5 font-bold">≥ 80</td>
                    <td class="py-1 px-1.5 text-emerald-300 font-semibold">AAA / AA+</td>
                    <td class="py-1 px-2 text-[8px] text-slate-300">Negligible default risk; top-quartile cash buffers.</td>
                    <td class="py-1 px-2 text-[8px] text-emerald-300 font-medium">Overweight / Core Alpha</td>
                  </tr>

                  <!-- TIER 2: STRONG -->
                  <tr
                    class="transition-colors duration-200"
                    :class="currentTierMeta.tier === 'STRONG'
                      ? 'bg-teal-500/20 font-bold border-l-3 border-teal-400 text-white'
                      : 'hover:bg-slate-800/30 text-slate-300'"
                  >
                    <td class="py-1 px-1.5 text-teal-300 flex items-center gap-1">
                      <span v-if="currentTierMeta.tier === 'STRONG'" class="text-teal-400">▶</span>
                      Strong
                    </td>
                    <td class="py-1 px-1.5 font-bold">65–79</td>
                    <td class="py-1 px-1.5 text-teal-300 font-semibold">AA / A+</td>
                    <td class="py-1 px-2 text-[8px] text-slate-300">Robust interest coverage; resilient cash flows.</td>
                    <td class="py-1 px-2 text-[8px] text-teal-300 font-medium">Long Factor Exposure</td>
                  </tr>

                  <!-- TIER 3: MODERATE -->
                  <tr
                    class="transition-colors duration-200"
                    :class="currentTierMeta.tier === 'MODERATE'
                      ? 'bg-emerald-600/20 font-bold border-l-3 border-emerald-500 text-white'
                      : 'hover:bg-slate-800/30 text-slate-300'"
                  >
                    <td class="py-1 px-1.5 text-emerald-400 flex items-center gap-1">
                      <span v-if="currentTierMeta.tier === 'MODERATE'" class="text-emerald-400">▶</span>
                      Moderate
                    </td>
                    <td class="py-1 px-1.5 font-bold">50–64</td>
                    <td class="py-1 px-1.5 text-emerald-400 font-semibold">BBB+ / BBB-</td>
                    <td class="py-1 px-2 text-[8px] text-slate-300">Median leverage; in-line sector operations.</td>
                    <td class="py-1 px-2 text-[8px] text-slate-300 font-medium">Sector-Neutral Hold</td>
                  </tr>

                  <!-- TIER 4: WEAK -->
                  <tr
                    class="transition-colors duration-200"
                    :class="currentTierMeta.tier === 'WEAK'
                      ? 'bg-amber-500/20 font-bold border-l-3 border-amber-400 text-white'
                      : 'hover:bg-slate-800/30 text-slate-300'"
                  >
                    <td class="py-1 px-1.5 text-amber-300 flex items-center gap-1">
                      <span v-if="currentTierMeta.tier === 'WEAK'" class="text-amber-400">▶</span>
                      Weak
                    </td>
                    <td class="py-1 px-1.5 font-bold">35–49</td>
                    <td class="py-1 px-1.5 text-amber-300 font-semibold">BB+ / BB-</td>
                    <td class="py-1 px-2 text-[8px] text-slate-300">Tightening liquidity; elevated debt service drag.</td>
                    <td class="py-1 px-2 text-[8px] text-amber-300 font-medium">Underweight / Watch</td>
                  </tr>

                  <!-- TIER 5: DISTRESSED -->
                  <tr
                    class="transition-colors duration-200"
                    :class="currentTierMeta.tier === 'DISTRESSED'
                      ? 'bg-rose-500/20 font-bold border-l-3 border-rose-400 text-white'
                      : 'hover:bg-slate-800/30 text-slate-300'"
                  >
                    <td class="py-1 px-1.5 text-rose-300 flex items-center gap-1">
                      <span v-if="currentTierMeta.tier === 'DISTRESSED'" class="text-rose-400">▶</span>
                      Distressed
                    </td>
                    <td class="py-1 px-1.5 font-bold">&lt; 35</td>
                    <td class="py-1 px-1.5 text-rose-300 font-semibold">B / C / D</td>
                    <td class="py-1 px-2 text-[8px] text-slate-300">Capital deficit drained; critical solvency breach.</td>
                    <td class="py-1 px-2 text-[8px] text-rose-300 font-medium">Preserve / Avoid</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Early Warning Callout Badge -->
            <div class="mt-2 bg-[#071411]/90 p-1.5 rounded border border-emerald-500/25 flex items-start gap-1.5 text-[8.5px] font-mono">
              <span class="text-emerald-400 font-bold text-[10px]">⚡ Early Warning Migration Lead:</span>
              <p class="text-slate-300 leading-tight">
                FinMetrics composite score signals cross-tier downward migration <strong class="text-emerald-300">2 quarters prior</strong> to official rating agency downgrade actions (CRISIL, ICRA).
              </p>
            </div>
          </div>
        </div>

        <!-- Weighted Composite Formula Card -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
              <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
                Composite Weighted Aggregation
              </span>
              <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
                Formula
              </span>
            </div>

            <!-- Formula Box -->
            <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/25 font-mono text-[9.5px] text-emerald-200 leading-tight mb-1">
              <div class="text-emerald-300 font-semibold">
                Score = ∑_{k=1}^5 Wₖ · ( ∑_{i ∈ 𝒫ₖ} w'_{k,i} · S(xᵢ) ) ∈ [0, 100]
              </div>
            </div>

            <!-- Where: Parameter Block -->
            <div class="text-[8px] leading-tight text-slate-300 bg-[#071411]/50 p-1 rounded border border-emerald-500/10">
              <div class="font-bold text-emerald-400 font-mono mb-0.5">Where:</div>
              <ul class="space-y-0.5 text-slate-400 font-mono">
                <li><strong class="text-white font-mono">Wₖ:</strong> Pillar macro weights (Profit: 25%, Leverage: 25%, Liq: 20%, Eff: 15%, Val: 15%)</li>
                <li><strong class="text-white font-mono">𝒫ₖ:</strong> Ratio subset assigned to analytical pillar k</li>
                <li><strong class="text-white font-mono">w'_{k,i}:</strong> Renormalized within-pillar weight ensuring exact 100-pt scale</li>
                <li><strong class="text-white font-mono">S(xᵢ):</strong> Calibrated Sigmoid score bounded in [0, 100]</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Bar -->
    <div class="glass-card px-3 py-1 flex items-center justify-between text-[9px] font-mono">
      <div class="flex items-center gap-2 text-slate-300">
        <span class="text-emerald-400 font-bold">Standardized Credit Calibration:</span>
        <span class="text-slate-400">
          Translates disparate statistical ratio distributions into actionable institutional credit tiers and quantitative portfolio sizing signals.
        </span>
      </div>
      <span class="text-emerald-300 text-[8px] bg-emerald-500/10 border border-emerald-500/25 px-1.5 py-0.5 rounded">
        Slide 13: Health Matrix
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
