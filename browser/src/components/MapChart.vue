<script setup lang="ts">
import { ref, reactive, onMounted, watch, nextTick } from "vue";
import axios from "axios";
import type { ICoord, ILocation } from '@/types'
// import AreaCodePoint from 'vue-baidu-map-3x/dist/areaCodePoint.json';
const center = defineModel<ICoord>("center")
// const center = ref({ lng: 116.412732, lat: 39.911707 });
const zoom = ref(17)
const keyword = ref()
const polygonPath = ref([
{ lng: 0, lat:0 },
  { lng: 116.412732, lat: 39.911707 },
  { lng: 116.39455, lat: 39.910932 },
  { lng: 116.403461, lat: 39.921336 },
  center.value
])
var geolocation:any;
const handleReady = ({ BMap, map }) => {
  //  对地图进行自定义操作
  console.log(BMap, map)

  geolocation = new BMap.Geolocation();
  // geolocation.getCurrentPosition(function (res:any) {
  //   var currentLocation = [res.longitude, res.latitude]
  //   console.log("当前位置经纬度", currentLocation)
  // });
};
const syncCenterAndZoom = (e: any) => {
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

const location = ref({ lat: 0, lng: 0 } as ICoord)
setInterval(() => {
  // navigator.geolocation.getCurrentPosition(
  //   (position) => {
  //     location.value.lat = position.coords.latitude;
  //     location.value.lng = position.coords.longitude;
  //     // console.log("loc",location.value)
  //   },
  //   (error) => {
  //     console.error("Error Code = " + error.code + " - " + error.message);
  //   },
  //   {
  //     enableHighAccuracy: true,
  //     maximumAge: 30000,
  //     timeout: 12000
  //   }
  // );
  geolocation.getCurrentPosition(function (res:any) {
    location.value.lng = res.longitude
    location.value.lat = res.latitude
    // console.log("当前位置经纬度", location.value)
  });
}, 1000)

</script>
<template>
  <main>
    <!-- <input v-model.number="center.lng">
    <input v-model.number="center.lat"> -->
    <!-- <input v-model.number="zoom"> -->
    <baidu-map class="map" :center="center" :zoom="zoom" @ready="handleReady" :scroll-wheel-zoom='true'
      @moving="syncCenterAndZoom" @moveend="syncCenterAndZoom" @zoomend="syncCenterAndZoom" map-type="BMAP_NORMAL_MAP">
      <!-- <bm-control :offset="{width: '10px', height: '10px'}">
      <bm-auto-complete v-model="keyword" :sugStyle="{zIndex: 1}">
        <input placeholder="请输入地名" />
      </bm-auto-complete>
    </bm-control> -->
      <!-- 目标景区中心的位置 -->
      <bm-marker :position="center" :dragging="true" animation="BMAP_ANIMATION_BOUNCE">
      </bm-marker>
      <!-- 人的位置 -->
      <bm-marker :position="location"
        :icon="{ url: 'http://developer.baidu.com/map/jsdemo/img/fox.gif', size: { width: 300, height: 157 } }">
      </bm-marker>

      <bm-local-search :keyword="keyword" :auto-viewport="true"></bm-local-search>
      <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
      <bm-polyline :path="polygonPath" :key="polygonPath"></bm-polyline>
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
  width: 100%;
  height: 100%;
}
</style>