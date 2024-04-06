<template>
  <div style="height: 100vh;" class="d-flex justify-center align-center">
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-card class="not-found-card w-100" elevation="0">
          <v-card-title class="not-found-title">
            Oops! Page Not Found
          </v-card-title>
          <v-card-text class="not-found-text">
            <p>The page you are looking for does not exist.</p>
            <p>Please check the URL or go back to the homepage.</p>
          </v-card-text>
          <v-card-actions class="not-found-actions">
            <v-btn color="primary" href="/">Go to Homepage</v-btn>
          </v-card-actions>
        </v-card>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
}
</script>

<style scoped>
.not-found-card {
  max-width: 400px;
  padding: 20px;
  text-align: center;
  margin: auto;
}

.not-found-title {
  font-size: 24px;
  font-weight: bold;
}

.not-found-text {
  font-size: 16px;
}

.not-found-actions {
  justify-content: center;
}
</style>
