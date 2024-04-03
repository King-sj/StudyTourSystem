import router from "@/router/index";
import { useStorage, useTimestamp } from '@vueuse/core'
import { ElMessageBox } from 'element-plus'
import { useUserStore } from "./stores/user";
/**
 * 判断路径是否是（不同端）的首页，是则返回true
 *  @param[path] 待判断路径
 */
function isHomePage(path: string): boolean {
  var homePages: string[] = ["/", "/home"];
  return homePages.some(value => value === path);
}

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const userData = userStore.userData;
  console.log("user storage:" , userData ,from,to)
  // user.value = null
  // 登录检查
  if (!userData && to.name != "login") {
    ElMessageBox.alert('Please login')
    next('/login');
  } else {
    next();
  }
});