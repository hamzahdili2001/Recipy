<template>
  <div class="px-15 pa-6">
    <v-carousel class="app-carousel" :show-arrows="showArrows" cycle interval="6000">
      <v-carousel-item v-for="recipe in  recipes " :key="recipe.id" :src="recipe.image" cover>
        <div class="w-100 h-100 d-flex flex-column justify-center align-start pt-15 text-white con-container"
          style="background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8)); padding-left: 112px;">
          <v-rating :model-value="recipeStore.convertToRating(recipe.spoonacularScore)" color="amber" density="compact"
            size="small" half-increments readonly></v-rating>
          <h2>{{ recipe.title }}</h2>
          <p class="car-para">{{ recipeStore.truncateSummary(recipe.summary, 100) }}</p>
          <v-btn class="mt-4" :to="'details/' + recipe.id">Show More</v-btn>
        </div>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>
<script>
import { useRecipesStore } from '@/store/recipesStore';
import { computed } from 'vue';
export default {
  data() {
    return {
      showArrows: true
    }
  },
  setup() {
    const recipeStore = useRecipesStore();
    recipeStore.getRecipes();
    // Filter recipes with the maximum spoonacularScore
    const maxScoreRecipes = computed(() => {
      return recipeStore.recipes.filter(recipe => recipe.spoonacularScore >= 95);
    });

    // Shuffle the maxScoreRecipes array
    const shuffledRecipes = computed(() => {
      return maxScoreRecipes.value.sort(() => Math.random() - 0.5);
    });

    const recipes = computed(() => shuffledRecipes.value.slice(0, 5));

    return {
      recipeStore,
      recipes,
    };
  },
  mounted() {
    window.addEventListener('resize', this.handleViewportChange);
    this.handleViewportChange();
  },

  methods: {
    handleViewportChange() {
      if (window.innerWidth <= 950) {
        this.showArrows = false;
      }
      else {
        this.showArrows = true;
      }
    }
  }
}
</script>
<style scoped>
.app-carousel {
  height: 650px !important;
}

.car-para {
  width: 50%;
}

@media (max-width: 950px) {
  .app-carousel {
    height: 580px !important;
  }

  .app-carousel .con-container {
    padding-top: 10px !important;
    padding-left: 20px !important;
  }

  .car-para {
    width: 80%;
  }
}


@media (max-width: 730px) {
  .app-carousel {
    height: 400px !important;
  }

  .car-para {
    width: 90%;
  }

  .px-15 {
    padding-left: 30px !important;
    padding-right: 30px !important;
  }

  .mx-15 {
    margin-left: 30px !important;
    margin-right: 30px !important;
  }
}
</style>
