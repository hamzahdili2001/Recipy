<template>
  <div class="mx-15 my-15">
    <v-form @submit.prevent="searchRecipes">
      <v-row>
        <v-col cols="12" md="12">
          <v-text-field v-model="query" label="Search Query" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-select v-model="cuisine" :items="cuisines" label="Cuisine" variant="outlined" multiple></v-select>
        </v-col>
        <v-col cols="12" md="4">
          <v-select v-model="diet" :items="diets" label="Diet" variant="outlined" multiple></v-select>
        </v-col>
        <v-col cols="12" md="4">
          <v-select v-model="intolerances" :items="intolerancesList" variant="outlined" label="Intolerances"
            multiple></v-select>
        </v-col>
        <v-col cols="12">
          <v-btn type="submit" size="x-large" block variant="flat" color="primary" class="text-white">Search</v-btn>
        </v-col>
      </v-row>
      <v-divider :thickness="2" class="my-8"></v-divider>
    </v-form>
    <v-list-item v-for="item in items" :key="item" link to="/">
      <v-list-item-title class="my-2 p-3 text-primary" rounded="5">{{ item }}</v-list-item-title>
    </v-list-item>
  </div>
</template>

<script>
import AppFiltersList from "@/components/AppFiltersList.vue"
export default {
  components: {
    AppFiltersList
  },
  data() {
    return {
      cuisines: [ 'African', 'American', 'British', 'Cajun', 'Caribbean', 'Chinese', 'Eastern European', 'European', 'French', 'German', 'Greek', 'Indian', 'Irish', 'Italian', 'Japanese', 'Jewish', 'Korean', 'Latin American', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic', 'Southern', 'Spanish', 'Thai', 'Vietnamese' ],
      diets: [ 'Gluten Free', 'Ketogenic', 'Vegetarian', 'Lacto-Vegetarian', 'Ovo-Vegetarian', 'Vegan', 'Pescetarian', 'Paleo', 'Primal', 'Whole30' ],
      intolerancesList: [ 'Dairy', 'Egg', 'Gluten', 'Grain', 'Peanut', 'Seafood', 'Sesame', 'Shellfish', 'Soy', 'Sulfite', 'Tree Nut', 'Wheat' ]
    };
  },
  methods: {
    searchRecipes() {
      console.log('Search Query:', this.query);
      console.log('Cuisine:', this.cuisine);
      console.log('Diet:', this.diet);
      console.log('Intolerances:', this.intolerances);
      console.log('Minimum Calories:', this.minCalories);
      console.log('Maximum Calories:', this.maxCalories);
      console.log('Minimum Cooking Time:', this.minCookTime);
      console.log('Maximum Cooking Time:', this.maxCookTime);
    }
  }
};
</script>

<style scoped></style>
