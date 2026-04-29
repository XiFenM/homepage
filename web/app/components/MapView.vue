<script setup lang="ts">
/**
 * The world map view (S6) — full-bleed.
 *
 * Stub — final implementation needs:
 *   - 9–10 hotspot SVG markers positioned over the map (data-driven)
 *   - Hover breathing animation per Hotspot Marker spec (DESIGN.md §5)
 *   - Click → open Hotspot Peek Card (or trigger V3 for观星塔)
 *   - Keyboard tab order following narrative-recommended sequence
 *
 * Will be wired in `$impeccable shape map` next.
 */
const { t } = useI18n()
</script>

<template>
  <div class="map-view">
    <img
      class="map-view__img"
      src="/art/map/world-map.png"
      :alt="t('map.title')"
      loading="eager"
    />
    <!-- TODO: hotspot markers + peek cards -->
  </div>
</template>

<style scoped>
.map-view {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-scroll-margin);
  background: var(--map-parchment-edge);
}

.map-view__img {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  object-fit: contain;
}
</style>
