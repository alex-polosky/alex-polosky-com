<script setup lang="ts">
import { ref, onMounted } from 'vue'

const videoElement = ref<HTMLVideoElement | null>(null)
const videoFailed = ref(false)
const videoSources = ref<{ src: string; type: string }[] | null>(null)

const handleVideoError = () => {
  console.warn('Video failed to load, using fallback background')
  videoFailed.value = true
}

onMounted(() => {
  videoSources.value = [
    {
      src: '/video/output.webm',
      type: 'video/webm',
    },
    {
      src: '/video/output.mp4',
      type: 'video/mp4',
    },
  ]
  setTimeout(() => {
    setTimeout(() => {
      try {
        if (videoElement.value) {
          videoElement.value.muted = true
          videoElement.value.play().catch((error) => {
            console.error('Video autoplay prevented:', error)
            handleVideoError()
          })
        }
      } catch (error) {
        console.error('Video element error:', error)
        handleVideoError()
      }
    }, 100)
  }, 100)
})
</script>

<template>
  <div class="video-background" :class="{ 'video-background__fallback': videoFailed }">
    <video
      v-if="videoSources"
      ref="videoElement"
      autoplay
      loop
      muted
      playsinline
      class="video-background__video"
      @error="handleVideoError"
    >
      <template v-for="(source, index) in videoSources" :key="index">
        <source :src="source.src" :type="source.type" @error="handleVideoError" />
      </template>
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

.video-background__fallback::before {
  background: #052b36;
  opacity: 1;
}

.video-background__fallback .video-background__video {
  display: none;
}
</style>
