// https://nuxt.com/docs/api/configuration/nuxt-config
//
// 主体 + 彩蛋 architecture (PRODUCT.md):
//   - 晚樵庐 = primary site (default landing at /)
//   - 勿忘我 = hidden Map Mode (reachable via /map, footer link, or
//     hover-on-the-corner-scroll easter egg)

export default defineNuxtConfig({
  modules: [
    '@nuxt/content',
    '@nuxtjs/i18n',
  ],

  devtools: { enabled: true },
  compatibilityDate: '2024-04-03',

  app: {
    head: {
      htmlAttrs: { lang: 'zh-CN' },
      title: '晚樵庐',
      meta: [
        { name: 'description', content: '夕丰木的私人记事——晚樵庐主站 + 勿忘我彩蛋。' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'color-scheme', content: 'light' },
      ],
      link: [
        { rel: 'icon', type: 'image/png', href: '/art/signatures/wordmark-zh.png' },
      ],
    },
  },

  css: [
    '~/assets/styles/global.css',
  ],

  i18n: {
    // ZH default per Design Principle #8 "中英对等，中文默认"
    defaultLocale: 'zh',
    locales: [
      { code: 'zh', name: '中文', file: 'zh.json', language: 'zh-CN' },
      { code: 'en', name: 'English', file: 'en.json', language: 'en-US' },
    ],
    strategy: 'no_prefix', // toggle in-place via cookie; URL stays clean
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n-locale',
      redirectOn: 'root',
      fallbackLocale: 'zh',
    },
    bundle: {
      optimizeTranslationDirective: false,
    },
  },

  content: {
    build: {
      markdown: {
        toc: { depth: 2, searchDepth: 2 },
      },
    },
  },

  // SSG: explicit prerender list. The crawler picks up linked routes; this
  // ensures all 5 category pages are generated even if no homepage links to
  // them yet (in case CardStack's <NuxtLink>s are not yet detected).
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: [
        '/',
        '/map',
        '/tech',
        '/life',
        '/interests',
        '/thoughts',
        '/blank',
      ],
    },
  },
})
