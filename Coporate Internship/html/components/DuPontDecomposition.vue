<script setup lang="ts">
import { ref, computed } from 'vue'

// Stage Mode: 3-Stage vs 5-Stage
const stageMode = ref<'3stage' | '5stage'>('5stage')

// Sector Preset Profiles
type SectorKey = 'it' | 'utilities' | 'fmcg' | 'distressed' | 'sandbox'
const activeSector = ref<SectorKey>('it')

// Model Factors State
const taxBurden = ref<number>(0.74) // NI / EBT (74% retained)
const interestBurden = ref<number>(1.00) // EBT / EBIT (1.00 = debt-free)
const operatingMargin = ref<number>(0.245) // EBIT / Sales (24.5%)
const assetTurnover = ref<number>(1.05) // Sales / Assets (1.05x)
const equityMultiplier = ref<number>(1.25) // Assets / Equity (1.25x)

// Computed 3-Stage Net Margin (Tax * Interest * Operating Margin)
const netMargin = computed(() => {
  return taxBurden.value * interestBurden.value * operatingMargin.value
})

// Computed Return on Equity (ROE)
const roe = computed(() => {
  return netMargin.value * assetTurnover.value * equityMultiplier.value
})

// Return on Assets (ROA)
const roa = computed(() => {
  return netMargin.value * assetTurnover.value
})

// Early Warning Flag: Leverage Overhang Warning
// Flagged when Equity Multiplier >= 3.5 AND (Operating Margin < 0.12 OR Interest Burden < 0.65)
const isLeverageOverhang = computed(() => {
  return equityMultiplier.value >= 3.5 && (operatingMargin.value < 0.12 || interestBurden.value < 0.65)
})

// Qualitative Diagnostic Assessment
const diagnosticAssessment = computed(() => {
  if (isLeverageOverhang.value) {
    return {
      severity: 'critical',
      badge: '⚠️ LEVERAGE OVERHANG DETECTED',
      badgeClass: 'bg-rose-500/20 text-rose-300 border-rose-500/50 animate-pulse',
      headline: 'Masked Operational Decay via Balance Sheet Gearing',
      detail: `Headline ROE (${(roe.value * 100).toFixed(1)}%) is artificially sustained by extreme financial leverage (EM = ${equityMultiplier.value.toFixed(2)}x) despite compressed operating margins (${(operatingMargin.value * 100).toFixed(1)}%) and high debt-service drag (${((1 - interestBurden.value) * 100).toFixed(0)}% of EBIT). Highly vulnerable to interest rate repricing.`,
    }
  } else if (equityMultiplier.value < 1.5 && operatingMargin.value > 0.18) {
    return {
      severity: 'pristine',
      badge: '✓ HIGH-QUALITY UNLEVERED ROE',
      badgeClass: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50',
      headline: 'Organic Pricing Power & Zero Balance Sheet Drag',
      detail: `Elite ROE (${(roe.value * 100).toFixed(1)}%) generated organically through robust operating margins (${(operatingMargin.value * 100).toFixed(1)}%) and near-zero debt burden (Interest Burden = ${interestBurden.value.toFixed(2)}). Immune to systemic credit contractions.`,
    }
  } else if (assetTurnover.value > 1.8) {
    return {
      severity: 'turnover',
      badge: '✓ ELITE ASSET VELOCITY DRIVER',
      badgeClass: 'bg-teal-500/20 text-teal-300 border-teal-500/50',
      headline: 'Rapid Working Capital & Throughput Velocity',
      detail: `Superior asset turnover (${assetTurnover.value.toFixed(2)}x) drives strong ROE (${(roe.value * 100).toFixed(1)}%) with conservative financial leverage (EM = ${equityMultiplier.value.toFixed(2)}x). Exemplifies consumer retail and FMCG supply chain excellence.`,
    }
  } else {
    return {
      severity: 'balanced',
      badge: 'BALANCED CAPITAL PROFILE',
      badgeClass: 'bg-sky-500/20 text-sky-300 border-sky-500/50',
      headline: 'Moderate Operational Margins with Stable Gearing',
      detail: `ROE of ${(roe.value * 100).toFixed(1)}% reflects typical industrial capital structure with balanced asset utilization and manageable debt-service coverage.`,
    }
  }
})

// Apply Sector Profile
function selectSector(sector: SectorKey) {
  activeSector.value = sector
  if (sector === 'it') {
    taxBurden.value = 0.74
    interestBurden.value = 1.00
    operatingMargin.value = 0.245
    assetTurnover.value = 1.05
    equityMultiplier.value = 1.25
  } else if (sector === 'utilities') {
    taxBurden.value = 0.78
    interestBurden.value = 0.52
    operatingMargin.value = 0.120
    assetTurnover.value = 0.45
    equityMultiplier.value = 4.20
  } else if (sector === 'fmcg') {
    taxBurden.value = 0.75
    interestBurden.value = 0.98
    operatingMargin.value = 0.182
    assetTurnover.value = 2.10
    equityMultiplier.value = 1.40
  } else if (sector === 'distressed') {
    taxBurden.value = 0.82
    interestBurden.value = 0.40
    operatingMargin.value = 0.055
    assetTurnover.value = 0.50
    equityMultiplier.value = 6.80
  }
}
</script>

<template>
  <div class="w-full h-full flex flex-col justify-between py-0.5 text-slate-100 select-none">
    <!-- Top Bar: Model Mode Toggle & Sector Case Presets -->
    <div class="flex items-center justify-between gap-3 px-3 py-1.5 glass-card">
      <!-- Sector Presets -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] font-mono uppercase tracking-wider text-emerald-400 font-bold mr-1">
          Sector Case:
        </span>
        <button
          class="px-2 py-0.8 rounded text-[11px] font-bold transition cursor-pointer"
          :class="activeSector === 'it'
            ? 'bg-emerald-500/30 text-white border border-emerald-400/50 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
            : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40 border border-transparent'"
          @click="selectSector('it')"
        >
          IT Services (TCS)
        </button>
        <button
          class="px-2 py-0.8 rounded text-[11px] font-bold transition cursor-pointer"
          :class="activeSector === 'utilities'
            ? 'bg-purple-500/30 text-white border border-purple-400/50 shadow-[0_0_8px_rgba(168,85,247,0.3)]'
            : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40 border border-transparent'"
          @click="selectSector('utilities')"
        >
          Utilities (Adani/Tata)
        </button>
        <button
          class="px-2 py-0.8 rounded text-[11px] font-bold transition cursor-pointer"
          :class="activeSector === 'fmcg'
            ? 'bg-teal-500/30 text-white border border-teal-400/50 shadow-[0_0_8px_rgba(20,184,166,0.3)]'
            : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40 border border-transparent'"
          @click="selectSector('fmcg')"
        >
          FMCG (HUL/Trent)
        </button>
        <button
          class="px-2 py-0.8 rounded text-[11px] font-bold transition cursor-pointer"
          :class="activeSector === 'distressed'
            ? 'bg-rose-500/30 text-white border border-rose-400/50 shadow-[0_0_8px_rgba(244,63,94,0.3)]'
            : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40 border border-transparent'"
          @click="selectSector('distressed')"
        >
          Distressed Levered
        </button>
        <button
          class="px-2 py-0.8 rounded text-[11px] font-bold transition cursor-pointer"
          :class="activeSector === 'sandbox'
            ? 'bg-cyan-500/30 text-white border border-cyan-400/50 shadow-[0_0_8px_rgba(6,182,212,0.3)]'
            : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40 border border-transparent'"
          @click="activeSector = 'sandbox'"
        >
          Manual Sandbox
        </button>
      </div>

      <!-- 3-Stage vs 5-Stage Toggle -->
      <div class="flex items-center gap-1 bg-[#071411]/80 p-0.5 rounded-lg border border-emerald-500/20">
        <button
          class="px-2.5 py-1 rounded text-[10px] font-bold transition cursor-pointer"
          :class="stageMode === '3stage'
            ? 'bg-emerald-500/30 text-emerald-300 shadow-sm'
            : 'text-slate-400 hover:text-slate-200'"
          @click="stageMode = '3stage'"
        >
          3-Stage Model
        </button>
        <button
          class="px-2.5 py-1 rounded text-[10px] font-bold transition cursor-pointer flex items-center gap-1"
          :class="stageMode === '5stage'
            ? 'bg-emerald-500/30 text-emerald-300 shadow-sm'
            : 'text-slate-400 hover:text-slate-200'"
          @click="stageMode = '5stage'"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
          <span>5-Stage Extended</span>
        </button>
      </div>
    </div>

    <!-- MAIN BODY GRID: Branching Tree (Left) vs Diagnostics & Controls (Right) -->
    <div class="grid grid-cols-12 gap-2.5 my-1.5 items-stretch">
      <!-- Left Column: Interactive Branching Decomposition Tree -->
      <div class="col-span-7 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Tree Header -->
          <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-emerald-500/15">
            <span class="text-xs font-bold text-white flex items-center gap-1.5">
              <span>Branching Tree:</span>
              <span class="text-emerald-300">{{ stageMode === '3stage' ? 'Classical 3-Factor' : 'Extended 5-Factor' }} Identity</span>
            </span>
            <span class="text-[10px] font-mono text-emerald-400">
              ROE = {{ (roe * 100).toFixed(1) }}%
            </span>
          </div>

          <!-- ROOT NODE: Return on Equity (ROE) -->
          <div class="flex justify-center mb-1.5">
            <div class="bg-gradient-to-r from-emerald-950/80 via-teal-950/80 to-emerald-950/80 border border-emerald-400/50 rounded-lg px-4 py-1.5 text-center shadow-[0_0_15px_rgba(52,211,153,0.2)]">
              <div class="text-[9px] font-mono text-slate-300 uppercase tracking-wider">
                Target Metric: Return on Equity (ROE)
              </div>
              <div class="text-lg font-black text-white font-mono tracking-tight">
                {{ (roe * 100).toFixed(1) }}%
              </div>
              <div class="text-[8.5px] font-mono text-emerald-300">
                Net Income / Shareholders Equity
              </div>
            </div>
          </div>

          <!-- SVG CONNECTING BRANCHES -->
          <div class="w-full flex justify-center -my-1">
            <svg class="w-full h-5" viewBox="0 0 500 20" preserveAspectRatio="none">
              <!-- Central Stem from Root -->
              <line x1="250" y1="0" x2="250" y2="8" stroke="#34D399" stroke-width="1.5" />
              <!-- Horizontal Distribution Bar -->
              <line
                :x1="stageMode === '3stage' ? 85 : 50"
                y1="8"
                :x2="stageMode === '3stage' ? 415 : 450"
                y2="8"
                stroke="#34D399"
                stroke-width="1.5"
                stroke-dasharray="2 2"
              />
              <!-- Vertical Drops into Factor Nodes -->
              <g v-if="stageMode === '3stage'">
                <line x1="85" y1="8" x2="85" y2="20" stroke="#34D399" stroke-width="1.5" />
                <line x1="250" y1="8" x2="250" y2="20" stroke="#34D399" stroke-width="1.5" />
                <line x1="415" y1="8" x2="415" y2="20" stroke="#34D399" stroke-width="1.5" />
              </g>
              <g v-else>
                <line x1="50" y1="8" x2="50" y2="20" stroke="#34D399" stroke-width="1.5" />
                <line x1="150" y1="8" x2="150" y2="20" stroke="#34D399" stroke-width="1.5" />
                <line x1="250" y1="8" x2="250" y2="20" stroke="#34D399" stroke-width="1.5" />
                <line x1="350" y1="8" x2="350" y2="20" stroke="#34D399" stroke-width="1.5" />
                <line x1="450" y1="8" x2="450" y2="20" stroke="#34D399" stroke-width="1.5" />
              </g>
            </svg>
          </div>

          <!-- FACTOR NODES (3-STAGE OR 5-STAGE) -->
          <!-- 3-STAGE NODES -->
          <div v-if="stageMode === '3stage'" class="grid grid-cols-3 gap-2 mt-1">
            <!-- Node 1: Net Margin -->
            <div class="bg-[#071411]/85 p-2 rounded-lg border border-emerald-400/35 text-center">
              <div class="text-[8.5px] font-bold text-emerald-400 uppercase tracking-wider">
                1. Net Margin (P1)
              </div>
              <div class="text-sm font-extrabold text-white font-mono my-0.5">
                {{ (netMargin * 100).toFixed(1) }}%
              </div>
              <div class="text-[8px] font-mono text-slate-300">
                Net Income / Sales
              </div>
              <div class="text-[8px] text-slate-400 mt-1 pt-1 border-t border-slate-800">
                Pricing Power & Cost
              </div>
            </div>

            <!-- Node 2: Asset Turnover -->
            <div class="bg-[#071411]/85 p-2 rounded-lg border border-teal-400/35 text-center">
              <div class="text-[8.5px] font-bold text-teal-400 uppercase tracking-wider">
                2. Asset Turnover (P5)
              </div>
              <div class="text-sm font-extrabold text-white font-mono my-0.5">
                {{ assetTurnover.toFixed(2) }}x
              </div>
              <div class="text-[8px] font-mono text-slate-300">
                Sales / Total Assets
              </div>
              <div class="text-[8px] text-slate-400 mt-1 pt-1 border-t border-slate-800">
                Capital Velocity
              </div>
            </div>

            <!-- Node 3: Equity Multiplier -->
            <div
              class="p-2 rounded-lg border text-center transition"
              :class="equityMultiplier >= 3.5
                ? 'bg-rose-950/40 border-rose-400/60 shadow-[0_0_8px_rgba(244,63,94,0.3)]'
                : 'bg-[#071411]/85 border-sky-400/35'"
            >
              <div class="text-[8.5px] font-bold uppercase tracking-wider" :class="equityMultiplier >= 3.5 ? 'text-rose-400' : 'text-sky-400'">
                3. Equity Multiplier (P2)
              </div>
              <div class="text-sm font-extrabold font-mono my-0.5" :class="equityMultiplier >= 3.5 ? 'text-rose-300' : 'text-white'">
                {{ equityMultiplier.toFixed(2) }}x
              </div>
              <div class="text-[8px] font-mono text-slate-300">
                Assets / Equity
              </div>
              <div class="text-[8px] text-slate-400 mt-1 pt-1 border-t border-slate-800">
                {{ equityMultiplier >= 3.5 ? '⚠️ Gearing Overhang' : 'Balance Sheet Gearing' }}
              </div>
            </div>
          </div>

          <!-- 5-STAGE NODES -->
          <div v-else class="grid grid-cols-5 gap-1.5 mt-1">
            <!-- Node 1: Tax Burden -->
            <div class="bg-[#071411]/85 p-1.5 rounded-lg border border-emerald-400/30 text-center">
              <div class="text-[8px] font-bold text-emerald-400 uppercase tracking-tight">
                Tax Retention
              </div>
              <div class="text-xs font-extrabold text-white font-mono my-0.5">
                {{ taxBurden.toFixed(2) }}
              </div>
              <div class="text-[7.5px] font-mono text-slate-300">
                NI / EBT
              </div>
              <div class="text-[7px] text-slate-400 mt-0.5 pt-0.5 border-t border-slate-800">
                Tax: {{ ((1 - taxBurden) * 100).toFixed(0) }}%
              </div>
            </div>

            <!-- Node 2: Interest Burden -->
            <div
              class="p-1.5 rounded-lg border text-center transition"
              :class="interestBurden < 0.65
                ? 'bg-amber-950/40 border-amber-400/50'
                : 'bg-[#071411]/85 border-sky-400/30'"
            >
              <div class="text-[8px] font-bold uppercase tracking-tight" :class="interestBurden < 0.65 ? 'text-amber-400' : 'text-sky-400'">
                Interest Drag
              </div>
              <div class="text-xs font-extrabold font-mono my-0.5" :class="interestBurden < 0.65 ? 'text-amber-300' : 'text-white'">
                {{ interestBurden.toFixed(2) }}
              </div>
              <div class="text-[7.5px] font-mono text-slate-300">
                EBT / EBIT
              </div>
              <div class="text-[7px] text-slate-400 mt-0.5 pt-0.5 border-t border-slate-800">
                Drag: {{ ((1 - interestBurden) * 100).toFixed(0) }}%
              </div>
            </div>

            <!-- Node 3: Operating Margin -->
            <div
              class="p-1.5 rounded-lg border text-center transition"
              :class="operatingMargin < 0.10
                ? 'bg-rose-950/40 border-rose-400/50'
                : 'bg-[#071411]/85 border-teal-400/30'"
            >
              <div class="text-[8px] font-bold uppercase tracking-tight" :class="operatingMargin < 0.10 ? 'text-rose-400' : 'text-teal-400'">
                Op Margin
              </div>
              <div class="text-xs font-extrabold font-mono my-0.5" :class="operatingMargin < 0.10 ? 'text-rose-300' : 'text-white'">
                {{ (operatingMargin * 100).toFixed(1) }}%
              </div>
              <div class="text-[7.5px] font-mono text-slate-300">
                EBIT / Sales
              </div>
              <div class="text-[7px] text-slate-400 mt-0.5 pt-0.5 border-t border-slate-800">
                Core Engine
              </div>
            </div>

            <!-- Node 4: Asset Turnover -->
            <div class="bg-[#071411]/85 p-1.5 rounded-lg border border-amber-400/30 text-center">
              <div class="text-[8px] font-bold text-amber-400 uppercase tracking-tight">
                Turnover
              </div>
              <div class="text-xs font-extrabold text-white font-mono my-0.5">
                {{ assetTurnover.toFixed(2) }}x
              </div>
              <div class="text-[7.5px] font-mono text-slate-300">
                Sales / Assets
              </div>
              <div class="text-[7px] text-slate-400 mt-0.5 pt-0.5 border-t border-slate-800">
                Velocity
              </div>
            </div>

            <!-- Node 5: Equity Multiplier -->
            <div
              class="p-1.5 rounded-lg border text-center transition"
              :class="equityMultiplier >= 3.5
                ? 'bg-rose-950/40 border-rose-400/60 shadow-[0_0_6px_rgba(244,63,94,0.3)]'
                : 'bg-[#071411]/85 border-purple-400/30'"
            >
              <div class="text-[8px] font-bold uppercase tracking-tight" :class="equityMultiplier >= 3.5 ? 'text-rose-400' : 'text-purple-400'">
                Leverage
              </div>
              <div class="text-xs font-extrabold font-mono my-0.5" :class="equityMultiplier >= 3.5 ? 'text-rose-300' : 'text-white'">
                {{ equityMultiplier.toFixed(2) }}x
              </div>
              <div class="text-[7.5px] font-mono text-slate-300">
                Assets / Equity
              </div>
              <div class="text-[7px] text-slate-400 mt-0.5 pt-0.5 border-t border-slate-800">
                {{ equityMultiplier >= 3.5 ? '⚠️ Overhang' : 'Gearing' }}
              </div>
            </div>
          </div>

          <!-- Multiplicative Product Bar Verification -->
          <div class="mt-2 bg-[#071411]/90 p-2 rounded-lg border border-emerald-500/20 text-center font-mono">
            <div class="text-[8.5px] text-slate-400 uppercase tracking-wider mb-0.5">
              Exact Multiplicative Identity Check:
            </div>
            <div v-if="stageMode === '3stage'" class="text-[10.5px] text-emerald-300 font-bold">
              {{ (netMargin * 100).toFixed(1) }}% <span class="text-slate-400 font-normal">(Margin)</span>
              &times; {{ assetTurnover.toFixed(2) }} <span class="text-slate-400 font-normal">(Turnover)</span>
              &times; {{ equityMultiplier.toFixed(2) }} <span class="text-slate-400 font-normal">(Leverage)</span>
              = <span class="text-white underline">{{ (roe * 100).toFixed(1) }}% ROE</span>
            </div>
            <div v-else class="text-[10px] text-emerald-300 font-bold">
              {{ taxBurden.toFixed(2) }} <span class="text-slate-400 font-normal">(Tax)</span>
              &times; {{ interestBurden.toFixed(2) }} <span class="text-slate-400 font-normal">(Interest)</span>
              &times; {{ (operatingMargin * 100).toFixed(1) }}% <span class="text-slate-400 font-normal">(EBIT)</span>
              &times; {{ assetTurnover.toFixed(2) }} <span class="text-slate-400 font-normal">(Turnover)</span>
              &times; {{ equityMultiplier.toFixed(2) }} <span class="text-slate-400 font-normal">(Leverage)</span>
              = <span class="text-white underline">{{ (roe * 100).toFixed(1) }}% ROE</span>
            </div>
          </div>
        </div>

        <div class="text-[9px] font-mono text-slate-400 pt-1 border-t border-emerald-500/10 flex justify-between">
          <span>Decomposition Architecture</span>
          <span class="text-emerald-400 font-bold">Orthogonal Variance Decomposition</span>
        </div>
      </div>

      <!-- Right Column: Diagnostics, Early Warning & Interactive Sandbox Sliders -->
      <div class="col-span-5 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <!-- Early Warning Alert Panel -->
          <div class="p-2 rounded-lg border mb-2" :class="diagnosticAssessment.badgeClass">
            <div class="flex items-center justify-between mb-0.5">
              <span class="text-[9.5px] font-black uppercase tracking-wider">
                {{ diagnosticAssessment.badge }}
              </span>
              <span class="text-[9px] font-mono">
                Risk Engine
              </span>
            </div>
            <div class="text-[11px] font-bold text-white mb-0.5">
              {{ diagnosticAssessment.headline }}
            </div>
            <div class="text-[9.5px] text-slate-300 leading-tight">
              {{ diagnosticAssessment.detail }}
            </div>
          </div>

          <!-- Parameter Definitions Block ("Where:") -->
          <div class="bg-[#071411]/80 p-2 rounded-lg border border-emerald-500/15 mb-2">
            <div class="text-[9.5px] font-bold text-slate-200 mb-1 flex items-center justify-between">
              <span class="text-emerald-400 font-bold">Where: Parameter Definitions</span>
              <span class="text-[8.5px] font-mono text-slate-400">Formal Accounting Taxonomies</span>
            </div>
            <ul class="text-[9px] text-slate-300 space-y-1 pl-3 list-disc">
              <li><strong>Tax Burden (NI/EBT):</strong> Proportion of pretax profits retained after taxes ($1 - t$).</li>
              <li><strong>Interest Burden (EBT/EBIT):</strong> Financial drag; equals 1.0 for unlevered debt-free firms.</li>
              <li><strong>Operating Margin (EBIT/Sales):</strong> Core unadulterated operational profitability.</li>
              <li><strong>Asset Turnover (Sales/Assets):</strong> Capital velocity and revenue asset efficiency.</li>
              <li><strong>Equity Multiplier (Assets/Equity):</strong> $1 + \text{Debt}/\text{Equity}$, measures leverage gearing.</li>
            </ul>
          </div>

          <!-- Sandbox Sliders (Active when in sandbox or always accessible) -->
          <div class="bg-[#071411]/60 p-2 rounded-lg border border-cyan-500/20">
            <div class="flex items-center justify-between text-[9.5px] font-bold text-cyan-300 mb-1">
              <span>Interactive Parameter Sandbox:</span>
              <span class="text-[8.5px] font-mono text-slate-400">Live Tree Update</span>
            </div>

            <div class="space-y-1.5 text-[9px] font-mono">
              <!-- Operating Margin Slider -->
              <div>
                <div class="flex justify-between text-slate-300">
                  <span>Operating Margin: {{ (operatingMargin * 100).toFixed(1) }}%</span>
                  <span class="text-slate-400">Core EBIT</span>
                </div>
                <input
                  v-model.number="operatingMargin"
                  type="range"
                  min="0.02"
                  max="0.40"
                  step="0.005"
                  class="w-full h-1 bg-slate-800 rounded appearance-none cursor-pointer accent-teal-400"
                >
              </div>

              <!-- Equity Multiplier Slider -->
              <div>
                <div class="flex justify-between text-slate-300">
                  <span :class="equityMultiplier >= 3.5 ? 'text-rose-400 font-bold' : ''">
                    Equity Multiplier: {{ equityMultiplier.toFixed(2) }}x {{ equityMultiplier >= 3.5 ? '⚠️' : '' }}
                  </span>
                  <span class="text-slate-400">Leverage</span>
                </div>
                <input
                  v-model.number="equityMultiplier"
                  type="range"
                  min="1.0"
                  max="8.0"
                  step="0.1"
                  class="w-full h-1 bg-slate-800 rounded appearance-none cursor-pointer accent-purple-400"
                >
              </div>

              <!-- Asset Turnover Slider -->
              <div>
                <div class="flex justify-between text-slate-300">
                  <span>Asset Turnover: {{ assetTurnover.toFixed(2) }}x</span>
                  <span class="text-slate-400">Velocity</span>
                </div>
                <input
                  v-model.number="assetTurnover"
                  type="range"
                  min="0.2"
                  max="3.0"
                  step="0.05"
                  class="w-full h-1 bg-slate-800 rounded appearance-none cursor-pointer accent-amber-400"
                >
              </div>
            </div>
          </div>
        </div>

        <div class="flex items-center justify-between text-[9px] font-mono text-slate-400 pt-1 border-t border-emerald-500/10">
          <span>Early Warning Trigger</span>
          <span :class="isLeverageOverhang ? 'text-rose-400 font-bold' : 'text-emerald-400 font-bold'">
            {{ isLeverageOverhang ? '🚨 Alert Active' : '✓ Normal Bounds' }}
          </span>
        </div>
      </div>
    </div>

    <!-- Bottom KPI Metric Cards Grid (4 Essential Metrics) -->
    <div class="grid grid-cols-4 gap-2.5 pt-0.5">
      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-emerald-400 uppercase tracking-wider">
          Total Headline ROE
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          {{ (roe * 100).toFixed(1) }}%
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          Product of Orthogonal Drivers
        </div>
      </div>

      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-teal-400 uppercase tracking-wider">
          Return on Assets (ROA)
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          {{ (roa * 100).toFixed(1) }}%
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          Net Margin &times; Asset Turnover
        </div>
      </div>

      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold text-sky-400 uppercase tracking-wider">
          Financing Burden
        </div>
        <div class="text-base font-extrabold text-white tracking-tight mt-0.5">
          {{ interestBurden.toFixed(2) }}
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          {{ interestBurden === 1.0 ? 'Zero Debt Drag' : `${((1 - interestBurden) * 100).toFixed(0)}% EBIT Drag` }}
        </div>
      </div>

      <div class="glass-card p-2 text-center border-emerald-400/25">
        <div class="text-[9.5px] font-bold uppercase tracking-wider" :class="equityMultiplier >= 3.5 ? 'text-rose-400' : 'text-purple-400'">
          Leverage Overhang Alert
        </div>
        <div class="text-base font-extrabold tracking-tight mt-0.5" :class="equityMultiplier >= 3.5 ? 'text-rose-300' : 'text-emerald-300'">
          {{ equityMultiplier >= 3.5 ? 'FLAGGED' : 'NORMAL' }}
        </div>
        <div class="text-[9.5px] text-slate-400 font-mono">
          Threshold: EM &ge; 3.50x
        </div>
      </div>
    </div>
  </div>
</template>
