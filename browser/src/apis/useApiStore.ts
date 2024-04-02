import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
export const useApiStore = defineStore('apiStore', () => {
  const SERVER: string = 'http://127.0.0.1'
  // const SERVER: string = "http://101.42.8.164"
  const PORT: String = '2004'
  const server = axios.create({
    baseURL: SERVER + ':' + PORT + '/api/',
    timeout: 1000,
    headers: { 'X-Custom-Header': 'foobar' }
  })

  return {}
})
