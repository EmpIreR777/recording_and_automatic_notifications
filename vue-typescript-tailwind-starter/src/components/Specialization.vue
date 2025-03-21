<script setup lang="ts">
import { useRouter } from "vue-router";

defineProps(["specialization", "description", "icon", "specialId"]);

const router = useRouter();
</script>

<template>
  <div
    class="bg-white rounded-xl shadow-lg overflow-hidden transition-transform duration-300 hover:scale-105 flex flex-col items-center justify-center p-6"
  >
    <div
      class="bg-blue-100 rounded-full p-6 w-28 h-28 flex items-center justify-center"
    >
      <i :class="icon + ' text-blue-600 text-4xl'" aria-hidden="true"></i>
    </div>
    <h3 class="text-xl font-bold text-gray-800 m-2">{{ specialization }}</h3>
    <p
      class="text-gray-600 mb-4 text-center h-30 overflow-hidden"
      title="{{ description }}"
    >
      {{ description }}
    </p>
    <button
      @click="() => router.push(`/doctors/${specialId}`)"
      class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition-colors"
    >
      Записаться
    </button>
  </div>
</template>

<style scoped></style>