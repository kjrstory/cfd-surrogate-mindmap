<template>
  <div ref="graphContainer" class="graph-container"></div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { DataSet, Network } from 'vis-network/standalone'
import 'vis-network/styles/vis-network.css'

const graphContainer = ref<HTMLElement>()

onMounted(async () => {
  // DEV('/') vs PROD('/<repo>/') 자동 처리
  const base = import.meta.env.DEV ? '/' : import.meta.env.BASE_URL
  const url  = `${base}assets/graph-data.json`

  console.log('[DynamicGraph] fetching JSON from', url)
  const res = await fetch(url)
  if (!res.ok) {
    console.error('[DynamicGraph] failed to load', res.status, res.statusText)
    return
  }
  const data = await res.json() as {
    nodes: Array<{ id: number; label: string }>,
    edges: Array<{ from: number; to: number }>
  }
  console.log('[DynamicGraph] loaded data:', data)

  // vis DataSet에 동적 데이터 적용
  const nodes = new DataSet(data.nodes)
  const edges = new DataSet(data.edges)

  // Network 생성
  new Network(graphContainer.value!, { nodes, edges }, {
    physics: { enabled: true, stabilization: false },
    layout: { randomSeed: 1 },
    nodes: { shape: 'box',
      font: {
        face: 'DynaPuff',
        size: 14,
        align: 'center'
      },
      shadow: {
        enabled: true,
        color: 'rgba(0,0,0,0.3)',
        size: 10,
        x: 5,
        y: 5
    }
   },
    edges: { 
        color: { color: '#000000' },
        smooth: { type: 'cubicBezier' }
    },
    interaction: { dragNodes: true, dragView: true, zoomView: true }
  })

  network.fit({
    animation: false
  })
})
</script>

<style scoped>
.graph-container {
  width: 100%;
  height: 800px;
  border: 1px solid #999;
}
</style>
