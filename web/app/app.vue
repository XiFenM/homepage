<script setup lang="ts">
// Root component. Updates html lang attr in sync with i18n locale, so that
// CSS [lang="en"] selectors and assistive tech are correct on every change.
const { locale, locales } = useI18n()
const localeMeta = computed(() =>
  (locales.value as Array<{ code: string; language?: string }>).find(
    (l) => l.code === locale.value,
  ),
)
useHead({
  htmlAttrs: () => ({
    lang: localeMeta.value?.language ?? 'zh-CN',
  }),
})
</script>

<template>
  <NuxtRouteAnnouncer />
  <NuxtPage />
</template>
