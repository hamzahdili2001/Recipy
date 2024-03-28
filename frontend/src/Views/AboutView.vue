<template>
  <v-container>
    <h1 class="display-1 text-center mb-5">About Our Recipe Project</h1>

    <v-row justify="center">
      <v-col cols="12" md="8">
        <p class="text-center">
          Welcome to our recipe project! Our mission is to provide a platform where users can discover, share, and enjoy
          delicious recipes from around the world.
        </p>
        <p class="text-center">
          Whether you're a seasoned chef or just starting out in the kitchen, our website is designed to inspire and
          empower you to explore new flavors and culinary experiences.
        </p>
      </v-col>
    </v-row>

    <h2 class="headline text-center ma-8">Key Features</h2>

    <v-row>
      <v-col cols="12" md="4">
        <v-card class="pa-5">
          <v-icon size="64" class="mx-auto">mdi-food-apple</v-icon>
          <h3 class="text-center">Wide Range of Recipes</h3>
          <p>
            Explore a diverse collection of recipes ranging from appetizers to desserts, including vegetarian, vegan,
            gluten-free, and more.
          </p>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="pa-5">
          <v-icon size="64" class="mx-auto">mdi-heart-outline</v-icon>
          <h3 class="text-center">Favorite and Bookmark</h3>
          <p>
            Save your favorite recipes and create personalized collections for quick access whenever you're ready to
            cook.
          </p>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card class="pa-5">
          <v-icon size="64" class="mx-auto">mdi-comment-text-outline</v-icon>
          <h3 class="text-center">Community Interaction</h3>
          <p>
            Engage with other users by leaving comments, ratings, and sharing your cooking experiences and tips.
          </p>
        </v-card>
      </v-col>
    </v-row>

    <h2 class="headline text-center ma-8">Our Team</h2>

    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="pa-5">
          <v-avatar size="100" class="mx-auto">
            <v-img src="https://pbs.twimg.com/profile_images/1770192320329142272/z_1EuoME_400x400.jpg"
              alt="Team Member"></v-img>

          </v-avatar>
          <h3 class="text-center">Hamza Hdili</h3>
          <p class="text-center">Software Engineer</p>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card class="pa-5">
          <v-avatar size="100" class="mx-auto">
            <v-img src="https://avatars.githubusercontent.com/u/115190839?v=4" alt="Team Member"></v-img>
          </v-avatar>
          <h3 class="text-center">Jane Smith</h3>
          <p class="text-center">He will write his name when he wakes up</p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  // Add any necessary script logic here
}
</script>

<style scoped>
/* Add custom styles here */
</style>
