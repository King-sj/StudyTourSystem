<script lang="ts" setup>
const props = defineProps<{
  name: string
  province: string
  city:string
}>()
const emit = defineEmits<{
  selectCard: [name: string] // 具名元组语法
}>()
const handleClick = (e:any)=>{
  console.log('hhhh');
  emit('selectCard',props.name)
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
      <p>main content</p>
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