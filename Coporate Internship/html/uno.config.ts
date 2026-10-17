import { defineConfig, presetUno, presetAttributify } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(),
    presetAttributify(),
  ],
  theme: {
    colors: {
      obsidian: '#071411',
      canvas: '#071411',
      mint: {
        DEFAULT: '#34D399',
        bright: '#34D399',
        glow: 'rgba(52, 211, 153, 0.35)',
      },
      jade: {
        DEFAULT: '#10B981',
        dark: '#064E3B',
      },
      hyper: '#00E599',
      platinum: '#F8FAFC',
      slate: {
        DEFAULT: '#94A3B8',
        sub: '#94A3B8',
        dim: '#64748B',
      },
    },
  },
  shortcuts: {
    'glass-card': 'bg-[#0d211b]/70 backdrop-blur-md border border-[#34d399]/18 rounded-xl shadow-[0_8px_32px_rgba(0,0,0,0.45)] transition-all duration-300',
    'glass-card-hover': 'hover:border-[#34d399]/40 hover:shadow-[0_12px_40px_rgba(16,185,129,0.18)] hover:-translate-y-0.5',
    'glass-inset': 'bg-[#071411]/85 backdrop-blur-sm border border-[#34d399]/12 rounded-lg',
    'glass-pill': 'inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-[#34d399]/12 text-[#34d399] border border-[#34d399]/28',
    'glow-mint': 'shadow-[0_0_20px_rgba(52,211,153,0.35)]',
    'glow-text': '[text-shadow:0_0_12px_rgba(52,211,153,0.45)]',
    'heading-gradient': 'bg-gradient-to-r from-emerald-300 via-teal-200 to-emerald-400 bg-clip-text text-transparent font-bold',
    'subheading-gradient': 'bg-gradient-to-r from-slate-200 to-slate-400 bg-clip-text text-transparent',
  },
})
