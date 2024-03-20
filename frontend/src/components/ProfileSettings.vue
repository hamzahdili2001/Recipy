<script setup>
</script>
<template>
    <v-card class="w-100 d-flex justify-center align-center bg-grey-lighten-5
 flex-column pa-10" rounded="0" flat>
        <v-avatar color="grey" class="" rounded="50" size="150">
            <v-img
                src="https://scontent.frba2-1.fna.fbcdn.net/v/t39.30808-6/406045656_1793154191108159_2378818591530544511_n.jpg?stp=dst-jpg_p526x296&_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_ohc=eo32MBmbkeAAX-rFnR2&_nc_ht=scontent.frba2-1.fna&oh=00_AfDfrEHZZOWprhuom_tVp4Hwn3RUxQGDbjTlgL8AKIyOnQ&oe=6600297F"
                cover></v-img>
        </v-avatar>
        <v-list-item class=" text-black text-center" subtitle="Sofware Engineer" title="Hamza Hdili"></v-list-item>
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