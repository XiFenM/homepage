<script setup lang="ts">
/**
 * Easter-egg scroll — visual primary path to /map.
 *
 * Default state:    static S4 image, ~10% peeking, rotated -6° "tucked under"
 * Hover (motion):   V2 video plays, scroll grows; stops + resets on mouseleave
 * Hover (reduced):  scroll grows but no video, S4 image stays
 * Click / Enter:    navigate to /map
 *
 * STRICT (PRODUCT.md anti-ref #9): no CTA text, arrows, glow halos, or
 * "click to explore" hints. The micro-protrusion + hover behavior IS the
 * entire invitation.
 */
const { t } = useI18n()
const router = useRouter()
const reducedMotion = ref(false)
const hovering = ref(false)
const videoEl = ref<HTMLVideoElement | null>(null)

onMounted(() => {
  reducedMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
})

const onEnter = async () => {
  hovering.value = true
  if (!reducedMotion.value && videoEl.value) {
    videoEl.value.currentTime = 0
    try {
      await videoEl.value.play()
    } catch {
      // autoplay can be blocked; falls back to scroll-grow visual still works
    }
  }
}

const onLeave = () => {
  hovering.value = false
  if (!reducedMotion.value && videoEl.value) {
    videoEl.value.pause()
    videoEl.value.currentTime = 0
  }
}

const open = () => router.push('/map')
const onKey = (e: KeyboardEvent) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault()
    open()
  }
}
</script>

<template>
  <div
    class="scroll-egg"
    :class="{ 'scroll-egg--open': hovering }"
    role="link"
    tabindex="0"
    :aria-label="t('easterEgg.scrollAlt')"
    @click="open"
    @keydown="onKey"
    @mouseenter="onEnter"
    @mouseleave="onLeave"
    @focus="onEnter"
    @blur="onLeave"
  >
    <!-- Static fallback always rendered, video layered on top when active -->
    <img
      class="scroll-egg__img"
      src="/art/homepage/parchment-scroll.png"
      :alt="t('easterEgg.scrollAlt')"
    />
    <video
      v-if="!reducedMotion"
      ref="videoEl"
      class="scroll-egg__video"
      :class="{ 'scroll-egg__video--visible': hovering }"
      src="/art/motion/parchment-unfurl.mp4"
      muted
      playsinline
      preload="metadata"
    />
  </div>
</template>

<style scoped>
.scroll-egg {
  position: relative;
  width: clamp(120px, 14vw, 220px);
  height: clamp(96px, 10vw, 160px);
  cursor: pointer;
  overflow: hidden;
  border-radius: var(--rounded-sticker);
  transform: rotate(-6deg);
  transform-origin: bottom left;
  transition: transform 600ms cubic-bezier(0.16, 1, 0.3, 1),
              width 800ms cubic-bezier(0.16, 1, 0.3, 1),
              height 800ms cubic-bezier(0.16, 1, 0.3, 1);
}

.scroll-egg:hover,
.scroll-egg:focus-visible {
  transform: rotate(-2deg);
}

.scroll-egg--open {
  width: clamp(220px, 28vw, 420px);
  height: clamp(170px, 22vw, 320px);
}

.scroll-egg__img,
.scroll-egg__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: top left;
}

.scroll-egg__video {
  opacity: 0;
  transition: opacity 200ms ease-out;
}

.scroll-egg__video--visible {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .scroll-egg,
  .scroll-egg--open {
    transition: none;
  }
}
</style>
