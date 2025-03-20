import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    { path: "/", name: "Home", component: Home },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior() {
        // Всегда прокручивать к верху страницы
        return { top: 0 };
    },
});

export default router;
