import { defineStore } from "pinia";
import axios from "axios";
import { reactive } from "vue";

export const useRecipesStore = defineStore("recipes", {
	state: () => ({
		loading: false,
		selection: 1,
		loadCount: 12,
		recipes: [],
		recipe: {},
		apiKey: "API_KEY"
	}),
	actions: {
		async loadMoreRecipes() {
			this.loadCount += 3;
			await this.getRecipes();
		},

		async getRecipes() {
			try {
				const apiUrl = `https://api.spoonacular.com/recipes/complexSearch?number=${this
					.loadCount}&addRecipeInformation=true&apiKey=${this.apiKey}`;
				const response = await axios.get(apiUrl);
				this.recipes = response.data.results;
				console.log(this.recipes[0]);
			} catch (error) {
				console.error("Error:", error);
			}
		},

		async getRecipeById(recipeId) {
			try {
				const url = `https://api.spoonacular.com/recipes/${recipeId}/information?apiKey=${this
					.apiKey}`;
				const response = await axios.get(url);
				this.recipe = response.data;
				console.log(this.recipe);
			} catch (error) {
				console.error("Error:", error);
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
