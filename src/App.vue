<script setup lang="ts">
import VideoBackground from './VideoBackground.vue'
</script>

<template>
  <VideoBackground>
    <div class="content">
      <div class="name">
        <div>Alex</div>
        <div>Polosky</div>
      </div>
      <div class="callout">
        <ol>
          <li>Developer</li>
          <li>|</li>
          <li>Tinkerer</li>
          <li>|</li>
          <li>Musician</li>
        </ol>
      </div>
      <nav>
        <a href="#">Tes 1</a>
        <a href="#">Test 2</a>
        <a href="#">And fina</a>
      </nav>
    </div>
  </VideoBackground>
</template>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);

  font-family: 'Montserrat', sans-serif;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}

.name {
  font-family: 'Major Mono Display', monospace;
  font-weight: 800;
  font-style: normal;
  color: #5ecdf0;
  font-size: calc(max(48px, 10vw));

  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: flex-start;

  padding: 0 0.1em;
  margin-bottom: 0.1em;
  margin-left: 5%;
  border: solid 0.1em #5ecdf0;

  filter: drop-shadow(0 0 30px rgba(94, 206, 240, 0.8));
}

.name > div {
  width: 100%;
  text-align: left;
}

.callout ol {
  list-style-type: none;
  display: inline;
  margin: 0;
  padding: 0;
}

.callout ol li {
  padding: 0 0.3em;
  font-size: 2em;
  float: left;
}

nav {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: flex-start;
  margin: 0 1em;
}

nav a {
}
</style>
