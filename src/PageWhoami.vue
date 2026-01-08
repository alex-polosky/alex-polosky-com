<script setup lang="ts"></script>

<template>
  <div class="transistor">
    <p>Hey there, I'm Alex Polosky.</p>
    <p>
      I like to make things, whether that's software, music, art, or lore is dependent on the day.
    </p>
    <hr />
    <p>
      <b>Lead Software Engineer:</b> Able to lead teams to perform full-stack development, along
      with deployments, with a preference for back-end roles.
    </p>
    <hr />
    <p>
      <b>Tinkerer:</b> Large interest in integrated circuitry (including writing custom CPU
      architectures, compilers, and assembly code) and connecting to the outside world.
    </p>
    <hr />
    <p>
      <b>Avid Local Musician:</b> I've performed in several local bands, written tons of unreleased
      scratch tracks, engineered front of house sound, performed in local fundraisers, and go to
      local shows
    </p>
    <hr />
    <p><b>TTRPG GM:</b> I run several games (DnD, PF2e) and love to create my own worlds.</p>
    <hr />
    <p>
      You can contact me through email by replacing the first `.` in the address bar with an `@`
      (and maybe replacing `http` with `smtp`), or
    </p>
    <p>... you can find out more about me at these places:</p>
    <nav>
      <a href="https://github.com/alex-polosky" target="_blank">Github</a>
      <a href="https://www.linkedin.com/in/alex-polosky/" target="_blank">LinkedIn</a>
    </nav>
  </div>
</template>

<style scoped>
nav {
  display: flex;
  flex-flow: column;
  align-content: center;
  align-items: center;
}

a {
  display: block;
  margin: 0.5em;
  padding: 1em;
  width: 10em;
  background-color: #0c637e;
  color: #fff;
  text-decoration: none;
  text-transform: uppercase;
}

a:hover {
  background-color: #5ecdf0;
  color: #fff;
  filter: drop-shadow(0 0 50px #5ecdf0);
}
</style>
