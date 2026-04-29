<script setup lang="ts">
/**
 * Hero wordmark — site signature「晚樵庐」 (S1).
 *
 * Per DESIGN.md "The Brush-Marks-the-Welcome Rule":
 *   Display-brush wordmark appears ONLY in: (a) hero top-left, (b) Quiet Mode
 *   header, (c) favicon. Never in body text or buttons.
 *
 * Sits on top of the lamp-glow halo without being engulfed by it.
 */
const { t } = useI18n()
</script>

<template>
  <div class="hero-wordmark" role="banner">
    <img
      class="hero-wordmark__img"
      src="/art/signatures/wordmark-zh.png"
      :alt="t('site.name')"
      width="800"
      height="300"
    />
  </div>
</template>

<style scoped>
.hero-wordmark {
  width: clamp(140px, 14vw, 240px);
  /* Slightly tilted to feel hand-placed, not centered-formal */
  transform: rotate(-2deg);
  transform-origin: top left;
}

.hero-wordmark__img {
  width: 100%;
  height: auto;
  /* Wordmark is dark ink on white paper background — multiply blend lets the
     desk warmth show through the white paper, looking less like a sticker. */
  mix-blend-mode: multiply;
  opacity: 0.92;
}
</style>
