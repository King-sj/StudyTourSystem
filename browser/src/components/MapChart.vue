<script setup lang="ts">
import { type Ref,ref, reactive, onMounted, watch, nextTick, computed } from "vue";
import axios from "axios";
import {
  BMap, BNavigation3d, BCityList, BLocation,
  BMarker, BDistrictLayer, DistrictType, useBrowserLocation
} from 'vue3-baidu-map-gl'
import { type MapType, type MapProps, type Point,
} from 'vue3-baidu-map-gl'
import { useApiStore } from "@/apis/useApiStore";
import { ElMessage } from "element-plus";
const props = defineProps<{
  key_nodes: Point[]
}>()
const dest = defineModel<Point>("dest", {
  default:{lat:0,lng:0}
});
const center = defineModel<Point>("center")
const polygonPath = defineModel<Point[]>("polygonPath")
const baiduPlanPath:Ref<Point[]> = ref([])

const server = useApiStore()

const type = ref<MapType>('BMAP_NORMAL_MAP')
const mapStyles = new Map<string, string>(
  [
    ["normal", ""],
    ["cyber", "4a9ef170ea4fc5403268f8ae1adbecff"],
  ]
)
const mapStyle = ref(mapStyles.get("normal"))
const zoom = ref(17)

const map = ref()
const { get, location, isLoading, isError, status } = useBrowserLocation({
  enableHighAccuracy:true,
  maximumAge:2000
}, () => {
  map.value.resetCenter()
})

watch(()=>location.value,async()=>{
  console.log("location change", location.value)
  center.value = location.value?.point;
  if(location.value?.point) {
    const res = await server.get_routes_by_baidu(
      location.value.point.lat,location.value.point.lng,
      dest.value.lat,dest.value.lng
    )
    if(!res.data.status) {
      ElMessage("获取驾车路线失败")
    }
    const paths = res.data.res.step
    console.log("baidu plan",res)
    baiduPlanPath.value = []
    paths.forEach((path:any)=>{
      var locations = path['path'].split(';')
      locations.forEach((loc:string)=>{
        var location = loc.split(',')
        baiduPlanPath.value.push({
          lng: Number(location[0]),
          lat: Number(location[1])
        })
      })
    })
    console.log("baidu plan res",baiduPlanPath.value)
  }

})


const syncCenterAndZoom = (e: any) => {
  const { lng, lat } = e.target.getCenter();
  zoom.value = e.target.getZoom();
  nextTick(() => {
    if (center.value) {
      center.value.lng = lng;
      center.value.lat = lat;
    }
  })
};



</script>
<template>
  <main>
    <div class="state" v-if="!isLoading && !isError">
      <span>
        城市 - {{ location.address?.province }}-{{ location.address?.city }}-{{ location.address?.district }}-{{
          location.address?.street
        }}
      </span>
      <span>纬度 : {{ location.point?.lat }}</span>
      <span>经度 : {{ location.point?.lng }}</span>
      <span>定位精度 : {{ location.accuracy }}m</span>
    </div>
    <div class="state" v-else-if="isError">出错了，{{ status }}</div>
    <div class="state" v-else>定位中...</div>
    <BMap
      ref="map" @initd="get"
      :heading="64.5" :tilt="73" :center="center" :zoom="zoom" :mapType="type" :enableDragging="true"
      :enableInertialDragging="true" :enableScrollWheelZoom="true" :enableContinuousZoom="true"
      :enableDoubleClickZoom="true" :enableKeyboard="true" :enablePinchToZoom="true" :enableTraffic="true"
      :displayOptions="{
        indoor: true
      }"
      :mapStyleId="mapStyle"
    >
    <BPolyline
      :path="baiduPlanPath.length == 0 ? [location.point || {},...polygonPath]: [...baiduPlanPath,...polygonPath]"
      stroke-color="#0ff"
      :stroke-opacity="1"
      :stroke-weight="8"
      :geodesic="true"
      strokeStyle="dashed"
    />
      <!-- 目标景区中心的位置 -->
      <BMarker icon="end" :position="
        polygonPath?.at(polygonPath.length-1) || dest
      " v-if="props.key_nodes.length==0"></BMarker>
      <BMarker :position="location.point || {}" icon="start">
      </BMarker>
      <BMarker :position="loc" v-for="loc in props.key_nodes" icon="simple_blue"></BMarker>
      <BNavigation3d />
      <BLocation />
      <template #loading>
        <div class="spinner">
          <div class="double-bounce1"></div>
          <div class="double-bounce2"></div>
        </div>
      </template>
    </BMap>
  </main>
</template>

<style lang="scss" scoped>
.spinner {
  width: 60px;
  height: 60px;

  position: relative;
  margin: 100px auto;
}

.double-bounce1,
.double-bounce2 {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #42b883;
  opacity: 0.6;
  position: absolute;
  top: 0;
  left: 0;

  -webkit-animation: bounce 2s infinite ease-in-out;
  animation: bounce 2s infinite ease-in-out;
}

.double-bounce2 {
  -webkit-animation-delay: -1s;
  animation-delay: -1s;
}

@-webkit-keyframes bounce {

  0%,
  100% {
    -webkit-transform: scale(0);
  }

  50% {
    -webkit-transform: scale(1);
  }
}

@keyframes bounce {

  0%,
  100% {
    transform: scale(0);
    -webkit-transform: scale(0);
  }

  50% {
    transform: scale(1);
    -webkit-transform: scale(1);
  }
}
.state {
  margin-top: 15px;
}
.state span {
  margin-right: 25px;
}
</style>