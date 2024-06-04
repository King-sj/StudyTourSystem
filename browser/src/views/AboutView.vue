<script lang="ts" setup>
import { useApiStore } from '@/apis/useApiStore';
import { onMounted, ref, type Ref } from 'vue';
const server = useApiStore()
const all:Ref<any[]> = ref([])
onMounted(async ()=>{
  var res = await server.get_all_scop()
  all.value = res.data
})

</script>
<template>
  This is about page
  <p v-for="item in all">
    {{item.province + item.city+ item.name}}
  </p>
</template>
