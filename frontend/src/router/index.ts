import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
  path: '/',
  name: 'Home',
  component: () => import('@/views/HomeView.vue')
},
    {
  path: '/productos',
  name: 'productos',
  component: () => import('@/views/ProductoView.vue')
},
   {
  path: '/tipos',
  name: 'tipos',
  component: () => import('@/views/TipoView.vue')
},
{
  path: '/proveedores',
  name: 'proveedores',
  component: () => import('@/views/ProveedorView.vue')
},
{
  path: '/categorias',
  name: 'categorias',
  component: () => import('@/views/CategoriaView.vue')
},
  ],
})

export default router
