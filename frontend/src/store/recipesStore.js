import { defineStore } from "pinia";
import axios from "axios";

export const useRecipesStore = defineStore("recipes", {
	state: () => ({
		loading: false,
		selection: 1,
		loadCount: 12,
		recipes: [],
		recipe: {},
		query: "",
		cuisine: [],
		diet: [],
		intolerances: [],
		filteredRecipes: [],
		cache: JSON.parse(localStorage.getItem("recipeCache")) || {},
		apiKey: "f132a26ce4c84c72a2c3020661631a1a",
		baseUrl: "https://api.spoonacular.com"
	}),
	actions: {
		async loadMoreRecipes() {
			this.loadCount += 3;
			await this.getRecipes();
		},

		async getRecipes() {
			const url = `${this.baseUrl}/recipes/complexSearch?number=${this
				.loadCount}&addRecipeInformation=true&apiKey=${this.apiKey}`;

			if (this.cache[url]) {
				this.recipes = this.cache[url];
				console.log("Data fetched from cache:", this.cache[url]);
			} else {
				try {
					const response = await axios.get(url);
					this.recipes = response.data.results;
					this.cache[url] = this.recipes; // Cache the response data
					localStorage.setItem("recipeCache", JSON.stringify(this.cache));
					console.log("Data fetched from API:", this.recipes);
				} catch (error) {
					console.error("Error:", error);
				}
			}
		},

		async getRecipeById(recipeId) {
			const url = `${this.baseUrl}/recipes/${recipeId}/information?apiKey=${this
				.apiKey}`;
			console.log("Data fetched from cache:", this.cache[url]);
			if (this.cache[url]) {
				this.recipe = this.cache[url];
			} else {
				try {
					const response = await axios.get(url);
					this.recipe = response.data;
					this.cache[url] = this.recipe;
					localStorage.setItem("recipeCache", JSON.stringify(this.cache));
					console.log("Data fetched from API:", this.recipe);
				} catch (error) {
					console.error("Error:", error);
				}
			}
		},
		async getFilteredRecipes() {
			const searchUrl = `${this.baseUrl}/recipes/complexSearch`;
			const params = new URLSearchParams({
				apiKey: this.apiKey,
				query: this.query,
				cuisine: this.cuisine.join(","),
				diet: this.diet.join(","),
				intolerances: this.intolerances.join(","),
				addRecipeInformation: true
			});
			const url = `${searchUrl}?${params}`;
			try {
				const response = await axios.get(url);
				console.log(url);
				this.filteredRecipes = response.data.results;
			} catch (error) {
				console.error("Error fetching recipes:", error);
			}
		},

		convertToRating(score) {
			return (parseInt(score) / 20).toFixed(1);
		},

		async reserve() {
			this.loading = true;
			setTimeout(() => (this.loading = false), 2000);
		},

		truncateSummary(summary, maxLength) {
			const parser = new DOMParser();
			const parsedHTML = parser.parseFromString(summary, "text/html");
			const textContent = parsedHTML.body.textContent.trim();
			if (textContent.length > maxLength) {
				return textContent.substring(0, maxLength) + "...";
			} else {
				return textContent;
			}
		}
	}
});
