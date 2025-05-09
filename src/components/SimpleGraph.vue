<template>
  <div ref="graphContainer" class="graph-container"></div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
// standalone 번들에서 DataSet, Network 가져오기
import { DataSet, Network } from 'vis-network/standalone'
// CSS 반드시 import
import 'vis-network/styles/vis-network.css'

const graphContainer = ref<HTMLElement>()

onMounted(() => {
  // 1) 노드 데이터 정의
  const nodes = new DataSet([
    { id: 1, label: 'Node 1' },
    { id: 2, label: 'Node 2' }
  ])

  // 2) 엣지 데이터 정의
  const edges = new DataSet([
    { from: 1, to: 2 }
  ])

  // 3) Network 인스턴스 생성
  new Network(graphContainer.value!, {
    nodes,
    edges
  }, {
    // 옵션: 자유 배치 (physics) 활성화
    physics: { enabled: true },
    interaction: { dragNodes: true, zoomView: true }
  })
})
</script>

<style scoped>
.graph-container {
  width: 100%;
  height: 400px;
  border: 1px solid #999;
}
</style>
