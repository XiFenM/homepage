<script setup lang="ts">
const route = useRoute()
const slug = computed(() => String(route.params.slug))
</script>

<template>
  <PostPage category="tech" :slug="slug" />
</template>
