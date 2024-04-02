<script lang="ts" setup>
import { useTimestamp } from '@vueuse/core'
import { useStorage } from '@vueuse/core';
const user =  useStorage("user", null);
</script>
<template>
  This is help page
  {{user}}
</template>
