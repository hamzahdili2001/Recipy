<template>
  <v-footer class="app-footer mt-12">
    <v-row justify="center" no-gutters>
      <v-btn v-for="link in links" :key="link" class="mx-2" color="black" rounded="xl" variant="text">
        {{ link }}
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
      'Home',
      'About Us',
      'Team',
      'Services',
      'Blog',
      'Contact Us',
    ],
  }),
}
</script>

<style>
.app-footer {
  border-top: 1px solid #DDD !important;
}
</style>
