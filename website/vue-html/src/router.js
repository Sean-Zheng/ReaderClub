import Vue from 'vue'
import Router from 'vue-router'
import BookDetail from './views/BookDetail'
import Login from './views/Login'
import Register from './views/Register'
import Home from './views/Home'
import Chapter from './views/Chapter'
import SearchResult from './views/SearchResult'
import TypeView from './views/TypeView'
import Space from './views/Space'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/detail',
      name: 'detail',
      component: BookDetail
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/chapter',
      name: 'chapter',
      component: Chapter
    },
    {
      path: '/search',
      name: 'search',
      component: SearchResult
    },
    {
      path: '/type/:typename',
      name: 'type',
      component: TypeView
    }, {
      path: '/space/:id',
      name: 'space',
      component: Space
    }
  ]
})
