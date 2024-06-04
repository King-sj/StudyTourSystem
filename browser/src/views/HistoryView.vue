<script lang="ts" setup>
import { useApiStore } from '@/apis/useApiStore';
import { ElMessageBox } from 'element-plus';
import { onMounted, ref, type Ref } from 'vue';
import HistoryItem from "@/components/HistoryItem.vue"
const server = useApiStore()
const histories: Ref<any[]> = ref([])
onMounted(async () => {
  var res = await server.get_history()
  if (!res.data.status) {
    ElMessageBox.alert("获取历史数据失败:\n" + res.data.res)
  }
  histories.value = res.data.res.sort(
    (a:any,b:any)=>{
      const dateA = new Date(a.date);
      const dateB = new Date(b.date);
      // 比较日期并返回排序结果, 最近的在前
      return dateB.getTime()-dateA.getTime()
    }
  )
})
</script>
<template>
  <h1 style="text-align: center;">游学记录</h1>
  <p v-if="histories.length == 0" id="loading">加载中...</p>
  <el-scrollbar class="history-list">
    <HistoryItem v-for="item in histories" :province="item.province" :city="item.city" :jour="item.data"
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