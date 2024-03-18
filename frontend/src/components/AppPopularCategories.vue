<template>
    <div class="mt-10 mx-15">
        <h1>Popular Categories</h1>
        <div class="d-flex justify-center align-center flex-wrap mt-8">
            <v-col style="min-width: 200px;" v-for="card in cards" :key="card" cols="12" sm="2">
                <v-card class="mx-auto" height="200" :image="card.image" max-width="200" theme="dark">
                    <v-card-title class="font-weight-bold w-100 h-100"
                        style="background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7));">{{ card.title
                        }}</v-card-title>
                </v-card>
            </v-col>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            cards: [
                {
                    title: "Health",
                    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHPzNZuSagkE-8oz4PAG8zkpii6vsuvsYa04yasyzVvQG17BJvfgvpciRzFsvsAIExjZ8&usqp=CAU"
                },
                {
                    title: "Vegetarian",
                    image: "https://hips.hearstapps.com/hmg-prod/images/easy-vegetarian-recipes-chickpea-salad-smashed-cucumbers-1656600167.jpeg"
                },
                {
                    title: "Breakfast",
                    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaDhCtkaqfiMCMBlGc8W8uhwkuy06jYtVKKQ&usqp=CAU"
                },
                {
                    title: "Summer",
                    image: "https://images.immediate.co.uk/production/volatile/sites/30/2022/12/Avocado-black-bean-eggs-3c81ec9.jpg?quality=90&crop=1520px,0px,4873px,4426px&resize=556,505"
                },
                {
                    title: "Dinner",
                    image: "https://static.chloeting.com/recipes/61ffa47c2a18c23f7d7f985a/images/vegan-breakfast-plate-1.webp"
                },
                {
                    title: "Eggs",
                    image: "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/easy-huevos-rancheros-a247533.jpg?quality=90&resize=500,454path/to/image6.jpg"
                }
            ]
        }
    }
}

</script>