import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import {serverConfig} from "@/configs"
// import { useUserStore } from '@/components/LoginSystem'

export const useAiStore = defineStore('aiStore', () => {
  // const SERVER: string = 'http://127.0.0.1'
  // const SERVER: string = "http://101.42.8.164"
  // const PORT: String = '2004'
  const server = axios.create({
    baseURL: serverConfig.SERVER + ':' + serverConfig.PORT + '/api/',
    timeout: 1000000,
    headers: { 'X-Custom-Header': 'foobar' }
  })
  async function get_ai_suggestion(name:string) {
    const res =await server.post("get_ai_suggestion",{
      name:name
    })
    return res
  }
  async function get_ai_response(question:string) {
    const res = await server.post("get_ai_response",{
      question:question
    })
    return res
  }
  return {
    get_ai_response,get_ai_suggestion
  }
})
