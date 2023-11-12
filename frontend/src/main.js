import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
// import router from './router'
import HomePage from './components/HomePage.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/home', component: HomePage },
    ]
});

const app = createApp(App)

app.use(router);
// app.component('food-items', FoodItems);
// app.component('animal-collection', AnimalCollection);
   
app.mount('#app')




