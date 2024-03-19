/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from "./vuetify";
import { createPinia } from "pinia";
import routes from "@/routes/main";

const pinia = createPinia();

export function registerPlugins(app) {
	app.use(vuetify);
	app.use(pinia);
	app.use(routes);
}
