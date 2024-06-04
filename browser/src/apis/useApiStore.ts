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
  /**
   * 返回匹配的景点信息列表
   * @param name
   * @param province
   * @param city
   * @returns
   */
  async function get_scops_info(name:string, province:string="", city:string="") {
    const res = await server.post("get_scops_info",{
      name:name,
      province:province,
      city:city
    })
    return res
  }
  async function upLoadJour(jour:string, scopName:string, score:number, province:string,city:string) {
    const token = useUserStore().userStorage.token
    const res = await server.post("upLoadJour",{
      jour:jour,
      scopName:scopName,
      score:score,
      province:province,
      city:city,
      token:token
    })
    return res
  }
  async function get_history() {
    const token = useUserStore().userStorage.token
    const res = await server.post("get_history",{
      token:token
    })
    return res
  }
  return {
    get_all_scop, get_routes, get_hot_scop,
    get_scops_info, upLoadJour, get_history
  }
})
