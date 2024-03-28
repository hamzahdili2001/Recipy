<template>
  <v-card class="w-100 d-flex justify-center align-center bg-grey-lighten-5 flex-column pa-10" rounded="0" flat>
    <v-avatar color="grey" class="" rounded="50" size="150">
      <v-img v-if="imageURL" :src="imageURL" cover></v-img>
      <v-img v-else
        src="https://media.istockphoto.com/id/1214428300/vector/default-profile-picture-avatar-photo-placeholder-vector-illustration.jpg?s=612x612&w=0&k=20&c=vftMdLhldDx9houN4V-g3C9k0xl6YeBcoB_Rk6Trce0="
        cover></v-img>
      <v-file-input class="file-input" @change="handleFileUpload" accept="image/png, image/jpeg, image/bmp"
        label="Avatar" placeholder="Pick an avatar" prepend-icon="mdi-camera"></v-file-input>

    </v-avatar>
    <v-list-item class="text-black text-center">
      <v-list-item-title>{{ userStore.user.first_name }}
        {{ userStore.user.last_name }}</v-list-item-title>
      <v-list-item-subtitle>{{ userStore.user.username }}</v-list-item-subtitle>
    </v-list-item>

    <div class="mt-4 d-flex justify-center align-center ga-4">
      <v-btn flat elevation="1" min-width="100px" to="/profile/bookmarks">Bookmarks</v-btn>
      <v-btn flat elevation="1" min-width="100px" to="/profile/posts">Edit Profile</v-btn>


      <v-btn class="bg-red-accent-2" flat elevation="1" min-width="100px">Delete Profile</v-btn>
    </div>
  </v-card>

  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import { useUserStore } from "@/store/userstore";
import axios from "axios";

export default {
  props: [ "imageURL" ],
  setup() {
    const userStore = useUserStore();

    // Function to handle file upload
    const handleFileUpload = async (event) => {
      const file = event.target.files[ 0 ];
      const formData = new FormData();
      formData.append("picture", file);

      try {
        const response = await axios.put(
          "http://127.0.0.1:8000/api/user/update_picture",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: "Bearer " + userStore.user.access, // Assuming you're using JWT token
            },
          }
        );
        location.reload();
      } catch (error) {
        console.error(error); // Log error if any
      }
    };

    return {
      userStore,
      handleFileUpload,
    };
  },
};
</script>


<style scoped>
.v-field__input,
input[type="file"],
.v-field {
  display: none;
}


/* Style the icon */
.v-input {
  color: #ffffff;
  /* Change color as needed */
  font-size: 24px;
  /* Change size as needed */
  cursor: pointer;
  position: absolute;
  top: 56%;
  left: 58%;
  transform: translate(-50%, -50%);

}
</style>
