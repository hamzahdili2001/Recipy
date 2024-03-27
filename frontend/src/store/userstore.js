import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore("user", {
	state: () => ({
		BackendBaseUrl: "http://127.0.0.1:8000",
		user: {
			isAuthenticated: false,
			id: null,
			username: null,
			email: null,
			first_name: null,
			last_name: null,
			access: null,
			refresh: null
		}
	}),
	actions: {
		initStore() {
			if (localStorage.getItem("user.access")) {
				this.user.access = localStorage.getItem("user.access");
				this.user.refresh = localStorage.getItem("user.refresh");
				// this.user.id = localStorage.getItem("user.id");
				this.user.username = localStorage.getItem("user.username");
				this.user.email = localStorage.getItem("user.email");
				this.user.first_name = localStorage.getItem("user.first_name");
				this.user.last_name = localStorage.getItem("user.last_name");
				this.user.isAuthenticated = localStorage.getItem(
					"user.isAuthenticated"
				);
				this.refreshToken();

				console.log("init user", this.user.isAuthenticated);
			}
		},
		setToken(data) {
			this.user.access = data.access.token;
			this.user.refresh = data.refresh.token;
			this.user.isAuthenticated = true;

			localStorage.setItem("user.access", data.access.token);
			localStorage.setItem("user.refresh", data.refresh.token);
		},

		removeToken() {
			console.log("removeToken");

			this.user.access = null;
			this.user.refresh = null;
			this.user.id = null;
			this.user.username = null;
			this.user.email = null;
			this.user.first_name = null;
			this.user.last_name = null;
			this.user.isAuthenticated = false;
			localStorage.setItem("user.access", "");
			localStorage.setItem("user.refresh", "");
			localStorage.setItem("user.id", "");
			localStorage.setItem("user.username", "");
			localStorage.setItem("user.email", "");
			localStorage.setItem("user.first_name", "");
			localStorage.setItem("user.last_name", "");
			localStorage.setItem("user.isAuthenticated", "");
		},
		setUserInfo(data) {
			console.log("setUserInfo", data);

			// this.user.id = localStorage.setItem("user.id", this.user.id);
			localStorage.setItem("user.username", data.username);
			localStorage.setItem("user.email", data.email.email);
			localStorage.setItem("user.first_name", data.first_name);
			localStorage.setItem("user.last_name", data.last_name);
			localStorage.setItem("user.isAuthenticated", true);
		},

		refreshToken() {
			axios
				.post(this.BackendBaseUrl + "/api/token/refresh", {
					refresh: this.user.refresh
				})
				.then(response => {
					console.log(response.data);
					this.user.access = response.data.access_token;

					localStorage.setItem("user.access", response.data.access_token);
					axios.defaults.headers.common["Authorization"] =
						"Bearer " + response.data.access_token;
				})
				.catch(error => {
					console.log(error);
					this.removeToken();
				});
		}
	}
});
