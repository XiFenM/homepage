<script setup lang="ts">
/**
 * Cosmos Sub-zone — the Stargazer's Tower hotspot's full-viewport takeover.
 *
 * State machine:
 *   1. 'entering'  — V3 video plays (motion), or 600ms opacity blend
 *      (reduced-motion). Map fades behind it.
 *   2. 'open'      — S7 starfield + Cosmos Observation Card with wishes.
 *   3. exits via the parent's close handler; CosmosView itself only manages
 *      the entrance.
 *
 * The Cosmos-Lockout Rule (DESIGN.md §2): cosmos-* tokens only appear in
 * this component. They never leak back to map or quiet zones.
 */
import type { Hotspot } from '~/data/hotspots'

const props = defineProps<{ hotspot: Hotspot }>()
const emit = defineEmits<{ close: [] }>()

const { t, locale } = useI18n()
const lang = computed<'zh' | 'en'>(() => (locale.value === 'en' ? 'en' : 'zh'))

const phase = ref<'entering' | 'open'>('entering')

const reducedMotion = ref(false)
onMounted(() => {
  reducedMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (reducedMotion.value) {
    // 600ms opacity blend, then settle into 'open'
    setTimeout(() => (phase.value = 'open'), 600)
  }
  document.addEventListener('keydown', onKey)
})

onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKey)
})

function onVideoEnded() {
  phase.value = 'open'
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') emit('close')
}

// Decorative near-layer stars — 9 positions with staggered breath delays.
const nearStars = [
  { x: '12%', y: '22%', d: 0,    s: 5 },
  { x: '78%', y: '15%', d: 1.4,  s: 4 },
  { x: '34%', y: '40%', d: 2.8,  s: 6 },
  { x: '88%', y: '52%', d: 0.6,  s: 5 },
  { x: '22%', y: '70%', d: 3.2,  s: 4 },
  { x: '62%', y: '78%', d: 1.0,  s: 5 },
  { x: '46%', y: '12%', d: 2.0,  s: 4 },
  { x: '8%',  y: '50%', d: 3.6,  s: 5 },
  { x: '70%', y: '36%', d: 0.4,  s: 5 },
]

const wishes = computed(() =>
  props.hotspot.body.type === 'wishes' ? props.hotspot.body.wishes : [],
)
</script>

<template>
  <div class="cosmos" role="dialog" aria-modal="true" :aria-label="hotspot.title[lang]">
    <!-- Phase 1: V3 transition video (motion) -->
    <video
      v-if="phase === 'entering' && !reducedMotion"
      class="cosmos__video"
      src="/art/motion/cosmos-transition.mp4"
      autoplay
      muted
      playsinline
      preload="auto"
      @ended="onVideoEnded"
    />

    <!-- Phase 1: reduced-motion blend (no video) -->
    <div
      v-else-if="phase === 'entering' && reducedMotion"
      class="cosmos__blend"
      aria-hidden="true"
    />

    <!-- Phase 2: starfield + card -->
    <template v-else>
      <img
        class="cosmos__starfield"
        src="/art/cosmos/starfield.png"
        alt=""
        aria-hidden="true"
      />

      <!-- Decorative near-layer stars, hand-placed, slow breathing -->
      <span
        v-for="(s, i) in nearStars"
        :key="i"
        class="cosmos__star"
        :style="{
          left: s.x,
          top: s.y,
          width: `${s.s}px`,
          height: `${s.s}px`,
          animationDelay: `${s.d}s`,
        }"
        aria-hidden="true"
      />

      <button
        type="button"
        class="cosmos__close"
        :aria-label="t('cosmos.back')"
        @click="emit('close')"
      >
        ← {{ t('cosmos.back') }}
      </button>

      <article class="cosmos__card">
        <h2 class="cosmos__title" :class="`cosmos__title--${lang}`">
          {{ hotspot.title[lang] }}
        </h2>

        <ol class="cosmos__wishes">
          <li
            v-for="(wish, i) in wishes"
            :key="i"
            class="cosmos__wish"
          >
            {{ wish[lang] }}
          </li>
        </ol>

        <p v-if="hotspot.meta" class="cosmos__meta">{{ hotspot.meta[lang] }}</p>
      </article>
    </template>
  </div>
</template>

<style scoped>
.cosmos {
  position: fixed;
  inset: 0;
  z-index: var(--z-cosmos-overlay);
  background: var(--cosmos-deep-night);
  color: var(--cosmos-ice-white);
  overflow: hidden;
  /* Slow fade-in of the deep-night base; the starfield/video lays on top. */
  animation: cosmos-fade-in 600ms ease-out;
}

@keyframes cosmos-fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.cosmos__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cosmos__blend {
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at center,
    var(--cosmos-pearl-blue) 0%,
    var(--cosmos-deep-night) 70%
  );
  opacity: 0.4;
  animation: cosmos-blend 600ms ease-out;
}
@keyframes cosmos-blend {
  from { opacity: 0; }
  to   { opacity: 0.4; }
}

.cosmos__starfield {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* Slight saturation drop so the painted stars feel less posterized
     when overlaid with the SVG near-layer. */
  filter: saturate(0.92);
  animation: cosmos-starfield-in 1200ms ease-out;
}
@keyframes cosmos-starfield-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* Near-layer stars: bright pearl-blue with a soft glow.
   8s slow breathe, opacity 0.6 → 1 → 0.6. Reduced-motion: static at 0.85. */
.cosmos__star {
  position: absolute;
  border-radius: var(--rounded-pill);
  background: var(--cosmos-ice-white);
  box-shadow: none;
  filter: drop-shadow(0 0 4px oklch(from var(--cosmos-pearl-blue) l c h / 0.85));
  opacity: 0.85;
}
@media (prefers-reduced-motion: no-preference) {
  .cosmos__star {
    animation: cosmos-star-breathe 8s ease-in-out infinite;
  }
}
@keyframes cosmos-star-breathe {
  0%, 100% { opacity: 0.6; transform: scale(0.95); }
  50%      { opacity: 1;   transform: scale(1.1); }
}

.cosmos__close {
  position: absolute;
  top: var(--space-lg);
  left: var(--space-lg);
  z-index: 2;
  background: transparent;
  border: 0;
  padding: 6px 10px;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--cosmos-ice-white) l c h / 0.7);
  cursor: pointer;
  transition: color 200ms ease-out;
}
.cosmos__close:hover, .cosmos__close:focus-visible {
  color: var(--cosmos-tangerine);
  outline: 0;
}

.cosmos__card {
  position: absolute;
  bottom: 12vh;
  left: 50%;
  transform: translateX(-50%);
  max-width: min(60ch, 88vw);
  padding: var(--space-lg);
  background: oklch(from var(--cosmos-deep-night) l c h / 0.65);
  border: 1px solid oklch(from var(--cosmos-pearl-blue) l c h / 0.45);
  text-align: left;
  animation: cosmos-card-in 1200ms 600ms ease-out backwards;
}
@keyframes cosmos-card-in {
  from { opacity: 0; transform: translate(-50%, 12px); }
  to   { opacity: 1; transform: translate(-50%, 0); }
}

.cosmos__title {
  margin: 0 0 var(--space-md) 0;
  font-size: clamp(1.4rem, 3vw, 1.9rem);
  font-weight: 600;
  color: var(--cosmos-ice-white);
}
.cosmos__title--zh { font-family: var(--font-serif-zh); letter-spacing: -0.02em; }
.cosmos__title--en {
  font-family: var(--font-serif-en);
  font-style: italic;
  font-weight: 500;
  letter-spacing: 0.02em;
}

.cosmos__wishes {
  margin: 0 0 var(--space-lg) 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}

.cosmos__wish {
  font-family: var(--font-handwritten);
  font-size: clamp(1.15rem, 2.2vw, 1.5rem);
  line-height: 1.55;
  color: var(--cosmos-tangerine);
}

.cosmos__meta {
  margin: 0;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--cosmos-ice-white) l c h / 0.55);
}

@media (max-width: 640px) {
  .cosmos__card {
    bottom: 6vh;
    padding: var(--space-md) var(--space-md) var(--space-lg);
  }
}
</style>
