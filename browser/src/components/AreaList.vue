<script lang="ts" setup>
import { ref, computed, onMounted, type Ref } from 'vue';
import { useApiStore } from '@/apis/useApiStore';
const selectArea: any = defineModel<any>('selectArea')

const api = useApiStore()

const loading = ref(false)
var areas: Ref<any[]> = ref([])
const noMore = computed(() => areas.value.length > 0)

const handleLoad = async () => {
  if (noMore.value || loading.value) return

  loading.value = true

  const res = await api.get_all_scop()
  res.data.forEach((ele: any) => {
    areas.value.push(ele)
  });
  console.log(areas)
  loading.value = false
}
handleLoad()

</script>
<template>
  <main>
    <ul v-infinite-scroll="handleLoad" class="infinite-list" style="overflow: auto">
      <li v-for="area in areas" :key="area.name" class="infinite-list-item" @click="selectArea = area"
        :class="{ 'selected': area == selectArea }">
        {{ area.name }}
      </li>
      <div v-if="loading" class="text">
        加载中...
      </div>
      <div v-if="noMore" class="text">
        没有更多了 🤪
      </div>
    </ul>
  </main>
</template>
<style lang="scss" scoped>
.infinite-list {
  height: 100%;
  padding: 0;
  margin: 0;
  list-style: none;

  .infinite-list-item {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px;
    background: var(--el-color-primary-light-9);
    margin: 1px;
    color: var(--el-color-primary);
  }

  .infinite-list-item:hover {
    background-color: greenyellow;
  }

  .selected {
    color: red;
  }
}
</style>