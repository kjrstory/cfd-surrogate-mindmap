<template>
  <aside class="detail-panel">
    <button class="close-btn" @click="$emit('close')">×</button>
    <h2>3.1.1 Structured Grids</h2>
    <table class="detail-table">
      <thead>
        <tr>
          <!-- 메서드 대신 간단한 논문 별칭을 'Paper' 라고 부릅니다 -->
          <th>Paper</th>
          <th>Source</th>
          <th>Backbone</th>
          <th>Scenarios</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in papers" :key="p.alias">
          <!-- alias 필드를 Paper 이름으로 쓰고, link 프로퍼티로 하이퍼링크 -->
          <td>
            <a :href="p.link" target="_blank" rel="noopener">
              {{ p.alias }}
            </a>
          </td>
          <td>{{ p.source }}</td>
          <td>{{ p.backbone }}</td>
          <td>{{ p.scenarios.join(', ') }}</td>
        </tr>
      </tbody>
    </table>
  </aside>
</template>

<script lang="ts" setup>
const emit = defineEmits<{
  (e: 'close'): void
}>()

interface Paper {
  alias: string    // DPUF, TF-Net 등의 간단 별칭
  link: string     // DOI 또는 GitHub URL 등
  source: string
  backbone: string
  scenarios: string[]
}

// 예제 데이터: 실제로는 JSON으로부터 가져와도 됩니다.
const papers: Paper[] = [
  {
    alias: 'DPUF [24]',
    link: 'https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/datadriven-prediction-of-unsteady-flow-over-a-circular-cylinder-using-deep-learning/0DB7E8CFF3BF3D5AB4C73A9F38150316',
    source: 'J. Fluid Mech.',
    backbone: 'CNN',
    scenarios: ['CylinderFlow']
  },
  {
    alias: 'TF-Net [25]',
    link: 'https://ucsdml.github.io/jekyll/update/2020/08/23/TF-Net.html',
    source: 'KDD 2020',
    backbone: 'CNN',
    scenarios: ['Turbulent flow']
  },
  {
    alias: 'EquNet [26]',
    link: 'https://arxiv.org/abs/2002.03061',
    source: 'ICLR 2021',
    backbone: 'CNN',
    scenarios: ['Rayleigh-Bénard', 'Oceans', 'Heat']
  },
  {
    alias: 'RSteer [27]',
    link: 'https://arxiv.org/abs/2201.11969',
    source: 'ICML 2022',
    backbone: 'CNN',
    scenarios: ['smoke']
  }
]
</script>

<style scoped>
.detail-panel {
  width: 350px;
  background: #fff;
  border-left: 1px solid #ddd;
  padding: 1rem;
  overflow-y: auto;
  box-shadow: -3px 0 6px rgba(0,0,0,0.1);
}

.close-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  border: none;
  background: none;
  font-size: 1.2rem;
  cursor: pointer;
}

.detail-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

/* 줄 무늬 효과 */
.detail-table tr:nth-child(even) {
  background: #f9f9f9;
}

/* hover 강조 */
.detail-table tr:hover {
  background: #eef;
}

.detail-table th,
.detail-table td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: left;
}

.detail-table th {
  background: #f5f5f5;
}
</style>
