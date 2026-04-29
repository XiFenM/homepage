<script setup lang="ts">
/**
 * Hotspot peek card — opens when a (non-cosmos) hotspot is clicked.
 *
 * Per DESIGN.md "Hotspot Peek Card":
 *   - Parchment surface, grain overlay, paper-curl bottom-right
 *   - Scale 0.6 → 1 + opacity 0 → 1, 320ms ease-out-quart on open
 *   - transform-origin = hotspot screen position, so the card visually flies
 *     out from the dot
 *   - 4mm seal-red signature corner; close via ESC / outside / handwritten ✕
 *   - Mobile <640px: bottom drawer instead of floating card
 */
import type { Hotspot } from '~/data/hotspots'

const props = defineProps<{
  hotspot: Hotspot
}>()

const emit = defineEmits<{ close: [] }>()

const { t, locale } = useI18n()

const lang = computed<'zh' | 'en'>(() => (locale.value === 'en' ? 'en' : 'zh'))

const titleClass = computed(() => `peek__title peek__title--${lang.value}`)

// transform-origin tracks the hotspot's relative position so the open
// animation emanates from the dot. Hotspot positions are percentages
// relative to the map frame; the peek card layer sits over the same frame,
// so the same percentages map onto its origin.
const originStyle = computed(() => ({
  transformOrigin: `${props.hotspot.position.x} ${props.hotspot.position.y}`,
}))

// Place the card on the **opposite** half of the viewport from its hotspot,
// so the marker stays visible while the card unfolds.
const sideClass = computed(() => {
  const x = parseFloat(props.hotspot.position.x)
  return x < 50 ? 'peek--right' : 'peek--left'
})

function onBackdropClick(e: MouseEvent) {
  if (e.target === e.currentTarget) emit('close')
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') emit('close')
}

onMounted(() => {
  document.addEventListener('keydown', onKey)
})
onBeforeUnmount(() => {
  document.removeEventListener('keydown', onKey)
})
</script>

<template>
  <Teleport to="body">
    <div
      class="peek-backdrop"
      :class="sideClass"
      role="dialog"
      aria-modal="true"
      :aria-label="hotspot.title[lang]"
      @click="onBackdropClick"
    >
      <article class="peek" :style="originStyle">
        <button
          type="button"
          class="peek__close"
          :aria-label="t('map.close')"
          @click="emit('close')"
        >
          ✕
        </button>

        <h2 :class="titleClass">{{ hotspot.title[lang] }}</h2>

        <!-- paragraphs -->
        <div v-if="hotspot.body.type === 'paragraphs'" class="peek__body">
          <p
            v-for="(para, i) in hotspot.body.paragraphs"
            :key="i"
            class="peek__para"
            :class="`peek__para--${lang}`"
          >
            {{ para[lang] }}
          </p>
        </div>

        <!-- three columns (旅人客栈) -->
        <div v-else-if="hotspot.body.type === 'columns'" class="peek__columns">
          <section
            v-for="(col, i) in hotspot.body.columns"
            :key="i"
            class="peek__col"
          >
            <h3 class="peek__col-label" :class="`peek__col-label--${lang}`">
              {{ col.label[lang] }}
            </h3>
            <ul class="peek__col-list">
              <li v-for="(item, j) in col.items" :key="j" :class="`peek__col-item peek__col-item--${lang}`">
                {{ item[lang] }}
              </li>
            </ul>
          </section>
        </div>

        <footer class="peek__footer">
          <span v-if="hotspot.meta" class="peek__meta">{{ hotspot.meta[lang] }}</span>
          <NuxtLink
            v-if="hotspot.link"
            :to="hotspot.link.to"
            class="peek__link"
          >
            {{ hotspot.link.label[lang] }}
          </NuxtLink>
        </footer>

        <span class="peek__seal" aria-hidden="true">桀</span>
      </article>
    </div>
  </Teleport>
</template>

<style scoped>
.peek-backdrop {
  position: fixed;
  inset: 0;
  z-index: var(--z-map-overlay);
  display: flex;
  align-items: center;
  /* Backdrop is barely visible — a faint parchment darkening, no blur (no
     glassmorphism); just enough to keep focus on the card. */
  background: oklch(from var(--map-parchment-edge) l c h / 0.35);
  padding: var(--space-xl);
  animation: peek-backdrop-in 320ms cubic-bezier(0.22, 1, 0.36, 1);
}

.peek-backdrop.peek--left  { justify-content: flex-start; padding-left: 6vw; }
.peek-backdrop.peek--right { justify-content: flex-end;   padding-right: 6vw; }

.peek {
  position: relative;
  width: clamp(280px, 30vw, 420px);
  padding: 28px 32px 36px;
  background: var(--map-parchment);
  color: var(--map-burgundy);
  border: 1px solid oklch(from var(--map-parchment-edge) l c h / 0.6);
  /* Paper-curl: bottom-right corner clipped diagonally. The clip is small
     (12px) so it reads as "page corner folded back" not "torn paper". */
  clip-path: polygon(
    0 0,
    100% 0,
    100% calc(100% - 16px),
    calc(100% - 16px) 100%,
    0 100%
  );
  /* Grain texture — subtle, multiplies the parchment color. */
  background-image:
    radial-gradient(circle at 20% 15%, oklch(from var(--map-parchment-deep) l c h / 0.18) 0%, transparent 40%),
    radial-gradient(circle at 80% 85%, oklch(from var(--map-parchment-edge)  l c h / 0.16) 0%, transparent 35%);
  animation: peek-in 360ms cubic-bezier(0.22, 1, 0.36, 1);
  /* transform-origin set inline by the script (hotspot %). */
}

@keyframes peek-backdrop-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

@keyframes peek-in {
  from { opacity: 0; transform: scale(0.6); }
  to   { opacity: 1; transform: scale(1); }
}

@media (prefers-reduced-motion: reduce) {
  .peek-backdrop, .peek {
    animation-duration: 200ms;
  }
  .peek {
    animation-name: peek-in-reduced;
  }
  @keyframes peek-in-reduced {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
}

.peek__close {
  position: absolute;
  top: 8px;
  right: 14px;
  background: transparent;
  border: 0;
  padding: 4px 8px;
  cursor: pointer;
  font-family: var(--font-handwritten);
  font-size: 1.4rem;
  color: oklch(from var(--map-burgundy) l c h / 0.6);
  transition: color 200ms ease-out;
}
.peek__close:hover, .peek__close:focus-visible {
  color: var(--seal-red);
  outline: 0;
}

.peek__title {
  margin: 0 0 var(--space-md) 0;
  font-size: 1.45rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.3;
}
.peek__title--zh { font-family: var(--font-serif-zh); }
.peek__title--en {
  font-family: var(--font-serif-en);
  font-style: italic;
  font-weight: 500;
  letter-spacing: 0.01em;
}

.peek__body { margin-bottom: var(--space-lg); }

.peek__para {
  margin: 0 0 var(--space-md) 0;
  font-size: 1rem;
  line-height: 1.85;
  color: oklch(from var(--ink-black) l c h / 0.88);
}
.peek__para--zh {
  font-family: var(--font-serif-zh);
  letter-spacing: -0.005em;
}
.peek__para--en {
  font-family: var(--font-serif-en);
  font-size: 1.05rem;
  line-height: 1.7;
}

/* Three-column "self" body (旅人客栈) — collapses to single column on mobile */
.peek__columns {
  display: flex;
  flex-direction: column;
  gap: var(--space-lg);
  margin-bottom: var(--space-lg);
}

.peek__col-label {
  margin: 0 0 var(--space-sm) 0;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--map-burgundy);
}
.peek__col-label--zh { font-family: var(--font-serif-zh); }
.peek__col-label--en {
  font-family: var(--font-serif-en);
  font-style: italic;
  letter-spacing: 0.02em;
}

.peek__col-list {
  margin: 0;
  padding-left: 1.1em;
  list-style: '· ';
}

.peek__col-item {
  margin-bottom: 6px;
  font-size: 0.92rem;
  line-height: 1.7;
  color: oklch(from var(--ink-black) l c h / 0.85);
}
.peek__col-item--zh { font-family: var(--font-serif-zh); }
.peek__col-item--en {
  font-family: var(--font-serif-en);
  font-size: 0.98rem;
}

.peek__footer {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding-top: var(--space-md);
  border-top: 1px dashed oklch(from var(--map-burgundy) l c h / 0.25);
}

.peek__meta {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--map-burgundy) l c h / 0.6);
}

.peek__link {
  align-self: flex-start;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  color: var(--seal-red);
  text-decoration: none;
  padding-top: 2px;
  transition: opacity 200ms ease-out;
}
.peek__link:hover { opacity: 0.7; }

.peek__seal {
  position: absolute;
  bottom: 16px;
  right: 28px;
  width: 18px;
  height: 18px;
  display: grid;
  place-items: center;
  background: var(--seal-red);
  color: var(--paper-white);
  font-family: var(--font-serif-zh);
  font-size: 0.72rem;
  font-weight: 700;
  line-height: 1;
  user-select: none;
}

/* Mobile drawer: card slides up from the bottom, fills the lower half. */
@media (max-width: 640px) {
  .peek-backdrop {
    align-items: flex-end;
    justify-content: stretch !important;
    padding: 0;
  }
  .peek {
    width: 100%;
    max-height: 70vh;
    overflow-y: auto;
    padding: 24px 22px 30px;
    clip-path: none;
    border: 0;
    border-top: 1px solid oklch(from var(--map-burgundy) l c h / 0.18);
    animation: peek-drawer-in 320ms cubic-bezier(0.22, 1, 0.36, 1);
    transform-origin: bottom center !important;
  }
  @keyframes peek-drawer-in {
    from { opacity: 0; transform: translateY(40px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @media (prefers-reduced-motion: reduce) {
    .peek {
      animation-name: peek-in-reduced;
    }
  }
  .peek__seal {
    bottom: 12px;
    right: 18px;
  }
}
</style>
