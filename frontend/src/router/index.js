import UserProfileBookmarks from "@/components/UserProfileBookmarks.vue";
import HomeView from "@/Views/HomeView.vue";
import ProfileView from "@/Views/ProfileView.vue";
import UserProfilePosts from "@/components/UserProfilePosts.vue";
import UserProfileEdit from "@/components/UserProfileEdit.vue";
import { createWebHistory, createRouter } from "vue-router";
import AppRecipeCardDetails from "@/components/AppRecipeCardDetails.vue";
import AppFilters from "@/components/AppFilters.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: "/",
			name: "home",
			component: HomeView
		},
		{
			path: "/profile",
			name: "user-profile",
			component: ProfileView,
			children: [
				{
					path: "bookmarks",
					name: "user-bookmarks",
					component: UserProfileBookmarks
				},
				{
					path: "posts",
					name: "user-posts",
					component: UserProfilePosts
				},
				{
					path: "edit",
					name: "profile-edit",
					component: UserProfileEdit
				}
			]
		},
		{
			path: "/details/:id",
			name: "recipe-details",
			component: AppRecipeCardDetails
		},
		{
			path: "/recipes-filter",
			name: "recipes-filter",
			component: AppFilters
		}
	]
});

export default router;
