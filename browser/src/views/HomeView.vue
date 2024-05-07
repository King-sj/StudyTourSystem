<script setup lang="ts">
import MapChart from '@/components/MapChart.vue';
import AreaList from '@/components/AreaList.vue'
import { ref, watch, type Ref } from 'vue';
import { type ICoord } from '@/types';
const selectArea = ref()
const center = ref({ lng: 116.364594, lat: 39.96725 } as ICoord);
watch(() => selectArea.value, (v) => {
  console.log("select change")
  if (selectArea.value) {
    center.value.lng = selectArea.value.lng
    center.value.lat = selectArea.value.lat
  }
})

</script>
<template>
  <main style="width: 100%;height: 100%;">
    <AreaList class="area-list" v-model:select-area="selectArea"></AreaList>
    <MapChart v-if="true" v-model:center="center" class="map"></MapChart>
    <n-space center>
      <el-button type='primary'>Begin Tour</el-button>
    </n-space>
  </main>
</template>

<style lang="scss" scoped>
.area-list {
  min-height: 10vh;
}

.map {
  height: 70%;
  width: 100%;
}

.el-button {
  margin-top: 30px;
}
</style>