import { defineStore } from "pinia";
import {useStorage} from "@vueuse/core"
import type {Ref} from "vue"
import {ref} from "vue"
import {User} from './User'
import { useApiServer } from "./apiServer";
import { ElMessageBox } from "element-plus";
export const useUserStore = defineStore("user",()=>{
  const api = useApiServer();
  const userStorage:Ref<User> = useStorage<User>("user",new User(),
    localStorage,
    {
      serializer:{
        read(raw:string){
          return raw ? JSON.parse(raw) : new User()
        },
        write(value:User) {
          return JSON.stringify(value)
        }
      }
    }
  );
  const ttl:number = 30*60*1000;  // 30 min
  const sendCaptcha = (email:string):boolean=>{
    try {
      api.sendCaptcha(email)
    } catch (err){
      ElMessageBox.alert("发送失败: \n" + err );
      return false;
    }
    return true
  }
  const signUp = async (user:User, captcha:string):Promise<boolean>=>{
    try {
      const res = await api.signUp(user,captcha)
      console.log(res)
      // TODO(SJ) do more
      if(!res.data.res[0]) {
        ElMessageBox.alert(res.data.res[1])
      }
      return res.data.res[0]
    } catch(err) {
      ElMessageBox.alert("SignUp error:\n" + err);
      return false
    }
  }
  const login = async (user:User):Promise<boolean>=>{
    try {
      var res = await api.login(user)
      console.log(res)
    } catch(err) {
      ElMessageBox.alert("login failed:\n"+err)
      return false;
    }
    if (!res.data.login) {
      ElMessageBox.alert(res.data.err)
      return false
    }
    userStorage.value = new User(user.email,user.password,res.data.token,new Date().getTime() + ttl);
    return true
  }
  const logout = ()=>{
    userStorage.value = new User();
  }
  const isExpired = ():boolean=>{
    return new Date().getTime() > userStorage.value.expiration;
  }
  return {sendCaptcha, signUp, login, logout, isExpired, userStorage}
})