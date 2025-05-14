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
  const network = new Network(graphContainer.value!, { nodes, edges }, {
    physics: {
      enabled: true,
      stabilization: {
        enabled: true,
        iterations: 2000,       // 안정화 반복 수
        updateInterval: 25
      },
      barnesHut: {
        gravitationalConstant: -3000,  // 음수일수록 강한 반발력
        centralGravity: 0.3,
        springLength: 150,
        springConstant: 0.02,
        damping: 0.09
      }
    },
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

  network.on('click', params => {
  if (!params.nodes.length) return;
  const nodeId = params.nodes[0];
  const node = nodes.get(nodeId);
  if (node && node.label.startsWith('3.1.1')) {
    emit('select', '3.1.1');
  }
});
})
</script>

<style scoped>
.graph-container {
  width: 100%;
  height: 800px;
  border: 1px solid #999;
}
</style>
