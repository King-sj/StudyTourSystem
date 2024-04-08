<script setup lang="ts">
import { ref, reactive, onMounted, watch, nextTick } from "vue";
import axios from "axios";
import type {ICoord,ILocation} from '@/types'
// import AreaCodePoint from 'vue-baidu-map-3x/dist/areaCodePoint.json';
const center = ref({lng: 116.364594, lat: 39.96725} as ICoord);
// const center = ref({ lng: 116.412732, lat: 39.911707 });
const zoom = ref(17)
const keyword = ref()
const polygonPath = ref([
  { lng: 116.412732, lat: 39.911707 },
  { lng: 116.39455, lat: 39.910932 },
  { lng: 116.403461, lat: 39.921336 }
])
const handleReady = ({BMap,map})=>{
  //  对地图进行自定义操作
  console.log(BMap,map)
};
const syncCenterAndZoom = (e:any) => {
  const { lng, lat } = e.target.getCenter();
  zoom.value = e.target.getZoom();
  nextTick(() => {
    center.value.lng = lng;
    center.value.lat = lat;
  })
};
const lushuPoint = ref({
  start: {
    lng: 116.301934,
    lat: 39.977552
  },
  end: {
    lng: 116.508328,
    lat: 39.919141
  },
});
</script>
<template>
  <main>
    <input v-model.number="center.lng">
    <input v-model.number="center.lat">
    <input v-model.number="zoom">
    <!--116.364594,39.96725-->
    <baidu-map class="map" :center="center" :zoom="zoom" @ready="handleReady"
    :scroll-wheel-zoom='true'
    @moving="syncCenterAndZoom"
    @moveend="syncCenterAndZoom"
    @zoomend="syncCenterAndZoom"
    map-type="BMAP_NORMAL_MAP"
    >
    <bm-control :offset="{width: '10px', height: '10px'}">
      <bm-auto-complete v-model="keyword" :sugStyle="{zIndex: 1}">
        <input placeholder="请输入地名关键字" />
      </bm-auto-complete>
    </bm-control>
    <bm-local-search :keyword="keyword" :auto-viewport="true"></bm-local-search>
    <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
    <bm-polyline :path="polygonPath"  :key="polygonPath"></bm-polyline>
  </baidu-map>
  </main>
</template>

<style lang="scss" scoped>
body {
  margin: 0;
  padding: 0;
}
/* 地图容器必须设置宽和高属性 */
.map {
  width: 80vw;
  height: 80vh;
}
</style>