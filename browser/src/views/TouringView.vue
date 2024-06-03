<script setup lang="ts">
import MapChart from '@/components/MapChart.vue';
import AreaList from '@/components/AreaList.vue'
import { ref, watch, type Ref, computed, onMounted, onUnmounted, onBeforeMount, onBeforeUnmount} from 'vue';
import { useApiStore } from '@/apis/useApiStore';
import { type Point } from 'vue3-baidu-map-gl'
import { useScopStore } from '@/stores/scop';
import { ElMessageBox } from 'element-plus';
import router from '@/router';
import { onBeforeRouteLeave } from 'vue-router';
const server = useApiStore()

const dest = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const center = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const polygonPath = ref([dest.value])
const buildingOptions:Ref<{label:string,value:string}[]> = ref([])
const fromBuilding = ref("")
const toBuilding = ref("")
const planPath = async ()=>{
  // TODO
  if (fromBuilding.value == "" || toBuilding.value == "" ) {
    console.log("from or to is null")
    return
  }
  const res = await server.get_routes(
    useScopStore().wannago.name,
    fromBuilding.value,
    toBuilding.value
  )
  console.log("routes", res)

  polygonPath.value = []
  var locs = res.data.split(";")
  locs.forEach((loc:string)=>{
    var location = loc.split(',')
    console.log(location)
    if(location.length == 2)
    polygonPath.value.push({
      lng: Number(location[0]),
      lat: Number(location[1])
    })
  })
  console.log(polygonPath.value)
}
watch(()=>fromBuilding.value,async ()=>{
  await planPath()
})
watch(()=>toBuilding.value,async ()=>{
  await planPath()
})

onMounted(async ()=>{
  var scop = useScopStore().wannago
  var infos = await server.get_scops_info(
    scop.name,
    scop.province,
    scop.city
  )
  // console.log(infos)
  if (!infos.data || infos.data.length != 1) {
    ElMessageBox.alert("景区信息加载错误")
  }
  var info = infos.data[0]
  console.log("info",info)
  useScopStore().buildings = []
  buildingOptions.value = []

  info.buildings.forEach((e:any) => {
    useScopStore().buildings.push(e.name)
    buildingOptions.value.push({
      label:e.name,
      value:e.name
    })
  });

  dest.value.lng = info.lng
  dest.value.lat = info.lat
  center.value.lng = info.lng
  center.value.lat = info.lat

  polygonPath.value = [
    dest.value
  ]
})


// onBeforeRouteLeave(async (to,from,next)=>{
//   // TODO(SJ) 这段代码会报错
//   // console.log(from,to,next)
//   if (to.name != 'grade')
//     router.push({name:"grade"})
//   else next()
// })
</script>
<template>
  <main style="width: 100%;height: 100%;">
    <p class="title">{{useScopStore().wannago.name}}</p>
    <div class="select">
      <el-select
        v-model="fromBuilding"
        placeholder="from"
        size="small"
        style="width: 15rem"
      >
        <el-option
          v-for="item in buildingOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
      <el-select
        v-model="toBuilding"
        placeholder="to"
        size="small"
        style="width: 15rem"
      >
        <el-option
          v-for="item in buildingOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
    </div>
    <MapChart
      :key="useScopStore().wannago.name"
      v-model:dest="dest"
      v-model:center="center"
      v-model:polygon-path="polygonPath"
      class="map">
    </MapChart>
  </main>
  <footer>
    <el-button type="primary" @click="router.push({name:'grade'})">
      结束游学
    </el-button>
  </footer>
</template>

<style lang="scss" scoped>
.area-list {
  min-height: 10%;
}

.map {
  height: 80%;
  width: 100%;
}

.el-button {
  margin-top: 30px;
}
.title{
  text-align: center;
  font-size: large;
  color: aqua;
}
.select{
  text-align: center;
  padding: 1px;
  .el-select{
    padding-left: 20px;
  }
}
</style>