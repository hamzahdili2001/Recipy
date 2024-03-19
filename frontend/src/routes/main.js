import { createMemoryHistory, createRouter } from "vue-router";

const routes = [
	//	{ path: "/about", component: AboutView }
];

const router = createRouter({
	history: createMemoryHistory(),
	routes
});

export default {
	routes
};
