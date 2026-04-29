import { defineContentConfig, defineCollection, z } from '@nuxt/content'

/**
 * One collection holds all posts. Language and category are frontmatter fields,
 * not URL segments — so URLs stay clean (`/tech/hello`, no `/zh/` prefix) and
 * the active locale picks which translation renders.
 *
 * On-disk path: content/<category>/<slug>.<lang>.md
 * URL: /<category>/<slug>  — looked up by frontmatter (category, slug, lang)
 */
export default defineContentConfig({
  collections: {
    posts: defineCollection({
      type: 'page',
      source: '**/*.md',
      schema: z.object({
        title: z.string(),
        date: z.string(),
        category: z.enum(['tech', 'life', 'interests', 'thoughts']),
        lang: z.enum(['zh', 'en']),
        slug: z.string(),
        summary: z.string().optional(),
        tags: z.array(z.string()).optional(),
      }),
    }),
  },
})
