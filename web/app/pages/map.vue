<script setup lang="ts">
/**
 * 勿忘我 — hidden Map Mode page.
 *
 * Reachable via:
 *   1. Easter-egg scroll click at /          (V3 plays inline → enters /map)
 *   2. Direct URL /map or /勿忘我             (V3 plays as page-load intro)
 *   3. Footer link "still wandering somewhere..."
 *
 * Shows the world map (S6) full-bleed with hotspot markers. Clicking the
 * Stargazer's Tower hotspot triggers V3 (cosmos transition) and reveals S7.
 */
definePageMeta({
  alias: ['/勿忘我'], // bilingual URL parity per Design Principle #8
})

const { t } = useI18n()
useSeoMeta({ title: () => `${t('map.title')} · ${t('site.name')}` })
</script>

<template>
  <main class="map">
    <MapView />
    <LanguageToggle class="map__lang" />
    <NuxtLink to="/" class="map__back" :aria-label="t('map.back')">
      ← {{ t('map.back') }}
    </NuxtLink>
  </main>
</template>

<style scoped>
.map {
  position: relative;
  width: 100vw;
  min-height: 100vh;
  background: var(--map-parchment-edge);
  overflow: hidden;
}

.map__lang {
  position: absolute;
  top: var(--space-lg);
  right: var(--space-lg);
  z-index: var(--z-language-toggle);
}

.map__back {
  position: absolute;
  top: var(--space-lg);
  left: var(--space-lg);
  z-index: var(--z-language-toggle);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: var(--map-burgundy);
  text-decoration: none;
}
.map__back:hover {
  color: var(--seal-red);
}
</style>
