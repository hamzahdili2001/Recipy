<template>
  <div class="mx-15 my-15" style="height: 100%;">
    <v-form @submit.prevent="recipeStore.getFilteredRecipes">
      <v-row>
        <v-col cols="12" md="12">
          <v-text-field v-model="recipeStore.query" label="Search Query" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-select v-model="recipeStore.cuisine" :items="cuisines" label="Cuisine" variant="outlined"
            multiple></v-select>
        </v-col>
        <v-col cols="12" md="4">
          <v-select v-model="recipeStore.diet" :items="diets" label="Diet" variant="outlined" multiple></v-select>
        </v-col>
        <v-col cols="12" md="4">
          <v-select v-model="recipeStore.intolerances" :items="intolerancesList" variant="outlined" label="Intolerances"
            multiple></v-select>
        </v-col>
        <v-col cols="12">
          <v-btn type="submit" size="x-large" block variant="flat" color="primary" class="text-white">Search</v-btn>
        </v-col>
      </v-row>
      <v-divider :thickness="2" class="my-8"></v-divider>
    </v-form>
    <!--     <v-list-item v-for="recipe in  recipeStore.filteredRecipes " :key="recipe.id" link :to="/details/">
      <v-list-item-title class="my-2 p-3 text-primary" rounded="5">{{ recipe.title }}</v-list-item-title>
    </v-list-item>
  --> <!-- New Cards -->

    <div class="d-flex justify-center ga-10 align-center flex-wrap mt-8">
      <v-col v-for="recipe of recipeStore.filteredRecipes" :key="recipe.id" class="pa-0" style="min-width: 322px;">
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
    </div>
  </div>
</template>
<script>
import { useRecipesStore } from '@/store/recipesStore';
import { ref } from 'vue';

export default {
  setup() {
    const recipeStore = useRecipesStore();

    const cuisines = ref([
      'African', 'American', 'British', 'Cajun', 'Caribbean', 'Chinese', 'Eastern European', 'European', 'French', 'German', 'Greek', 'Indian', 'Irish', 'Italian', 'Japanese', 'Jewish', 'Korean', 'Latin American', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic', 'Southern', 'Spanish', 'Thai', 'Vietnamese'
    ]);
    const diets = ref([
      'Gluten Free', 'Ketogenic', 'Vegetarian', 'Lacto-Vegetarian', 'Ovo-Vegetarian', 'Vegan', 'Pescetarian', 'Paleo', 'Primal', 'Whole30'
    ]);
    const intolerancesList = ref([
      'Dairy', 'Egg', 'Gluten', 'Grain', 'Peanut', 'Seafood', 'Sesame', 'Shellfish', 'Soy', 'Sulfite', 'Tree Nut', 'Wheat'
    ]);

    const getFilteredRecipes = async () => {
      await recipeStore.getFilteredRecipes();
    };

    return {
      recipeStore,
      cuisines,
      diets,
      intolerancesList,
      getFilteredRecipes
    };
  }
};
</script>
