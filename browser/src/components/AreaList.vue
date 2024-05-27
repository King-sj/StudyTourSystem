<script lang="ts" setup>
import { ref, computed, onMounted, type Ref, watch } from 'vue';
import { useApiStore } from '@/apis/useApiStore';
const selectArea: any = defineModel<any>('selectArea')

const api = useApiStore()

const loading = ref(false)
var areas: Ref<any[]> = ref([])
const noMore = computed(() => areas.value.length > 100)
const options:Ref<any[]> = ref([]);
const handleLoad = async () => {
  console.log("begin load area data")
  if (noMore.value || loading.value) return

  loading.value = true

  const res = await api.get_all_scop()
  res.data.forEach((ele: any) => {
    areas.value.push(ele)
  });
  console.log("areas", areas.value)

  areas.value.forEach((ele,idx)=>{
    options.value.push(
      {
        label: ele.name,
        value: idx,
      }
    )
  })
  loading.value = false
}
handleLoad()
const val =  ref(null)
watch(() => val.value, () => {
  console.log("select area change", val.value)
  if(val.value != null)
    selectArea.value = areas.value[val.value]
})
</script>
<template>
  <main>
    <n-space vertical>
      <n-select v-model:value="val" :options="options" />
    </n-space>
  </main>
</template>
<style lang="scss" scoped>
</style>