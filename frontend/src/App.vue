<script setup>
import AppNavigationBar from './components/AppNavigationBar.vue';
import AppFooter from './components/AppFooter.vue';
</script>

<template>
  <v-app>
    <AppNavigationBar />
    <router-view></router-view>
    <AppFooter />
  </v-app>
</template>

<style>
@import "@/assets/styles/main.css";
</style>
