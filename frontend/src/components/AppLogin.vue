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

                        <a class="text-caption text-decoration-none text-blue" href="#" rel="noopener noreferrer"
                            target="_blank">
                            Forgot login password?</a>
                    </div>

                    <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'" density="compact" placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline" variant="outlined"
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
                <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">

                    <div class="text-subtitle-1 text-medium-emphasis">User Name</div>
                    <v-text-field density="compact" placeholder="First Name" prepend-inner-icon="mdi-account-outline"
                        variant="outlined"></v-text-field>

                    <div class="text-subtitle-1 text-medium-emphasis">Email</div>

                    <v-text-field density="compact" placeholder="Email address" prepend-inner-icon="mdi-email-outline"
                        variant="outlined"></v-text-field>

                    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Password
                    </div>

                    <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'" density="compact" placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline" variant="outlined"
                        @click:append-inner="visible = !visible"></v-text-field>

                    <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                        Confirm Password
                    </div>

                    <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="visible ? 'text' : 'password'" density="compact" placeholder="Enter your password"
                        prepend-inner-icon="mdi-lock-outline" variant="outlined"
                        @click:append-inner="visible = !visible"></v-text-field>

                    <v-btn class="mb-8" color="blue" size="large" variant="tonal" block append-icon="mdi-arrow-right">
                        Next
                    </v-btn>
                    <v-card-text class="text-center">
                        <a class="text-blue text-decoration-none cursor-pointer" @click="appStore.LoginRegister = true"
                            rel="noopener noreferrer">
                            <v-icon icon="mdi-chevron-left"></v-icon> Login
                        </a>
                    </v-card-text>


                </v-card>
            </div>
        </v-overlay>
    </div>
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
        visible: false,
    })
}
</script>

<style>
.app-login-close-icon {
    position: absolute;
    top: -51px;
    right: -43px;
}
</style>
