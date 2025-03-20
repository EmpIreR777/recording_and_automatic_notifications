import { createApp } from "vue";
import App from "./App.vue";
import "./assets/styles/index.css";
import router from "./router";
import { VueTelegramPlugin } from "vue-tg";

const app = createApp(App);
app.use(router);
app.use(VueTelegramPlugin);
app.provide("BASE_SITE", "https://mir-doctor24.loca.lt");
app.mount("#app");