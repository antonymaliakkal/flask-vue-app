import { createRouter, createWebHistory } from 'vue-router'
// import HomePage from './../views/Sample.vue'

// import RegisterPage from './../views/Register.vue'
import AdminPage from './../views/Admin.vue'
import HomePage from './../views/HomePage.vue'
// import CartPage from './../views/Cart.vue'
import ManagerPage from './../views/ManagerPage.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home', 
      component: HomePage
    },
    {
      path : '/admin',
      component : AdminPage,
      meta : {
        requiresAuth : true ,
        roles : ['admin']
      }
    },
    {
      path : '/manager',
      component : ManagerPage,
      meta : {
        requiresAuth : true ,
        roles : ['manager']
      }
    },
  ],
});

router.beforeEach((to,from,next) => {

    console.log(localStorage.getItem('token'));
    if(to.matched.some(record => record.meta.requiresAuth)) {
      const role = localStorage.getItem('role')
      const allowedroles = to.meta.roles;

      if(!allowedroles.includes(role)) {
        next('/register');
      } else {
        next();
      }

    }
  
  else {
    console.log('elsed');
    next();
  }
});

export default router;