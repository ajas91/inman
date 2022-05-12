import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about/',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView')
  },
  {
    path: '/inventory/',
    name: 'inventory',
    component: () => import('../views/Inventory')
  },
  {
    path: '/customers/',
    name: 'customers',
    component: () => import('../views/Customers')
  },
  {
    path: '/orders/',
    name: 'orders',
    component: () => import('../views/Orders')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
