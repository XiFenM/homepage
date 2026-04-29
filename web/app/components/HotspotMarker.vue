<script setup lang="ts">
/**
 * 勿忘我 hotspot — a single golden dot on the parchment.
 *
 * Per DESIGN.md "Hotspot Marker" + "The No-Levitation Rule":
 *   - 20px desktop / 16px mobile, mustard-gold fill + 1px ink-black outline
 *   - Hover (motion): slow 8s breathing + lamp-glow halo
 *   - Hover (reduced-motion): static halo only, no scale
 *   - Focus (keyboard): 8px ink-black double dashed ring (matches CardStack)
 *   - **Never** translateY on hover — state lives in glow + breath, not levitation
 *
 * The Stargazer's Tower marker uses size='lg' so it reads as the natural
 * climax of the tab order before the Cosmos sub-zone takes over.
 */
defineProps<{
  position: { x: string; y: string }
  ariaLabel: string
  size?: 'md' | 'lg'
}>()

defineEmits<{ activate: [] }>()
</script>

<template>
  <button
    type="button"
    class="hotspot"
    :class="size === 'lg' ? 'hotspot--lg' : 'hotspot--md'"
    :style="{ left: position.x, top: position.y }"
    :aria-label="ariaLabel"
    @click="$emit('activate')"
    @keydown.enter.prevent="$emit('activate')"
    @keydown.space.prevent="$emit('activate')"
  >
    <span class="hotspot__halo" aria-hidden="true" />
    <span class="hotspot__dot" aria-hidden="true" />
  </button>
</template>

<style scoped>
.hotspot {
  position: absolute;
  transform: translate(-50%, -50%);
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  background: transparent;
  border: 0;
  padding: 0;
  cursor: pointer;
  outline: 0;
}

.hotspot__dot {
  display: block;
  background: var(--map-mustard-gold);
  border: 1px solid var(--ink-black);
  border-radius: var(--rounded-pill);
  position: relative;
  z-index: 2;
}
.hotspot--md .hotspot__dot { width: 20px; height: 20px; }
.hotspot--lg .hotspot__dot { width: 26px; height: 26px; }

.hotspot__halo {
  position: absolute;
  inset: 0;
  border-radius: var(--rounded-pill);
  background: radial-gradient(
    circle,
    oklch(from var(--lamp-glow) l c h / 0.55) 0%,
    oklch(from var(--lamp-glow) l c h / 0) 70%
  );
  opacity: 0;
  transition: opacity 220ms ease-out;
  z-index: 1;
}

.hotspot:hover .hotspot__halo,
.hotspot:focus-visible .hotspot__halo {
  opacity: 1;
}

/* Slow 8s breathing on the dot itself — only when motion is allowed. */
@media (prefers-reduced-motion: no-preference) {
  .hotspot:hover .hotspot__dot {
    animation: hotspot-breathe 8s ease-in-out infinite;
  }
}

@keyframes hotspot-breathe {
  0%, 100% { transform: scale(1); }
  50%      { transform: scale(1.15); }
}

/* Focus ring — ink-black dashed double ring, matches CardStack focus */
.hotspot:focus-visible {
  outline: 1px dashed var(--ink-black);
  outline-offset: 6px;
  border-radius: var(--rounded-pill);
}

@media (max-width: 640px) {
  .hotspot { width: 28px; height: 28px; }
  .hotspot--md .hotspot__dot { width: 16px; height: 16px; }
  .hotspot--lg .hotspot__dot { width: 22px; height: 22px; }
}
</style>
