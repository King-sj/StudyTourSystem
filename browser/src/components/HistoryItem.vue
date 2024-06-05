<script lang="ts" setup>
import { ref } from 'vue'
import { type ScopBasicInfo } from '@/types';
const props = defineProps<{
  name: string
  province: string
  city: string
  jour: string
  score: Number
  date: string
  user?:string
}>()
const score = ref(props.score.valueOf() / 2)
const colors = ref(['#99A9BF', '#F7BA2A', '#FF9900'])
const line_cnt = ref("2")
</script>
<template>
  <el-card
  @click="
    console.log('click');
    line_cnt= line_cnt == '' ? '2':''
    "
  >
    <template #header>
      <div class="card-header">
        <p>{{ props.user }}</p>
        <p>
          <el-rate v-model="score" :colors="colors" size="large"
            clearable allow-half
            text-color="aqua" disabled />
        </p>
        <span>{{
            props.province +
            (props.city == props.province ? "" : props.city)
            + props.name
          }}
        </span>
      </div>
    </template>
    <div class="card-main">

      <n-ellipsis :line-clamp="line_cnt"
      >
        {{ jour.length == 0 ? "这家伙懒得评论..." : jour }}
      </n-ellipsis>
    </div>
    <template #footer>
      {{ props.date }}
    </template>
  </el-card>
</template>
<style lang="scss" scoped>
.el-card {
  background-color: rgba(255, 255, 255, 0.5);
  border-color: #9ef3f3fa;
  width: 100%;
}

.card-header {
  text-align: center;

  span {
    margin: 0.5rem;
    color: #000;
  }
}

.card-main {
  text-align: center;
}
</style>