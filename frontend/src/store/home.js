import { defineStore } from "pinia";
export const useAppLoginStore = defineStore({
	id: "app-login",
	state: () => ({
		overlay: false,
		LoginRegister: true
	})
});
