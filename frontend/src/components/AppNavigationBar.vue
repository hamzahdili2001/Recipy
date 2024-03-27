<template>
  <v-card rounded="0" flat>
    <v-toolbar density="compact" color="white" class="py-4 px-15 nav-container" style="min-height: fit-content;">
      <v-app-bar-nav-icon class="d-none d-block-md" @click.stop="drawer = true"></v-app-bar-nav-icon>
      <h3 class=" fs-30 d-none-md font-weight-medium"
        style="font-family: 'Smooch', cursive; font-size: 30px; color: #000000;">Recipy
      </h3>
      <v-list class="d-none-md">
        <v-btn to="/" link>Home</v-btn>
        <v-btn to="/recipes">Recipes</v-btn>
        <v-btn to="/category">Categories</v-btn>
        <v-btn to="about">About</v-btn>
      </v-list>
      <div>
        <v-btn icon to="/recipes-filter">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-menu v-model="menu" :close-on-content-click="false" location="bottom" v-if="userStore.user.isAuthenticated">
          <template v-slot:activator="{ props }">
            <v-avatar class="ml-3 cursor-pointer" v-bind="props">
              <v-img v-if="userStore.user.profil" :width="100"
                :src="'http://127.0.0.1:8000/' + userStore.user.profil"></v-img>
              <v-img v-else :width="100"
                src="https://media.istockphoto.com/id/1214428300/vector/default-profile-picture-avatar-photo-placeholder-vector-illustration.jpg?s=612x612&w=0&k=20&c=vftMdLhldDx9houN4V-g3C9k0xl6YeBcoB_Rk6Trce0="></v-img>
            </v-avatar>
          </template>
          <v-card min-width="300" class="mt-2 mr-4 bg-white">
            <v-list>
              <v-list-item
                :prepend-avatar="userStore.user.profil ? 'http://127.0.0.1:8000/' + userStore.user.profil : 'https://media.istockphoto.com/id/1214428300/vector/default-profile-picture-avatar-photo-placeholder-vector-illustration.jpg?s=612x612&w=0&k=20&c=vftMdLhldDx9houN4V-g3C9k0xl6YeBcoB_Rk6Trce0='">

                <v-list-item-content>
                  <v-list-item-title>
                    {{ userStore.user.first_name }} {{ userStore.user.last_name }}
                  </v-list-item-title>
                  <v-list-item-subtitle>{{ userStore.user.username }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>

            <v-divider></v-divider>

            <v-list>
              <v-list-item>
                <v-btn class="w-100" variant="text" to="/profile/">Profile</v-btn>
              </v-list-item>
              <v-list-item>
                <v-btn class="w-100" to="/profile/bookmarks">Bookmarks</v-btn>
              </v-list-item>
            </v-list>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn width='100%' color="red" variant="text" @click="userStore.removeToken">
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
    <v-list-item class="pa-4" link to="/" title="Home"></v-list-item>
    <v-list-item class="pa-4" link to="/recipes" title="Recipes"></v-list-item>
    <v-list-item class="pa-4" link to="/categories" title="Categories"></v-list-item>
    <v-list-item class="pa-4" link to="/about" title="About"></v-list-item>
  </v-navigation-drawer>
</template>
<script>
import { useAppLoginStore } from '@/store/home';
import { useUserStore } from '@/store/userstore';
export default {
  setup() {
    const appStore = useAppLoginStore();
    const userStore = useUserStore();
    return {
      appStore,
      userStore,
    }
  },
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
