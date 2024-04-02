<script setup lang="ts">
import { map, latLng, tileLayer } from "leaflet";
import type {MapOptions} from "leaflet"
import { ref, reactive, onMounted, watch } from "vue";
import axios from "axios";
const options: MapOptions = {
  center: latLng(40.731253, -73.996139),
  zoom: 12,
};
onMounted(()=>{
  var mymap = map('map').setView([39.917241237249904, 116.397128], 13);
  tileLayer('http://localhost:8080/styles/basic-preview/512/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(mymap);

  // 监听地图的点击事件
  mymap.on('click', function(e) {
      var lat = e.latlng.lat;
      var lng = e.latlng.lng;
      // 显示点击的坐标
      alert("你点击的坐标是: " + lat + ", " + lng);
      // 你可以在这里添加代码来使用地理编码服务查询更多信息，比如建筑名称
  });
})
</script>
<template>
  <main>
    This is main page
    <div id="map"></div>
  </main>
</template>

<style lang="scss" scoped>
body {
  margin: 0;
  padding: 0;
}
#map {
  height: 500px;
  width: 500px;
  background-color: aqua;
}
</style>