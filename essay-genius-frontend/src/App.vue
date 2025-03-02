<script setup lang="ts">
import PaperCheck from './components/PaperCheck.vue'
</script>

<template>
  <main class="app-main">
    <PaperCheck />
  </main>
</template>

<style>
@import './assets/base.css';

#app {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0;
  font-weight: normal;
  display: flex;
  justify-content: center;
}

.app-main {
  width: 100%;
  max-width: 100%;
  display: flex;
  justify-content: center;
  padding: 0;
  margin: 0;
}

body {
  min-height: 100vh;
  width: 100%;
  margin: 0;
  padding: 0;
  color: #2c3e50;
  background: #f5f7fa;
  line-height: 1.6;
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  font-size: 16px;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
