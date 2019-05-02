import Vue from 'vue'
import Router from 'vue-router'
import Info from './views/Info'
import Login from './views/Login'
import Register from './views/Register'
import Home from './views/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/info',
      name: 'info',
      component: Info
    },
    {
      path:'/login',
      name:'login',
      component:Login
    },
    {
      path:'/register',
      name:'register',
      component:Register
    },
    {
      path:'/',
      name:'home',
      component:Home
    }
  ]
})
