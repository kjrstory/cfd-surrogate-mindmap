<template>
  <div id="app" class="app">
    <div class="graph-panel">
      <header class="header">
        <h1>Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey</h1>
        <p class="caption">Visualization based on the above survey (not authored by me).</p>
      </header>
      <DynamicGraph @select="selected = $event" />
    </div>

    <!-- selected가 '3.1.1'일 때만 패널 보여주기 -->
    <aside class="detail-panel" v-if="selected === '3.1.1'">
      <Section3_1_1Detail @close="selected = null" />
    </aside>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import DynamicGraph from './components/DynamicGraph.vue'
import Section3_1_1Detail from './components/Section3_1_1Detail.vue'

const selected = ref<string|null>(null)
</script>

<style>
.header {
  text-align: center;
  padding: 1rem 0;
  background: #f5f5f5;
  border-bottom: 1px solid #ddd;
}

.header h1 {
  margin: 0;
  font-size: 1.8rem;
  color: #333;
}

.header .caption {
  margin: 0.5rem 0 0;
  font-size: 0.9rem;
  color: #666;
}

#app, .app {
  width: 100%; height: 100vh;
  margin: 0; padding: 0;
}

.app {
  display: flex;
}

/* 그래프 영역 */
.graph-panel {
  flex: 1;
  position: relative;
}

/* 상세 패널 (aside) */
.detail-panel {
  width: 400px;             /* 원하는 너비 */
  background: #fff;
  border-left: 1px solid #ddd;
  overflow-y: auto;
  box-shadow: -2px 0 6px rgba(0,0,0,0.1);
}
</style>



