<script setup lang="ts">
/**
 * Category landing page — list view of posts in one category, filtered by the
 * active locale. Rendered by the 5 static category routes
 * (`pages/{tech,life,interests,thoughts,blank}.vue`).
 *
 * 'blank' stays a wordless placeholder per the "未写就" intent in PRODUCT.md;
 * the other 4 categories query @nuxt/content for posts and render a list.
 */
const props = defineProps<{
  category: 'tech' | 'life' | 'interests' | 'thoughts' | 'blank'
}>()

const { t, locale } = useI18n()
const titleKey = computed(() => `nav.${props.category}`)

useSeoMeta({
  title: () => `${t(titleKey.value)} · ${t('site.name')}`,
})

const isBlank = computed(() => props.category === 'blank')

// Query posts for this category in the active locale. Watch `locale` so the
// list refreshes when the user toggles 中/EN.
const { data: posts } = await useAsyncData(
  `posts-${props.category}`,
  () => {
    if (props.category === 'blank') return Promise.resolve([])
    return queryCollection('posts')
      .where('category', '=', props.category)
      .where('lang', '=', locale.value)
      .order('date', 'DESC')
      .all()
  },
  { watch: [locale] },
)

function formatDate(iso: string): string {
  // ISO yyyy-mm-dd → "2026.04.20" (mono-feel, locale-agnostic)
  return iso.replaceAll('-', '.')
}
</script>

<template>
  <article class="category">
    <header class="category__header">
      <NuxtLink to="/" class="category__back">← {{ t('site.name') }}</NuxtLink>
      <h1 class="category__title">{{ t(titleKey) }}</h1>
    </header>

    <section v-if="isBlank" class="category__placeholder">
      <p class="category__hint">{{ t('post.blankPlaceholder') }}</p>
      <p class="category__hint--en">{{ t('post.blankPlaceholderEn') }}</p>
    </section>

    <section v-else-if="posts && posts.length > 0" class="category__list">
      <NuxtLink
        v-for="post in posts"
        :key="post.slug"
        :to="`/${category}/${post.slug}`"
        class="post-card"
      >
        <div class="post-card__meta">
          <time class="post-card__date">{{ formatDate(post.date) }}</time>
          <span v-if="post.tags?.length" class="post-card__tags">
            <span v-for="tag in post.tags" :key="tag" class="post-card__tag">
              #{{ tag }}
            </span>
          </span>
        </div>
        <h2 class="post-card__title">{{ post.title }}</h2>
        <p v-if="post.summary" class="post-card__summary">{{ post.summary }}</p>
        <span class="post-card__more">{{ t('post.readMore') }}</span>
      </NuxtLink>
    </section>

    <section v-else class="category__placeholder">
      <p class="category__hint">{{ t('post.noPostsYet') }}</p>
      <p class="category__hint--en">{{ t('post.noPostsYetEn') }}</p>
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
  margin: 0 0 var(--space-xl) 0;
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

.category__list {
  display: flex;
  flex-direction: column;
  gap: var(--space-xl);
  max-width: 65ch;
}

.post-card {
  display: block;
  padding: var(--space-md) 0;
  text-decoration: none;
  color: var(--ink-black);
  border-top: 1px solid oklch(from var(--ink-black) l c h / 0.12);
  transition: background-color 200ms ease-out;
}
.post-card:hover {
  background-color: oklch(from var(--quiet-lime) l c h / 0.08);
}

.post-card__meta {
  display: flex;
  gap: var(--space-md);
  align-items: baseline;
  margin-bottom: var(--space-sm);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  color: oklch(from var(--ink-black) l c h / 0.55);
}

.post-card__tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.post-card__tag {
  color: oklch(from var(--quiet-lime-deep) l c h / 0.85);
}

.post-card__title {
  margin: 0 0 var(--space-sm) 0;
  font-family: var(--font-heading-zh);
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}
html[lang="en"] .post-card__title {
  font-family: var(--font-serif-en);
  font-weight: 500;
  letter-spacing: 0;
}

.post-card__summary {
  margin: 0 0 var(--space-sm) 0;
  font-family: var(--font-serif-zh);
  font-size: 0.95rem;
  line-height: 1.7;
  color: oklch(from var(--ink-black) l c h / 0.75);
}
html[lang="en"] .post-card__summary {
  font-family: var(--font-serif-en);
  font-style: italic;
}

.post-card__more {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--seal-red) l c h / 0.85);
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
