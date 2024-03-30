import { defineStore } from "pinia";
import axios from "axios";
import router from "@/router/index";

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
			profile_picture: null,
			access: null,
			refresh: null,
			bookmarkedRecipes: {}
		}
	}),
	actions: {
		initStore() {
			if (localStorage.getItem("user.access")) {
				this.user.access = localStorage.getItem("user.access");
				this.user.refresh = localStorage.getItem("user.refresh");
				this.user.profile_picture = localStorage.getItem("user.profil");
				this.user.username = localStorage.getItem("user.username");
				this.user.email = localStorage.getItem("user.email");
				this.user.first_name = localStorage.getItem("user.first_name");
				this.user.last_name = localStorage.getItem("user.last_name");
				this.user.isAuthenticated = localStorage.getItem(
					"user.isAuthenticated"
				);
				this.fetchUserProfilePicture();
				this.refreshToken();

				console.log("init user", this.userProfileImageUrl);
			}
		},
		async fetchUserProfilePicture() {
			try {
				const response = await axios.get(
					"http://127.0.0.1:8000/api/user/profil",
					{
						headers: {
							Authorization: "Bearer " + this.user.access
						},
						responseType: "blob"
					}
				);
				if (response.data) {
					console.log(response.data); // Update state with profile picture URL
					const urlCreator = window.URL || window.webkitURL;
					const imageUrl = urlCreator.createObjectURL(response.data);
					this.user.profile_picture = imageUrl;
				} else {
					this.user.profile_picture = null;
				}
			} catch (error) {
				console.error(error); // Log error if any
				// Handle error
			}
		},
		async fetchBookmarkedRecipes() {
			try {
				const response = await fetch(
					"http://127.0.0.1:8000/api/recipe/get_bookmarks",
					{
						method: "GET",
						headers: {
							Authorization: "Bearer " + this.user.access // Replace with your JWT token
						}
					}
				);
				if (response.ok) {
					const data = await response.json();
					this.user.bookmarkedRecipes = data.data;
					console.log("Bookmarked Recipes:", this.user.bookmarkedRecipes);
				} else {
					console.error(
						"Failed to fetch bookmarked recipes:",
						response.statusText
					);
				}
			} catch (error) {
				console.error("Failed to fetch bookmarked recipes:", error);
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
			this.user.profile_picture = null;
			this.user.isAuthenticated = false;
			localStorage.setItem("user.access", "");
			localStorage.setItem("user.refresh", "");
			localStorage.setItem("user.id", "");
			localStorage.setItem("user.username", "");
			localStorage.setItem("user.email", "");
			localStorage.setItem("user.first_name", "");
			localStorage.setItem("user.last_name", "");
			localStorage.setItem("user.profil", "");
			localStorage.setItem("user.isAuthenticated", "");
			router.push({ name: "home" });
		},
		setUserInfo(data) {
			console.log("setUserInfo", data);

			// this.user.id = localStorage.setItem("user.id", this.user.id);
			localStorage.setItem("user.username", data.username);
			localStorage.setItem("user.email", data.email.email);
			localStorage.setItem("user.first_name", data.first_name);
			localStorage.setItem("user.last_name", data.last_name);
			localStorage.setItem("user.profil", data.profil);
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
	},
	getters: {
		userProfileImageUrl: state => state.user.profile_picture
	}
});
