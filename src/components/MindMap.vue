<template>
  <div ref="canvas" class="mindmap-canvas"></div>
</template>

<script lang="ts" setup>
import 'vis-network/styles/vis-network.css'
import { onMounted, ref, watch } from 'vue'
import { DataSet, Network } from 'vis-network/standalone'

type Paper   = { method:string; source:string; backbone:string; scenario:string[] }
type SecData = { title:string; papers:Paper[] }
type Sections = Record<string,SecData>

// 부모로부터 sections만 받음
const props = defineProps<{ sections: Sections }>()
const emit  = defineEmits<{
  (e: 'select', secKey: string): void
}>()

const canvas = ref<HTMLElement>()

function initGraph(secs: Sections) {
  let id = 0
  const nodes: any[] = []
  const edges: any[] = []

  nodes.push({ id: ++id, label: 'ML for CFD', secKey: null, group:'root' })

  Object.entries(secs).forEach(([key, info]) => {
    // 부모 찾기 (§3.1.1 → parentKey='3.1', §3.1 → '3')
    const parts = key.split('.')
    const parentKey = parts.length > 1 ? parts.slice(0, -1).join('.') : null

    // 부모 노드 ID 조회
    const parentNode = nodes.find(n => n.secKey === parentKey) || nodes[0]
    const nodeId = ++id

    nodes.push({
      id: nodeId,
      label: info.title,
      secKey: key,
      group: 'section'
    })
    edges.push({ from: parentNode.id, to: nodeId })
  })

  const network = new Network(canvas.value!, {
    nodes: new DataSet(nodes),
    edges: new DataSet(edges)
  }, {
    physics: { enabled: true, stabilization: false },
    layout: { randomSeed: 1 },
    nodes: { shape: 'box', margin: 10 },
    interaction: { dragNodes: true, dragView: true, zoomView: true }
  })

  network.on('click', params => {
    if (!params.nodes.length) return
    const node = nodes.find(n => n.id === params.nodes[0])
    if (node?.secKey) emit('select', node.secKey)
  })
}

onMounted(() => initGraph(props.sections))
watch(() => props.sections, s => initGraph(s))
</script>

<style scoped>
.mindmap-canvas {
  width: 70%;
  height: 100%;
  border: 1px solid #ccc;
}
</style>
