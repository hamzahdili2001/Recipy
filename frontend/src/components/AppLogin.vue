<template>
  <div class="text-center" style="overflow-y: auto;">
    <v-overlay v-model="appStore.overlay" class="d-flex justify-center align-center app-overlay">
      <v-btn @click="appStore.overlay = false" icon="mdi-close" variant="plain" text
        class="app-login-close-icon text-white"></v-btn>
      <div id='login' style="width: 650px; max-width: 500px; min-width: 320px;" v-show="appStore.LoginRegister">
        <v-card class="mx-auto pa-12 pb-8 login-card" elevation="8" max-width="648" rounded="lg">
          <h3 class="mx-auto mb-8 font-weight-medium text-center" max-width="100%"
            style="font-family: 'Smooch', cursive; font-size: 50px; color: #000000;">Recipy
          </h3>

          <div class="text-subtitle-1 text-medium-emphasis">Account</div>

          <v-text-field density="compact" v-model="cleanLoginData.username" placeholder="Email address or username"
            prepend-inner-icon="mdi-email-outline" variant="outlined"></v-text-field>

          <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
            Password

            <a class="text-caption text-decoration-none text-blue" href="#" rel="noopener noreferrer" target="_blank">
              Forgot login password?</a>
          </div>

          <v-text-field v-model="cleanLoginData.password" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
            :type="visible ? 'text' : 'password'" density="compact" placeholder="Enter your password"
            prepend-inner-icon="mdi-lock-outline" variant="outlined"
            @click:append-inner="visible = !visible"></v-text-field>

          <v-btn @click="login" class="mb-8" color="blue" size="large" variant="tonal" block>
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

      <div id="register" style="height: 100%; width: 750px; max-width: 700px; min-width: 320px; overflow-y: auto;"
        v-show="!appStore.LoginRegister">
        <form @submit.prevent="register">
          <v-card class="mx-auto h-100 pa-12 pb-8 register-card" style="overflow-y:auto;" elevation="8" max-width="748"
            rounded="lg">
            <v-row>
              <v-col cols="12" sm="6">
                <div class="text-subtitle-1 text-medium-emphasis">First Name</div>
                <v-text-field density="compact" v-model="registerFormData.first_name" placeholder="First Name"
                  prepend-inner-icon="mdi-account-outline" variant="outlined"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <div class="text-subtitle-1 text-medium-emphasis">Last Name</div>
                <v-text-field density="compact" v-model="registerFormData.last_name" placeholder="Last Name"
                  prepend-inner-icon="mdi-account-outline" variant="outlined"></v-text-field>
              </v-col>
            </v-row>
            <div class="text-subtitle-1 text-medium-emphasis">User Name</div>
            <v-text-field density="compact" v-model="registerFormData.username" placeholder="User Name"
              prepend-inner-icon="mdi-account-outline" variant="outlined"></v-text-field>

            <div class="text-subtitle-1 text-medium-emphasis">Email</div>

            <v-text-field type="email" density="compact" v-model="registerFormData.email" placeholder="Email address"
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
              :type="visible ? 'text' : 'password'" density="compact" placeholder="Enter your password"
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
import { useUserStore } from '@/store/userstore';
import axios from "axios";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

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
    cleanLoginData: {
      username: "",
      password: "",
    },
    errors: []
  }),
  mounted() {
    this.userStore.initStore();
  },
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
            toast("Your have been registerd you can login", {
              "theme": "colored",
              "type": "success",
              "dangerouslyHTMLString": true
            })
            this.appStore.LoginRegister = true

            // Redirect or show a success message
          }).catch(error => {
            if (error.response && error.response.data) {
              const responseData = error.response.data;
              if (typeof responseData === 'object' && Object.keys(responseData).length > 0) {
                // Iterate over the fields with errors
                for (const field in responseData) {
                  if (Object.hasOwnProperty.call(responseData, field)) {
                    // Iterate over the error messages for the field
                    responseData[ field ].forEach(errorMessage => {
                      toast(errorMessage, {
                        "theme": "colored",
                        "type": "error",
                        "dangerouslyHTMLString": true
                      });
                    });
                  }
                }
              } else {
                // Handle unexpected response data
                console.error('Unexpected error response:', responseData);
              }
            } else {
              // Handle other types of errors
              console.error('Error occurred:', error);
            }
          });
      } else {
        for (const error of this.errors) {
          toast(error, {
            "theme": "colored",
            "type": "error",
            "dangerouslyHTMLString": true
          })
        }
      }
    },
    async login() {
      this.errors = [];

      // Trim whitespace from input fields
      this.cleanLoginData.username = this.cleanLoginData.username.trim();
      this.cleanLoginData.password = this.cleanLoginData.password.trim();

      // Input validation
      if (
        !this.cleanLoginData.username ||
        !this.cleanLoginData.password
      ) {
        toast("Please enter your email/username and password.", {
          "theme": "colored",
          "type": "error",
          "dangerouslyHTMLString": true
        });
        return;
      }

      try {
        let response;
        response = await axios.post('http://127.0.0.1:8000/api/user/login', this.cleanLoginData);
        console.log(response.data); // Handle successful response
        // Redirect or show a success message
        this.userStore.setToken(response.data);

        const accessToken = this.userStore.user.access;

        const userInfoResponse = await axios.get('http://127.0.0.1:8000/api/user/info', {
          headers: {
            'Authorization': `Bearer ${accessToken}`
          }
        });

        console.log(userInfoResponse.data);
        this.userStore.setUserInfo(userInfoResponse.data);
        this.appStore.overlay = false;
        this.userStore.initStore();
        await this.userStore.fetchUserProfilePicture();

      } catch (error) {
        const errorMessage = error.response ? error.response.data.error : error.message;
        if (errorMessage) {
          toast(errorMessage, {
            "theme": "colored",
            "type": "error",
            "dangerouslyHTMLString": true
          });
        } else {
          // If error message is empty or undefined, display a generic error message
          toast("An error occurred. Please try again later.", {
            "theme": "colored",
            "type": "error",
            "dangerouslyHTMLString": true
          });
        }
      }
    },
  }
}
</script>

<style>
.app-overlay {
  overflow-x: hidden;
  overflow-y: auto;
  height: 100% !important;
  width: 100% !important;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.app-login-close-icon {
  position: absolute;
  top: -51px;
  right: -43px;
}

@media (max-width:595px) {
  #login .login-card {
    max-width: 448px !important;
  }


}

@media (max-width:800px) {
  #register .register-card {
    max-width: 448px !important;
  }

  .app-login-close-icon {
    right: 50%;
    transform: translateX(50%);
  }
}

@media (max-width:470px) {
  #login .login-card {
    max-width: 400px !important;
  }

  #register .register-card {
    max-width: 400px !important;
  }
}

@media (max-width:420px) {
  #login .login-card {
    max-width: 370px !important;
  }

  #register .register-card {
    max-width: 370px !important;
  }
}


@media (max-width:378px) {
  #login .login-card {
    max-width: 320px !important;
  }

  #register .register-card {
    max-width: 320px !important;
  }
}
</style>
