<script setup lang="ts">
import { ref } from 'vue'

interface Props {
  universityName?: string
  schoolName?: string
  departmentName?: string
  programName?: string
  candidateName?: string
  regNo?: string
  guideName?: string
  projectTitle?: string
  projectSubtitle?: string
  logoSrc?: string
}

const props = withDefaults(defineProps<Props>(), {
  universityName: 'Pondicherry University',
  schoolName: 'Ramanujan School of Mathematical Sciences',
  departmentName: 'Department of Statistics',
  programName: 'M.Sc. Quantitative Finance (MSQF)',
  candidateName: 'N Rohit Vedhanandh',
  regNo: '25MSQUFPY0002',
  guideName: 'Dr. Kiruthika',
  projectTitle: 'FinMetrics Suite',
  projectSubtitle: 'Automated Cross-Sectional Fundamental Diagnostics & Robust Anomaly Intelligence',
  logoSrc: '/pondicherry_university_logo.png',
})

const isHovered = ref(false)
</script>

<template>
  <div class="w-full flex flex-col items-center justify-between h-full py-1 text-slate-100 select-none">
    <!-- Top Institutional Header -->
    <div class="w-full max-w-4xl flex items-center justify-between px-4 py-2 glass-card border-opacity-30">
      <div class="flex items-center gap-3.5">
        <div class="relative flex items-center justify-center">
          <div class="absolute -inset-1 rounded-full bg-emerald-400/20 blur-sm animate-pulse-emerald" />
          <img
            :src="props.logoSrc"
            alt="Pondicherry University Logo"
            class="relative h-12 w-12 object-contain drop-shadow-[0_0_8px_rgba(52,211,153,0.35)]"
          />
        </div>
        <div class="flex flex-col text-left">
          <div class="text-sm font-extrabold tracking-wide text-emerald-400">
            {{ props.universityName }}
          </div>
          <div class="text-[11px] font-semibold text-emerald-200/90 tracking-tight">
            {{ props.departmentName }} &bull; {{ props.schoolName }}
          </div>
          <div class="text-[10px] text-slate-400 font-mono tracking-tight">
            {{ props.programName }}
          </div>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <div class="glass-pill text-[10px] py-0.5 px-2.5 border-emerald-400/30">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping inline-block" />
          <span>Executive Presentation</span>
        </div>
        <div class="glass-pill text-[10px] py-0.5 px-2.5 border-emerald-400/30 text-teal-300">
          <span>Batch 2024–2026</span>
        </div>
      </div>
    </div>

    <!-- Center Hero Section -->
    <div
      class="w-full max-w-4xl my-3 px-6 py-5 glass-card relative overflow-hidden text-center flex flex-col items-center justify-center transition-all duration-500"
      :class="isHovered ? 'border-emerald-400/50 shadow-[0_0_40px_rgba(16,185,129,0.22)]' : ''"
      @mouseenter="isHovered = true"
      @mouseleave="isHovered = false"
    >
      <!-- Background Ambient Glow & Radial Rings -->
      <div class="absolute -top-16 -left-16 w-48 h-48 rounded-full bg-emerald-500/10 blur-2xl pointer-events-none" />
      <div class="absolute -bottom-16 -right-16 w-48 h-48 rounded-full bg-teal-500/10 blur-2xl pointer-events-none" />

      <!-- Animated Pulse Ring & Emblem -->
      <div class="relative mb-3 flex items-center justify-center">
        <!-- Outer Glowing Aura -->
        <div class="absolute w-20 h-20 rounded-full bg-emerald-500/15 blur-md animate-pulse-emerald" />
        
        <!-- Rotating Geometric Orbit -->
        <div class="w-16 h-16 rounded-full border border-emerald-400/30 flex items-center justify-center relative bg-[#071411]/90 shadow-[0_0_20px_rgba(52,211,153,0.25)]">
          <!-- Orbital Satellite Dot -->
          <div class="absolute -top-1 left-1/2 -translate-x-1/2 w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#34D399]" />
          
          <!-- FinMetrics Quantitative Emblem -->
          <svg class="w-8 h-8 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
            <polyline points="16 7 22 7 22 13" />
            <circle cx="8.5" cy="10.5" r="1.5" fill="#34D399" />
            <circle cx="13.5" cy="15.5" r="1.5" fill="#34D399" />
          </svg>
        </div>
      </div>

      <!-- Main Title -->
      <h1 class="text-4xl font-extrabold tracking-tight mb-2">
        <span class="bg-gradient-to-r from-emerald-200 via-teal-100 to-emerald-400 bg-clip-text text-transparent [text-shadow:0_0_24px_rgba(52,211,153,0.35)]">
          {{ props.projectTitle }}
        </span>
      </h1>

      <!-- Subtitle -->
      <p class="text-sm font-medium text-slate-300 max-w-2xl mx-auto leading-relaxed">
        {{ props.projectSubtitle }}
      </p>

      <!-- Architecture Technology Badges -->
      <div class="flex flex-wrap items-center justify-center gap-2 mt-3.5">
        <span class="glass-inset px-2.5 py-1 text-[11px] font-mono text-emerald-300 border-emerald-500/20">
          Python 3.11+
        </span>
        <span class="glass-inset px-2.5 py-1 text-[11px] font-mono text-teal-300 border-teal-500/20">
          FastAPI &amp; Polars
        </span>
        <span class="glass-inset px-2.5 py-1 text-[11px] font-mono text-emerald-300 border-emerald-500/20">
          Scikit-Learn iForest
        </span>
        <span class="glass-inset px-2.5 py-1 text-[11px] font-mono text-cyan-300 border-cyan-500/20">
          Rob-MAD &amp; Tukey IQR
        </span>
        <span class="glass-inset px-2.5 py-1 text-[11px] font-mono text-emerald-300 border-emerald-500/20">
          OpenPyXL 6-Tab Audit
        </span>
      </div>
    </div>

    <!-- Bottom Executive Attribution Card -->
    <div class="w-full max-w-4xl glass-card px-6 py-3 border-emerald-400/25">
      <div class="grid grid-cols-2 gap-6 items-center">
        <!-- Candidate Attribution -->
        <div class="flex flex-col text-left border-r border-emerald-500/20 pr-4">
          <div class="flex items-center gap-2 mb-1">
            <span class="text-[10px] font-bold tracking-wider uppercase text-emerald-400">
              Candidate Attribution
            </span>
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400" />
          </div>
          <div class="text-base font-bold text-white tracking-tight flex items-center gap-2">
            <span>{{ props.candidateName }}</span>
            <span class="text-xs font-mono font-normal text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-400/20">
              {{ props.regNo }}
            </span>
          </div>
          <div class="text-xs text-slate-400 mt-0.5 font-medium">
            {{ props.programName }} &bull; Department of Statistics
          </div>
        </div>

        <!-- Faculty Guidance Attribution -->
        <div class="flex flex-col text-left pl-2">
          <div class="flex items-center gap-2 mb-1">
            <span class="text-[10px] font-bold tracking-wider uppercase text-emerald-400">
              Faculty Guidance
            </span>
            <span class="w-1.5 h-1.5 rounded-full bg-teal-400" />
          </div>
          <div class="text-base font-bold text-white tracking-tight flex items-center gap-2">
            <span>{{ props.guideName }}</span>
            <span class="text-xs font-medium text-teal-300 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-400/20">
              Supervisor &amp; Guide
            </span>
          </div>
          <div class="text-xs text-slate-400 mt-0.5 font-medium">
            {{ props.schoolName }} &bull; {{ props.universityName }}
          </div>
        </div>
      </div>
    </div>

    <!-- Live Engineering Telemetry Strip -->
    <div class="w-full max-w-4xl flex items-center justify-between px-2 pt-2 text-[10px] font-mono text-slate-400">
      <div class="flex items-center gap-3">
        <span class="flex items-center gap-1.5 text-emerald-400 font-semibold">
          <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block animate-pulse" />
          Production Ingestion SLA: &lt;1.8s
        </span>
        <span class="text-slate-600">|</span>
        <span>Coverage: 150+ NSE Equities</span>
        <span class="text-slate-600">|</span>
        <span>Breakdown Point: &epsilon;* = 50%</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-emerald-400 font-semibold">Deterministic Schema Normalization</span>
        <span class="text-slate-600">&bull;</span>
        <span>v2.4 Live Build</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes pulse-emerald {
  0%, 100% {
    transform: scale(1);
    opacity: 0.8;
  }
  50% {
    transform: scale(1.08);
    opacity: 1;
  }
}

.animate-pulse-emerald {
  animation: pulse-emerald 2.5s ease-in-out infinite;
}
</style>
