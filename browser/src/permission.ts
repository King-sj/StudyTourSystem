import router from "@/router/index";
import { ElMessageBox } from 'element-plus'
import { useUserStore } from "@/components/LoginSystem";
const noNeedLogin = (name: String | undefined):boolean=>{
  const pages : String[] = ["login", "signUp", "setting"]
  return name ? pages.includes(name) : false
}
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  // userStore.logout()
  const user = userStore.userStorage;
  console.log('user storage',user, user.email, user.password, user.expiration)
  if (userStore.isExpired() && !noNeedLogin(to.name?.toString())) {
    ElMessageBox.alert('登录过期，请重新登录').then(() => {
      next('/login')
    })
  } else {
    next();
  }
})