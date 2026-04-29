<script setup lang="ts">
/**
 * Hero scene — desk background.
 *
 * - Default: V1 video loop (desk-ambient.mp4) plays auto-loop muted
 * - prefers-reduced-motion: replaced by S3 static image
 * - All media loaded from /art/* and treated as cosmetic (no JS interactivity)
 *
 * This component owns ONLY the background. Cards, scroll, toggles are siblings
 * placed by the parent page so the desk is always the bottom layer.
 */
const reducedMotion = ref(false)
onMounted(() => {
  reducedMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
})
</script>

<template>
  <div class="hero-scene" :aria-hidden="true">
    <img
      v-if="reducedMotion"
      class="hero-scene__media"
      src="/art/homepage/desk-scene.png"
      alt=""
      loading="eager"
    />
    <video
      v-else
      class="hero-scene__media"
      src="/art/motion/desk-ambient.mp4"
      autoplay
      loop
      muted
      playsinline
      poster="/art/homepage/desk-scene.png"
    />
    <div class="hero-scene__grain" />
  </div>
</template>

<style scoped>
.hero-scene {
  position: absolute;
  inset: 0;
  z-index: var(--z-hero-bg);
  pointer-events: none;
  background: var(--desk-walnut-deep);
  overflow: hidden;
}

.hero-scene__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* grain overlay for paper texture; mix-blend-mode multiply at low opacity */
.hero-scene__grain {
  position: absolute;
  inset: 0;
  background-image: url('/art/textures/grain-paper.png');
  background-size: 512px 512px;
  background-repeat: repeat;
  opacity: 0.08;
  mix-blend-mode: multiply;
  pointer-events: none;
}
</style>
