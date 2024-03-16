<template>
  <v-card rounded="0" flat>
    <v-toolbar density="compact" color="white" class="pa-4 nav-container" height="0px">
      <v-app-bar-nav-icon class="d-none d-block-md" @click.stop="drawer = true"></v-app-bar-nav-icon>
      <v-toolbar-title class="fw-400 fs-30 d-none-md"
        style="font-family: 'Smooch', cursive; font-size: 30px; color: #000000;">Recipy</v-toolbar-title>
      <v-nav-list class="d-none-md">
        <v-btn class='h-100'>Home</v-btn>
        <v-btn>Recipes</v-btn>
        <v-btn>Categories</v-btn>
        <v-btn>About</v-btn>
      </v-nav-list>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-menu v-model="menu" :close-on-content-click="false" location="bottom">
        <template v-slot:activator="{ props }">
          <v-avatar class="ml-3 cursor-pointer" v-bind="props">
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
  <v-navigation-drawer class="px-4 d-none d-block-md" :width="300" v-model="drawer">
    <div class="title">
      <v-toolbar-title class="fw-400 fs-30"
        style="font-family: 'Smooch', cursive; font-size: 30px; color: #000000;">Recipy</v-toolbar-title>
      <v-btn icon flat @click.stop="drawer = false">
        <v-icon>mdi-window-close</v-icon>
      </v-btn>
    </div>
    <v-divider class="mb-4"></v-divider>
    <v-list-item class="pa-4" link title="Home"></v-list-item>
    <v-list-item class="pa-4" link title="Recipes"></v-list-item>
    <v-list-item class="pa-4" link title="Categories"></v-list-item>
    <v-list-item class="pa-4" link title="About"></v-list-item>
  </v-navigation-drawer>
</template>

<style>
.title {
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-drawer {
  left: 0;
}

@media (max-width: 760px) {
  .nav-container>div {
    position: static;
    z-index: 1;
  }

  .d-none-md {
    display: none;
  }

  .d-block-md {
    display: block !important;
  }
}
</style>

<script>
export default {
  data: () => ({
    drawer: false,
    fav: true,
    menu: false,
    message: false,
    hints: true,
  }),
  watch: {
    group() {
      this.drawer = false
    },
  },
}
</script>
