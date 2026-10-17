<script setup lang="ts">
import { ref, computed } from 'vue'

const cacheState = ref<'warm' | 'cold'>('warm')
const selectedAliasIndex = ref<number>(0)

interface SchemaMapping {
  rawLabel: string
  sourceStandard: string
  canonicalToken: string
  targetCategory: string
  exampleValue: string
  sanitizedValue: string
  regexPattern: string
  status: 'harmonized' | 'flagged' | 'sanitized'
}

const schemaMappings: SchemaMapping[] = [
  {
    rawLabel: 'RevenueFromOperations',
    sourceStandard: 'Ind-AS Division II / MCA',
    canonicalToken: 'rev',
    targetCategory: 'Operating Revenue',
    exampleValue: '₹48,250.00 Cr',
    sanitizedValue: '482500000000.0 (IEEE-754 Float)',
    regexPattern: '(?i)(revenue.*operations|net.*sales|total.*operating.*rev)',
    status: 'harmonized',
  },
  {
    rawLabel: 'GrossSalesLessReturns',
    sourceStandard: 'Historical Indian GAAP',
    canonicalToken: 'rev',
    targetCategory: 'Operating Revenue',
    exampleValue: '₹31,420.50 Cr',
    sanitizedValue: '314205000000.0 (IEEE-754 Float)',
    regexPattern: '(?i)(gross.*sales|turnover|net.*revenue)',
    status: 'harmonized',
  },
  {
    rawLabel: 'ProfitBeforeTaxAndExceptional',
    sourceStandard: 'XBRL Filing Standard',
    canonicalToken: 'ebt',
    targetCategory: 'Earnings Before Tax',
    exampleValue: '₹7,890.15 Cr',
    sanitizedValue: '78901500000.0 (IEEE-754 Float)',
    regexPattern: '(?i)(profit.*before.*tax|ebt|pbt)',
    status: 'harmonized',
  },
  {
    rawLabel: 'CashAndBankBalancesWithRBI',
    sourceStandard: 'RBI Banking Disclosures',
    canonicalToken: 'cash',
    targetCategory: 'Cash & Liquid Assets',
    exampleValue: '₹14,520.00 Cr',
    sanitizedValue: '145200000000.0 (IEEE-754 Float)',
    regexPattern: '(?i)(cash.*bank.*balances|cash.*equivalents|balances.*rbi)',
    status: 'harmonized',
  },
  {
    rawLabel: 'NegativeEquityDeficit_Sample',
    sourceStandard: 'Distressed Stressed Asset',
    canonicalToken: 'equity_isolated',
    targetCategory: 'Solvency Interceptor',
    exampleValue: '-₹1,840.00 Cr',
    sanitizedValue: 'INTERCEPTED: Insolvent (D/E Trap Suppressed)',
    regexPattern: '(?i)(equity.*deficit|negative.*networth)',
    status: 'flagged',
  },
  {
    rawLabel: 'ZeroInterestExpense_DivZero',
    sourceStandard: 'Debt-Free Pure Equity Firm',
    canonicalToken: 'safe_divide_nan',
    targetCategory: 'Singularity Guard',
    exampleValue: 'Interest = ₹0.00 Cr',
    sanitizedValue: 'safe_divide(EBIT, 0) ➔ IEEE NaN (Zero Crash)',
    regexPattern: '(?i)(interest.*finance.*cost)',
    status: 'sanitized',
  },
]

// Gauge Metrics depending on Warm vs Cold Cache
const hitRate = computed(() => (cacheState.value === 'warm' ? 88.5 : 0.0))
const latencyMs = computed(() => (cacheState.value === 'warm' ? 214 : 28400))
const ioReduction = computed(() => (cacheState.value === 'warm' ? '12x' : '1x'))
const apiCalls = computed(() => (cacheState.value === 'warm' ? '0 Calls' : '150 Calls'))
const rateLimitRisk = computed(() => (cacheState.value === 'warm' ? '0.0% (Zero HTTP 429)' : 'High (Risk 429)'))

// SVG Gauge geometry
// Semi-circle arc: radius 64, circumference for 180 degrees = PI * 64 ≈ 201.06
const gaugeRadius = 64
const arcLength = Math.PI * gaugeRadius
const strokeDashoffset = computed(() => {
  const fraction = hitRate.value / 100
  return arcLength * (1 - fraction)
})

function selectAlias(idx: number) {
  selectedAliasIndex.value = idx
}
</script>

<template>
  <div class="w-full flex flex-col gap-2.5 text-slate-100 select-none">
    <!-- Top Interactive Control Bar: Cache Mode Selector -->
    <div class="glass-card px-3.5 py-2 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <span class="text-xs font-bold text-white tracking-wide">Multi-Tier Ingestion & Caching State:</span>

        <div class="flex items-center gap-1.5 bg-[#071411]/90 p-0.5 rounded-lg border border-emerald-500/20">
          <button
            class="px-2.5 py-1 text-[11px] font-semibold rounded transition cursor-pointer flex items-center gap-1.5"
            :class="cacheState === 'warm'
              ? 'bg-emerald-500/30 text-emerald-300 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
              : 'text-slate-400 hover:text-slate-200'"
            @click="cacheState = 'warm'"
          >
            <span class="w-2 h-2 rounded-full bg-emerald-400" />
            <span>Warm Cache (88.5% Hit Rate)</span>
          </button>
          <button
            class="px-2.5 py-1 text-[11px] font-semibold rounded transition cursor-pointer flex items-center gap-1.5"
            :class="cacheState === 'cold'
              ? 'bg-amber-500/30 text-amber-300 shadow-[0_0_8px_rgba(245,158,11,0.3)]'
              : 'text-slate-400 hover:text-slate-200'"
            @click="cacheState = 'cold'"
          >
            <span class="w-2 h-2 rounded-full bg-amber-400" />
            <span>Cold Start / Cache Miss (0%)</span>
          </button>
        </div>
      </div>

      <div class="flex items-center gap-3 text-[11px] font-mono">
        <span class="text-slate-400">Ingestion Latency:</span>
        <span
          class="font-bold px-2 py-0.5 rounded border"
          :class="cacheState === 'warm'
            ? 'text-emerald-300 bg-[#071411] border-emerald-500/30'
            : 'text-rose-400 bg-rose-950/40 border-rose-500/40'"
        >
          {{ cacheState === 'warm' ? `${latencyMs} ms` : `${(latencyMs / 1000).toFixed(1)} s` }}
        </span>
        <span class="text-slate-400">Disk I/O:</span>
        <span class="text-white font-bold bg-[#071411] px-2 py-0.5 rounded border border-emerald-500/20">
          {{ ioReduction }} Reduction
        </span>
      </div>
    </div>

    <!-- Main Content: Dual-Panel Layout (Left: Cache Architecture & Radial Gauge | Right: Schema Harmonizer) -->
    <div class="grid grid-cols-12 gap-3 items-stretch">
      <!-- Left Column: Radial Hit Rate Gauge & Columnar Storage Tiers -->
      <div class="col-span-5 glass-card p-3 flex flex-col justify-between relative overflow-hidden">
        <div class="flex items-center justify-between mb-1">
          <span class="text-xs font-bold text-white tracking-wide">Multi-Tier Parquet Cache</span>
          <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
            Snappy Columnar
          </span>
        </div>

        <!-- Radial Semi-Circle Gauge -->
        <div class="relative w-full h-[120px] flex flex-col items-center justify-center -my-1">
          <svg viewBox="0 0 160 95" class="w-48 h-28">
            <defs>
              <linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#10b981" />
                <stop offset="50%" stop-color="#34d399" />
                <stop offset="100%" stop-color="#00e599" />
              </linearGradient>
            </defs>

            <!-- Background Arc (180 deg) -->
            <path
              d="M 16 85 A 64 64 0 0 1 144 85"
              fill="none"
              stroke="#1e293b"
              stroke-width="12"
              stroke-linecap="round"
            />

            <!-- Animated Value Arc -->
            <path
              d="M 16 85 A 64 64 0 0 1 144 85"
              fill="none"
              stroke="url(#gaugeGrad)"
              stroke-width="12"
              stroke-linecap="round"
              :stroke-dasharray="arcLength"
              :stroke-dashoffset="strokeDashoffset"
              class="transition-all duration-700 ease-out"
            />

            <!-- Center Text -->
            <text
              x="80"
              y="68"
              text-anchor="middle"
              fill="#ffffff"
              font-size="20"
              font-weight="bold"
              font-family="monospace"
            >
              {{ hitRate.toFixed(1) }}%
            </text>
            <text
              x="80"
              y="82"
              text-anchor="middle"
              fill="#94a3b8"
              font-size="8"
              font-weight="bold"
              letter-spacing="0.05em"
            >
              CACHE HIT EFFICIENCY
            </text>
          </svg>
        </div>

        <!-- Tier 1 & Tier 2 Storage Hierarchy -->
        <div class="space-y-1.5 mt-1">
          <!-- Tier 1 -->
          <div class="p-2 rounded bg-[#071411]/90 border border-emerald-500/20 flex items-center justify-between text-[10.5px]">
            <div>
              <div class="font-bold text-white flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <span>Tier 1: In-Memory RAM LRU Cache</span>
              </div>
              <div class="text-[9.5px] text-slate-400">Sub-millisecond volatile session memory</div>
            </div>
            <div class="font-mono font-bold text-emerald-300 text-right">
              &lt; 1 ms
            </div>
          </div>

          <!-- Tier 2 -->
          <div class="p-2 rounded bg-[#071411]/90 border border-emerald-500/20 flex items-center justify-between text-[10.5px]">
            <div>
              <div class="font-bold text-white flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-teal-400" />
                <span>Tier 2: Snappy Parquet Disk Store</span>
              </div>
              <div class="text-[9.5px] text-slate-400">IEEE-754 precision, 4-yr aligned tensors</div>
            </div>
            <div class="font-mono font-bold text-teal-300 text-right">
              &lt; 15 ms
            </div>
          </div>
        </div>

        <!-- Telemetry Pill Footer -->
        <div class="mt-2 pt-1.5 border-t border-emerald-500/15 flex items-center justify-between text-[10px] text-slate-400">
          <span>API Call Relief: <strong class="text-emerald-300 font-mono">{{ apiCalls }}</strong></span>
          <span>HTTP 429 Risk: <strong class="text-emerald-300 font-mono">{{ rateLimitRisk }}</strong></span>
        </div>
      </div>

      <!-- Right Column: Interactive Schema Harmonizer & Guardrails -->
      <div class="col-span-7 flex flex-col justify-between gap-2.5">
        <!-- Interactive Alias Reconciler -->
        <div class="glass-card p-3 border-emerald-500/25">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold text-white tracking-wide">
              Deterministic Schema Alias Harmonization
            </span>
            <span class="text-[10px] font-mono text-emerald-400">
              Disparate Filings ➔ Canonical Tokens
            </span>
          </div>

          <!-- Alias Item Selector Chips -->
          <div class="flex flex-wrap gap-1.5 mb-2.5">
            <button
              v-for="(item, idx) in schemaMappings"
              :key="idx"
              class="px-2 py-0.5 rounded text-[10px] font-mono font-medium transition cursor-pointer border"
              :class="selectedAliasIndex === idx
                ? 'bg-emerald-500/30 text-emerald-300 border-emerald-400/60 shadow-[0_0_8px_rgba(52,211,153,0.25)]'
                : 'bg-[#071411]/80 text-slate-400 border-slate-700/60 hover:text-slate-200'"
              @click="selectAlias(idx)"
            >
              {{ item.rawLabel }}
            </button>
          </div>

          <!-- Active Alias Inspector Box -->
          <div class="p-2.5 rounded bg-[#071411]/95 border border-emerald-500/25 space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <div class="flex items-center gap-2">
                <span class="text-slate-400 font-mono text-[11px]">Raw Filing Label:</span>
                <span class="font-bold text-white font-mono">{{ schemaMappings[selectedAliasIndex].rawLabel }}</span>
              </div>
              <span class="text-[9.5px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">
                {{ schemaMappings[selectedAliasIndex].sourceStandard }}
              </span>
            </div>

            <!-- Regex Pattern Matcher Bar -->
            <div class="flex items-center gap-2 text-[10.5px]">
              <span class="text-slate-500 font-mono">Regex Match:</span>
              <span class="font-mono text-amber-300/90 bg-slate-900/80 px-1.5 py-0.5 rounded border border-amber-500/20 text-[10px] truncate max-w-[280px]">
                {{ schemaMappings[selectedAliasIndex].regexPattern }}
              </span>
              <span class="text-emerald-400 font-bold ml-auto text-[10px]">100% Match</span>
            </div>

            <!-- Resolution into Canonical & Sanitized Output -->
            <div class="pt-1 border-t border-emerald-500/15 flex items-center justify-between text-xs">
              <div class="flex items-center gap-1.5">
                <span class="text-slate-400 font-mono text-[11px]">Canonical Token:</span>
                <span class="font-mono font-bold text-emerald-300 bg-emerald-950/40 px-2 py-0.5 rounded border border-emerald-500/30">
                  {{ schemaMappings[selectedAliasIndex].canonicalToken }}
                </span>
                <span class="text-[10px] text-slate-400">({{ schemaMappings[selectedAliasIndex].targetCategory }})</span>
              </div>
              <div class="font-mono text-[10px]" :class="schemaMappings[selectedAliasIndex].status === 'flagged' ? 'text-amber-400' : 'text-slate-300'">
                {{ schemaMappings[selectedAliasIndex].sanitizedValue }}
              </div>
            </div>
          </div>
        </div>

        <!-- Pre-Engine Singularity Sanitization & Accounting Invariants -->
        <div class="glass-card p-3 border-emerald-500/25 flex-1 flex flex-col justify-between">
          <div class="text-[11px] font-bold text-white mb-1.5 flex items-center justify-between">
            <span>Pre-Engine Singularity Sanitization &amp; Identity Guards</span>
            <span class="text-[10px] font-mono text-emerald-400">IEEE-754 Safe</span>
          </div>

          <div class="grid grid-cols-3 gap-2 text-[10.5px]">
            <!-- Guard 1 -->
            <div class="p-2 rounded bg-[#071411]/90 border border-emerald-500/25 flex flex-col justify-between">
              <div>
                <div class="font-bold text-emerald-300 flex items-center gap-1 mb-0.5">
                  <span>✓</span>
                  <span>Balance Sheet Identity</span>
                </div>
                <div class="text-[9.5px] text-slate-300 leading-tight">
                  Assets ≈ Liabilities + Equity ($|\Delta| &lt; \epsilon$)
                </div>
              </div>
              <div class="text-[9px] font-mono text-emerald-400 mt-1">Status: Validated</div>
            </div>

            <!-- Guard 2 -->
            <div class="p-2 rounded bg-[#071411]/90 border border-amber-500/25 flex flex-col justify-between">
              <div>
                <div class="font-bold text-amber-300 flex items-center gap-1 mb-0.5">
                  <span>🛡️</span>
                  <span>Negative Equity Guard</span>
                </div>
                <div class="text-[9.5px] text-slate-300 leading-tight">
                  Intercepts insolvent firms ($\text{Equity} &lt; 0$) from $D/E$ traps
                </div>
              </div>
              <div class="text-[9px] font-mono text-amber-400 mt-1">Status: Active Isolation</div>
            </div>

            <!-- Guard 3 -->
            <div class="p-2 rounded bg-[#071411]/90 border border-teal-500/25 flex flex-col justify-between">
              <div>
                <div class="font-bold text-teal-300 flex items-center gap-1 mb-0.5">
                  <span>⚡</span>
                  <span>safe_divide(a, b, ε)</span>
                </div>
                <div class="text-[9.5px] text-slate-300 leading-tight">
                  Replaces zero denominators with typed IEEE NaNs
                </div>
              </div>
              <div class="text-[9px] font-mono text-teal-400 mt-1">Status: Zero Crashes</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
