import { createRouter, createWebHistory } from "vue-router";
// import Doctors from "../views/Doctors.vue";
// import Booking from "../views/DoctorDetail.vue";
import Home from "../views/Home.vue";

const routes = [
    { path: "/", name: "Home", component: Home },
    // { path: "/doctors/:specialId", name: "Doctors", component: Doctors},
    // { path: "/booking/:doctorId", name: "Booking", component: Booking},
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
