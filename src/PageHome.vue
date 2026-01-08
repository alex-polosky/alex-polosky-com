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
          <li>Tinkerer</li>
          <li>Musician</li>
        </ol>
      </div>
      <nav>
        <a href="#">$(whoami)</a>
        <a href="#">projects</a>
        <a href="#">skills</a>
      </nav>
    </div>
  </VideoBackground>
</template>

<style scoped>
.content {
  height: 100vh;
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.name {
  /* Consider 'Audiowide' */
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
  margin: 5% 0 0.1em 5%;
  border: solid 0.1em #5ecdf0;

  filter: drop-shadow(0 0 50px #5ecdf0);
}

.name > div {
  width: 100%;
  text-align: left;
}

.callout {
  width: 100%;
  text-align: center;
  font-size: 1.75em;
}

.callout ol {
  list-style-type: none;
}

@media (min-aspect-ratio: 2/3) {
  .callout {
    font-size: calc(4vw);
  }

  .callout ol {
    list-style-type: none;
    display: inline-block;
    margin: 0;
    padding: 0;
  }

  .callout ol li {
    padding: 0;
    float: left;
  }

  .callout ol li:nth-child(even)::before,
  .callout ol li:nth-child(even)::after {
    padding: 0 0.3em;
    content: '|';
  }
}

@media (max-aspect-ratio: 2/3) {
  .callout {
    font-size: calc(max(24px, 7vw));
  }

  .callout ol li::before,
  .callout ol li::after {
    padding: 0 0.3em;
    content: '|';
  }
}

nav {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

nav a {
  display: block;
  padding: 1em;
  width: 10em;
  /* background-color: #5ecdf0; */
  border: solid 0.25em #5ecdf0;
  color: #fff;
  text-decoration: none;
  text-transform: uppercase;
}

nav a:hover {
  background-color: #5ecdf0;
  color: #fff;
  filter: drop-shadow(0 0 50px #5ecdf0);
}

@media (max-aspect-ratio: 1.8) {
  nav {
    flex-direction: column;
    height: 50vh;
  }

  nav a {
    margin: 1em 0;
  }
}

@media (min-aspect-ratio: 1.8) {
  nav a {
    margin: 2em 6em;
  }
}
</style>
