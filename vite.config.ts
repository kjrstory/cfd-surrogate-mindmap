import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


export default defineConfig(({ mode }) => ({
  base: mode === 'production'
    ? '/cfd-surrogate-mindmap/'  // 빌드된 후 gh-pages 배포용
    : '/',                       // 개발 서버(dev)는 항상 루트(/)
  plugins: [vue()]
}))