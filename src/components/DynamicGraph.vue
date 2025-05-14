<template>
  <div ref="graphContainer" class="graph-container"></div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { DataSet, Network } from 'vis-network/standalone'
import 'vis-network/styles/vis-network.css'

const emit = defineEmits<{
  (e: 'select', sectionKey: string | null): void
}>()


const graphContainer = ref<HTMLElement>()

onMounted(async () => {
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
  // 1) 클릭된 노드가 있으면 ID, 없으면 undefined
  const nodeId = params.nodes[0] as number | undefined

  // 2) 기본은 null (패널 닫기)
  let sectionKey: string | null = null

  if (nodeId !== undefined) {
    // 3) DataSet에서 노드 객체 꺼내기
    const nodeData = nodes.get(nodeId)
    if (nodeData && typeof nodeData.label === 'string') {
      // 4) label 맨 앞 숫자 토큰을 sectionKey 로 추출
      sectionKey = nodeData.label.split(' ')[0]
    }
  }

  // 5) 최종 선택 키(또는 null) emit
  emit('select', sectionKey)
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
