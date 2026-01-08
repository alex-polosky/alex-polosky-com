<script setup lang="ts">
import { useRoute } from 'vue-router'
import SiteNav from './SiteNav.vue'

const route = useRoute()
console.log(route.path)
</script>

<template>
  <RouterView v-if="route.path === '/'" />
  <SiteNav v-else> </SiteNav>
</template>

<style scoped></style>
