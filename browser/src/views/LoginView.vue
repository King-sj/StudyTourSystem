<script lang="ts" setup>
import type { Ref } from 'vue';
import { ref } from 'vue';
import { User, useUserStore } from '@/components/LoginSystem'
import { useRouter } from 'vue-router';
const router = useRouter()
const email: Ref<string> = ref('')
const psw: Ref<string> = ref('')
const login = async () => {
  const succ = await useUserStore().login(
    new User(email.value, psw.value)
  )
  if (succ) {
    router.push({name:"home"})
  }
}
const signUp = ()=>{
  router.push({ name : "signUp" })
}
</script>

<template>
  <main>
    <n-space vertical>
      <n-input v-model:value="email" type="text" placeholder="please input email" :maxlength="32" />
      <n-input v-model:value="psw" type="password" show-password-on="mousedown" placeholder="please input password"
        :maxlength="16" />
      <n-space>
        <n-button @click="login">登录</n-button>
        <n-button @click="signUp">注册</n-button>
      </n-space>
    </n-space>
  </main>
</template>

<style lang="scss" scoped>
.n-space {
  display: flex;
  font-size: 1rem;
  .n-input {
    width: 50%;
    margin: 0;
  }

  .n-button {
    margin: 0;
    // color: var(--color-text);
  }
}
</style>