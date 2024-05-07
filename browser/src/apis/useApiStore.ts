import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import {serverConfig} from "@/configs"
export const useApiStore = defineStore('apiStore', () => {
  // const SERVER: string = 'http://127.0.0.1'
  // const SERVER: string = "http://101.42.8.164"
  // const PORT: String = '2004'
  const server = axios.create({
    baseURL: serverConfig.SERVER + ':' + serverConfig.PORT + '/api/',
    timeout: 1000,
    headers: { 'X-Custom-Header': 'foobar' }
  })
  async function get_all_scop() {
    const res = await server.post('get_all_scop')
    return res
  }
  return {get_all_scop}
})
