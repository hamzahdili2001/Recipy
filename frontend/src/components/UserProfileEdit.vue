<template>
  <h3 class="px-15 pa-10">Your Posts</h3>
  <div class="px-15 mb-15">
    <v-card class="mx-auto pa-8 pb-8" max-width="100%" rounded="0">
      <v-text-field label="Username" prepend-inner-icon="mdi-account-outline" variant="outlined"
        v-model="userStore.user.username"></v-text-field>
      <div class="d-flex justify-center align-center flex-wrap ga-10">
        <v-text-field label="First Name" prepend-inner-icon="mdi-text-short" variant="outlined"
          v-model="userStore.user.first_name"></v-text-field>
        <v-text-field label="Last Name" prepend-inner-icon="mdi-text-short" variant="outlined"
          v-model="userStore.user.last_name"></v-text-field>
      </div>
      <v-btn @click="updateUser" size="x-large" block variant="flat" color="primary" class="text-white">Submit</v-btn>
      <!-- <v-text-field label="Email" prepend-inner-icon="mdi-email-outline" variant="outlined"
        v-model="userStore.user.email"></v-text-field>
      <div class="d-flex justify-center align-center flex-wrap ga-10">
        <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
          label="Password" prepend-inner-icon="mdi-lock-outline" variant="outlined"
          @click:append-inner="visible = !visible"></v-text-field>
        <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
          label="Confirm Password" prepend-inner-icon="mdi-lock-outline" variant="outlined"
          @click:append-inner="visible = !visible"></v-text-field>
      </div> -->

    </v-card>

  </div>
</template>

<script>
import { useUserStore } from '@/store/userstore';
import axios from 'axios';
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
export default {
  setup() {
    const userStore = useUserStore()
    return {
      userStore
    }
  },
  data: () => ({
    visible: false,

  }),
  methods: {
    updateUser() {
      const userData = {
        first_name: this.userStore.user.first_name,
        last_name: this.userStore.user.last_name,
        username: this.userStore.user.username
      };

      axios.put(`${this.userStore.BackendBaseUrl}/api/user/update_data`, userData)
        .then(response => {
          console.log(response.data.message); // Output: "ok"
          if (response.data.message == 'ok') {
            toast("Your data was updated successfully!", {
              "theme": "colored",
              "type": "success",
              "dangerouslyHTMLString": true
            })
            localStorage.setItem("user.username", userData.username);
            localStorage.setItem("user.first_name", userData.first_name);
            localStorage.setItem("user.last_name", userData.last_name);

          }
        })
        .catch(error => {
          toast("Something went wrong! Try again or change to another username", {
            "theme": "colored",
            "type": "error",
            "dangerouslyHTMLString": true
          })
        });
    },
  }
}
</script>
