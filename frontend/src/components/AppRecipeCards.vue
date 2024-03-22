<template>
  <div class="mt-10 mb-10 mx-15">
    <h1>Hand-Picked Recipes</h1>
    <div class="d-flex justify-center ga-10 align-center flex-wrap mt-8">
      <v-col v-if="recipeStore.recipes.length > 0" v-for="recipe of recipeStore.recipes" :key="recipe.id" class="pa-0"
        style="min-width: 322px;">
        <v-card :loading="recipeStore.loading" class="my-2">
          <template v-slot:loader="{ isActive }">
            <v-progress-linear :active="isActive" color="deep-purple" height="4" indeterminate></v-progress-linear>
          </template>

          <v-img height="250" :src="recipe.image" cover></v-img>

          <v-card-item>
            <v-card-title>{{ recipe.title }}</v-card-title>

            <v-card-subtitle>
              <span class="me-1">Ready in {{ recipe.readyInMinutes }} minutes</span>
              <v-icon color="error" icon="mdi-fire-circle" size="small"></v-icon>
            </v-card-subtitle>
          </v-card-item>

          <v-card-text>
            <v-row align="center" class="mx-0">
              <v-rating :model-value="recipeStore.convertToRating(recipe.spoonacularScore)" color="amber"
                density="compact" size="small" half-increments readonly></v-rating>

              <div class="text-grey ms-4">
                {{ recipeStore.convertToRating(recipe.spoonacularScore) }}
              </div>
            </v-row>

            <div class="my-4 text-subtitle-1" v-if="recipe.cuisines.length > 0">
              <v-icon size="medium" class="mb-1 text-grey">mdi-chef-hat</v-icon> {{ recipe.cuisines.join(', ') }}
            </div>

            <div class="my-4 text-subtitle-1" v-else>
              <v-icon size="medium" class="mb-1 text-grey">mdi-chef-hat</v-icon> Global
            </div>

            <div class="my-4">{{ recipeStore.truncateSummary(recipe.summary, 200) }}</div>
          </v-card-text>

          <v-card-actions>
            <v-btn color="deep-purple-lighten-2" variant="text" @click="recipeStore.reserve"
              :to="'/details/' + recipe.id">
              READ MORE
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col v-else class="text-center p-15 text-grey">
        <h1>No Recipe Found</h1>
        <p>Maybe you need an API Key, Go to <a href="https://spoonacular.com/" target="_blank">spoonacular.com</a> to
          get it.
        </p>
      </v-col>
    </div>

    <div class="d-flex justify-center mt-8" v-if="recipeStore.recipes.length > 0">
      <v-btn style="border: 2px solid #000;" @click="recipeStore.loadMoreRecipes" class="rounded-0 text-center"
        elevation="0">Load More</v-btn>
    </div>
  </div>
</template>
<script>
import { useRecipesStore } from '@/store/recipesStore';

export default {
  setup() {
    const recipeStore = useRecipesStore();
    recipeStore.getRecipes();
    return {
      recipeStore
    };
  }
}
</script>
