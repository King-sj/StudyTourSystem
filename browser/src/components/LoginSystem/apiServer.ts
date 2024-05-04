import {defineStore} from 'pinia'
import axios from 'axios';
import {User} from './User'
import {SERVER,PORT} from "@/configs"
export const useApiServer = defineStore("loginSystemApiServer",()=>{
  // const server:string = 'http://127.0.0.1:2004/';
  const axiosInst = axios.create({
    baseURL: SERVER+":"+ PORT + '/loginSystem/',
    timeout: 1000,
    headers: { 'X-Custom-Header': 'foobar' }
  })
  function sendCaptcha(email:string) {
    axiosInst.post('captcha',{
      email:email
    })
  }
  async function signUp(user:User,captcha:String) {
    const res = await axiosInst.post("signup",{
      email:user.email,
      password:user.password,
      captcha:captcha
    })
    return res
  }
  async function login(user:User) {
    const res = await axiosInst.post("login",{
      email:user.email,
      password:user.password,
    })
    return res
  }
  return {sendCaptcha, signUp, login}
})