<script lang="ts" setup>
import {ref, watch} from 'vue'
import { useUserStore } from '@/components/LoginSystem';
import { useRouter } from 'vue-router';
import {toggleTheme} from "@/styles/setting.ts"
const router = useRouter()
const logout = ()=>{
  useUserStore().logout()
  router.push({name:"login"})
}
const themes = ['dark','light','white']
const theme = ref(themes[2])

watch(theme,
()=>{
  toggleTheme(theme.value);
},
{
  immediate:true
}
)
</script>
<template>
  <main style="text-align: center;">
    <div>
    <el-select
      v-model="theme"
      placeholder="Select"
      size="small"
      style="width: 240px"
    >
      <el-option
        v-for="item in themes"
        :key="item"
        :label="item"
        :value="item"
      />
    </el-select>
  </div>
    <n-button @click="logout">
      注销
    </n-button>
  </main>
</template>
<style scss scoped>
*{
  /* color: var(--color-text); */
  margin-top: 1rem;
}
.el-select{
  background-color: black;
}
</style>