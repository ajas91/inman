import { createRouter, createWebHashHistory } from 'vue-router'
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
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
