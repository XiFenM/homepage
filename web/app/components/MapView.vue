<script setup lang="ts">
/**
 * 勿忘我 — full-bleed parchment world map (S6) with overlaid hotspot dots.
 *
 * Composition:
 *   - Frame container, aspect-ratio 16/9, centered in the viewport with
 *     12vw scroll-margin breathing on all four sides (DESIGN.md §6 Do).
 *   - World map image fills the frame.
 *   - N hotspot markers positioned by percentages relative to the frame.
 *   - Click handler routes to either HotspotPeekCard (kind='peek') or
 *     CosmosView (kind='cosmos').
 *
 * Tab order is the data array order (narrative, not geographic) — Wayfarer's
 * Inn first, Stargazer's Tower last (because the tower steals the viewport).
 */
import { hotspots, type Hotspot } from '~/data/hotspots'

const { t, locale } = useI18n()
const lang = computed<'zh' | 'en'>(() => (locale.value === 'en' ? 'en' : 'zh'))

const openId = ref<string | null>(null)
const cosmosOpen = ref(false)

const openHotspot = computed<Hotspot | null>(() =>
  openId.value ? hotspots.find((h) => h.id === openId.value) ?? null : null,
)

function activate(h: Hotspot) {
  if (h.kind === 'cosmos') {
    cosmosOpen.value = true
  } else {
    openId.value = h.id
  }
}

function closePeek() {
  openId.value = null
}

function closeCosmos() {
  cosmosOpen.value = false
}
</script>

<template>
  <div class="map-view">
    <div class="map-view__frame">
      <img
        class="map-view__img"
        src="/art/map/world-map.png"
        :alt="t('map.title')"
        loading="eager"
      />
      <HotspotMarker
        v-for="h in hotspots"
        :key="h.id"
        :position="h.position"
        :size="h.kind === 'cosmos' ? 'lg' : 'md'"
        :aria-label="`${h.title[lang]} — ${t('map.openHotspot')}`"
        @activate="activate(h)"
      />
    </div>

    <HotspotPeekCard
      v-if="openHotspot"
      :hotspot="openHotspot"
      @close="closePeek"
    />

    <CosmosView
      v-if="cosmosOpen"
      :hotspot="hotspots.find((h) => h.kind === 'cosmos')!"
      @close="closeCosmos"
    />
  </div>
</template>

<style scoped>
.map-view {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  padding: var(--space-scroll-margin);
  background: var(--map-parchment-edge);
}

.map-view__frame {
  position: relative;
  width: 100%;
  /* Fill the available space while keeping 16:9 — the smaller of width-bound
     or height-bound wins. */
  max-width: calc((100vh - 2 * var(--space-scroll-margin)) * 16 / 9);
  max-height: 100%;
  aspect-ratio: 16 / 9;
}

.map-view__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* Subtle grain — parchment already has it baked, but keep a hair of
     texture darkening at the corners for the "well-thumbed" feel. */
  filter: saturate(0.96);
  user-select: none;
  -webkit-user-drag: none;
}
</style>
