<script lang="ts" setup>
import { ref } from 'vue'
import type { Ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore, User} from '@/components/LoginSystem'
import { ElMessageBox } from 'element-plus';

const router = useRouter()

const psw: Ref<string> = ref('')
const email: Ref<string> = ref('')
const captcha: Ref<string> = ref('')

const disabledSendCaptcha = ref(false)
const waitTime_sendCaptcha : Ref<null|number> = ref(null)
const signUp = async () => {
  // TODO
  if(!emailCheck(email.value)) {
    ElMessageBox.alert("邮箱格式错误");
    return;
  }
  if (captcha.value.length!= 6) {
    ElMessageBox.alert("验证码格式错误")
    return
  }
  const success = await useUserStore().signUp(new User(
    email.value,psw.value
  ), captcha.value)
  console.log(success)
  if (success){
    ElMessageBox.alert('注册成功')
    router.push({ name: "login" })
  } else {
    ElMessageBox.alert('注册失败')
  }
}
const sendCaptcha = async ()=>{
  if (!emailCheck(email.value)) {
    ElMessageBox.alert("邮箱格式不对")
    return
  }
  if(!useUserStore().sendCaptcha(email.value))return;

  disabledSendCaptcha.value = true
  waitTime_sendCaptcha.value = 60
  // waitTime_sendCaptcha.value = 3
  var interval =  setInterval(()=>{
    if (null == waitTime_sendCaptcha.value) {
      clearInterval(interval);
      return;
    }
    waitTime_sendCaptcha.value-=1;
    if (waitTime_sendCaptcha.value == 0) {
      waitTime_sendCaptcha.value = null
      disabledSendCaptcha.value = false
      clearInterval(interval)
    }
  },1000)
}
const emailCheck = (email:string) : boolean=>{
  return /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/.test(email)
}
</script>
<template>
  <main>
    <n-space style="text-align: center;" vertical>
      <n-input v-model:value="email" type="text"  :maxlength="32">
        <template #prefix>邮箱</template>
      </n-input>
      <n-input v-model:value="psw" type="password" show-password-on="mousedown"
        :maxlength="16">
        <template #prefix>密码</template>
      </n-input>
      <n-input v-model:value="captcha" type="text" :maxlength="6">
        <template #prefix>验证码</template>
        <template #suffix>
          <n-button style="color:black" @click="sendCaptcha" :disabled='disabledSendCaptcha'>
            发送{{waitTime_sendCaptcha}}
          </n-button>
        </template>
      </n-input>
      <n-space justify="center">
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
    color: var(--color-text);
  }
}
</style>