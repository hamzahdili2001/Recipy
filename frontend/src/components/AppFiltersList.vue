<template>
  <v-list-item v-for="item in items" :key="item" link to="/">
    <v-list-item-title class="my-2 p-3 text-primary" rounded="5">{{ item }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  data() {
    return {
      items: [ "item1", "item2", "item3" ]
    };
  }
}
</script>
