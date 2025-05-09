<template>
  <div class="panel">
    <button class="close" @click="$emit('close')">×</button>
    <h3>{{ data.title }}</h3>
    <ul>
      <li v-for="p in data.papers" :key="p.method">
        <strong>{{ p.method }}</strong>
        <span> ({{ p.source }}, {{ p.backbone }})</span>
        <div>Scenario: {{ p.scenario.join(', ') }}</div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
interface Paper { method:string; source:string; backbone:string; scenario:string[] }
interface Section { title:string; papers:Paper[] }
const props = defineProps<{ data: Section }>();
</script>

<style scoped>
.panel {
  width:30%; height:80vh; overflow:auto;
  border-left:1px solid #ccc; padding:1rem;
  background:#fafafa;
}
.close {
  float:right; font-size:1.2rem; background:none; border:none;
}
</style>
