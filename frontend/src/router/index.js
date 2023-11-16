import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './../views/Sample.vue'
import LogIn from './../components/Login.vue'
import SignUp from './../components/SignUp.vue'
import ManagerRequest from './../components/ManagerRequest.vue'
import CatCreate from './../components/CatCreate.vue'
import ProdCreate from './../components/ProdCreate.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path : '/login',
      name : 'login',
      component : LogIn
    },
    {
      path : '/signup',
      name : 'signup',
      component : SignUp
    },
    {
      path : '/manager_request',
      name : 'manager_request',
      component : ManagerRequest
    },
    {
      path : '/create_category',
      component : CatCreate
    },
    {
      path : '/create_product',
      component : ProdCreate
    },
  ],
});

export default router;