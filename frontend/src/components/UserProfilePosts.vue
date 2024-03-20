<template>
    <h3 class="px-15 pa-10">Your Posts</h3>
    <div>
        <v-row align="center" justify="center" wrap class="ga-4 flex-wrap w-100 px-15">
            <v-col v-for="i in 5" :key="i">
                <v-card max-width="300" min-width="300" hover>
                    <v-card-item>
                        <v-card-title>
                            Post title
                        </v-card-title>
                        <v-card-subtitle>
                            Post subtitle secondary text
                        </v-card-subtitle>
                    </v-card-item>

                    <v-card-text>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                        labore
                        et
                        dolore magna aliqua.
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
export default {
    data: () => {
        title: "Your Posts"
    }
}
</script>