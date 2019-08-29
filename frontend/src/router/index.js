import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const login = r => require.ensure([], () => r(require('@/page/login')), 'login');
const activityList = r => require.ensure([], () => r(require('@/page/activityList')), 'activityList');

const routes = [
  {
    path: '/',
    component: login
  },
  {
    path: '/activityList',
    component: activityList
  },
]

export default new Router({
  routes,
  strict: process.env.NODE_ENV !== 'production',
})
