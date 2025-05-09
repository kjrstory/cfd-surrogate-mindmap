<template>
  <!-- 네트워크를 그릴 컨테이너 -->
  <div ref="container" class="mindmap-container"></div>
</template>

<script lang="ts" setup>
// Vue Composition API 불러오기
import { onMounted, ref, watch } from 'vue';
// vis-network의 DataSet, Network 불러오기
import { DataSet, Network } from 'vis-network/standalone';
// 방금 만든 타입
import type { TreeData } from './MindMap.types';

// Props로 트리 데이터 받기
interface Props { tree: TreeData }
const props = defineProps<Props>();

// 렌더링 컨테이너 참조
const container = ref<HTMLElement>();

// vis.Network 인스턴스
let network: Network;

/**
 * TreeData → vis-network nodes, edges로 변환
 */
function buildVisData(tree: TreeData) {
  let id = 0;
  const nodes: any[] = [];
  const edges: any[] = [];

  // 루트(Backbone) 레벨
  for (const [bb, grids] of Object.entries(tree)) {
    const bbId = ++id;
    nodes.push({ id: bbId, label: bb, group: 'backbone' });

    // GridType 레벨
    for (const [gt, methods] of Object.entries(grids)) {
      const gtId = ++id;
      nodes.push({ id: gtId, label: gt, group: 'grid' });
      edges.push({ from: bbId, to: gtId });

      // Method 레벨
      for (const method of Object.keys(methods)) {
        const mId = ++id;
        nodes.push({ id: mId, label: method, group: 'method' });
        edges.push({ from: gtId, to: mId });
      }
    }
  }

  return {
    nodes: new DataSet(nodes),
    edges: new DataSet(edges)
  };
}

// 컴포넌트 마운트 시 실행
onMounted(() => {
  const { nodes, edges } = buildVisData(props.tree);
  network = new Network(container.value!, { nodes, edges }, {
    layout: { hierarchical: { enabled: true } },
    nodes: { shape: 'box' },
    interaction: { hover: true }
  });

  // 클릭 이벤트 처리
  network.on('click', params => {
    if (params.nodes.length) {
      const nodeId = params.nodes[0];
      const label = network.body.data.nodes.get(nodeId).label;
      // 예: 부모 컴포넌트로 클릭된 레이블 emit
      // emit('select-node', label);
      console.log('Clicked:', label);
    }
  });
});

// props.tree가 바뀌면 다시 렌더링
watch(() => props.tree, (newTree) => {
  const { nodes, edges } = buildVisData(newTree);
  network.setData({ nodes, edges });
});
</script>

<style scoped>
.mindmap-container {
  width: 100%;
  height: 600px;
  border: 1px solid #ddd;
}
</style>
