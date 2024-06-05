<script lang="ts" setup>
import { useApiStore } from '@/apis/useApiStore';
import { ElMessageBox } from 'element-plus';
import { onMounted, ref, watch, type Ref } from 'vue';
import HistoryItem from "@/components/HistoryItem.vue"
const server = useApiStore()
const histories: Ref<any[]> = ref([])
const scop = ref("")
watch(()=>scop.value,async () => {
  var res = await server.get_jour_by_scop_name(scop.value)
  // if (!res.data.status) {
  //   console.log("获取数据失败:\n" + res.data.res)
  //   return
  // }
  histories.value = []
  res.data.forEach((jour:any)=>{
    jour.jour.forEach((item:any)=>{
      histories.value.push({
        scop_name: item.scop_name,
        province: item.province,
        city: item.city,
        data: item.data,
        score: item.score,
        date: item.date,
        user:jour.user
      })
    })
  })
  histories.value = histories.value.sort(
    (a:any,b:any)=>{
      const dateA = new Date(a.date);
      const dateB = new Date(b.date);
      // 比较日期并返回排序结果, 最近的在前
      return dateB.getTime()-dateA.getTime()
    }
  )
  console.log("jour data", histories.value)
})
</script>
<template>
  <h1 style="text-align: center;">日记搜索</h1>
  <p v-if="histories.length == 0" id="loading">加载中...</p>
  <el-input v-model="scop" placeholder="景区名"></el-input>
  <el-scrollbar class="history-list">
    <HistoryItem v-for="item in histories"
    :user="item.user"
    :province="item.province" :city="item.city" :jour="item.data"
      :name="item.scop_name" :score="item.score" :date="item.date"
      class="history-item"
    >
    </HistoryItem>
  </el-scrollbar>

</template>
<style lang="scss" scoped>
#loading {
  text-align: center;
  font-size: 2rem;
  color: aqua;
}
.history-list{
  height: 30rem;
  .history-item{
    margin-bottom: 5px;
  }
}
</style>