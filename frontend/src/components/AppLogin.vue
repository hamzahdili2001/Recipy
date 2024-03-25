<template>
  <div class="text-center">
    <v-overlay v-model="appStore.overlay" class="d-flex justify-center align-center">
      <v-btn @click="appStore.overlay = false" icon="mdi-close" variant="plain" text
        class="app-login-close-icon text-white"></v-btn>
      <div style="width: 450px; max-width: 500px; min-width: 320px;" v-show="appStore.LoginRegister">
        <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
          <h3 class="mx-auto mb-8 font-weight-medium text-center" max-width="100%"
            style="font-family: 'Smooch', cursive; font-size: 50px; color: #000000;">Recipy
          </h3>

          <div class="text-subtitle-1 text-medium-emphasis">Account</div>

          <v-text-field density="compact" placeholder="Email address" prepend-inner-icon="mdi-email-outline"
            variant="outlined"></v-text-field>

          <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
            Password

            <a class="text-caption text-decoration-none text-blue" href="#" rel="noopener noreferrer" target="_blank">
              Forgot login password?</a>
          </div>

          <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
            density="compact" placeholder="Enter your password" prepend-inner-icon="mdi-lock-outline" variant="outlined"
            @click:append-inner="visible = !visible"></v-text-field>

          <!-- <v-card class="mb-12" color="surface-variant" variant="tonal">
                        <v-card-text class="text-medium-emphasis text-caption">
                            Warning: After 3 consecutive failed login attempts, you account will be temporarily
                            locked for three hours. If you must login now, you can also click "Forgot login
                            password?" below to reset the login password.
                        </v-card-text>
                    </v-card> -->

          <v-btn class="mb-8" color="blue" size="large" variant="tonal" block>
            Log In
          </v-btn>

          <v-card-text class="text-center">
            <a class="text-blue text-decoration-none cursor-pointer" @click="appStore.LoginRegister = false"
              rel="noopener noreferrer">
              Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
            </a>
          </v-card-text>
        </v-card>
      </div>

      <div style="width: 450px; max-width: 500px; min-width: 320px;" v-show="!appStore.LoginRegister">
        <form @submit.prevent="register">
          <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">

            <div class="text-subtitle-1 text-medium-emphasis">First Name</div>
            <v-text-field density="compact" v-model="registerFormData.first_name" placeholder="First Name"
              prepend-inner-icon="mdi-account-outline" variant="outlined"></v-text-field>
            <div class="text-subtitle-1 text-medium-emphasis">Last Name</div>
            <v-text-field density="compact" v-model="registerFormData.last_name" placeholder="User Name"
              prepend-inner-icon="mdi-account-outline" variant="outlined"></v-text-field>
            <div class="text-subtitle-1 text-medium-emphasis">User Name</div>
            <v-text-field density="compact" v-model="registerFormData.username" placeholder="User Name"
              prepend-inner-icon="mdi-account-outline" variant="outlined"></v-text-field>

            <div class="text-subtitle-1 text-medium-emphasis">Email</div>

            <v-text-field density="compact" v-model="registerFormData.email" placeholder="Email address"
              prepend-inner-icon="mdi-email-outline" variant="outlined"></v-text-field>

            <div class="text-subtitle-1  text-medium-emphasis d-flex align-center justify-space-between">
              Password
            </div>

            <v-text-field v-model="registerFormData.password1" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
              :type="visible ? 'text' : 'password'" density="compact" placeholder="Enter your password"
              prepend-inner-icon="mdi-lock-outline" variant="outlined"
              @click:append-inner="visible = !visible"></v-text-field>

            <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
              Confirm Password
            </div>

            <v-text-field v-model="registerFormData.password2" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
              :type="visible ? 'text' : 'passwod'" density="compact" placeholder="Enter your password"
              prepend-inner-icon="mdi-lock-outline" variant="outlined"
              @click:append-inner="visible = !visible"></v-text-field>

            <v-btn type="submit" class="mb-8" color="blue" size="large" variant="tonal" block
              append-icon="mdi-arrow-right">
              Next
            </v-btn>
            <v-card-text class="text-center">
              <a class="text-blue text-decoration-none cursor-pointer" @click="appStore.LoginRegister = true"
                rel="noopener noreferrer">
                <v-icon icon="mdi-chevron-left"></v-icon> Login
              </a>
            </v-card-text>


          </v-card>
        </form>
      </div>
    </v-overlay>
  </div>
</template>
<script>
import { useAppLoginStore } from '@/store/home';
import axios from "axios";
export default {
  setup() {
    const appStore = useAppLoginStore();
    return {
      appStore,
    }
  },
  data: () => ({
    visible: false,
    registerFormData: {
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      password1: "",
      password2: ""
    },
    cleanRegistrationData: {
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      password: ""
    },
    errors: []
  }),
  methods: {
    async register() {
      this.errors = [];
      for (const field in this.registerFormData) {
        if (this.registerFormData[ field ] === "") {
          this.errors.push(`${field.replace('_', ' ')} is missing`);
        } else {
          if (field === 'password1') {
            this.cleanRegistrationData.password = this.registerFormData.password1.trim();
          } else {
            this.cleanRegistrationData[ field ] = this.registerFormData[ field ].trim();
          }
        }
      }

      if (this.registerFormData.password1 !== this.registerFormData.password2) {
        this.errors.push("Passwords do not match");
      }

      if (this.errors.length === 0) {
        axios.post('http://127.0.0.1:8000/api/user/register', this.cleanRegistrationData)
          .then(response => {
            console.log(response.data); // Handle successful response
            // Redirect or show a success message
          }).catch(error => {
            console.error(error.response.data); // Handle error response
            // Display error messages to the user
          });
      }
    }
  }
}
</script>

<style>
.app-login-close-icon {
  position: absolute;
  top: -51px;
  right: -43px;
}
</style>
