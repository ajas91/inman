import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView'
// import AboutView from '../views/AboutView'
// import CustomersView from '../views/CustomersView'
// import InventoryView from '../views/InventoryView'
// import OrdersView from '../views/OrdersView'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // component: AboutView
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView')
  },
  {
    path: '/inventory',
    name: 'inventory',
    // component: InventoryView
    component: () => import('../views/InventoryView')
  },
  {
    path: '/customers',
    name: 'customers',
    // component: CustomersView
    component: () => import('../views/CustomersView')
  },
  {
    path: '/orders',
    name: 'orders',
    // component: OrdersView
    component: () => import('../views/OrdersView')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
