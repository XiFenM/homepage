<script setup lang="ts">
/**
 * Footer easter-egg link — redundant path #2 to /map.
 *
 * Cryptic phrase, no UI affordance beyond the text. Per anti-ref #9 we MUST
 * NOT add icons / arrows / "→" CTA decorations beyond the natural arrow that
 * the text itself ends with.
 */
const { t } = useI18n()
</script>

<template>
  <NuxtLink to="/map" class="footer-egg">
    {{ t('easterEgg.footerLink') }}
  </NuxtLink>
</template>

<style scoped>
.footer-egg {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--ink-black) l c h / 0.6);
  text-decoration: none;
  transition: color 200ms ease-out;
}

.footer-egg:hover,
.footer-egg:focus-visible {
  color: oklch(from var(--seal-red) l c h / 0.8);
}
</style>
