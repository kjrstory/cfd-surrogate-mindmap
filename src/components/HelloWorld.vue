<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue'

const props = defineProps<{ msg: string }>()
</script>

<style scoped>
.hello {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: Arial, sans-serif;
}
</style>
