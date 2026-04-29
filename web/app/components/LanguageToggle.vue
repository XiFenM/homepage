<script setup lang="ts">
/**
 * Language toggle.
 *
 * Per DESIGN.md §5 Language Toggle:
 *   - Two adjacent rounded-sticker tags 「中 / EN」
 *   - Default: paper-white bg + ink-black text
 *   - Active: seal-red bg + paper-white text (small seal semantics)
 *   - Toggle in-place; preserve current page position (no navigation reload)
 */
const { locale, setLocale } = useI18n()
</script>

<template>
  <div class="lang-toggle">
    <button
      type="button"
      class="lang-toggle__btn"
      :class="{ 'lang-toggle__btn--active': locale === 'zh' }"
      :aria-pressed="locale === 'zh'"
      @click="setLocale('zh')"
    >
      中
    </button>
    <button
      type="button"
      class="lang-toggle__btn"
      :class="{ 'lang-toggle__btn--active': locale === 'en' }"
      :aria-pressed="locale === 'en'"
      @click="setLocale('en')"
    >
      EN
    </button>
  </div>
</template>

<style scoped>
.lang-toggle {
  display: inline-flex;
  gap: 4px;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
}

.lang-toggle__btn {
  padding: 4px 10px;
  background: var(--paper-white);
  color: var(--ink-black);
  border-radius: var(--rounded-sticker);
  cursor: pointer;
  transition: background-color 200ms ease-out, color 200ms ease-out;
}

.lang-toggle__btn--active {
  background: var(--seal-red);
  color: var(--paper-white);
}
</style>
