import { useFetch } from "@vueuse/core";
import { ref, computed, onMounted, onBeforeUnmount } from "vue";
import { inject } from "vue";
import Specialization from "@/components/Specialization.vue";


interface Doctor {
    id: number;
    specialization: string;
    description: string;
    icon: string;
    }

const BASE_SITE = inject('BASE_SITE') as string;
const searchQuery = ref('');

const {
    data: doctors,
    isFetching,
    error
    } = useFetch(`${BASE_SITE}/specialists`).get().json();

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



<script setup lang="ts">
</script>


<template>
    <!-- header -->
    <div>Тут будет контент главной страницы</div>
</template>
<style scoped></style>
