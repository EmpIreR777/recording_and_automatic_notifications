import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";
import router from "./router";
import { VueTelegramPlugin } from "vue-tg";

const app = createApp(App);
app.use(router);
app.use(VueTelegramPlugin);
app.provide("BASE_SITE", "http://127.0.0.1:5000");
app.mount("#app");