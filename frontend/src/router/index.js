import UserProfileBookmarks from "@/components/UserProfileBookmarks.vue";
import HomeView from "@/Views/HomeView.vue";
import ProfileView from "@/Views/ProfileView.vue";
import UserProfilePosts from "@/components/UserProfilePosts.vue";
import UserProfileEdit from "@/components/UserProfileEdit.vue";
import { createWebHistory, createRouter } from "vue-router";
import DetailsView from "@/Views/DetailsView.vue";
import FiltersView from "@/Views/FiltersView.vue";
import AppRecipeCards from "@/components/AppRecipeCards.vue";
import AboutView from "@/Views/AboutView.vue";
import NotFoundView from "@/Views/NotFoundView.vue";

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
			meta: { requiresAuth: true },
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
			component: DetailsView
		},
		{
			path: "/recipes-filter",
			name: "recipes-filter",
			component: FiltersView
		},
		{
			path: "/recipes",
			name: "all-recipes",
			component: AppRecipeCards
		},
		{
			path: "/about",
			name: "about",
			component: AboutView
		},
		{
			path: "/:pathMatch(.*)*",
			name: "NotFound",
			component: NotFoundView
		}
	]
});

export default router;
