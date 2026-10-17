import { defineConfig } from 'vite'
import fsp from 'node:fs/promises'

export default defineConfig({
  server: {
    fs: {
      strict: false,
    },
  },
  plugins: [
    {
      name: 'decode-spaces-plugin',
      enforce: 'pre',
      transformIndexHtml: {
        order: 'pre',
        handler(html) {
          return html.replace(/src="([^"]+)"/g, (match, p1) => {
            return `src="${decodeURI(p1)}"`
          })
        },
      },
      resolveId(id) {
        if (id && id.includes('%20')) {
          return decodeURI(id)
        }
      },
      async load(id) {
        if (id && id.includes('%20')) {
          try {
            return await fsp.readFile(decodeURI(id), 'utf-8')
          } catch {
            return null
          }
        }
      },
    },
  ],
})
