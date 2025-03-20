<script setup lang="ts">
import Header from './components/Header.vue';
</script>

<template>
  <div id="app">
    <Header />
    <main class="p-4">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
/* Глобальные стили приложения */
</style>