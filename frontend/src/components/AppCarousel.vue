<template>
    <div class="px-15 pa-6">
        <v-carousel height="650" :show-arrows="true" cycle interval="6000">
            <v-carousel-item v-for="(item, i) in items" :key="i" :src="item.src" cover>
                <div class="w-100 h-100 d-flex flex-column justify-center align-start pt-15 text-white"
                    style="background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8)); padding-left: 112px;">
                    <v-rating :model-value="4.5" color="amber" density="compact" size="small" half-increments
                        readonly></v-rating>
                    <h2>Hello World</h2>
                    <p class=" w-50">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolorum atque nemo
                        nesciunt quisquam
                        cupiditate fuga sapiente, in quasi eius nisi sint molestiae corrupti quo veritatis, ad facere
                        quas provident inventore!</p>
                    <v-btn class="mt-4">Show More</v-btn>
                </div>
            </v-carousel-item>
        </v-carousel>
    </div>
</template>
<script>
export default {
    data() {
        return {
            items: [
                {
                    src: 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                },
                {
                    src: 'https://images.unsplash.com/photo-1511994714008-b6d68a8b32a2?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                },
                {
                    src: 'https://images.unsplash.com/photo-1494859802809-d069c3b71a8a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                },
                {
                    src: 'https://images.unsplash.com/photo-1608835291093-394b0c943a75?q=80&w=2072&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                },
            ],
        }
    },
}
</script>