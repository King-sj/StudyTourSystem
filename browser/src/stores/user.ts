import { ref, computed } from 'vue'
import type {Ref} from 'vue'
import { defineStore } from 'pinia'
import { useStorage, useTimestamp } from '@vueuse/core'
import {useEventListener} from "@/utils"
export interface IUserData{
  name:string,
  lastLoginTimeStamp:number
}
export const useUserStore = defineStore('user', () => {
  const userData = computed(
    () => useStorage<IUserData>(
      "user",
      null,
      localStorage,
      {mergeDefaults: true}
    )
  )
  function bindWindowClose() {
    alert("bind success")
    useEventListener(window,"beforeunload",(e:BeforeUnloadEvent)=>{
      alert("will close")
      userData.value.value.lastLoginTimeStamp = useTimestamp().value
      e.preventDefault()
      e.returnValue = ''; // Chrome 需要设置 returnValue
      // return ""
    })
  }
  bindWindowClose(); // 手动调用
  function update(_userData:IUserData) {
    userData.value.value = _userData
  }

  return {userData,update}
})
