<template>
  <aside class="detail-panel">
    <button class="close-btn" @click="$emit('close')">×</button>
    <h2>3.1.1 Structured Grids</h2>

    <div v-if="loading" class="loading">Loading…</div>
    <div v-else>
      <table class="detail-table">
        <thead>
          <tr>
            <th>Paper</th>
            <th>Source</th>
            <th>Backbone</th>
            <th>Scenarios</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in papers" :key="p.alias">
            <td>
              <a :href="p.link" target="_blank" rel="noopener">
                {{ p.alias }}
              </a>
            </td>
            <td>{{ p.source }}</td>
            <td>{{ p.backbone }}</td>
            <td>{{ p.scenarios.join(', ') }}</td>
          </tr>
        </tbody>
      </table>
      <div v-if="!papers.length" class="no-data">
        No papers found for this section.
      </div>
    </div>
  </aside>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'

const emit = defineEmits<{
  (e: 'close'): void
}>()

interface Paper {
  alias: string
  link: string
  source: string
  backbone: string
  scenarios: string[]
}

const papers = ref<Paper[]>([])
const loading = ref(true)

onMounted(async () => {
  try {
    const base = import.meta.env.DEV ? '/' : import.meta.env.BASE_URL
    const res = await fetch(`${base}assets/section-papers.json`)
    if (!res.ok) throw new Error(res.statusText)
    const all = await res.json() as Record<string, Paper[]>
    papers.value = all['3.1.1'] || []
  } catch (e) {
    console.error('Failed to load section-papers.json', e)
    papers.value = []
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.detail-panel {
  width: 350px;
  background: #fff;
  border-left: 1px solid #ddd;
  padding: 1rem;
  overflow-y: auto;
  box-shadow: -3px 0 6px rgba(0,0,0,0.1);
  position: relative;
}

.loading,
.no-data {
  text-align: center;
  padding: 1rem;
  color: #666;
}

.close-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  border: none;
  background: none;
  font-size: 1.2rem;
  cursor: pointer;
}

.detail-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.detail-table tr:nth-child(even) {
  background: #f9f9f9;
}

.detail-table tr:hover {
  background: #eef;
}

.detail-table th,
.detail-table td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: left;
}

.detail-table th {
  background: #f5f5f5;
}
</style>
