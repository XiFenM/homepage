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
  /* Wordmark PNG now has transparent background (post-processed), so the brush
     strokes are pure ink-black on transparency — no blend mode needed. Keep
     a tiny opacity drop for that "ink-bled-into-wood" feel. */
  opacity: 0.95;
}
</style>
