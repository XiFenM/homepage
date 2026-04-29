<script setup lang="ts">
/**
 * Card stack — primary navigation in the晚樵庐 hero.
 *
 * 5 cards, 5 routes. Each card's CLICK region is a rectangle positioned over
 * the corresponding card's visible top edge (where its motif sits).
 *
 * Hover / focus per DESIGN.md:
 *   - Outline 1px ink-black dashed (subtle visual feedback)
 *   - filter: brightness(1.08) on the underlying card area
 *   - Handwritten label slides in above the region
 *   - **No translateY** — The No-Levitation Rule
 *
 * Region coordinates are PERCENTAGES of the card-stack container. They are
 * tuned by inspecting the live S5C image. To refine: open DevTools, edit the
 * inline styles on `.card-stack__hit`, copy back into the `cards` array.
 */
const { t } = useI18n()

interface Card {
  route: string
  label: string // i18n key
  motif: string // for code comments only
  region: { top: string; left: string; width: string; height: string }
}

const cards: Card[] = [
  // top of fan — mountain motif (山水 = travel / life)
  { route: '/life',      label: 'nav.life',
    motif: '山水',
    region: { top: '5%',  left: '24%', width: '50%', height: '20%' } },
  // 2nd — flower stem (花草 = thoughts / daily)
  { route: '/thoughts',  label: 'nav.thoughts',
    motif: '花草',
    region: { top: '22%', left: '38%', width: '42%', height: '14%' } },
  // 3rd — three-dot constellation (星点 = interests)
  { route: '/interests', label: 'nav.interests',
    motif: '星点',
    region: { top: '36%', left: '50%', width: '36%', height: '14%' } },
  // 4th — cinnabar seal (章 = tech, "stamped serious work")
  { route: '/tech',      label: 'nav.tech',
    motif: '朱砂章',
    region: { top: '50%', left: '58%', width: '32%', height: '14%' } },
  // 5th — blank ("blank space, what's not yet written")
  { route: '/blank',     label: 'nav.blank',
    motif: '空白',
    region: { top: '64%', left: '62%', width: '30%', height: '15%' } },
]
</script>

<template>
  <div class="card-stack">
    <img
      class="card-stack__bg"
      src="/art/homepage/card-stack.png"
      :alt="t('site.tagline')"
      loading="eager"
    />
    <NuxtLink
      v-for="card in cards"
      :key="card.route"
      :to="card.route"
      class="card-stack__hit"
      :aria-label="t(card.label)"
      :style="card.region"
    >
      <span class="card-stack__label">{{ t(card.label) }}</span>
    </NuxtLink>
  </div>
</template>

<style scoped>
.card-stack {
  position: relative;
  width: clamp(360px, 42vw, 640px);
  aspect-ratio: 5 / 4;
}

.card-stack__bg {
  width: 100%;
  height: 100%;
  object-fit: contain;
  pointer-events: none;
}

.card-stack__hit {
  position: absolute;
  display: block;
  text-decoration: none;
  border-radius: var(--rounded-sticker);
  outline: 1px dashed transparent;
  outline-offset: -2px;
  transition: outline-color 200ms ease-out, filter 200ms ease-out,
              background-color 200ms ease-out;
}

.card-stack__hit:hover,
.card-stack__hit:focus-visible {
  outline-color: oklch(from var(--ink-black) l c h / 0.5);
  background-color: oklch(from var(--quiet-lime) l c h / 0.12);
  filter: brightness(1.05);
}

.card-stack__label {
  position: absolute;
  top: 100%;
  left: 0;
  margin-top: 6px;
  padding: 2px 10px;
  font-family: var(--font-handwritten);
  font-size: 1.05rem;
  color: var(--ink-black);
  background: oklch(from var(--paper-white) l c h / 0.92);
  border-radius: var(--rounded-sticker);
  white-space: nowrap;
  opacity: 0;
  transform: translateY(-4px);
  pointer-events: none;
  transition: opacity 220ms ease-out, transform 220ms ease-out;
}

.card-stack__hit:hover .card-stack__label,
.card-stack__hit:focus-visible .card-stack__label {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  .card-stack__hit:hover,
  .card-stack__hit:focus-visible {
    filter: none;
  }
}
</style>
