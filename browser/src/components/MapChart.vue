<script lang="ts">
// import { defineComponent, onMounted, ref } from 'vue';
// import * as echarts from 'echarts/core';
// import { GeoComponent, TooltipComponent } from 'echarts/components';
// import { MapChart } from 'echarts/charts';
// import { CanvasRenderer } from 'echarts/renderers';
// // import ChinaMapData from './path/to/china.json'; // 确保你有中国地图的JSON

// echarts.use([GeoComponent, TooltipComponent, MapChart, CanvasRenderer]);

// const name = ref('MapChart');
// const chart = ref<HTMLElement>();

// onMounted(() => {
//   const myChart = echarts.init(chart.value!);

//   echarts.registerMap('china', ChinaMapData);

//   myChart.setOption({
//     tooltip: {
//       trigger: 'item',
//       formatter: '{b}'
//     },
//     series: [
//       {
//         name: '中国',
//         type: 'map',
//         map: 'china',
//         label: {
//           show: true
//         },
//         data: [
//           // 示例数据
//           { name: '北京', value: Math.round(Math.random() * 1000) },
//           { name: '天津', value: Math.round(Math.random() * 1000) }
//           // 更多省份数据...
//         ]
//       }
//     ]
//   });
// });
</script>

<template>
  <div ref="chart" style="width: 600px; height: 400px;"></div>
</template>