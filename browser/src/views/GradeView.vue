<script lang="ts" setup>
import {ref, type Ref} from 'vue'
import { useApiStore } from '@/apis/useApiStore';
import { useScopStore } from '@/stores/scop';
import router from '@/router';
import { ElMessage, ElMessageBox } from 'element-plus';

const server = useApiStore()
const scop = useScopStore()
const score = ref(3.5)
const colors = ref(['#99A9BF', '#F7BA2A', '#FF9900'])
const jour = ref("")
const uploadJour = async ()=>{
  var res = await server.upLoadJour(jour.value, scop.wannago.name, 2*score.value,
    scop.wannago.province, scop.wannago.city
  )
  console.log("upload res",res,scop.wannago)
  if (res.data.status) {
    ElMessage("上传成功")
    router.push({name:"home"})
  } else {
    ElMessageBox.alert("上传失败\n"+res.data.msg)
  }
  console.log("click")
  router.push({name:"home"})
}
</script>
<template>
  <header>
    <h1 class="title">评个分再走吧!</h1>
  </header>
  <main>
    <div class="score-container">
      <el-rate v-model="score" :colors="colors" size="large"
        :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
        show-text
        clearable
        allow-half
        text-color="aqua"
      />
    </div>
    <el-input
      class="jour-input"
      v-model="jour"
      :autosize="{ minRows: 10, maxRows: 40  }"
      type="textarea"
      placeholder="输入日记"
    />
  </main>
  <footer style="text-align: center;">
    <el-button type="primary" @click="uploadJour">
      完成
    </el-button>
  </footer>
</template>
<style lang="scss" scoped>
.title{
  text-align: center;
  color: aqua;
}
.score-container{
  text-align: center;
}
.jour-input{
  background-color: red;
}
</style>