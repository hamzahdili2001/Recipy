<template>
  <v-card class="w-100 d-flex justify-center align-center bg-grey-lighten-5
 flex-column pa-10" rounded="0" flat>
    <v-avatar color="grey" class="" rounded="50" size="150">
      <v-img
        src="https://media.istockphoto.com/id/1223671392/vector/default-profile-picture-avatar-photo-placeholder-vector-illustration.jpg?s=612x612&w=0&k=20&c=s0aTdmT5aU6b8ot7VKm11DeID6NctRCpB755rA1BIP0="
        cover></v-img>
    </v-avatar>
    <v-list-item class=" text-black text-center">
      <v-list-item-title>{{ userStore.user.first_name }} {{ userStore.user.last_name }}</v-list-item-title>
      <v-list-item-subtitle>{{ userStore.user.username }}</v-list-item-subtitle>
    </v-list-item>

    <div class="mt-4 d-flex justify-center align-center ga-4">
      <v-btn flat elevation="1" min-width="100px" to="/profile/bookmarks">Bookmarks</v-btn>
      <v-btn flat elevation="1" min-width="100px" to="/profile/posts">Your Posts</v-btn>
      <v-btn flat elevation="1" min-width="100px" to="/profile/edit">Edit Profile</v-btn>
      <v-btn class="bg-red-accent-2" flat elevation="1" min-width="100px">Delete Profile</v-btn>
    </div>
  </v-card>

  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import { useUserStore } from '@/store/userstore';

export default {
  setup() {
    const userStore = useUserStore()
    return {
      userStore,
    }
  }
}
</script>