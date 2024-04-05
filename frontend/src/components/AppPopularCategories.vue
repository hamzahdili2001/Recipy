<template>
  <div class="mt-10 mx-15">
    <h1>Popular Cuisines</h1>
    <div class="d-flex justify-center align-center mt-8 ga-4 flex-wrap w-100">
      <v-col v-for="card in cards" :key="card" class="pa-0">
        <v-card style="max-width: 100%;" class="mx-auto" height="200" :image="card.image" min-width="200" theme="dark">
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
          title: "Italian",
          image: "https://cdn.britannica.com/59/1759-050-FCD5A574/Flag-Italy.jpg"
        },
        {
          title: "American",
          image: "https://cdn.britannica.com/33/4833-050-F6E415FE/Flag-United-States-of-America.jpg"
        },
        {
          title: "Spanish",
          image: "https://cdn.britannica.com/36/4336-050-056AC114/Flag-Spain.jpg"
        },
        {
          title: "Mexican",
          image: "https://cdn.britannica.com/73/2573-050-C825CE68/Flag-Mexico.jpg"
        },
        {
          title: "French",
          image: "https://cdn.britannica.com/82/682-004-F0B47FCB/Flag-France.jpg"
        },
        {
          title: "Japanese",
          image: "https://cdn.britannica.com/91/1791-050-270C9B3E/Flag-Japan.jpg"
        }
      ]
    }
  }
}

</script>

<style></style>
