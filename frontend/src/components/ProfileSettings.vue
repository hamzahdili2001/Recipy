<template>
  <v-card class="w-100 d-flex justify-center align-center bg-grey-lighten-5 flex-column pa-10" rounded="0" flat>
    <v-avatar color="grey" class="" rounded="50" size="150">
      <v-img v-if="profileImageUrl" :src="profileImageUrl" cover></v-img>
      <v-img v-else
        src="https://media.istockphoto.com/id/1214428300/vector/default-profile-picture-avatar-photo-placeholder-vector-illustration.jpg?s=612x612&w=0&k=20&c=vftMdLhldDx9houN4V-g3C9k0xl6YeBcoB_Rk6Trce0="
        cover></v-img>
    </v-avatar>
    <v-list-item class=" text-black text-center">
      <v-list-item-title>{{ userStore.user.first_name }} {{ userStore.user.last_name }}</v-list-item-title>
      <v-list-item-subtitle>{{ userStore.user.username }}</v-list-item-subtitle>
    </v-list-item>

    <div class="mt-4 d-flex justify-center align-center ga-4">
      <v-btn flat elevation="1" min-width="100px" to="/profile/bookmarks">Bookmarks</v-btn>
      <v-btn flat elevation="1" min-width="100px" to="/profile/posts">Your Posts</v-btn>
      <input type="file" @change="handleFileUpload" accept="image/*" /> <!-- File input for uploading picture -->
      <v-btn class="bg-red-accent-2" flat elevation="1" min-width="100px">Delete Profile</v-btn>
    </div>
  </v-card>

  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import { useUserStore } from '@/store/userstore';
import axios from 'axios';

export default {
  setup() {
    const userStore = useUserStore()

    // Function to handle file upload
    const handleFileUpload = async (event) => {
      const file = event.target.files[ 0 ];
      const formData = new FormData();
      formData.append('picture', file);

      try {
        const response = await axios.put('http://127.0.0.1:8000/api/user/update_picture', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: 'Bearer ' + userStore.user.access // Assuming you're using JWT token
          },
        });
        console.log(response.data); // Log response from the server
        // Optionally, you can update the user profile picture in the store or trigger a reload of user data
      } catch (error) {
        console.error(error); // Log error if any
        // Handle error
      }
    };

    // Computed property to generate the profile picture URL
    const fetchProfilePicture = async () => {
      await userStore.fetchUserProfilePicture();
    };
    fetchProfilePicture();
    const profileImageUrl = userStore.userProfileImageUrl;
    return {
      userStore,
      handleFileUpload,
      profileImageUrl
    }
  }
}
</script>
