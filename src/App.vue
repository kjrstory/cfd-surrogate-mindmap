<template>
  <div id="app">
    <!-- MindMap 컴포넌트에 JSON 트리 데이터 전달 -->
    <MindMap :tree="treeData" />
  </div>
</template>

<script lang="ts" setup>
// JSON 파일 import
import treeData from '/assets/data.json'
// 방금 만든 MindMap.vue import
import MindMap from './components/MindMap.vue'
</script>

<style>
/* 필요하면 전역 스타일 추가 */
#app {
  padding: 1rem;
}
</style>
