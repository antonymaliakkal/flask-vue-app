import Vue from 'vue'
import Router from 'vue-router'

import HomePage from './../components/HomePage.vue'

Vue.use(Router)


// const routes = createRouter({
//     history : createWebHistory(import.meta.env.BASE_URL),
//     routes : [
//     {
//         path : '/home',
//         name : 'Home',
//         component : HomePage
//     },
// ]
// })

  
export default new Router({
    routes : [
        {
            path : '/home',
            component : HomePage
        }
    ]
})