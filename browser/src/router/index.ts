import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
    ,
    {
      path: '/help',
      name: 'help',
      component: () => import('../views/HelpView.vue')
    }
    ,
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue')
    }
    ,
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path:"/signUp",
      name:"signUp",
      component: () => import('../views/SignUpView.vue')
    },
    {
      path:"/setting",
      name:"setting",
      component:()=>import("../views/SettingView.vue")
    },
    {
      path:"/touring",
      name:"touring",
      component:()=>import("../views/TouringView.vue")
    },
    {
      path:"/grade",
      name:"grade",
      component:()=>import("../views/GradeView.vue")
    }
  ]
})

export default router
