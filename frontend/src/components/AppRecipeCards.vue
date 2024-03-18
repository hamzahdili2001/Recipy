<template>

    <div class="mt-10 mb-10 mx-15">
        <h1>Hand-Picked Recipes</h1>
        <div class="d-flex justify-center ga-10 align-center flex-wrap mt-8">
            <v-col v-for="card of cardsInfo" :key="card" class="pa-0">
                <v-card :loading="loading" class="mx-auto my-2" width="100%">
                    <template v-slot:loader="{ isActive }">
                        <v-progress-linear :active="isActive" color="deep-purple" height="4"
                            indeterminate></v-progress-linear>
                    </template>

                    <v-img height="250" :src="card.image" cover></v-img>

                    <v-card-item>
                        <v-card-title>Cafe Badilico</v-card-title>

                        <v-card-subtitle>
                            <span class="me-1">Local Favorite</span>

                            <v-icon color="error" icon="mdi-fire-circle" size="small"></v-icon>
                        </v-card-subtitle>
                    </v-card-item>

                    <v-card-text>
                        <v-row align="center" class="mx-0">
                            <v-rating :model-value="4.5" color="amber" density="compact" size="small" half-increments
                                readonly></v-rating>

                            <div class="text-grey ms-4">
                                4.5 (413)
                            </div>
                        </v-row>

                        <div class="my-4 text-subtitle-1">
                            $ • Italian, Cafe
                        </div>

                        <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio
                            seating.
                        </div>
                    </v-card-text>

                    <v-divider class="mx-4 mb-1"></v-divider>

                    <v-card-title>Tonight's availability</v-card-title>

                    <div class="px-4">
                        <v-chip-group v-model="selection">
                            <v-chip>5:30PM</v-chip>

                            <v-chip>7:30PM</v-chip>

                            <v-chip>8:00PM</v-chip>

                            <v-chip>9:00PM</v-chip>
                        </v-chip-group>
                    </div>

                    <v-card-actions>
                        <v-btn color="deep-purple-lighten-2" variant="text" @click="reserve">
                            Reserve
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </div>
        <div class="d-flex justify-center mt-8">
            <v-btn style="border: 2px solid #000;" class="rounded-0 text-center" elevation="0">Load More</v-btn>
        </div>
    </div>
</template>
<script>
export default {
    data: () => ({
        loading: false,
        selection: 1,
        cardsInfo: [
            {
                image: "https://www.homemademastery.com/wp-content/uploads/2020/09/IMG_0909.jpg",
            },
            {
                image: "https://www.simplyrecipes.com/thmb/zSvZNZj70cA9uzOgV3oZEV5dvrQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Baklava-LEAD-4-a9d125c8d66547ef9f92c6564a5d5241.jpg",
            },
            {
                image: "https://www.simplyrecipes.com/thmb/KRw_r32s4gQeOX-d07NWY1OlOFk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Homemade-Pizza-Dough-Lead-Shot-1c-c2b1885d27d4481c9cfe6f6286a64342.jpg",
            },
            {
                image: "https://assets.bonappetit.com/photos/61b775620fb3fcc4cbf036c1/1:1/w_1920,c_limit/20211208%20Spaghetti%20Squash%20with%20Tomato%20Sauce%20and%20Mozarella%20LEDE.jpg",
            },
            {
                image: "https://www.foodandwine.com/thmb/fVmYbaQzXCz1Prx8VxrW9sMcjMU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Braciole-FT-RECIPE1122-66acf49cef0e4390bec780945709e7f3.jpg",
            },
            {
                image: "https://www.inspiredtaste.net/wp-content/uploads/2023/01/Easy-Bean-Salad-Recipe-Video.jpg",
            },

        ]
    }),

    methods: {
        reserve() {
            this.loading = true

            setTimeout(() => (this.loading = false), 2000)
        },
    },
}
</script>