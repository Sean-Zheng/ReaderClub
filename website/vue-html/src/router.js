import Vue from 'vue'
import Router from 'vue-router'
import Info from './views/Info.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/info',
      name: 'info',
      component: Info
    }
  ]
})
