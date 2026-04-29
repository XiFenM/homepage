<script setup lang="ts">
/**
 * Single-post body. Each `pages/<category>/[slug].vue` is a thin shell that
 * passes its category and slug into this component — keeping the dynamic
 * surface narrow (only `[slug]` is dynamic, never the category) so prerender
 * + i18n + 404 behave predictably.
 */
const props = defineProps<{
  category: 'tech' | 'life' | 'interests' | 'thoughts'
  slug: string
}>()

const { t, locale } = useI18n()

const { data: post } = await useAsyncData(
  `post-${props.category}-${props.slug}`,
  async () => {
    const inLocale = await queryCollection('posts')
      .where('category', '=', props.category)
      .where('slug', '=', props.slug)
      .where('lang', '=', locale.value)
      .first()
    if (inLocale) return inLocale

    // Graceful fallback: post exists in the other language but not yet
    // translated — render that instead of 404 so the URL still resolves.
    const otherLang = locale.value === 'zh' ? 'en' : 'zh'
    return queryCollection('posts')
      .where('category', '=', props.category)
      .where('slug', '=', props.slug)
      .where('lang', '=', otherLang)
      .first()
  },
  { watch: [locale] },
)

if (!post.value) {
  throw createError({ statusCode: 404, statusMessage: 'Post not found', fatal: true })
}

useSeoMeta({
  title: () => `${post.value!.title} · ${t('site.name')}`,
  description: () => post.value!.summary,
})

function formatDate(iso: string): string {
  return iso.replaceAll('-', '.')
}

const isFallback = computed(() => post.value && post.value.lang !== locale.value)
const categoryLabelKey = computed(() => `nav.${props.category}`)
</script>

<template>
  <article v-if="post" class="post">
    <header class="post__header">
      <NuxtLink :to="`/${category}`" class="post__back">
        ← {{ t(categoryLabelKey) }}
      </NuxtLink>
      <p v-if="isFallback" class="post__fallback-note">
        {{ post.lang === 'zh' ? '（暂未翻译，原文为中文）' : '(not yet translated — original is in English)' }}
      </p>
      <h1 class="post__title">{{ post.title }}</h1>
      <div class="post__meta">
        <time class="post__date">{{ t('post.writtenOn') }} {{ formatDate(post.date) }}</time>
        <span v-if="post.tags?.length" class="post__tags">
          <span v-for="tag in post.tags" :key="tag" class="post__tag">#{{ tag }}</span>
        </span>
      </div>
    </header>

    <ContentRenderer :value="post" class="post__body prose" />

    <LanguageToggle class="post__lang" />
  </article>
</template>

<style scoped>
.post {
  position: relative;
  min-height: 100vh;
  background: var(--quiet-paper);
  padding: var(--space-xxl) var(--space-xl);
  color: var(--ink-black);
}

.post__back {
  display: inline-block;
  margin-bottom: var(--space-lg);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--ink-black) l c h / 0.6);
  text-decoration: none;
  transition: color 200ms ease-out;
}
.post__back:hover {
  color: var(--seal-red);
}

.post__fallback-note {
  margin: 0 0 var(--space-sm) 0;
  font-family: var(--font-handwritten);
  font-size: 0.95rem;
  color: oklch(from var(--ink-black) l c h / 0.5);
}

.post__title {
  margin: 0 0 var(--space-md) 0;
  max-width: 22ch;
  font-family: var(--font-heading-zh);
  font-size: clamp(1.6rem, 3vw, 2.2rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.25;
}
html[lang="en"] .post__title {
  font-family: var(--font-serif-en);
  font-weight: 600;
  letter-spacing: 0;
}

.post__meta {
  display: flex;
  gap: var(--space-md);
  align-items: baseline;
  margin-bottom: var(--space-xl);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  color: oklch(from var(--ink-black) l c h / 0.55);
}

.post__tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.post__tag {
  color: oklch(from var(--quiet-lime-deep) l c h / 0.85);
}

.post__body {
  max-width: 65ch;
}

.post__lang {
  position: absolute;
  top: var(--space-lg);
  right: var(--space-lg);
}

/* Prose styles for markdown content rendered by <ContentRenderer>.
   Honors DESIGN.md typography: serif body in zh & en, no shadows, ink-black
   on quiet-paper, seal-red accents only on links. */
.prose :deep(h2) {
  margin: var(--space-xl) 0 var(--space-md) 0;
  font-family: var(--font-heading-zh);
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--ink-black);
}
html[lang="en"] .prose :deep(h2) {
  font-family: var(--font-serif-en);
  font-weight: 600;
  font-style: italic;
}

.prose :deep(h3) {
  margin: var(--space-lg) 0 var(--space-sm) 0;
  font-family: var(--font-heading-zh);
  font-size: 1rem;
  font-weight: 600;
}

.prose :deep(p) {
  margin: 0 0 var(--space-md) 0;
  font-family: var(--font-serif-zh);
  font-size: 1rem;
  line-height: 1.85;
  color: var(--ink-black);
}
html[lang="en"] .prose :deep(p) {
  font-family: var(--font-serif-en);
  font-size: 1.05rem;
  line-height: 1.75;
}

.prose :deep(strong) {
  font-weight: 700;
  color: var(--ink-black);
}

.prose :deep(em) {
  font-style: italic;
  color: oklch(from var(--ink-black) l c h / 0.85);
}

.prose :deep(a) {
  color: var(--seal-red);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
  transition: opacity 200ms ease-out;
}
.prose :deep(a:hover) {
  opacity: 0.7;
}

.prose :deep(ul),
.prose :deep(ol) {
  margin: 0 0 var(--space-md) 0;
  padding-left: 1.4em;
  font-family: var(--font-serif-zh);
  line-height: 1.85;
}
html[lang="en"] .prose :deep(ul),
html[lang="en"] .prose :deep(ol) {
  font-family: var(--font-serif-en);
}

.prose :deep(li) {
  margin: 0 0 var(--space-xs) 0;
}

.prose :deep(blockquote) {
  margin: var(--space-md) 0;
  padding: 0 0 0 var(--space-md);
  border-left: 2px solid oklch(from var(--quiet-lime-deep) l c h / 0.6);
  color: oklch(from var(--ink-black) l c h / 0.75);
  font-style: italic;
}

.prose :deep(code) {
  padding: 1px 6px;
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: oklch(from var(--quiet-mist) l c h / 0.7);
  border-radius: var(--rounded-sticker);
}

.prose :deep(pre) {
  margin: var(--space-md) 0;
  padding: var(--space-md);
  font-family: var(--font-mono);
  font-size: 0.85rem;
  line-height: 1.6;
  background: oklch(from var(--quiet-mist) l c h / 0.5);
  border-radius: var(--rounded-sticker);
  overflow-x: auto;
}
.prose :deep(pre code) {
  padding: 0;
  background: transparent;
}

.prose :deep(hr) {
  margin: var(--space-xl) 0;
  border: none;
  border-top: 1px dashed oklch(from var(--ink-black) l c h / 0.18);
}
</style>
