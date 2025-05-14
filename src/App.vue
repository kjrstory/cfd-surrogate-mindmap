<template>
  <div id="app">
    <header class="header">
      <h1>Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey</h1>
      <p class="caption">Visualization based on the above survey (not authored by me).</p>
    </header>
    <DynamicGraph @select="selected = $event" />

    <!-- selected가 '3.1.1'일 때만 패널 보여주기 -->
    <Section3_1_1Detail
      v-if="selected === '3.1.1'"
      @close="selected = null"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import DynamicGraph from './components/DynamicGraph.vue'
import Section3_1_1Detail from './components/Section3_1_1Detail.vue'

const selected = ref<string|null>(null)
</script>

<style>
#app {
  font-family: Arial, sans-serif;
}

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
</style>
