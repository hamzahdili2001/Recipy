<template>
  <div>
    <h3 class="px-15 pa-10">Bookmarks</h3>
    <v-row align="center" justify="center" wrap class="w-100 px-15">
      <v-col cols="12" sm="6" md="4" lg="4" v-for="bookmark of userStore.user.bookmarkedRecipes" :key="bookmark.id">
        <v-card class="elevation-2">
          <v-card-title>{{ bookmark.title }}</v-card-title>
          <v-card-actions>
            <v-btn :to="'/details/' + bookmark.recipe_id">Open</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { useUserStore } from '@/store/userstore';

export default {
  setup() {

    const userStore = useUserStore();
    userStore.fetchBookmarkedRecipes();

    return {
      userStore
    };
  }
}
</script>
