<script setup lang="ts">
import AreaList from '@/components/AreaList.vue'
import { ref, watch, type Ref, computed, onMounted} from 'vue';
import { useApiStore } from '@/apis/useApiStore';
import { type Point } from 'vue3-baidu-map-gl'
import { useRouter } from 'vue-router';
import ScopCard from "@/components/ScopCard.vue"

const server = useApiStore()
const router = useRouter()

const hot_scops = ref()
const selectArea:Ref<any> = ref({name:""})

const dest = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const center = ref({ lng: 116.364594, lat: 39.96725 } as Point);
const polygonPath = ref([dest.value])
watch(() => selectArea.value, (v) => {
  console.log("select change", selectArea.value)
  if (selectArea.value) {
    dest.value.lng = selectArea.value.lng
    dest.value.lat = selectArea.value.lat
    center.value.lng = selectArea.value.lng
    center.value.lat = selectArea.value.lat

    polygonPath.value = [
      dest.value
    ]
  }
})
const handle_select_card = (name:string)=>{
  console.log("wanna_go", name)
  router.push({name:"touring"})
}
onMounted(async ()=>{
  hot_scops.value = await server.get_hot_scop()
  console.log("hot", hot_scops.value)
})
</script>
<template>
  <main style="width: 100%;height: 100%;">
    <p id="hot-scop-title">热门景点</p>
    <div class="cities-view">
      <el-scrollbar >
        <div class="card-container">
          <ScopCard
            v-for="scop in hot_scops?.data" :key="scop['name']"
            :name="scop['name']" :province="scop['province']" :city="scop['city']" class="city-card"
            @select-card="handle_select_card"
          />
        </div>
      </el-scrollbar>
    </div>
  </main>
</template>

<style lang="scss" scoped>
.area-list {
  min-height: 10%;
}

.map {
  height: 70%;
  width: 100%;
}

.el-button {
  margin-top: 30px;
}
#hot-scop-title{
  text-align: center;
  color: red;
  font-size: 1.5rem;
}
.cities-view{
  margin: 0;
  padding: 0.1rem;
  height: 50%;
  // background-color: red;
  .card-container {
    display: flex; /* 启用弹性布局 */
    flex-wrap: wrap; /* 允许子元素换行 */
    justify-content: space-between; /* 子元素在主轴上的对齐方式 */
    .city-card{
      width: 31%;
      margin: 0.5rem;
      padding: 0;
    }
  }
}
</style>