<template>
    <h3 class="px-15 pa-10">Your Posts</h3>
    <div class="px-15 mb-15">
        <v-card class="mx-auto pa-8 pb-8" max-width="100%" rounded="0">
            <v-text-field label="Username" prepend-inner-icon="mdi-account-outline" variant="outlined"
                v-model="uname"></v-text-field>
            <div class="d-flex justify-center align-center flex-wrap ga-10">
                <v-text-field label="First Name" prepend-inner-icon="mdi-text-short" variant="outlined"
                    v-model="fname"></v-text-field>
                <v-text-field label="Last Name" prepend-inner-icon="mdi-text-short" variant="outlined"
                    v-model="lname"></v-text-field>
            </div>
            <v-text-field label="Email" prepend-inner-icon="mdi-email-outline" variant="outlined"
                v-model="email"></v-text-field>
            <div class="d-flex justify-center align-center flex-wrap ga-10">
                <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                    :type="visible ? 'text' : 'password'" label="Password" prepend-inner-icon="mdi-lock-outline"
                    variant="outlined" @click:append-inner="visible = !visible"></v-text-field>
                <v-text-field :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                    :type="visible ? 'text' : 'password'" label="Confirm Password" prepend-inner-icon="mdi-lock-outline"
                    variant="outlined" @click:append-inner="visible = !visible"></v-text-field>
            </div>

        </v-card>

    </div>
</template>

<script>
export default {
    data: () => ({
        email: "hdilihamza955@gmail.com",
        fname: "Hamza",
        lname: "Hdili",
        uname: "cupstorms",
        password: "0000000",
        visible: false,

    })
}
</script>