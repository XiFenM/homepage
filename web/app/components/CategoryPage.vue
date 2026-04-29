<script setup lang="ts">
/**
 * Shared category page body. The 5 category routes (`pages/tech.vue` etc.)
 * each render this with their own `category` prop. Centralizing here keeps
 * markup + styling consistent without dynamic-route SSR risk.
 *
 * Real content (Markdown via @nuxt/content) wires in once posts are written;
 * for now this is a "still being written" placeholder.
 */
const props = defineProps<{
  category: 'tech' | 'life' | 'interests' | 'thoughts' | 'blank'
}>()

const { t } = useI18n()
const titleKey = computed(() => `nav.${props.category}`)

useSeoMeta({
  title: () => `${t(titleKey.value)} · ${t('site.name')}`,
})
</script>

<template>
  <article class="category">
    <header class="category__header">
      <NuxtLink to="/" class="category__back">← {{ t('site.name') }}</NuxtLink>
      <h1 class="category__title">{{ t(titleKey) }}</h1>
    </header>

    <section class="category__placeholder">
      <p class="category__hint">还在写。</p>
      <p class="category__hint--en">still being written.</p>
    </section>

    <LanguageToggle class="category__lang" />
  </article>
</template>

<style scoped>
.category {
  position: relative;
  min-height: 100vh;
  background: var(--quiet-paper);
  padding: var(--space-xxl) var(--space-xl);
  color: var(--ink-black);
}

.category__back {
  display: inline-block;
  margin-bottom: var(--space-lg);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--ink-black) l c h / 0.6);
  text-decoration: none;
  transition: color 200ms ease-out;
}
.category__back:hover {
  color: var(--seal-red);
}

.category__title {
  margin: 0;
  font-family: var(--font-heading-zh);
  font-size: clamp(1.4rem, 2.6vw, 1.8rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--ink-black);
}
html[lang="en"] .category__title {
  font-family: var(--font-heading-en);
  font-weight: 600;
  letter-spacing: 0.05em;
}

.category__placeholder {
  margin-top: var(--space-xl);
  max-width: 65ch;
  font-family: var(--font-handwritten);
  font-size: 1.2rem;
  color: oklch(from var(--ink-black) l c h / 0.6);
}

.category__hint--en {
  font-style: italic;
  opacity: 0.5;
  margin-top: var(--space-sm);
}

.category__lang {
  position: absolute;
  top: var(--space-lg);
  right: var(--space-lg);
}
</style>
