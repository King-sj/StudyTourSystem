<script setup lang="ts">
import { ref, reactive, onMounted, watch, nextTick, computed } from "vue";
import axios from "axios";
import type { ICoord, ILocation } from '@/types'

const dest = defineModel<ICoord>("dest")
const center = defineModel<ICoord>("center")
const polygonPath = defineModel("polygonPath")
const location = defineModel<ICoord>("location")
// const dest = ref({ lng: 116.364594, lat: 39.96725 } as ICoord);
// const center = ref({ lng: 116.364594, lat: 39.96725 } as ICoord);
// const location = ref({ lng: 116.364594, lat: 39.96725 } as ICoord);
// const polygonPath = ref([location.value,dest.value])

const zoom = ref(17)
const keyword = ref()


var geolocation:any;
const handleReady = ({ BMap, map }) => {
  //  对地图进行自定义操作
  console.log(BMap, map)
  // TODO(SJ) 添加下面这段会一直报错
  // geolocation = new BMap.Geolocation();
};
const syncCenterAndZoom = (e: any) => {
  const { lng, lat } = e.target.getCenter();
  zoom.value = e.target.getZoom();
  nextTick(() => {
    if(center.value) {
      center.value.lng = lng;
      center.value.lat = lat;
    }
  })
};

onMounted(()=>{
  setInterval(() => {
  geolocation?.getCurrentPosition(function (res:any) {
    if (location.value==undefined || res == null)return
    location.value.lng = res.longitude
    location.value.lat = res.latitude
    // console.log("当前位置经纬度", location.value)
  });
  }, 1000)
})
const click_map = (e:any) => {
  console.log("click location" , e.point)
}
</script>
<template>
  <main>
    <!-- <input v-model.number="center.lng">
    <input v-model.number="center.lat"> -->
    <!-- <input v-model.number="zoom"> -->
    <baidu-map class="map" :center="center" :zoom="zoom" @ready="handleReady"
      :scroll-wheel-zoom='true'
      @moving="syncCenterAndZoom" @moveend="syncCenterAndZoom" @zoomend="syncCenterAndZoom"
      map-type="BMAP_NORMAL_MAP"
      @click="click_map"
    >
      <!-- <bm-control :offset="{width: '10px', height: '10px'}">
      <bm-auto-complete v-model="keyword" :sugStyle="{zIndex: 1}">
        <input placeholder="请输入地名" />
      </bm-auto-complete>
    </bm-control> -->
      <!-- 目标景区中心的位置 -->
      <bm-marker :position="dest" :dragging="true" animation="BMAP_ANIMATION_BOUNCE"
      >
      </bm-marker>
      <!-- 人的位置 -->
      <bm-marker :position="location"
        :icon="{ url: 'http://developer.baidu.com/map/jsdemo/img/fox.gif', size: { width: 300, height: 157 } }">
      </bm-marker>

      <!-- <bm-local-search :keyword="keyword" :auto-viewport="true"></bm-local-search> -->

      <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true" :autoLocation="true"></bm-geolocation>

      <bm-polyline :path="polygonPath" :key="zoom"
      ></bm-polyline>
      <bm-walking :start="location" :end="dest" :auto-viewport="true" location="北京"></bm-walking>
    </baidu-map>
  </main>
</template>

<style lang="scss" scoped>
/* 地图容器必须设置宽和高属性 */
.map {
  width: 100%;
  height: 100%;
}
</style>