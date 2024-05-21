<script lang="ts" setup>
</script>
<template>
  <baidu-map class="map" style="overflow:auto" center="北京">
    <bm-walking start="百度大厦" end="北京邮电大学西门" :auto-viewport="true" location="北京"></bm-walking>
  </baidu-map>
</template>

<style>
.map {
  width: 100%;
  height: 300px;
}
</style>
