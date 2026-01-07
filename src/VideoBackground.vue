<script setup lang="ts">
import { ref, onMounted } from 'vue'

const videoElement = ref<HTMLVideoElement | null>(null)

onMounted(() => {
  // Ensure video plays (some browsers block autoplay)
  if (videoElement.value) {
    // Firefox requires explicit muting
    videoElement.value.muted = true
    videoElement.value.play().catch((error) => {
      console.error('Video autoplay prevented:', error)
    })
  }
})
</script>

<template>
  <div class="video-background">
    <video ref="videoElement" autoplay loop muted playsinline class="video-background__video">
      <source src="/video/output.webm" type="video/webm" />
      <source src="/video/output.mp4" type="video/mp4" />
    </video>
    <div class="video-background__overlay">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.video-background {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.video-background__video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  transform: translate(-50%, -50%);
  object-fit: cover;
  z-index: -1;
}

.video-background__overlay {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
}

.video-background::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(5, 43, 54, 0.9);
  z-index: 0;
}
</style>
