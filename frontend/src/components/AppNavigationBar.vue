<template>
  <v-card rounded="0" flat>
    <v-toolbar density="compact" color="white" class="pa-4" height="0px">
      <v-toolbar-title
        style="font-family: 'Smooch', cursive; font-size: 30px;font-weight: 400; color: #000000;">Recipy</v-toolbar-title>
      <v-btn>Home</v-btn>
      <v-btn>Recipes</v-btn>
      <v-btn>Categories</v-btn>
      <v-btn>About</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-menu v-model="menu" :close-on-content-click="false" location="bottom">
        <template v-slot:activator="{ props }">
          <v-avatar class="ml-3" v-bind="props">
            <v-img :width="100"
              src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?q=80&w=1780&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"></v-img>
          </v-avatar>
        </template>
        <v-card min-width="300" class="mt-2 mr-4 bg-white">
          <v-list>
            <v-list-item
              prepend-avatar="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?q=80&w=1780&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              subtitle="software engineer" title="Hamza Hdili">
            </v-list-item>
          </v-list>

          <v-divider></v-divider>

          <v-list>
            <v-list-item>
              <v-btn class="w-100" variant="text">Profile</v-btn>
            </v-list-item>
            <v-list-item>
              <v-btn class="w-100">Bookmarks</v-btn>
            </v-list-item>
          </v-list>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn width='100%' color="red" variant="text">
              Logout
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-menu>
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    fav: true,
    menu: false,
    message: false,
    hints: true,
  }),
}
</script>
