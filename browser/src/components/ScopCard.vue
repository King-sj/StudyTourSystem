<script lang="ts" setup>
import {ref} from 'vue'
import { type ScopBasicInfo } from '@/types';
const props = defineProps<{
  name: string
  province: string
  city:string
  visited_person:Number
  score:Number
}>()
const score = ref(props.score.valueOf()/2)
const colors = ref(['#99A9BF', '#F7BA2A', '#FF9900'])
const emit = defineEmits<{
  selectCard: [scop:ScopBasicInfo] // 具名元组语法
}>()
const handleClick = (e:any)=>{
  emit('selectCard',{
    name:props.name,
    province:props.province,
    city:props.city
  })
}
</script>
<template>
  <el-card @click="handleClick">
    <template #header>
      <div class="card-header">
        <span>{{ props.name }}</span>
      </div>
    </template>
    <div class="card-main">
      <p>
        平均评分:
        <el-rate v-model="score" :colors="colors" size="large"
        :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
        show-text
        clearable
        allow-half
        text-color="aqua"
        disabled
      />
      </p>
      <p>总人次:{{props.visited_person}}</p>
    </div>
    <template #footer>所在地:
      {{ props.province }}
      {{ props.city == props.province ? "" : props.city}}
    </template>
  </el-card>
</template>
<style lang="scss" scoped>
.el-card{
  background-color: #eff7;
  width: 100%;
}
</style>