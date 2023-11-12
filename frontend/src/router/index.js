import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './../views/Sample.vue'
import LogIn from './../components/Login.vue'

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
  ],
});

export default router;