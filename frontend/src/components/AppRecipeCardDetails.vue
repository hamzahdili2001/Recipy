<template>
  <div>
    <v-card width="70%" class="mx-auto my-15">
      <v-img class="text-white" height="400" :src="recipesStore.recipe.image" cover>
        <v-card-item class="w-100 h-100" style="background: rgba(0,0,0,0.7)">
          <v-card-title>{{ recipesStore.recipe.title
            }}</v-card-title>
          <v-card-subtitle>Ready in {{ recipesStore.recipe.readyInMinutes }} min</v-card-subtitle>
          <v-btn icon="mdi-bookmark" variant="text"></v-btn>
          <v-btn icon="mdi-heart" variant="text"></v-btn>
          <div style="display: inline;">
            <v-btn @click="showInput" icon variant="text">
              <v-icon>mdi-share</v-icon>
            </v-btn>
            <v-dialog v-model="inputVisible" persistent max-width="400px">
              <v-card>
                <v-card-title>Copy URL</v-card-title>
                <v-card-text>
                  <v-text-field v-model="url" readonly></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <v-btn @click="copyUrl" variant="text">
                    <v-icon>mdi-content-copy</v-icon>
                    Copy
                  </v-btn>
                  <v-btn @click="inputVisible = false" text>
                    Cancel
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-card-item>
      </v-img>
      <v-card-text>
        <v-list>
          <h2 class="mb-5">Recipe Summary:</h2>
          <p v-html="recipesStore.recipe.summary"></p>
          <h2 class="my-5">Information:</h2>
          <strong>Health Score : </strong> {{ recipesStore.recipe.healthScore }}% <br>
          <strong>Spoonacular Score : </strong> {{ truncateDigits(recipesStore.recipe.spoonacularScore) }}% <br>
          <strong>cheap : </strong> {{ recipesStore.recipe.cheap ? "Yes" : "No" }} <br>
          <strong>cuisines: </strong>
          {{ recipesStore.recipe.cuisines && recipesStore.recipe.cuisines.length > 0 ?
        recipesStore.recipe.cuisines.join(", ") : "Unknown" }}
          <br>
          <strong>Dietary Preferences : </strong>
          <span v-if="recipesStore.recipe.vegetarian">Vegetarian</span>
          <span v-else-if="recipesStore.recipe.vegan">Vegan</span>
          <span v-else>Not specified</span>
          <br>
          <strong>Dish Types: </strong>
          {{ recipesStore.recipe.dishTypes && Array.isArray(recipesStore.recipe.dishTypes) &&
        recipesStore.recipe.dishTypes.length > 0 ?
        recipesStore.recipe.dishTypes.join(", ") : "Unknown" }}
          <br>
        </v-list>
        <h2 class="my-5">Ingredients :</h2>
        <v-list v-for="(ingredient, index) in recipesStore.recipe.extendedIngredients" :key="index">
          <v-icon>mdi-arrow-right-thin</v-icon> {{ ingredient.original }} <br>
          <span>- {{ ingredient.aisle }}</span>
        </v-list>
        <h2 class="my-5">Taste Profile:</h2>
        <p class="mb-2 mx-2 d-inline-block" v-for="(value, key) in recipesStore.recipe.taste" :key="key">
          <v-chip><strong>{{ key }}:</strong> {{ value }}%</v-chip>
        </p>
        <v-list>
          <h2 class="my-5" v-if="recipesStore.recipe.similarRecipes && recipesStore.recipe.similarRecipes.length > 0">
            Similar recipes :</h2>
          <ul v-if="recipesStore.recipe.similarRecipes && recipesStore.recipe.similarRecipes.length > 0">
            <li v-for="similarRecipe in recipesStore.recipe.similarRecipes" :key="similarRecipe.id">
              <a :href="similarRecipe.sourceUrl">{{ similarRecipe.title }}</a>
            </li>
          </ul>

        </v-list>
      </v-card-text>
    </v-card>
  </div>

</template>

<script>
import { useRecipesStore } from "@/store/recipesStore";
import { useRoute } from "vue-router";
import { ref } from 'vue';
import AppNavigationBar from "./AppNavigationBar.vue";
export default {
  components: {
    AppNavigationBar,
  },
  setup() {
    const route = useRoute();
    const recipesStore = useRecipesStore();
    const recipeId = route.params.id;
    const inputVisible = ref(false);
    const url = ref(window.location.href);

    const showInput = () => {
      inputVisible.value = true;
    };

    const copyUrl = async () => {
      try {
        await navigator.clipboard.writeText(url.value);
        inputVisible.value = false; // Hide the dialog after copying
        console.log('URL copied to clipboard');
      } catch (err) {
        console.error('Failed to copy URL:', err);
      }
    };

    recipesStore.getRecipeById(recipeId);
    return {
      recipesStore,
      inputVisible,
      url,
      showInput,
      copyUrl
    }
  },
  methods: {
    truncateDigits(value) {
      return parseInt(value).toFixed(2);
    }
  }
}
</script>

<style scoped>
.input-container {
  display: flex;
  align-items: center;
}

.input-container input {
  flex: 1;
  margin-right: 8px;
}
</style>
