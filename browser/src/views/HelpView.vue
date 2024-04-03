<script lang="ts" setup>
import { useTimestamp } from '@vueuse/core'
import { useUserStore } from '@/stores/user';
const userData = useUserStore().userData
</script>
<template>
  This is help page
  {{userData}}
</template>
