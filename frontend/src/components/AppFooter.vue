<template>
  <v-footer class="app-footer mt-12">
    <v-row justify="center" no-gutters>
      <v-btn v-for="link in links" :key="link.route" class="mx-2" color="black" rounded="xl" variant="text"
        :to="link.route">
        {{ link.name }}
      </v-btn>
      <v-col class="text-center mt-4" cols="12">
        {{ new Date().getFullYear() }} — <strong>Hamzed</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    links: [
      {
        name: "Home",
        route: "/"
      },
      {
        name: "About us",
        route: "/about"
      },
      {
        name: "Recipes",
        route: "/recipes"
      },
      {
        name: "search",
        route: "/recipes-filter"
      }
    ]
  })
}
</script>

<style>
.app-footer {
  border-top: 1px solid #DDD !important;
}
</style>
