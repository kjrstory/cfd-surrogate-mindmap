<template>
  <div class="app">
    <!-- sections가 로드되면 MindMap 렌더 -->
    <MindMap
      v-if="sections"
      :sections="sections"
      @select="onSelect"
    />
    <!-- 선택된 섹션이 있으면 우측 패널 열기 -->
    <SectionPanel
      v-if="selectedSection"
      :data="sections[selectedSection]"
      @close="selectedSection = null"
    />
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import MindMap from './components/MindMap.vue'
import SectionPanel from './components/SectionPanel.vue'

type Paper   = { method:string; source:string; backbone:string; scenario:string[] }
type SecData = { title:string; papers:Paper[] }
type Sections = Record<string,SecData>

const sections = ref<Sections|null>(null)
const selectedSection = ref<string|null>(null)

onMounted(async () => {
  // 여기도 BASE_URL 사용
  const url = `${import.meta.env.BASE_URL}assets/sections.json`
  console.log('Fetching sections from', url)
  const res = await fetch(url)
  if (!res.ok) {
    console.error('sections.json load failed:', res.status)
    return
  }
  sections.value = await res.json()
})

function onSelect(secKey: string) {
  selectedSection.value = secKey
}
</script>

<style>
.app {
  display: flex;
  height: 100vh;
}
</style>
