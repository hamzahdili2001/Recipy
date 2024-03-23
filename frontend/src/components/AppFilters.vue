<template>
  <div class="mx-15 my-15">
    <v-form @submit.prevent="searchRecipes">
      <v-row>
        <v-col cols="12" md="12">
          <v-text-field v-model="query" label="Search Query" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12" md="3">
          <v-select v-model="cuisine" :items="cuisines" label="Cuisine" variant="outlined" multiple></v-select>
        </v-col>
        <v-col cols="12" md="3">
          <v-select v-model="diet" :items="diets" label="Diet" variant="outlined" multiple></v-select>
        </v-col>
        <v-col cols="12" md="3">
          <v-select v-model="intolerances" :items="intolerancesList" variant="outlined" label="Intolerances"
            multiple></v-select>
        </v-col>
        <v-col cols="12" md="3">
          <v-text-field v-model="minCalories" label="Minimum Calories" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field v-model="maxCalories" label="Maximum Calories" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field v-model="minCookTime" label="Minimum Cooking Time (minutes)" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12" md="4">
          <v-text-field v-model="maxCookTime" label="Maximum Cooking Time (minutes)" variant="outlined"></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-btn type="submit" size="x-large" block variant="flat" color="primary" class="text-white">Search</v-btn>
        </v-col>
      </v-row>
      <v-divider :thickness="2" class="my-13"></v-divider>
    </v-form>
  </div>

</template>

<script>
export default {
  data() {
    return {
      query: '',
      cuisine: [],
      diet: [],
      intolerances: [],
      minCalories: null,
      maxCalories: null,
      minCookTime: null,
      maxCookTime: null,
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
