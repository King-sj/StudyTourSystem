import { ref, computed, type Ref } from 'vue'
import { defineStore } from 'pinia'
import { type ScopBasicInfo } from '@/types';
export const useScopStore = defineStore('scop', () => {
  const wannago:Ref<ScopBasicInfo> = ref({
    name:"",
    province:"",
    city:""
  });
  const buildings:Ref<string[]> = ref([])
  return { wannago, buildings}
})
