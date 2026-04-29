<script setup lang="ts">
/**
 * 晚樵庐 Hero — primary landing page.
 *
 * Composition (per DESIGN.md §5 Hero Scene):
 *   - <HeroScene>              — full-bleed desk background (V1 video / S3 fallback)
 *   - <CardStack>              — center, 5 cards (主导航)
 *   - <EasterEggScroll>        — bottom-left corner scroll (彩蛋触发器)
 *   - <FooterLink>             — easter-egg redundant path #2
 *   - <LanguageToggle>         — top-right
 *
 * This file is a thin shell — visual & interaction details live in the
 * components themselves and will be detailed in `$impeccable shape homepage`.
 */
const { t } = useI18n()
useSeoMeta({ title: () => t('site.name'), description: () => t('site.tagline') })
</script>

<template>
  <main class="hero">
    <HeroScene />
    <HeroWordmark class="hero__wordmark" />
    <CardStack class="hero__cards" />
    <EasterEggScroll class="hero__scroll" />
    <LanguageToggle class="hero__lang" />
    <FooterLink class="hero__footer" />
  </main>
</template>

<style scoped>
.hero {
  position: relative;
  width: 100vw;
  min-height: 100vh;
  overflow: hidden;
}

.hero__wordmark {
  position: absolute;
  top: var(--space-xl);
  left: var(--space-xl);
  z-index: var(--z-hero-objects);
}

/* Card stack offset toward upper-left so it sits inside the lamp's lit pool
   (S3 background has its warm circle centered around 30% x, 35% y). */
.hero__cards {
  position: absolute;
  top: 45%;
  left: 42%;
  transform: translate(-50%, -50%);
  z-index: var(--z-hero-objects);
}

.hero__scroll {
  position: absolute;
  left: 4%;
  bottom: 6%;
  z-index: var(--z-hero-easter-egg);
}

.hero__lang {
  position: absolute;
  top: var(--space-lg);
  right: var(--space-lg);
  z-index: var(--z-language-toggle);
}

.hero__footer {
  position: absolute;
  bottom: var(--space-lg);
  right: var(--space-xl);
  z-index: var(--z-language-toggle);
}
</style>
