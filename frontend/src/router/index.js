import { createRouter, createWebHistory } from 'vue-router'
// import HomePage from './../views/Sample.vue'

// import RegisterPage from './../views/Register.vue'
import AdminPage from './../views/Admin.vue'
import HomePage from './../views/HomePage.vue'
// import CartPage from './../views/Cart.vue'


import EditCat from './../components/EditCat.vue'
import ProdCreate from './../components/ProdCreate.vue'
import DeleteProduct from './../components/DelProd.vue'
import DeleteCategory from './../components/DelCat.vue'


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
      path : '/edit_cat',
      component : EditCat
    },
    {
      path : '/create_product',
      component : ProdCreate
    },
    {
      path : '/delete_product',
      component : DeleteProduct
    },
    {
      path : '/delete_category',
      component : DeleteCategory
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