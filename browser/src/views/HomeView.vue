<script setup lang="ts">
import AreaList from '@/components/AreaList.vue'
import { ref, watch, type Ref, computed, onMounted } from 'vue';
import { useApiStore } from '@/apis/useApiStore';
import { type Point } from 'vue3-baidu-map-gl'
import { useRouter } from 'vue-router';
import ScopCard from "@/components/ScopCard.vue"
import { ElMessage, ElMessageBox } from 'element-plus';
import { useScopStore } from '@/stores/scop';
import { type ScopBasicInfo } from '@/types';

import pca_json from '../assets/pca.json'

const province_option: Ref<{ value: string, label: string }[]> = ref([])
const province_select = ref("")
const city_option: Ref<{ value: string, label: string }[]> = ref([])
const city_select = ref("")
const scop_name = ref("")
const scops = ref()
const hot_scops = ref()
const is_loading = ref(false)
const filteredScops = computed(()=>{
  console.log("scops change", scops.value, hot_scops.value)
  if (scops.value != undefined) {
    return scops.value
  } else if (hot_scops.value != undefined) {
    return hot_scops.value.data
  } else {
    return []
  }
})
const flash_scops = async ()=>{
  is_loading.value = true
  var res = await server.get_scops_info(scop_name.value,province_select.value, city_select.value)
  scops.value = res.data
  is_loading.value = false
}
watch(()=>province_select.value, async()=>{await flash_scops()})
watch(()=>city_select.value, async()=>{await flash_scops()})
watch(()=>scop_name.value, async()=>{await flash_scops()})

for (let province in pca_json) {
  province_option.value.push({
    label: province,
    value: province
  })
}
watch(() => province_select.value, () => {
  city_option.value = []
  let provinceKey: keyof typeof pca_json = province_select.value as any;
  for (let city in pca_json[provinceKey]) {
    city_option.value.push({
      label: city,
      value: city
    })
  }
})
const server = useApiStore()
const router = useRouter()



const selectArea: Ref<any> = ref({ name: "" })

const dest = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const center = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const polygonPath = ref([dest.value])
watch(() => selectArea.value, (v) => {
  console.log("select change", selectArea.value)
  if (selectArea.value) {
    dest.value.lng = selectArea.value.lng
    dest.value.lat = selectArea.value.lat
    center.value.lng = selectArea.value.lng
    center.value.lat = selectArea.value.lat

    polygonPath.value = [
      dest.value
    ]
  }
})
const handle_select_card = (scop: ScopBasicInfo) => {
  ElMessageBox.confirm(
    `确定去${scop.name}吗?`,
    '',
    {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      type: 'info',
    }
  )
    .then(() => {
      console.log("wannago", scop)
      useScopStore().wannago = scop
      console.log("wannagoed", scop)
      router.push({ name: "touring" })
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '已取消',
      })
    })
}
onMounted(async () => {
  hot_scops.value = await server.get_hot_scop()
  console.log("hot", hot_scops.value)
})
</script>
<template>
  <main style="width: 100%;height: 100%;">
    <h1 style="text-align: center;color: aquamarine;" v-if="is_loading">加载中...</h1>

    <p id="hot-scop-title" v-if="province_select.length + city_select.length + scop_name.length == 0">热门景点</p>
    <div class="area-select">
      <el-select v-model="province_select" placeholder="province" size="large" style="width: 240px">
        <el-option v-for="item in province_option" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
      <el-select v-model="city_select" placeholder="city" size="large" style="width: 240px">
        <el-option v-for="item in city_option" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
      <el-input placeholder="景区名" v-model="scop_name" style="width: 240px" />
    </div>
    <div class="cities-view">
      <h1 style="text-align: center;color: aquamarine;" v-if="filteredScops.length == 0 && !is_loading">此地暂无数据哦(⊙o⊙)</h1>
      <el-scrollbar>
        <div class="card-container">
          <ScopCard

            v-for="scop in filteredScops"
            :scop="scop"
            :key="scop['name']" :name="scop['name']"
            :province="scop['province']" :city="scop['city']" class="city-card" :visited_person="scop['visited_person']"
            :score="scop['score']" @select-card="handle_select_card" />
        </div>
      </el-scrollbar>
    </div>
  </main>
</template>

<style lang="scss" scoped>
.area-list {
  min-height: 10%;
}

.map {
  height: 70%;
  width: 100%;
}

.el-button {
  margin-top: 30px;
}

#hot-scop-title {
  text-align: center;
  color: red;
  font-size: 1.5rem;
}

.cities-view {
  margin: 0;
  padding: 0.1rem;
  height: 50%;

  // background-color: red;
  .card-container {
    display: flex;
    /* 启用弹性布局 */
    flex-wrap: wrap;
    /* 允许子元素换行 */
    justify-content:flex-start;

    /* 子元素在主轴上的对齐方式 */
    .city-card {
      width: 31%;
      margin: 0.5rem;
      padding: 0;
    }
  }
}

.area-select {
  text-align: center;

  * {
    margin-left: 1rem;
    margin-right: 1rem;
  }
}
</style>