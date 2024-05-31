<script setup lang="ts">
import MapChart from '@/components/MapChart.vue';
import AreaList from '@/components/AreaList.vue'
import { ref, watch, type Ref, computed} from 'vue';
import { useApiStore } from '@/apis/useApiStore';
import { type Point } from 'vue3-baidu-map-gl'

const server = useApiStore()

const selectArea:Ref<any> = ref({name:""})

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
const beginTour = async ()=>{
  const res = await server.get_routes(selectArea.value.name)
  console.log("routes", res)
}
</script>
<template>
  <main style="width: 100%;height: 100%;">
    <AreaList class="area-list" v-model:select-area="selectArea"></AreaList>
    <MapChart
      :key="selectArea.name"
      v-model:dest="dest"
      v-model:center="center"
      v-model:polygon-path="polygonPath"
      class="map"></MapChart>
    <n-space dest>
      <el-button type='primary' @click="beginTour()">Begin Tour</el-button>
    </n-space>
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
</style>