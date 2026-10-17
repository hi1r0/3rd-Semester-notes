<script setup lang="ts">
import { ref, computed } from 'vue'

interface PeerFirm {
  ticker: string
  name: string
  value: number
  subsector: string
}

// Sector datasets with realistic NSE corporate ratios
const sectorData: Record<string, { label: string; metric: string; unit: string; description: string; firms: PeerFirm[] }> = {
  it: {
    label: 'IT Services',
    metric: 'Operating Margin',
    unit: '%',
    description: 'Operating margin distribution across Tier-1 and Mid-cap Indian software exporters.',
    firms: [
      { ticker: 'TCS', name: 'Tata Consultancy Services', value: 25.2, subsector: 'Tier-1 IT' },
      { ticker: 'INFY', name: 'Infosys Ltd', value: 21.4, subsector: 'Tier-1 IT' },
      { ticker: 'HCLTECH', name: 'HCL Technologies', value: 18.6, subsector: 'Tier-1 IT' },
      { ticker: 'WIPRO', name: 'Wipro Ltd', value: 16.2, subsector: 'Tier-1 IT' },
      { ticker: 'TECHM', name: 'Tech Mahindra', value: 12.8, subsector: 'Tier-1 IT' },
      { ticker: 'LTIM', name: 'LTIMindtree', value: 17.5, subsector: 'Mid-Cap IT' },
      { ticker: 'PERSISTENT', name: 'Persistent Systems', value: 15.2, subsector: 'Mid-Cap IT' },
      { ticker: 'COFORGE', name: 'Coforge Ltd', value: 17.8, subsector: 'Mid-Cap IT' },
      { ticker: 'MPHASIS', name: 'Mphasis Ltd', value: 15.4, subsector: 'Mid-Cap IT' },
      { ticker: 'TATAELXSI', name: 'Tata Elxsi', value: 28.4, subsector: 'ER&D Tech' },
      { ticker: 'KPITTECH', name: 'KPIT Technologies', value: 20.1, subsector: 'Auto Tech' },
      { ticker: 'CYIENT', name: 'Cyient Ltd', value: 16.0, subsector: 'Engineering' },
      { ticker: 'ZENSAR', name: 'Zensar Technologies', value: 14.8, subsector: 'Enterprise IT' },
      { ticker: 'BIRLASOFT', name: 'Birlasoft Ltd', value: 15.7, subsector: 'Enterprise IT' },
      { ticker: 'SONATACOMT', name: 'Sonata Software', value: 24.0, subsector: 'Platform Tech' },
      { ticker: 'LTTS', name: 'L&T Technology Services', value: 17.1, subsector: 'ER&D Tech' },
      { ticker: 'OFSS', name: 'Oracle Financial Services', value: 45.2, subsector: 'Banking Software' }, // Mild/Extreme Outlier
      { ticker: 'BSOSOFT', name: 'BSE Tech Soft', value: 14.2, subsector: 'Mid-Cap IT' },
      { ticker: 'HAPPSTMNDS', name: 'Happiest Minds', value: 18.0, subsector: 'Digital IT' },
      { ticker: 'INTELLECT', name: 'Intellect Design Arena', value: 21.5, subsector: 'Fintech Products' },
      { ticker: 'RATEGAIN', name: 'RateGain Travel Tech', value: 19.8, subsector: 'Travel SaaS' },
      { ticker: 'NAZARA', name: 'Nazara Technologies', value: 11.2, subsector: 'Gaming / Media' },
      { ticker: 'TANLA', name: 'Tanla Platforms', value: 22.3, subsector: 'CPaaS Telecom' },
      { ticker: 'MAPMYINDIA', name: 'C.E. Info Systems', value: 39.5, subsector: 'GeoSpatial SaaS' }, // Mild Outlier
      { ticker: 'NEWGEN', name: 'Newgen Software', value: 20.5, subsector: 'Enterprise SaaS' },
      { ticker: 'DISTRESSED', name: 'Legacy Turnaround Soft', value: -8.5, subsector: 'Legacy IT' }, // Extreme Anomaly
    ],
  },
  infra: {
    label: 'Infra & Utilities',
    metric: 'Debt-to-Equity (D/E)',
    unit: 'x',
    description: 'Capital structure gearing showing heavy right-skew where symmetric Gaussian models fail.',
    firms: [
      { ticker: 'LT', name: 'Larsen & Toubro', value: 0.82, subsector: 'Diversified Infra' },
      { ticker: 'NTPC', name: 'NTPC Ltd', value: 1.42, subsector: 'Thermal Power' },
      { ticker: 'POWERGRID', name: 'Power Grid Corp', value: 1.35, subsector: 'Transmission' },
      { ticker: 'TATAPOWER', name: 'Tata Power', value: 1.58, subsector: 'Integrated Power' },
      { ticker: 'JSWENERGY', name: 'JSW Energy', value: 1.20, subsector: 'Renewables / Power' },
      { ticker: 'BHEL', name: 'Bharat Heavy Electricals', value: 0.15, subsector: 'Heavy Electrical' },
      { ticker: 'ADANIENT', name: 'Adani Enterprises', value: 2.10, subsector: 'Incubation Infra' },
      { ticker: 'ADANIGREEN', name: 'Adani Green Energy', value: 4.85, subsector: 'Renewable Capex' }, // Mild Outlier
      { ticker: 'GMRINFRA', name: 'GMR Airports Infra', value: 3.75, subsector: 'Airport Concessions' },
      { ticker: 'SUZLON', name: 'Suzlon Energy', value: 0.35, subsector: 'Wind Equipment' },
      { ticker: 'NHPC', name: 'NHPC Ltd', value: 0.78, subsector: 'Hydro Power' },
      { ticker: 'SJVN', name: 'SJVN Ltd', value: 1.10, subsector: 'Hydro / Solar' },
      { ticker: 'CESC', name: 'CESC Ltd', value: 1.45, subsector: 'Power Distribution' },
      { ticker: 'TORNTPOWER', name: 'Torrent Power', value: 0.92, subsector: 'Power Generation' },
      { ticker: 'IEX', name: 'Indian Energy Exchange', value: 0.02, subsector: 'Market Exchange' },
      { ticker: 'IRB', name: 'IRB Infrastructure', value: 2.45, subsector: 'Highways / BOT' },
      { ticker: 'NCC', name: 'NCC Ltd', value: 0.65, subsector: 'Civil Construction' },
      { ticker: 'PNCINFRA', name: 'PNC Infratech', value: 0.42, subsector: 'Roadways' },
      { ticker: 'KNRCON', name: 'KNR Constructions', value: 0.38, subsector: 'EPC Highways' },
      { ticker: 'ASHOKA', name: 'Ashoka Buildcon', value: 1.85, subsector: 'Highways EPC' },
      { ticker: 'RELINFRA', name: 'Reliance Infrastructure', value: 6.80, subsector: 'Distressed Concession' }, // Extreme Anomaly
      { ticker: 'DBL', name: 'Dilip Buildcon', value: 1.75, subsector: 'Roadways Construction' },
      { ticker: 'ENGINERSIN', name: 'Engineers India', value: 0.00, subsector: 'Zero Debt EPC' },
      { ticker: 'NBCC', name: 'NBCC India Ltd', value: 0.01, subsector: 'Zero Debt PMC' },
      { ticker: 'RITES', name: 'RITES Ltd', value: 0.05, subsector: 'Railway Advisory' },
    ],
  },
  fmcg: {
    label: 'FMCG & Retail',
    metric: 'Asset Turnover',
    unit: 'x',
    description: 'Capital velocity distribution capturing high inventory churn versus capital asset drag.',
    firms: [
      { ticker: 'HUL', name: 'Hindustan Unilever', value: 2.15, subsector: 'Home & Personal' },
      { ticker: 'ITC', name: 'ITC Ltd', value: 0.95, subsector: 'Cash & Hotels' },
      { ticker: 'NESTLEIND', name: 'Nestle India', value: 2.85, subsector: 'Packaged Foods' },
      { ticker: 'BRITANNIA', name: 'Britannia Industries', value: 2.60, subsector: 'Bakery Foods' },
      { ticker: 'TATACONSUM', name: 'Tata Consumer Products', value: 1.45, subsector: 'Beverages & Foods' },
      { ticker: 'DABUR', name: 'Dabur India', value: 1.80, subsector: 'Ayurvedic Care' },
      { ticker: 'MARICO', name: 'Marico Ltd', value: 2.30, subsector: 'Edible Oils' },
      { ticker: 'GODREJCP', name: 'Godrej Consumer', value: 1.70, subsector: 'Personal Care' },
      { ticker: 'VBL', name: 'Varun Beverages', value: 1.30, subsector: 'Bottling & Dist.' },
      { ticker: 'COLPAL', name: 'Colgate-Palmolive', value: 2.95, subsector: 'Oral Care' },
      { ticker: 'EMAMILTD', name: 'Emami Ltd', value: 1.65, subsector: 'Health & Beauty' },
      { ticker: 'JYOTHYLAB', name: 'Jyothy Labs', value: 2.05, subsector: 'Fabric & Dish' },
      { ticker: 'RADICO', name: 'Radico Khaitan', value: 1.40, subsector: 'Spirits & Alcobev' },
      { ticker: 'UBL', name: 'United Breweries', value: 1.50, subsector: 'Brewing' },
      { ticker: 'TRENT', name: 'Trent Ltd (Zudio)', value: 3.55, subsector: 'Fast Fashion Retail' }, // Mild Outlier
      { ticker: 'DMART', name: 'Avenue Supermarts', value: 4.10, subsector: 'Hypermarket Retail' }, // Extreme Anomaly
      { ticker: 'SHOPPERS', name: 'Shoppers Stop', value: 1.90, subsector: 'Department Stores' },
      { ticker: 'BATAINDIA', name: 'Bata India', value: 1.25, subsector: 'Footwear Retail' },
      { ticker: 'RELAXO', name: 'Relaxo Footwears', value: 1.75, subsector: 'Value Footwear' },
      { ticker: 'TITAN', name: 'Titan Company', value: 2.40, subsector: 'Jewellery & Watches' },
      { ticker: 'BIKAJI', name: 'Bikaji Foods', value: 1.85, subsector: 'Ethnic Snacks' },
      { ticker: 'PATANJALI', name: 'Patanjali Foods', value: 2.20, subsector: 'Edible Oils & Foods' },
      { ticker: 'GODFRYPHLP', name: 'Godfrey Phillips', value: 1.35, subsector: 'Tobacco Goods' },
      { ticker: 'KRBL', name: 'KRBL Ltd (India Gate)', value: 1.15, subsector: 'Basmati Rice' },
      { ticker: 'BALRAMCHIN', name: 'Balrampur Chini', value: 1.05, subsector: 'Sugar & Bio-Energy' },
    ],
  },
}

// Active State
const activeSectorKey = ref<string>('it')
const injectAnomaly = ref<boolean>(false)
const injectedAnomalyValue = ref<number>(54.0)
const hoveredFirm = ref<PeerFirm | null>(null)
const selectedFirm = ref<PeerFirm | null>(null)

// Percentile Calculation (Standard Linear Interpolation)
function calculateQuantile(sortedArr: number[], q: number): number {
  if (sortedArr.length === 0) return 0
  if (sortedArr.length === 1) return sortedArr[0]
  const pos = (sortedArr.length - 1) * q
  const base = Math.floor(pos)
  const rest = pos - base
  if (sortedArr[base + 1] !== undefined) {
    return sortedArr[base] + rest * (sortedArr[base + 1] - sortedArr[base])
  }
  return sortedArr[base]
}

// Active dataset combining base peer firms + optional injected anomaly
const currentFirms = computed(() => {
  const base = [...sectorData[activeSectorKey.value].firms]
  if (injectAnomaly.value) {
    base.push({
      ticker: 'ROGUE_CORP',
      name: 'Synthetic Injected Anomaly',
      value: injectedAnomalyValue.value,
      subsector: 'Injected Outlier',
    })
  }
  return base
})

// Sorted values
const sortedValues = computed(() => {
  return [...currentFirms.value.map(f => f.value)].sort((a, b) => a - b)
})

// Quartiles & Interquartile Range
const q1 = computed(() => calculateQuantile(sortedValues.value, 0.25))
const median = computed(() => calculateQuantile(sortedValues.value, 0.50))
const q3 = computed(() => calculateQuantile(sortedValues.value, 0.75))
const iqr = computed(() => q3.value - q1.value)

// Inner Fences (1.5 * IQR)
const fLower = computed(() => q1.value - 1.5 * iqr.value)
const fUpper = computed(() => q3.value + 1.5 * iqr.value)

// Outer Fences (3.0 * IQR)
const fOuterLower = computed(() => q1.value - 3.0 * iqr.value)
const fOuterUpper = computed(() => q3.value + 3.0 * iqr.value)

// Whiskers (Extend to most extreme data points within inner fences)
const whiskerLower = computed(() => {
  const valid = sortedValues.value.filter(v => v >= fLower.value)
  return valid.length > 0 ? valid[0] : fLower.value
})

const whiskerUpper = computed(() => {
  const valid = sortedValues.value.filter(v => v <= fUpper.value)
  return valid.length > 0 ? valid[valid.length - 1] : fUpper.value
})

// Categorize firm into Tukey Outlier Classes
function getOutlierCategory(val: number): 'nominal' | 'mild' | 'extreme' {
  if (val < fOuterLower.value || val > fOuterUpper.value) {
    return 'extreme'
  } else if (val < fLower.value || val > fUpper.value) {
    return 'mild'
  }
  return 'nominal'
}

// Cohort classification counts
const cohortStats = computed(() => {
  let nominal = 0
  let mild = 0
  let extreme = 0
  for (const firm of currentFirms.value) {
    const cat = getOutlierCategory(firm.value)
    if (cat === 'nominal') nominal++
    else if (cat === 'mild') mild++
    else extreme++
  }
  return {
    total: currentFirms.value.length,
    nominal,
    mild,
    extreme,
  }
})

// SVG Horizontal Boxplot Scaling
const svgWidth = 860
const svgHeight = 135
const paddingLeft = 45
const paddingRight = 45
const plotWidth = svgWidth - paddingLeft - paddingRight

// Dynamic domain with padding around extreme data & fences
const domainMin = computed(() => {
  const minVal = Math.min(...sortedValues.value, fOuterLower.value)
  const range = Math.max(...sortedValues.value, fOuterUpper.value) - minVal
  return minVal - range * 0.08
})

const domainMax = computed(() => {
  const maxVal = Math.max(...sortedValues.value, fOuterUpper.value)
  const range = maxVal - Math.min(...sortedValues.value, fOuterLower.value)
  return maxVal + range * 0.08
})

function scaleX(val: number): number {
  const dMin = domainMin.value
  const dMax = domainMax.value
  if (dMax === dMin) return paddingLeft + plotWidth / 2
  const clamped = Math.max(dMin, Math.min(dMax, val))
  return paddingLeft + ((clamped - dMin) / (dMax - dMin)) * plotWidth
}

// Pseudo-random deterministic jitter for dots to prevent direct collision
function getJitterY(index: number, cat: 'nominal' | 'mild' | 'extreme'): number {
  if (cat === 'extreme') return 72 // centered on axis
  const offsets = [0, -11, 11, -19, 19, -6, 6, -14, 14]
  return 72 + offsets[index % offsets.length]
}

// Active inspected firm (hovered firm takes precedence, then selected)
const activeInspectedFirm = computed(() => {
  return hoveredFirm.value || selectedFirm.value || currentFirms.value[0]
})

function setSector(key: string) {
  activeSectorKey.value = key
  hoveredFirm.value = null
  selectedFirm.value = null
  if (key === 'it') injectedAnomalyValue.value = 54.0
  else if (key === 'infra') injectedAnomalyValue.value = 8.5
  else if (key === 'fmcg') injectedAnomalyValue.value = 5.6
}
</script>

<template>
  <div class="w-full flex flex-col gap-2 select-none text-slate-100">
    <!-- Top Interactive Header: Sector Selector, Anomaly Injector & Quick KPI Badges -->
    <div class="glass-card px-3 py-1.5 flex items-center justify-between gap-2">
      <!-- Sector Preset Buttons -->
      <div class="flex items-center gap-1.5">
        <span class="text-[10px] uppercase font-bold tracking-wider text-emerald-400/90 font-mono mr-1">Sector:</span>
        <button
          v-for="(sec, key) in sectorData"
          :key="key"
          class="px-2.5 py-1 rounded text-[11px] font-medium transition-all duration-200"
          :class="activeSectorKey === key
            ? 'bg-emerald-500/25 text-emerald-300 border border-emerald-500/40 shadow-[0_0_8px_rgba(52,211,153,0.3)]'
            : 'text-slate-400 hover:text-slate-200 bg-[#071411]/80 border border-emerald-500/10'"
          @click="setSector(key as string)"
        >
          {{ sec.label }}
        </button>
      </div>

      <!-- Outlier Injection Sandbox Controller -->
      <div class="flex items-center gap-2 bg-[#071411]/90 px-2.5 py-0.5 rounded-lg border border-emerald-500/20">
        <label class="flex items-center gap-1.5 cursor-pointer text-[11px] font-medium text-slate-300">
          <input
            v-model="injectAnomaly"
            type="checkbox"
            class="accent-emerald-400 rounded cursor-pointer w-3.5 h-3.5"
          >
          <span :class="injectAnomaly ? 'text-amber-300 font-bold' : 'text-slate-400'">
            Inject Rogue Peer
          </span>
        </label>

        <div v-if="injectAnomaly" class="flex items-center gap-1.5 pl-1 border-l border-emerald-500/20">
          <span class="text-[10px] font-mono text-slate-400">x_rogue =</span>
          <input
            v-model.number="injectedAnomalyValue"
            type="range"
            :min="activeSectorKey === 'it' ? -15 : activeSectorKey === 'infra' ? -1 : 0.5"
            :max="activeSectorKey === 'it' ? 65 : activeSectorKey === 'infra' ? 10 : 6.5"
            :step="activeSectorKey === 'it' ? 1 : 0.2"
            class="w-20 h-1 bg-slate-700 rounded appearance-none cursor-pointer accent-amber-400"
          >
          <span class="text-[11px] font-mono font-bold text-amber-300 min-w-[36px]">
            {{ injectedAnomalyValue.toFixed(1) }}{{ sectorData[activeSectorKey].unit }}
          </span>
        </div>
      </div>

      <!-- Quick Summary Badges -->
      <div class="flex items-center gap-2 font-mono text-[10px]">
        <span class="px-2 py-0.5 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
          Nominal: {{ cohortStats.nominal }}/{{ cohortStats.total }}
        </span>
        <span class="px-2 py-0.5 rounded bg-amber-500/15 text-amber-300 border border-amber-500/30">
          Mild (1.5x): {{ cohortStats.mild }}
        </span>
        <span class="px-2 py-0.5 rounded bg-rose-500/15 text-rose-300 border border-rose-500/30">
          Extreme (3.0x): {{ cohortStats.extreme }}
        </span>
      </div>
    </div>

    <!-- Main Visual Stage: SVG Horizontal Tukey Boxplot -->
    <div class="glass-card p-2.5 relative flex flex-col justify-between overflow-hidden">
      <!-- Top Title & Active Sector Metric Metadata -->
      <div class="flex items-center justify-between mb-0.5 px-1">
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold text-white tracking-wide">
            Tukey Exploratory Boxplot & Fence Partitions
          </span>
          <span class="text-[10px] text-slate-400 font-mono">
            [{{ sectorData[activeSectorKey].metric }} | Unit: {{ sectorData[activeSectorKey].unit }}]
          </span>
        </div>

        <div class="flex items-center gap-3 text-[10px] font-mono">
          <span class="flex items-center gap-1 text-emerald-400">
            <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block" /> Nominal Peer
          </span>
          <span class="flex items-center gap-1 text-amber-400">
            <span class="w-2 h-2 rounded-full bg-amber-400 inline-block" /> Mild Outlier (&gt;1.5 IQR)
          </span>
          <span class="flex items-center gap-1 text-rose-400">
            <span class="w-2 h-2 rounded-full bg-rose-400 inline-block" /> Extreme Anomaly (&gt;3.0 IQR)
          </span>
        </div>
      </div>

      <!-- SVG Canvas Stage -->
      <div class="relative w-full h-[142px] bg-[#071411]/95 rounded-lg border border-emerald-500/15 overflow-hidden flex items-center justify-center">
        <svg :viewBox="`0 0 ${svgWidth} ${svgHeight}`" class="w-full h-full">
          <defs>
            <!-- Normal Corridor Gradient -->
            <linearGradient id="nominalZoneGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#10b981" stop-opacity="0.12" />
              <stop offset="100%" stop-color="#10b981" stop-opacity="0.02" />
            </linearGradient>

            <!-- Box Gradient -->
            <linearGradient id="boxBodyGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#064e3b" stop-opacity="0.85" />
              <stop offset="50%" stop-color="#0d211b" stop-opacity="0.95" />
              <stop offset="100%" stop-color="#064e3b" stop-opacity="0.85" />
            </linearGradient>

            <!-- Glow Filters -->
            <filter id="medianGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="2" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="outlierGlow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          <!-- Zone Shading: Extreme Left Anomaly Zone -->
          <rect
            :x="scaleX(domainMin)"
            y="18"
            :width="Math.max(0, scaleX(fOuterLower) - scaleX(domainMin))"
            height="90"
            fill="rgba(244, 63, 94, 0.08)"
          />

          <!-- Zone Shading: Mild Left Outlier Zone -->
          <rect
            :x="scaleX(fOuterLower)"
            y="18"
            :width="Math.max(0, scaleX(fLower) - scaleX(fOuterLower))"
            height="90"
            fill="rgba(245, 158, 11, 0.08)"
          />

          <!-- Zone Shading: Nominal Safe Peer Corridor [fLower, fUpper] -->
          <rect
            :x="scaleX(fLower)"
            y="18"
            :width="Math.max(0, scaleX(fUpper) - scaleX(fLower))"
            height="90"
            fill="url(#nominalZoneGrad)"
          />

          <!-- Zone Shading: Mild Right Outlier Zone -->
          <rect
            :x="scaleX(fUpper)"
            y="18"
            :width="Math.max(0, scaleX(fOuterUpper) - scaleX(fUpper))"
            height="90"
            fill="rgba(245, 158, 11, 0.08)"
          />

          <!-- Zone Shading: Extreme Right Anomaly Zone -->
          <rect
            :x="scaleX(fOuterUpper)"
            y="18"
            :width="Math.max(0, scaleX(domainMax) - scaleX(fOuterUpper))"
            height="90"
            fill="rgba(244, 63, 94, 0.08)"
          />

          <!-- Horizontal Reference Axis -->
          <line
            :x1="paddingLeft"
            y1="72"
            :x2="svgWidth - paddingRight"
            y2="72"
            stroke="#334155"
            stroke-width="1"
            stroke-dasharray="2 3"
          />

          <!-- Outer Fences (3.0 * IQR) -->
          <line
            :x1="scaleX(fOuterLower)"
            y1="22"
            :x2="scaleX(fOuterLower)"
            y2="104"
            stroke="#f43f5e"
            stroke-width="1.2"
            stroke-dasharray="3 3"
            stroke-opacity="0.8"
          />
          <text
            :x="scaleX(fOuterLower)"
            y="16"
            fill="#f43f5e"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            F_outer_low (-3.0 IQR)
          </text>

          <line
            :x1="scaleX(fOuterUpper)"
            y1="22"
            :x2="scaleX(fOuterUpper)"
            y2="104"
            stroke="#f43f5e"
            stroke-width="1.2"
            stroke-dasharray="3 3"
            stroke-opacity="0.8"
          />
          <text
            :x="scaleX(fOuterUpper)"
            y="16"
            fill="#f43f5e"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            F_outer_up (+3.0 IQR)
          </text>

          <!-- Inner Fences (1.5 * IQR) -->
          <line
            :x1="scaleX(fLower)"
            y1="25"
            :x2="scaleX(fLower)"
            y2="101"
            stroke="#fbbf24"
            stroke-width="1.4"
            stroke-dasharray="4 3"
          />
          <text
            :x="scaleX(fLower)"
            y="23"
            fill="#fbbf24"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            F_lower (-1.5 IQR)
          </text>

          <line
            :x1="scaleX(fUpper)"
            y1="25"
            :x2="scaleX(fUpper)"
            y2="101"
            stroke="#fbbf24"
            stroke-width="1.4"
            stroke-dasharray="4 3"
          />
          <text
            :x="scaleX(fUpper)"
            y="23"
            fill="#fbbf24"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            F_upper (+1.5 IQR)
          </text>

          <!-- Horizontal Whiskers -->
          <!-- Lower Whisker: from whiskerLower to Q1 -->
          <line
            :x1="scaleX(whiskerLower)"
            y1="72"
            :x2="scaleX(q1)"
            y2="72"
            stroke="#34d399"
            stroke-width="1.8"
          />
          <!-- Whisker Lower End Cap -->
          <line
            :x1="scaleX(whiskerLower)"
            y1="56"
            :x2="scaleX(whiskerLower)"
            y2="88"
            stroke="#34d399"
            stroke-width="2"
            stroke-linecap="round"
          />

          <!-- Upper Whisker: from Q3 to whiskerUpper -->
          <line
            :x1="scaleX(q3)"
            y1="72"
            :x2="scaleX(whiskerUpper)"
            y2="72"
            stroke="#34d399"
            stroke-width="1.8"
          />
          <!-- Whisker Upper End Cap -->
          <line
            :x1="scaleX(whiskerUpper)"
            y1="56"
            :x2="scaleX(whiskerUpper)"
            y2="88"
            stroke="#34d399"
            stroke-width="2"
            stroke-linecap="round"
          />

          <!-- Central Box: Q1 to Q3 -->
          <rect
            :x="scaleX(q1)"
            y="44"
            :width="Math.max(2, scaleX(q3) - scaleX(q1))"
            height="56"
            fill="url(#boxBodyGrad)"
            stroke="#34d399"
            stroke-width="1.8"
            rx="3"
          />

          <!-- Median Vertical Bar -->
          <line
            :x1="scaleX(median)"
            y1="42"
            :x2="scaleX(median)"
            y2="102"
            stroke="#00e599"
            stroke-width="3"
            stroke-linecap="round"
            filter="url(#medianGlow)"
          />

          <!-- Top IQR Span Bracket -->
          <g>
            <path
              :d="`M ${scaleX(q1)} 38 L ${scaleX(q1)} 32 L ${scaleX(q3)} 32 L ${scaleX(q3)} 38`"
              fill="none"
              stroke="#34d399"
              stroke-width="1.2"
            />
            <text
              :x="(scaleX(q1) + scaleX(q3)) / 2"
              y="28"
              fill="#34d399"
              font-size="9"
              font-family="monospace"
              text-anchor="middle"
              font-weight="bold"
            >
              IQR = {{ iqr.toFixed(2) }}{{ sectorData[activeSectorKey].unit }}
            </text>
          </g>

          <!-- Quartile Labels Below Box -->
          <text
            :x="scaleX(q1)"
            y="115"
            fill="#a7f3d0"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
          >
            Q₁ (25%): {{ q1.toFixed(1) }}
          </text>

          <text
            :x="scaleX(median)"
            y="126"
            fill="#00e599"
            font-size="9.5"
            font-family="monospace"
            text-anchor="middle"
            font-weight="bold"
          >
            Median (50%): {{ median.toFixed(1) }}
          </text>

          <text
            :x="scaleX(q3)"
            y="115"
            fill="#a7f3d0"
            font-size="8.5"
            font-family="monospace"
            text-anchor="middle"
          >
            Q₃ (75%): {{ q3.toFixed(1) }}
          </text>

          <!-- Peer Firm Data Points -->
          <g v-for="(firm, idx) in currentFirms" :key="firm.ticker">
            <!-- Normal Peer Dot -->
            <circle
              v-if="getOutlierCategory(firm.value) === 'nominal'"
              :cx="scaleX(firm.value)"
              :cy="getJitterY(idx, 'nominal')"
              :r="hoveredFirm?.ticker === firm.ticker || selectedFirm?.ticker === firm.ticker ? 5.5 : 3.5"
              fill="#34d399"
              stroke="#071411"
              stroke-width="1.2"
              class="cursor-pointer transition-all duration-150 hover:fill-emerald-200"
              :class="{ 'filter drop-shadow-[0_0_6px_#34d399]': hoveredFirm?.ticker === firm.ticker }"
              @mouseenter="hoveredFirm = firm"
              @mouseleave="hoveredFirm = null"
              @click="selectedFirm = firm"
            />

            <!-- Mild Outlier Dot -->
            <circle
              v-else-if="getOutlierCategory(firm.value) === 'mild'"
              :cx="scaleX(firm.value)"
              :cy="getJitterY(idx, 'mild')"
              :r="hoveredFirm?.ticker === firm.ticker || selectedFirm?.ticker === firm.ticker ? 6.5 : 4.5"
              fill="#f59e0b"
              stroke="#071411"
              stroke-width="1.5"
              class="cursor-pointer transition-all duration-150 animate-pulse hover:fill-amber-200"
              :class="{ 'filter drop-shadow-[0_0_8px_#f59e0b]': hoveredFirm?.ticker === firm.ticker }"
              @mouseenter="hoveredFirm = firm"
              @mouseleave="hoveredFirm = null"
              @click="selectedFirm = firm"
            />

            <!-- Extreme Outlier Dot -->
            <circle
              v-else
              :cx="scaleX(firm.value)"
              :cy="getJitterY(idx, 'extreme')"
              :r="hoveredFirm?.ticker === firm.ticker || selectedFirm?.ticker === firm.ticker ? 7.5 : 5.5"
              fill="#f43f5e"
              stroke="#ffffff"
              stroke-width="1.5"
              class="cursor-pointer transition-all duration-150 hover:fill-rose-300 filter drop-shadow-[0_0_8px_#f43f5e]"
              @mouseenter="hoveredFirm = firm"
              @mouseleave="hoveredFirm = null"
              @click="selectedFirm = firm"
            />
          </g>

          <!-- Interactive Hover Tag Callout on SVG -->
          <g v-if="hoveredFirm">
            <rect
              :x="Math.min(svgWidth - 140, Math.max(10, scaleX(hoveredFirm.value) - 60))"
              y="32"
              width="120"
              height="26"
              rx="4"
              fill="#071411"
              stroke="#34d399"
              stroke-width="1"
              filter="url(#outlierGlow)"
            />
            <text
              :x="Math.min(svgWidth - 80, Math.max(70, scaleX(hoveredFirm.value)))"
              y="45"
              fill="#ffffff"
              font-size="8.5"
              font-family="monospace"
              text-anchor="middle"
              font-weight="bold"
            >
              {{ hoveredFirm.ticker }}: {{ hoveredFirm.value.toFixed(1) }}{{ sectorData[activeSectorKey].unit }}
            </text>
            <text
              :x="Math.min(svgWidth - 80, Math.max(70, scaleX(hoveredFirm.value)))"
              y="54"
              :fill="getOutlierCategory(hoveredFirm.value) === 'nominal' ? '#34d399' : getOutlierCategory(hoveredFirm.value) === 'mild' ? '#fbbf24' : '#f43f5e'"
              font-size="7.5"
              font-family="monospace"
              text-anchor="middle"
            >
              {{ getOutlierCategory(hoveredFirm.value).toUpperCase() }}
            </text>
          </g>
        </svg>
      </div>
    </div>

    <!-- Bottom 3-Column Structured Analytical Invariants Grid -->
    <div class="grid grid-cols-12 gap-2.5 items-stretch">
      <!-- Column 1: Formal Mathematical Cutoffs with Parameter "Where:" Block -->
      <div class="col-span-4 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
            <span class="text-[11px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Tukey Fences Formulation
            </span>
            <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              EDA Standard
            </span>
          </div>

          <!-- Formula Text -->
          <div class="bg-[#071411]/90 p-2 rounded border border-emerald-500/20 font-mono text-[10.5px] leading-relaxed text-emerald-200">
            <div>F_lower = Q₁ - 1.5 × IQR</div>
            <div>F_upper = Q₃ + 1.5 × IQR</div>
            <div class="text-[9.5px] text-slate-400 mt-1 border-t border-emerald-500/15 pt-1">
              IQR = Q₃ - Q₁ &nbsp;|&nbsp; Outer: ±3.0 × IQR
            </div>
          </div>

          <!-- Structured "Where:" Parameter Definitions -->
          <div class="mt-1.5 text-[9.5px] leading-tight text-slate-300">
            <div class="font-bold text-emerald-400 font-mono mb-0.5">Where:</div>
            <ul class="space-y-0.5 text-slate-300">
              <li><strong class="text-white font-mono">Q₁, Q₃:</strong> 25th & 75th empirical percentiles of the peer cohort</li>
              <li><strong class="text-white font-mono">IQR:</strong> Interquartile range containing central 50% equity mass</li>
              <li><strong class="text-white font-mono">±1.5·IQR:</strong> Inner fence boundary (flags mild candidate outliers)</li>
              <li><strong class="text-white font-mono">±3.0·IQR:</strong> Outer fence boundary (flags extreme structural anomalies)</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Column 2: Non-Parametric Invariants & 25% Breakdown Defense -->
      <div class="col-span-4 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
            <span class="text-[11px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Non-Parametric Invariants
            </span>
            <span class="text-[9px] px-1.5 py-0.2 bg-emerald-500/15 text-emerald-400 rounded font-mono">
              Robustness Proof
            </span>
          </div>

          <div class="space-y-1.5 text-[10px] leading-tight text-slate-300">
            <div class="bg-[#071411]/70 p-1.5 rounded border border-emerald-500/15">
              <span class="text-emerald-300 font-semibold font-mono">25% Breakdown Resistance:</span>
              <p class="text-slate-300 text-[9.5px] mt-0.5">
                Up to 25% of peer observations in either tail can be distorted to arbitrary extremes without shifting Q₁ or Q₃ cutoff anchors.
              </p>
            </div>

            <div class="bg-[#071411]/70 p-1.5 rounded border border-emerald-500/15">
              <span class="text-teal-300 font-semibold font-mono">Asymmetry Preservation:</span>
              <p class="text-slate-300 text-[9.5px] mt-0.5">
                Adapts natively to skewed balance sheet metrics (Debt/Equity, P/E) without triggering false symmetrical Gaussian penalties.
              </p>
            </div>

            <div class="bg-[#071411]/70 p-1.5 rounded border border-emerald-500/15">
              <span class="text-amber-300 font-semibold font-mono">Distribution-Free Guarantee:</span>
              <p class="text-slate-300 text-[9.5px] mt-0.5">
                Zero assumptions of normality, protecting equity screening during heavy-tailed systemic liquidity and macro shocks.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Column 3: Inspected Peer Telemetry & Cohort Statistics -->
      <div class="col-span-4 glass-card p-2.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between pb-1 mb-1.5 border-b border-emerald-500/15">
            <span class="text-[11px] font-bold text-emerald-300 uppercase tracking-wider font-mono">
              Peer Diagnostic Card
            </span>
            <span
              class="text-[9px] px-1.5 py-0.2 rounded font-mono font-bold uppercase"
              :class="getOutlierCategory(activeInspectedFirm.value) === 'nominal'
                ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                : getOutlierCategory(activeInspectedFirm.value) === 'mild'
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                  : 'bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse'"
            >
              {{ getOutlierCategory(activeInspectedFirm.value) }}
            </span>
          </div>

          <!-- Inspected Firm Identity -->
          <div class="bg-[#071411]/90 p-2 rounded border border-emerald-500/20 mb-1.5">
            <div class="flex items-center justify-between">
              <span class="text-sm font-bold text-white font-mono">{{ activeInspectedFirm.ticker }}</span>
              <span class="text-xs font-mono font-bold text-emerald-400">
                {{ activeInspectedFirm.value.toFixed(2) }}{{ sectorData[activeSectorKey].unit }}
              </span>
            </div>
            <div class="text-[9.5px] text-slate-400 truncate">{{ activeInspectedFirm.name }}</div>
            <div class="text-[9px] text-slate-500 font-mono">{{ activeInspectedFirm.subsector }}</div>
          </div>

          <!-- Position Metrics -->
          <div class="grid grid-cols-2 gap-1 text-[9.5px] font-mono">
            <div class="bg-[#071411]/70 p-1.5 rounded border border-emerald-500/15">
              <span class="text-slate-400 text-[8.5px] block">Median Distance:</span>
              <span class="text-white font-bold">
                {{ (activeInspectedFirm.value - median >= 0 ? '+' : '') }}{{ (activeInspectedFirm.value - median).toFixed(2) }}{{ sectorData[activeSectorKey].unit }}
              </span>
            </div>
            <div class="bg-[#071411]/70 p-1.5 rounded border border-emerald-500/15">
              <span class="text-slate-400 text-[8.5px] block">Distance / IQR:</span>
              <span
                class="font-bold"
                :class="Math.abs((activeInspectedFirm.value - median) / iqr) > 3.0
                  ? 'text-rose-400'
                  : Math.abs((activeInspectedFirm.value - median) / iqr) > 1.5
                    ? 'text-amber-400'
                    : 'text-emerald-400'"
              >
                {{ (Math.abs(activeInspectedFirm.value - median) / (iqr || 0.001)).toFixed(2) }}x IQR
              </span>
            </div>
          </div>

          <!-- Interactive Instruction Hint -->
          <div class="text-[8.5px] text-slate-400 mt-1 text-center font-mono">
            Hover or click any SVG dot point to inspect peer firm position.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
