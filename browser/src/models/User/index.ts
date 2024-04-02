import { useTimestamp } from '@vueuse/core'
import {ref} from "vue"
import type {Ref} from 'vue'
import {useEventListener} from "@/utils"
class User {
  public name: Ref<string>;
  public lastLoginTimeStamp:Ref<number>;  // 最后登录的时间戳
  public static readonly MAX_OFFLINE_TIME:number = 100000;
  public constructor(name:string) {
    this.name = ref(name);
    this.lastLoginTimeStamp = ref(useTimestamp().value);

    window.addEventListener('beforeunload', (event) => {
      alert("will close")
      event.preventDefault(); // 阻止默认行为
      event.returnValue = ''; // Chrome 需要设置 returnValue
    });


    // useEventListener(window,"beforeunload",(e:BeforeUnloadEvent)=>{
    //   alert("will close")
    //   this.lastLoginTimeStamp = useTimestamp();
    //   e.preventDefault()
    //   e.returnValue = ''; // Chrome 需要设置 returnValue
    // })
  }
}

export default User;