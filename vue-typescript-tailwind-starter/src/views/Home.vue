<script setup lang="ts">
import { useFetch } from '@vueuse/core';
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { inject } from 'vue';
import Specialization from '../components/Specialization.vue';

interface Doctor {
    id: number;
    specialization: string;
    description: string;
    icon: string;
}

const BASE_SITE = inject('BASE_SITE') as string;
const searchQuery = ref<string>('');

const {
    data: doctors,
    isFetching,
    error
} = useFetch<Doctor[]>(`${BASE_SITE}/specialists`).get().json();

const filteredDoctors = computed(() => {
    if (!doctors.value) return [] as Doctor[];

    const query = searchQuery.value.toLowerCase().trim();
    if (!query) return doctors.value;

    return doctors.value.filter((doctor: Doctor) => {
        return (
            doctor.specialization.toLowerCase().includes(query) ||
            doctor.description.toLowerCase().includes(query)
        );
    });
});

// Обработчик клика по документу
const handleClickOutside = (event: MouseEvent) => {
    const inputElement = document.getElementById('search');
    if (inputElement && !inputElement.contains(event.target as Node)) {
        inputElement.blur(); // Снять фокус с поля ввода
    }
};

// Установка обработчика при монтировании компонента
onMounted(() => {
    document.addEventListener('click', handleClickOutside);
});

// Удаление обработчика при размонтировании компонента
onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
    <div class="mb-12 mt-5">
        <div class="relative max-w-xl mx-auto">
            <input v-model="searchQuery" type="text" id="search" placeholder="Поиск специалиста..."
                class="w-full px-4 py-3 rounded-lg shadow-sm border border-gray-500 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500" />
            <button class="absolute right-3 top-3 text-gray-400">
                <i class="fas fa-search"></i>
            </button>
        </div>
    </div>

    <div>
        <div v-if="isFetching" class="text-center">
            <p>Загрузка...</p>
        </div>

        <div v-else-if="error" class="text-center text-red-500">
            <p>Ошибка: {{ error.message }}</p>
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div v-for="doctor in filteredDoctors" :key="doctor.id">
                <Specialization :specialization="doctor.specialization" :description="doctor.description"
                    :icon="doctor.icon" :specialId="doctor.id" />
            </div>
        </div>
    </div>
</template>