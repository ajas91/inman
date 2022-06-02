import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView')
  },
  {
    path: '/inventory',
    name: 'inventory',
    component: () => import('../views/InventoryView')
  },
  {
    path: '/inventory/:itemID',
    name: 'itemDetails',
    component: () => import('../views/ItemDetailsView')
  },
  {
    path: '/customers',
    name: 'customers',
    component: () => import('../views/CustomersView')
  },
  {
    path: '/customers/:customerID',
    name: 'customerDetails',
    component: () => import('../views/CustomerDetailsView')
  },
  {
    path: '/orders',
    name: 'orders',
    component: () => import('../views/OrdersView')
  },
  {
    path: '/orders/:orderID',
    name: 'orderDetails',
    component: () => import('../views/OrderDetailsView')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
