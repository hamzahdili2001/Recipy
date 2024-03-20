<template>
  <v-card rounded="0" flat>
    <v-toolbar density="compact" color="white" class="py-4 px-15 nav-container" height="0px">
      <v-app-bar-nav-icon class="d-none d-block-md" @click.stop="drawer = true"></v-app-bar-nav-icon>
      <h3 class=" fs-30 d-none-md font-weight-medium"
        style="font-family: 'Smooch', cursive; font-size: 30px; color: #000000;">Recipy
      </h3>
      <v-nav-list class="d-none-md">
        <v-btn>Home</v-btn>
        <v-btn>Recipes</v-btn>
        <v-btn>Categories</v-btn>
        <v-btn>About</v-btn>
      </v-nav-list>
      <div>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-menu v-model="menu" :close-on-content-click="false" location="bottom" v-if="loggedIn">
          <template v-slot:activator="{ props }">
            <v-avatar class="ml-3 cursor-pointer" v-bind="props">
              <v-img :width="100"
                src="https://media.licdn.com/dms/image/C4D03AQHi1VAvIqvgag/profile-displayphoto-shrink_800_800/0/1622817007783?e=1716422400&v=beta&t=SaXMCLfmC0aM5L6re85uvHgyNHmr_LrPR6WZ7SKp7vw"></v-img>
            </v-avatar>
          </template>
          <v-card min-width="300" class="mt-2 mr-4 bg-white">
            <v-list>
              <v-list-item
                prepend-avatar="https://media.licdn.com/dms/image/C4D03AQHi1VAvIqvgag/profile-displayphoto-shrink_800_800/0/1622817007783?e=1716422400&v=beta&t=SaXMCLfmC0aM5L6re85uvHgyNHmr_LrPR6WZ7SKp7vw"
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
        <v-btn icon="mdi-login-variant" v-else @click.stop="appStore.overlay = true"></v-btn>
      </div>
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
<script>
import { useAppLoginStore } from '@/store/home';
export default {
  setup() {
    const appStore = useAppLoginStore();
    return {
      appStore,
    }
  },
  data: () => ({
    drawer: false,
    fav: true,
    menu: false,
    message: false,
    hints: true,
    loggedIn: false,
  }),
  watch: {
    group() {
      this.drawer = false
    },
  },
}
</script>
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

.nav-container>div {
  display: flex;
  justify-content: space-between;
  align-items: center;
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
