/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */
import vuetify from "./vuetify";
import { createPinia } from "pinia";
import router from "@/router/";
// Create Pinia instance
const pinia = createPinia();

export function registerPlugins(app) {
	// Register Vue plugins
	app.use(vuetify);

	// Register Pinia
	app.use(pinia);

	// Register Vue Router
	app.use(router);
}
