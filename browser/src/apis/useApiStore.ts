import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import {serverConfig} from "@/configs"
import { useUserStore } from '@/components/LoginSystem'
export const useApiStore = defineStore('apiStore', () => {
  // const SERVER: string = 'http://127.0.0.1'
  // const SERVER: string = "http://101.42.8.164"
  // const PORT: String = '2004'
  const server = axios.create({
    baseURL: serverConfig.SERVER + ':' + serverConfig.PORT + '/api/',
    timeout: 10000,
    headers: { 'X-Custom-Header': 'foobar' }
  })
  async function get_all_scop() {
    const res = await server.post('get_all_scop',{},{
      timeout:30000
    })
    return res
  }
  async function get_routes(area:string,origin:string,dest:string) {
    const token = useUserStore().token
    const res = await server.post("get_routes", {
      area:area,
      origin:origin,
      dest:dest,
      token:token
    })
    return res
  }
  async function get_hot_scop() {
    const res = await server.get("get_hot_scop")
    return res
  }
  return {get_all_scop, get_routes, get_hot_scop}
})
