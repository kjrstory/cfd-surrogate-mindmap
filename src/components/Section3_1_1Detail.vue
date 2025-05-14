<template>
  <div class="detail-panel">
    <button class="close-btn" @click="$emit('close')">×</button>
    <h2>3.1.1 Structured Grids</h2>
    <table class="detail-table">
      <thead>
        <tr>
          <th>Methods</th>
          <th>Source</th>
          <th>Backbone</th>
          <th>Scenarios</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in papers" :key="p.method">
          <td>{{ p.method }} {{ p.ref }}</td>
          <td>{{ p.source }}</td>
          <td>{{ p.backbone }}</td>
          <td>{{ p.scenarios.join(', ') }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts" setup>
import { defineEmits } from 'vue'

const emit = defineEmits<{ (e: 'close'): void }>()

interface Paper {
  method: string
  ref: string
  source: string
  backbone: string
  scenarios: string[]
}

// 3.1.1 용 하드코딩 데이터
const papers: Paper[] = [
  { method: 'DPUF',   ref: '[24]', source: 'J. Fluid Mech.',     backbone: 'CNN', scenarios: ['CylinderFlow'] },
  { method: 'TF-Net', ref: '[25]', source: 'KDD 2020',           backbone: 'CNN', scenarios: ['Turbulent flow'] },
  { method: 'EquNet', ref: '[26]', source: 'ICLR 2021',          backbone: 'CNN', scenarios: ['Rayleigh-Bénard', 'Oceans', 'Heat'] },
  { method: 'RSteer', ref: '[27]', source: 'ICML 2022',          backbone: 'CNN', scenarios: ['smoke'] }
]
</script>

<style scoped>
.detail-panel {
  width: 400px;
  height: 100vh;
  overflow: auto;
  border-left: 1px solid #ddd;
  background: #fff;
  padding: 1rem;
  box-shadow: -2px 0 5px rgba(0,0,0,0.1);
  position: relative;
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
.detail-table th,
.detail-table td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: left;
}
.detail-table th {
  background: #f9f9f9;
}
</style>
