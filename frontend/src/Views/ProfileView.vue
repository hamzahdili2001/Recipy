<script setup>
import AppNavigationBar from "@/components/AppNavigationBar.vue";
import ProfileSettings from "@/components/ProfileSettings.vue";
</script>
<template>
  <ProfileSettings :imageURL="userStore.userProfileImageUrl" />
</template>

<script>
import { useUserStore } from "@/store/userstore";

export default {
  data() {
    return {
      userStore: useUserStore(),
    };
  },
  mounted() {
    this.userStore.fetchUserProfilePicture();
  },
};
</script>
