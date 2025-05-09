<template>
  <div ref="container" class="mindmap-container"></div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { DataSet, Network } from 'vis-network/standalone'

interface Paper   { method:string; source:string; backbone:string; scenario:string[] }
interface SecData { title:string; papers:Paper[] }
type Sections   = Record<string,SecData>

// 1) 컨테이너 ref
const container = ref<HTMLElement>()

// 2) 마인드맵 그리기 함수
async function draw() {
  // 경로 계산 (dev vs prod)
  const base = import.meta.env.DEV ? '/' : import.meta.env.BASE_URL
  const url  = `${base}assets/sections.json`
  console.log('[MindMap] fetch', url)

  // JSON 불러오기
  let secs: Sections
  try {
    const res = await fetch(url)
    if (!res.ok) throw new Error(res.statusText)
    secs = await res.json()
    console.log('[MindMap] loaded', secs)
  } catch (err) {
    console.error('[MindMap] load failed, using fallback', err)
    // 최소 예제
    secs = {
      '3.1.1': { title:'§3.1.1 Structured Grids', papers:[
        { method:'DPUF', source:'J.FluidMech.', backbone:'CNN', scenario:['CylinderFlow'] }
      ]},
      '3.1.2': { title:'§3.1.2 Unstructured Mesh', papers:[
        { method:'GNS', source:'ICML2020', backbone:'GNN', scenario:['Variousmaterials'] }
      ]}
    }
  }

  // 3) 노드·엣지 생성
  let id = 0
  const nodes: any[] = []
  const edges: any[] = []

  // 루트
  nodes.push({ id: ++id, label: 'ML for CFD', group:'root' })

  // 섹션별
  Object.entries(secs).forEach(([key, info]) => {
    const parts = key.split('.')
    const parentKey = parts.length > 1 ? parts.slice(0,-1).join('.') : null
    // 부모 노드 찾기 (label 기준)
    const parent = parentKey
      ? nodes.find(n=>n.label.startsWith(`§${parentKey}`))
      : nodes[0]
    const nid = ++id
    nodes.push({ id: nid, label: info.title, group:'section' })
    edges.push({ from: parent.id, to: nid })
  })

  // 4) vis 네트워크
  const net = new Network(container.value!, {
    nodes: new DataSet(nodes),
    edges: new DataSet(edges)
  }, {
    layout: {
      hierarchical: {
        enabled: true,
        direction: 'UD',
        sortMethod: 'directed',
        levelSeparation: 150,
        nodeSpacing: 100
      }
    },
    physics: false,
    nodes: { shape:'box', margin:10 },
    edges: { smooth:{ type:'cubicBezier' } },
    interaction: { dragView:true, zoomView:true }
  })

  // 전체가 보이도록
  net.fit()
}

// 5) mounted시 실행
onMounted(draw)
</script>

<style scoped>
.mindmap-container {
  width: 100%;
  height: 100vh;
  border: 1px solid #444;
}
</style>
