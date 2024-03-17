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
  var mymap = map('map').setView([116.3512345449219, 39.96383372433723], 13);
  tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
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
const name = ref('北京邮电大学')
const res = ref('result')
watch(name, ()=>{
  axios.get('https://photon.komoot.io/api/?q=柏林')
  .then(response => {
    console.log(response);
    return response.data
  })
  .then(data => {
    // 假设我们只关心第一个搜索结果
    var firstResult = data.features[0];
    var placeName = firstResult.properties.name; // 地点名称
    var coordinates = firstResult.geometry.coordinates; // 坐标，数组形式 [经度, 纬度]
    // alert('地点名称:'+ name + coordinates);
    res.value = `地点名称: ${placeName}, 坐标: ${coordinates.join(', ')}`; // 更新res的值
    console.log(res)
  })
  .catch(error => console.log('请求失败', error));
})
</script>
<template>
  <main>
    This is main page
    <div id="map"></div>
    {{name}}:{{res}}
    <input v-model="name">
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