<script setup lang="ts">
import router from './router'

const routes = router.getRoutes()
</script>

<template>
  <div class="resistor">
    <nav>
      <template v-for="(route, index) in routes" :key="index">
        <RouterLink :to="route.path">{{ route.name }}</RouterLink>
      </template>
    </nav>
    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
.resistor {
  display: flex;
  flex-direction: row;
  background-color: #020e12;
  color: #5ecdf0;
  height: 100vh;
  overflow: hidden;
}

.resistor nav {
  width: 30%;
  flex-shrink: 0;
}

.resistor .content {
  flex: 1;
  overflow-y: auto;
  padding: 1em 2em;
}

nav {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  position: relative;
}

nav::after {
  z-index: 0;
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 80%;
  background: linear-gradient(to left, #052b36, #020e12);
  pointer-events: none;
}

nav a {
  z-index: 1;
  display: block;
  color: #0c637e;
  text-decoration: none;
  font-size: 2em;
  padding: 0.3em 0;
  width: 100%;
  margin-left: 3em;
}

nav a:hover,
a.router-link-active {
  color: #5ecdf0;
  filter: drop-shadow(0 0 50px #5ecdf0);
}
</style>
