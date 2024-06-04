<script setup lang="ts">
import MapChart from '@/components/MapChart.vue';
import AreaList from '@/components/AreaList.vue'
import { ref, watch, type Ref, computed, onMounted, onUnmounted, onBeforeMount, onBeforeUnmount } from 'vue';
import { useApiStore } from '@/apis/useApiStore';
import { useAiStore } from '@/apis/aiStore'
import { type Point } from 'vue3-baidu-map-gl'
import { useScopStore } from '@/stores/scop';
import { ElMessage, ElMessageBox } from 'element-plus';
import router from '@/router';
import { onBeforeRouteLeave } from 'vue-router';
import { Search } from '@element-plus/icons-vue'
const server = useApiStore()
const ai = useAiStore()

const dest = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const center = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const polygonPath = ref([dest.value])
const keyNode: Ref<Point[]> = ref([])
const buildingOptions: Ref<{ label: string, value: string }[]> = ref([])
const fromBuilding = ref("")
const toBuilding = ref("")
const planPath = async () => {
  // TODO
  if (fromBuilding.value == "" || toBuilding.value == "") {
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
  var locs = res.data[0].split(";")
  locs.forEach((loc: string) => {
    var location = loc.split(',')
    console.log(location)
    if (location.length == 2)
      polygonPath.value.push({
        lng: Number(location[0]),
        lat: Number(location[1])
      })
  })
  keyNode.value = []
  var key_nodes = res.data[1].split(";")
  key_nodes.forEach((loc: string) => {
    var location = loc.split(',')
    console.log(location)
    if (location.length == 2)
      keyNode.value.push({
        lng: Number(location[0]),
        lat: Number(location[1])
      })
  })
  dest.value.lat = keyNode.value[0].lat
  dest.value.lng = keyNode.value[0].lng
  console.log("key node", keyNode.value)
}
watch(() => fromBuilding.value, async () => {
  await planPath()
})
watch(() => toBuilding.value, async () => {
  await planPath()
})
const scop_ai_info = ref("")
onMounted(async () => {
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
  console.log("info", info)
  useScopStore().buildings = []
  buildingOptions.value = []

  info.buildings.forEach((e: any) => {
    useScopStore().buildings.push(e.name)
    buildingOptions.value.push({
      label: e.name,
      value: e.name
    })
  });

  dest.value.lng = info.lng
  dest.value.lat = info.lat
  center.value.lng = info.lng
  center.value.lat = info.lat

  polygonPath.value = [
    dest.value
  ]
  var scop_ai_info_res = await ai.get_ai_suggestion(scop.name)
  if (scop_ai_info_res.data.status) {
    scop_ai_info.value = scop_ai_info_res.data.msg
  } else {
    ElMessage("获取ai回答失败:\n" + scop_ai_info_res.data.msg)
  }
})


// onBeforeRouteLeave(async (to,from,next)=>{
//   // TODO(SJ) 这段代码会报错
//   // console.log(from,to,next)
//   if (to.name != 'grade')
//     router.push({name:"grade"})
//   else next()
// })
const endTour = () => {
  console.log("end tour")
  var res = router.push({ name: 'grade' })
  router.onError((res) => {
    console.log("router ocurr ", res)
  })
  console.log("end jump", res)
}

const ai_drawer = ref(false)
const question_for_ai = ref("")
const qa_list:Ref<{sender:string,data:string}[]> = ref([])
const ai_answering = ref(false)
const getAiAns = async () => {
  ai_answering.value = true
  qa_list.value.push({sender:"you",data:question_for_ai.value})
  var res = await ai.get_ai_response(question_for_ai.value)
  question_for_ai.value = ""
  if (res.data.status) {
    var ans = res.data.msg
    qa_list.value.push({sender:"ai",data:ans})
  } else {
    ElMessage("获取ai回答失败:\n" + res.data.msg)
    qa_list.value.push({sender:"ai",data:"I don't know"})
  }
  ai_answering.value = false
}
</script>
<template>
  <main style="width: 100%;height: 100%;">
    <p class="title">{{ useScopStore().wannago.name }}</p>
    <div class="select">
      <el-select v-model="fromBuilding" placeholder="from" size="small" style="width: 15rem">
        <el-option v-for="item in buildingOptions" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
      <el-select v-model="toBuilding" placeholder="to" size="small" style="width: 15rem">
        <el-option v-for="item in buildingOptions" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
    </div>
    <n-space>
      <n-ellipsis :line-clamp="2" style="width: 100%;text-indent: 2rem;color: aquamarine">
        {{ scop_ai_info }}
      </n-ellipsis>
    </n-space>
    <n-space justify="space-between">
      <el-button type="primary" @click="endTour">
        结束游学
      </el-button>
      <el-avatar :size="50" src="http://bupt.online/Material/G1MHMK6E.png" @click='ai_drawer = true' />
    </n-space>

    <MapChart :key="useScopStore().wannago.name" v-model:dest="dest" v-model:center="center"
      v-model:polygon-path="polygonPath" :key_nodes="keyNode" class="map">
    </MapChart>
    <el-drawer v-model="ai_drawer" size="70%">
      <template #header="{ close, titleId, titleClass }">
        <h1 :id="titleId" :class="titleClass" style="text-align: center;color: aquamarine">Ai Bot</h1>
      </template>
      <!-- res view -->
      <el-scrollbar class='qa_area'>
      <el-card v-for="msg in qa_list">
        <template #header>
          <div class="card-header">
            <span>{{ msg.sender }}</span>
          </div>
        </template>
        {{ msg.data }}
        <!-- <template #footer></template> -->
      </el-card>
    </el-scrollbar>


      <template #footer>
        <el-input v-model="question_for_ai" placeholder="Please input your question" class="input-with-select"
        :disabled='ai_answering'
        >
          <template #prepend>
            question:
          </template>
          <template #append>
            <el-button :icon="Search" @click="getAiAns" />
          </template>
        </el-input>
      </template>
    </el-drawer>
  </main>
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

.title {
  text-align: center;
  font-size: large;
  color: aqua;
}

.select {
  text-align: center;
  padding: 1px;

  .el-select {
    padding-left: 20px;
  }
}
.qa_area{
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  overflow: auto;
  padding: 10px;
  background-color: antiquewhite;
  *{
    margin-bottom: 10px
  }
}
</style>