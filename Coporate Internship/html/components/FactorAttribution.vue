<script setup lang="ts">
import { ref, computed } from 'vue'

// Factor Item Interface
interface FactorContribution {
  id: string
  name: string
  pillar: string
  macroWeight: number // W_k
  innerWeight: number // w'_{k,i}
  rawValue: string
  peerMedian: string
  score: number // S(x_i) in [0, 100]
  positioning: 'Opportunity' | 'Risk Watch' | 'Neutral'
}

interface AttributionProfile {
  id: string
  ticker: string
  name: string
  score: number
  tier: string
  factors: FactorContribution[]
}

const profiles: Record<string, AttributionProfile> = {
  tcs: {
    id: 'tcs',
    ticker: 'TCS',
    name: 'Tata Consultancy Services',
    score: 88.4,
    tier: 'EXCELLENT',
    factors: [
      { id: 'f1', name: 'Operating Margin', pillar: 'Profitability', macroWeight: 0.25, innerWeight: 0.40, rawValue: '26.8%', peerMedian: '18.0%', score: 84.5, positioning: 'Opportunity' },
      { id: 'f2', name: 'Net Debt / Equity', pillar: 'Leverage', macroWeight: 0.25, innerWeight: 0.40, rawValue: '0.00x', peerMedian: '0.80x', score: 98.0, positioning: 'Opportunity' },
      { id: 'f3', name: 'Return on Equity', pillar: 'Profitability', macroWeight: 0.25, innerWeight: 0.35, rawValue: '48.2%', peerMedian: '15.0%', score: 82.0, positioning: 'Opportunity' },
      { id: 'f4', name: 'Cash Flow Margin', pillar: 'Liquidity', macroWeight: 0.20, innerWeight: 0.45, rawValue: '22.4%', peerMedian: '12.0%', score: 91.0, positioning: 'Opportunity' },
      { id: 'f5', name: 'Asset Turnover', pillar: 'Efficiency', macroWeight: 0.15, innerWeight: 0.50, rawValue: '1.45x', peerMedian: '1.05x', score: 81.5, positioning: 'Opportunity' },
    ],
  },
  tatamotors: {
    id: 'tatamotors',
    ticker: 'TATA MOTORS',
    name: 'Tata Motors Limited',
    score: 56.5,
    tier: 'MODERATE',
    factors: [
      { id: 'f1', name: 'Operating Margin', pillar: 'Profitability', macroWeight: 0.25, innerWeight: 0.40, rawValue: '19.2%', peerMedian: '18.0%', score: 56.0, positioning: 'Neutral' },
      { id: 'f2', name: 'Net Debt / Equity', pillar: 'Leverage', macroWeight: 0.25, innerWeight: 0.40, rawValue: '1.25x', peerMedian: '0.80x', score: 37.0, positioning: 'Risk Watch' },
      { id: 'f3', name: 'Return on Equity', pillar: 'Profitability', macroWeight: 0.25, innerWeight: 0.35, rawValue: '17.8%', peerMedian: '15.0%', score: 62.5, positioning: 'Neutral' },
      { id: 'f4', name: 'Cash Flow Margin', pillar: 'Liquidity', macroWeight: 0.20, innerWeight: 0.45, rawValue: '11.8%', peerMedian: '12.0%', score: 49.5, positioning: 'Neutral' },
      { id: 'f5', name: 'Asset Turnover', pillar: 'Efficiency', macroWeight: 0.15, innerWeight: 0.50, rawValue: '1.40x', peerMedian: '1.05x', score: 69.5, positioning: 'Opportunity' },
    ],
  },
  distressed: {
    id: 'distressed',
    ticker: 'DISTRESSED INFRA',
    name: 'Stressed EPC Firm',
    score: 22.8,
    tier: 'DISTRESSED',
    factors: [
      { id: 'f1', name: 'Operating Margin', pillar: 'Profitability', macroWeight: 0.25, innerWeight: 0.40, rawValue: '4.5%', peerMedian: '18.0%', score: 22.5, positioning: 'Risk Watch' },
      { id: 'f2', name: 'Net Debt / Equity', pillar: 'Leverage', macroWeight: 0.25, innerWeight: 0.40, rawValue: '3.80x', peerMedian: '0.80x', score: 12.0, positioning: 'Risk Watch' },
      { id: 'f3', name: 'Return on Equity', pillar: 'Profitability', macroWeight: 0.25, innerWeight: 0.35, rawValue: '-8.5%', peerMedian: '15.0%', score: 28.0, positioning: 'Risk Watch' },
      { id: 'f4', name: 'Cash Flow Margin', pillar: 'Liquidity', macroWeight: 0.20, innerWeight: 0.45, rawValue: '-4.2%', peerMedian: '12.0%', score: 19.5, positioning: 'Risk Watch' },
      { id: 'f5', name: 'Asset Turnover', pillar: 'Efficiency', macroWeight: 0.15, innerWeight: 0.50, rawValue: '0.55x', peerMedian: '1.05x', score: 32.0, positioning: 'Risk Watch' },
    ],
  },
}

// Active State
const activeProfileKey = ref<string>('tcs')
const hoveredFactor = ref<any | null>(null)

// Current Profile
const currentProfile = computed(() => profiles[activeProfileKey.value])

// Calculate Factor Deltas: ΔS_i = W_k · w'_{k,i} · (S(x_i) - 50.0)
const calculatedFactors = computed(() => {
  return currentProfile.value.factors.map(f => {
    const effectiveWeight = f.macroWeight * f.innerWeight
    const scoreDiff = f.score - 50.0
    const delta = effectiveWeight * scoreDiff
    return {
      ...f,
      effectiveWeight,
      scoreDiff,
      delta,
      deltaFormatted: `${delta >= 0 ? '+' : ''}${delta.toFixed(2)} pts`,
      isPositive: delta >= 0,
    }
  })
})

// Net Delta
const netDelta = computed(() => {
  return calculatedFactors.value.reduce((acc, f) => acc + f.delta, 0)
})

// Reconstructed Composite Score from Waterfall: 50 + sum(Delta)
const reconstructedScore = computed(() => {
  return 50.0 + netDelta.value
})

// Waterfall Steps Geometry for SVG
// Baseline = 50 pts
// Running score starts at 50
interface WaterfallBar {
  label: string
  sublabel: string
  startVal: number
  endVal: number
  delta: number
  isTotal: boolean
  isBase: boolean
  isPositive: boolean
  color: string
}

const waterfallBars = computed<WaterfallBar[]>(() => {
  const bars: WaterfallBar[] = []

  // 1. Base Benchmark Bar (Sector Median = 50.0)
  bars.push({
    label: 'Median',
    sublabel: 'Base (50)',
    startVal: 0,
    endVal: 50.0,
    delta: 50.0,
    isTotal: false,
    isBase: true,
    isPositive: true,
    color: '#059669',
  })

  // 2. Factor Increments
  let running = 50.0
  for (const f of calculatedFactors.value) {
    const start = running
    const end = running + f.delta
    bars.push({
      label: f.name.replace('Operating ', 'Op. ').replace('Return on ', 'RO').replace('Net Debt / ', 'D/'),
      sublabel: f.pillar,
      startVal: start,
      endVal: end,
      delta: f.delta,
      isTotal: false,
      isBase: false,
      isPositive: f.delta >= 0,
      color: f.delta >= 0 ? '#34D399' : '#F43F5E',
    })
    running = end
  }

  // 3. Final Composite Score Bar
  bars.push({
    label: 'Final Score',
    sublabel: currentProfile.value.ticker,
    startVal: 0,
    endVal: running,
    delta: running - 50.0,
    isTotal: true,
    isBase: false,
    isPositive: running >= 50.0,
    color: running >= 65 ? '#00E599' : running >= 50 ? '#10B981' : '#F59E0B',
  })

  return bars
})

// SVG Dimensions
const svgW = 480
const svgH = 195
const padL = 36
const padR = 15
const padT = 20
const padB = 40
const plotW = svgW - padL - padR
const plotH = svgH - padT - padB

function scoreToY(score: number): number {
  const clamped = Math.max(0, Math.min(100, score))
  return padT + plotH - (clamped / 100) * plotH
}

const barWidth = 44
const barStep = plotW / 7

function barX(index: number): number {
  return padL + index * barStep + (barStep - barWidth) / 2
}

// Strategy Long/Short Simulation Metrics
const strategyMetrics = {
  spreadAlpha: '+14.8%',
  longReturn: '+21.3%',
  shortReturn: '+6.5%',
  sharpeRatio: '1.74',
  benchmarkSharpe: '0.92',
  maxDrawdown: '-11.2%',
  benchmarkDrawdown: '-23.5%',
}
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between text-slate-100 select-none pb-0.5">
    <!-- Top Action & Profile Switcher Bar -->
    <div class="flex items-center justify-between gap-2 bg-[#071411]/90 px-3 py-1.5 rounded-xl border border-emerald-500/20 mb-2">
      <!-- Profile Buttons -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 mr-1">
          Entity Profile:
        </span>
        <button
          @click="activeProfileKey = 'tcs'"
          class="px-2.5 py-0.8 rounded-lg text-[10px] font-semibold font-mono transition-all border flex items-center gap-1.5"
          :class="activeProfileKey === 'tcs'
            ? 'bg-emerald-500/25 text-emerald-300 border-emerald-500/60 shadow-[0_0_12px_rgba(52,211,153,0.30)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          <span>TCS (Alpha Driver: +38.4)</span>
        </button>

        <button
          @click="activeProfileKey = 'tatamotors'"
          class="px-2.5 py-0.8 rounded-lg text-[10px] font-semibold font-mono transition-all border flex items-center gap-1.5"
          :class="activeProfileKey === 'tatamotors'
            ? 'bg-teal-500/25 text-teal-300 border-teal-500/60 shadow-[0_0_12px_rgba(20,184,166,0.30)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-teal-400"></span>
          <span>Tata Motors (Balanced: +6.5)</span>
        </button>

        <button
          @click="activeProfileKey = 'distressed'"
          class="px-2.5 py-0.8 rounded-lg text-[10px] font-semibold font-mono transition-all border flex items-center gap-1.5"
          :class="activeProfileKey === 'distressed'
            ? 'bg-rose-500/25 text-rose-300 border-rose-500/60 shadow-[0_0_12px_rgba(244,63,94,0.30)]'
            : 'bg-[#0d211b]/80 text-slate-400 border-emerald-500/15 hover:border-emerald-500/40'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-rose-400 animate-pulse"></span>
          <span>Distressed EPC (Drag: -27.2)</span>
        </button>
      </div>

      <!-- Net Composite Delta Readout -->
      <div class="flex items-center gap-2">
        <div class="flex items-center gap-1.5 px-2.5 py-0.8 rounded-lg bg-[#071411] border border-emerald-500/30">
          <span class="text-[9px] font-mono text-slate-400">Net Delta (ΔS):</span>
          <strong
            class="text-xs font-black font-mono tracking-tight"
            :class="netDelta >= 0 ? 'text-emerald-300' : 'text-rose-400'"
          >
            {{ netDelta >= 0 ? '+' : '' }}{{ netDelta.toFixed(1) }} pts
          </strong>
          <span class="text-[8.5px] font-mono text-slate-400 border-l border-emerald-500/20 pl-1.5">
            ➔ Score: <span class="text-white font-bold">{{ reconstructedScore.toFixed(1) }}</span>
          </span>
        </div>
      </div>
    </div>

    <!-- Main Content Grid: Waterfall Chart (7 Col) vs Strategy & Badges (5 Col) -->
    <div class="grid grid-cols-12 gap-2.5 mb-2">
      <!-- LEFT COLUMN: Interactive Factor Delta Waterfall Bar Chart -->
      <div class="col-span-7 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-1 mb-1 border-b border-emerald-500/15">
            <span class="text-xs font-bold text-white font-mono flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#34D399]"></span>
              Factor Delta Waterfall Attribution
            </span>
            <div class="flex items-center gap-2 text-[8px] font-mono">
              <span class="flex items-center gap-1 text-emerald-400">
                <span class="w-2 h-2 rounded bg-emerald-400"></span> Alpha Driver (+ΔS)
              </span>
              <span class="flex items-center gap-1 text-rose-400">
                <span class="w-2 h-2 rounded bg-rose-500"></span> Risk Drag (-ΔS)
              </span>
            </div>
          </div>

          <!-- SVG Waterfall Chart Stage -->
          <div class="relative bg-[#071411]/95 rounded-lg border border-emerald-500/20 p-1">
            <svg class="w-full h-42" viewBox="0 0 480 195" preserveAspectRatio="xMidYMid meet">
              <defs>
                <filter id="waterfallGlow" x="-20%" y="-20%" width="140%" height="140%">
                  <feGaussianBlur stdDeviation="3" result="blur" />
                  <feComposite in="SourceGraphic" in2="blur" operator="over" />
                </filter>
              </defs>

              <!-- Reference Horizontal Lines -->
              <!-- 100 pts -->
              <line :x1="padL" :y1="scoreToY(100)" :x2="svgW - padR" :y2="scoreToY(100)" stroke="#64748B" stroke-width="0.6" stroke-dasharray="2,2" opacity="0.4" />
              <text :x="padL - 4" :y="scoreToY(100) + 3" text-anchor="end" fill="#64748B" font-size="7.5" font-family="monospace">100</text>

              <!-- Median Benchmark 50.0 pts (Bold line) -->
              <line :x1="padL" :y1="scoreToY(50)" :x2="svgW - padR" :y2="scoreToY(50)" stroke="rgba(52, 211, 153, 0.45)" stroke-width="1.2" stroke-dasharray="3,3" />
              <text :x="padL - 4" :y="scoreToY(50) + 3" text-anchor="end" fill="#34D399" font-size="8" font-weight="bold" font-family="monospace">50</text>

              <!-- 0 pts -->
              <line :x1="padL" :y1="scoreToY(0)" :x2="svgW - padR" :y2="scoreToY(0)" stroke="#64748B" stroke-width="0.8" opacity="0.6" />
              <text :x="padL - 4" :y="scoreToY(0) + 3" text-anchor="end" fill="#64748B" font-size="7.5" font-family="monospace">0</text>

              <!-- WATERFALL BARS -->
              <g v-for="(bar, idx) in waterfallBars" :key="idx">
                <!-- Bar Rectangle -->
                <rect
                  :x="barX(idx)"
                  :y="scoreToY(Math.max(bar.startVal, bar.endVal))"
                  :width="barWidth"
                  :height="Math.max(3, Math.abs(scoreToY(bar.startVal) - scoreToY(bar.endVal)))"
                  :rx="4"
                  :fill="bar.color"
                  :stroke="bar.isTotal ? '#00E599' : '#071411'"
                  :stroke-width="bar.isTotal ? 1.5 : 1"
                  :opacity="bar.isBase ? 0.75 : 0.90"
                  class="transition-all duration-300"
                />

                <!-- Connecting Dashed Line to Next Bar -->
                <line
                  v-if="idx < waterfallBars.length - 1"
                  :x1="barX(idx) + barWidth"
                  :y1="scoreToY(bar.endVal)"
                  :x2="barX(idx + 1)"
                  :y2="scoreToY(bar.endVal)"
                  stroke="#94A3B8"
                  stroke-width="0.8"
                  stroke-dasharray="2,2"
                  opacity="0.6"
                />

                <!-- Value Badge on Bar -->
                <text
                  :x="barX(idx) + barWidth / 2"
                  :y="scoreToY(Math.max(bar.startVal, bar.endVal)) - 3"
                  text-anchor="middle"
                  :fill="bar.isTotal ? '#00E599' : bar.delta >= 0 ? '#34D399' : '#F43F5E'"
                  font-size="7.5"
                  font-weight="bold"
                  font-family="monospace"
                >
                  <tspan v-if="bar.isBase">50.0</tspan>
                  <tspan v-else-if="bar.isTotal">{{ bar.endVal.toFixed(1) }}</tspan>
                  <tspan v-else>{{ bar.delta >= 0 ? '+' : '' }}{{ bar.delta.toFixed(1) }}</tspan>
                </text>

                <!-- Factor Label Under X-Axis -->
                <text
                  :x="barX(idx) + barWidth / 2"
                  :y="svgH - padB + 13"
                  text-anchor="middle"
                  fill="#F8FAFC"
                  font-size="7.2"
                  font-family="monospace"
                  font-weight="bold"
                >
                  {{ bar.label }}
                </text>
                <text
                  :x="barX(idx) + barWidth / 2"
                  :y="svgH - padB + 23"
                  text-anchor="middle"
                  fill="#94A3B8"
                  font-size="6.5"
                  font-family="monospace"
                >
                  {{ bar.sublabel }}
                </text>
              </g>
            </svg>
          </div>
        </div>

        <!-- Metric Details Table for Active Entity -->
        <div class="mt-2 bg-[#071411]/90 rounded border border-emerald-500/20 overflow-hidden font-mono text-[8px]">
          <div class="grid grid-cols-12 bg-[#0d211b] text-emerald-400 font-bold px-1.5 py-0.5 border-b border-emerald-500/20">
            <span class="col-span-3">Financial Metric</span>
            <span class="col-span-2 text-center">Raw Value</span>
            <span class="col-span-2 text-center">Peer Med</span>
            <span class="col-span-2 text-center">Score S(x)</span>
            <span class="col-span-3 text-right">Attribution (ΔSᵢ)</span>
          </div>
          <div
            v-for="f in calculatedFactors"
            :key="f.id"
            class="grid grid-cols-12 px-1.5 py-0.8 border-b border-emerald-500/10 hover:bg-slate-800/25 items-center"
          >
            <span class="col-span-3 text-slate-200 font-medium truncate">{{ f.name }}</span>
            <span class="col-span-2 text-center text-white font-semibold">{{ f.rawValue }}</span>
            <span class="col-span-2 text-center text-slate-400">{{ f.peerMedian }}</span>
            <span class="col-span-2 text-center text-emerald-300">{{ f.score.toFixed(1) }}</span>
            <span
              class="col-span-3 text-right font-bold"
              :class="f.delta >= 0 ? 'text-emerald-300' : 'text-rose-400'"
            >
              {{ f.deltaFormatted }}
            </span>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Mathematical Attribution Card & Long/Short Strategy Visualizer -->
      <div class="col-span-5 flex flex-col justify-between gap-2">
        <!-- CARD 1: Factor Delta Formulation Card -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-emerald-500/15">
              <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
                Factor Delta Attribution (ΔSᵢ)
              </span>
              <span class="text-[8px] px-1 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
                Decomposition
              </span>
            </div>

            <!-- Mathematical Formula Box -->
            <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/25 font-mono text-[9px] text-emerald-200 leading-tight mb-1">
              <div class="text-emerald-300 font-semibold">
                ΔSᵢ = Wₖ · w'_{k,i} × ( S(xᵢ) - 50.0 )
              </div>
              <div class="text-[7.5px] text-slate-400 mt-0.5">
                Composite Score = 50.0 + ∑ᵢ ΔSᵢ
              </div>
            </div>

            <!-- Where: Parameter Block -->
            <div class="text-[8px] leading-tight text-slate-300 bg-[#071411]/50 p-1 rounded border border-emerald-500/10 mb-1">
              <div class="font-bold text-emerald-400 font-mono mb-0.5">Where:</div>
              <ul class="space-y-0.5 text-slate-400 font-mono">
                <li><strong class="text-white font-mono">Wₖ · w'_{k,i}:</strong> Joint hierarchical weight of ratio i in pillar k</li>
                <li><strong class="text-white font-mono">50.0:</strong> Invariant neutral sector median performance baseline</li>
                <li><strong class="text-white font-mono">ΔSᵢ &gt; 0:</strong> Alpha driver outperforming median peer benchmark</li>
                <li><strong class="text-white font-mono">ΔSᵢ &lt; 0:</strong> Fundamental drag pinpointing capital destruction</li>
              </ul>
            </div>

            <!-- Empirical Positioning Badges Block -->
            <div class="bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20 font-mono text-[8px]">
              <div class="font-bold text-slate-300 mb-1">Empirical Factor Positioning Triage:</div>
              <div class="grid grid-cols-3 gap-1 text-center">
                <div class="bg-emerald-500/15 border border-emerald-500/40 p-1 rounded">
                  <div class="text-emerald-300 font-bold">Opportunity</div>
                  <div class="text-slate-400 text-[7px]">xᵢ ≥ Q₃ (Top 25%)</div>
                </div>
                <div class="bg-slate-800/60 border border-slate-700/60 p-1 rounded">
                  <div class="text-slate-300 font-bold">Neutral</div>
                  <div class="text-slate-400 text-[7px]">Q₁ &lt; xᵢ &lt; Q₃</div>
                </div>
                <div class="bg-rose-500/15 border border-rose-500/40 p-1 rounded">
                  <div class="text-rose-300 font-bold">Risk Watch</div>
                  <div class="text-slate-400 text-[7px]">xᵢ ≤ Q₁ (Bottom 25%)</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- CARD 2: Systematic Long/Short Factor Strategy -->
        <div class="glass-card p-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-0.5 mb-1 border-b border-teal-500/15">
              <span class="text-[10px] font-bold text-teal-300 uppercase tracking-wider font-mono">
                Systematic Long/Short Strategy
              </span>
              <span class="text-[8px] px-1 py-0.2 bg-teal-500/15 text-teal-300 rounded font-mono">
                Factor Portfolio
              </span>
            </div>

            <!-- Strategy Architecture Description -->
            <p class="text-[8px] text-slate-400 mb-1 leading-tight">
              Quintile long/short equity portfolio constructed from 5-pillar composite health scores across 150+ NSE equities:
            </p>

            <!-- Quintile Visualizer Bar -->
            <div class="grid grid-cols-5 gap-1 text-center font-mono text-[7.5px] mb-1.5">
              <div class="bg-rose-500/20 border border-rose-500/50 p-1 rounded text-rose-300">
                <div class="font-bold">Q1: Short</div>
                <div class="text-[6.5px] text-slate-400">Distressed (&lt;35)</div>
              </div>
              <div class="bg-amber-500/15 border border-amber-500/30 p-1 rounded text-amber-300">
                <div class="font-bold">Q2: Under</div>
                <div class="text-[6.5px] text-slate-400">Weak (35-49)</div>
              </div>
              <div class="bg-slate-800 border border-slate-700 p-1 rounded text-slate-400">
                <div class="font-bold">Q3: Neutral</div>
                <div class="text-[6.5px] text-slate-400">Median (50-64)</div>
              </div>
              <div class="bg-teal-500/15 border border-teal-500/30 p-1 rounded text-teal-300">
                <div class="font-bold">Q4: Over</div>
                <div class="text-[6.5px] text-slate-400">Strong (65-79)</div>
              </div>
              <div class="bg-emerald-500/25 border border-emerald-500/60 p-1 rounded text-emerald-300 font-bold shadow-[0_0_8px_rgba(52,211,153,0.25)]">
                <div>Q5: Long</div>
                <div class="text-[6.5px] text-slate-300">Pristine (≥80)</div>
              </div>
            </div>

            <!-- Empirical Performance Simulation Grid -->
            <div class="grid grid-cols-3 gap-1 bg-[#071411]/90 p-1.5 rounded border border-emerald-500/20 font-mono text-[8.5px]">
              <div class="text-center border-r border-emerald-500/15 pr-1">
                <div class="text-[7px] text-slate-400">Alpha Spread</div>
                <div class="text-emerald-300 font-bold text-[10px]">{{ strategyMetrics.spreadAlpha }}</div>
                <div class="text-[6.5px] text-slate-500">Long - Short</div>
              </div>
              <div class="text-center border-r border-emerald-500/15 px-1">
                <div class="text-[7px] text-slate-400">Sharpe Ratio</div>
                <div class="text-teal-300 font-bold text-[10px]">{{ strategyMetrics.sharpeRatio }}</div>
                <div class="text-[6.5px] text-slate-500">vs Index 0.92</div>
              </div>
              <div class="text-center pl-1">
                <div class="text-[7px] text-slate-400">Max Drawdown</div>
                <div class="text-emerald-400 font-bold text-[10px]">{{ strategyMetrics.maxDrawdown }}</div>
                <div class="text-[6.5px] text-slate-500">vs Index -23.5%</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Bar -->
    <div class="glass-card px-3 py-1 flex items-center justify-between text-[9px] font-mono">
      <div class="flex items-center gap-2 text-slate-300">
        <span class="text-emerald-400 font-bold">Systematic Factor Utility:</span>
        <span class="text-slate-400">
          Decomposes composite performance into actionable ratio-level alpha drivers and delivers institutional quantitative screening for long/short factor portfolios.
        </span>
      </div>
      <span class="text-emerald-300 text-[8px] bg-emerald-500/10 border border-emerald-500/25 px-1.5 py-0.5 rounded">
        Slide 14: Portfolio Attribution
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
