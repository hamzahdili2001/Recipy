// Plugins
import { registerPlugins } from "@/plugins";
import routes from "@/routes/main";
// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

const app = createApp(App);

app.use(routes);
registerPlugins(app);

app.mount("#app");
