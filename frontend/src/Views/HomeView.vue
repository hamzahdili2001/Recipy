<script setup>
import AppNavigationBar from '@/components/AppNavigationBar.vue';
import AppCarousel from '@/components/AppCarousel.vue';
import AppPopularCategories from '@/components/AppPopularCategories.vue';
import AppRecipeCards from "@/components/AppRecipeCards.vue";
import AppSubscribe from "@/components/AppSubscribe.vue";
import AppFooter from "@/components/AppFooter.vue";
import AppLogin from "@/components/AppLogin.vue"
</script>
<template>
  <AppCarousel />
  <AppPopularCategories />
  <AppRecipeCards />
  <AppSubscribe />
  <AppLogin />
</template>
