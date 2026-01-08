<script setup lang="ts">
import { ref } from 'vue'
import router from './router'

const routes = router.getRoutes()
const showMenu = ref(false)
</script>

<template>
  <div class="resistor">
    <header>
      <span class="menu" @click="showMenu = !showMenu">☰</span>
      <span class="content"></span>
    </header>
    <nav :class="[showMenu ? '' : 'hide-menu']">
      <template v-for="(route, index) in routes" :key="index">
        <RouterLink :to="route.path" @click="showMenu = false">{{ route.name }}</RouterLink>
      </template>
    </nav>
    <div class="transistor">
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
  flex-shrink: 0;
}

.resistor .transistor {
  flex: 1;
  overflow-y: auto;
  padding: 1em calc(min(2em, 2.5vw));
  color: #eff;
}

nav {
  flex-basis: 0%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  position: relative;
}

nav a {
  z-index: 1;
  display: block;
  color: #0c637e;
  text-decoration: none;
  font-size: 2em;
  padding: 0.3em 0 0.3em 2em;
  width: 100%;
  box-sizing: border-box;
}

nav a:hover,
a.router-link-active {
  color: #5ecdf0;
  filter: drop-shadow(0 0 50px #5ecdf0);
}

header {
  display: none;
}

header span.menu {
  font-size: 2.5em;
  margin-left: 0.25em;
}

@media (min-width: 900px) {
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
}

@media (max-width: 900px) {
  nav.hide-menu {
    display: none;
  }

  .resistor {
    display: block;
  }

  header {
    display: block;
  }

  nav {
    display: flex;
    background: linear-gradient(to left, #052b36, #020e12);
  }

  nav a {
    padding-left: 0em;
    margin: 0 auto;
    width: 50%;
  }

  .transistor {
    display: block;
    height: 90vh;
  }
}
</style>
