<script setup>
import { productStore } from '../store/productStore.js'
import { categoryStore } from '../store/miscStore.js'
import { onMounted, reactive, ref, watch } from 'vue';
import { userStore } from '@/store/userStore';
import { cartStore } from '@/store/cartStore';
// import categoryStore from './../store/miscStore';

let products = reactive({})
let selected = ref('')
let quantity = ref(0)

watch(selected, (newValue) => {
    if (newValue == 'all') {
        products.value = productStore.products
    } else {
        products.value = Object.values(productStore.products).filter(products => (products.cat == newValue))
    }
})

onMounted(async () => {
    await productStore.get();
    await categoryStore.get()
    selected.value = 'all'
},

)

function viewcat(key) {
    selected.value = key;
}

function addcart(key){
    if(userStore.token){
        let data = {'p_id' : key , 'qty' : quantity.value , 'user_id' : localStorage.getItem('id')}
        console.log(data)
        cartStore.add_cart(data)

    }
    else {
        console.log(userStore.isLoggedIn)
        console.log('not logged in!!!')
    }
}

</script>
<template>
    <h1>HOME PAGE</h1>
    <div class="main row">
        <div class="col card">
            <!-- Category list -->
            <ul class="list-group list-group-flush">
                <li class="card-header" @click="viewcat('all')">ALL</li>
                <li class="list-group-item" v-for="(value, key) in categoryStore.cat_new" :key="key" @click="viewcat(key)">
                    {{ value.name }}
                </li>
            </ul>
        </div>
        <div class="col-9 products">
            <div class="card" v-for="(value, key) in products.value" :key="key">
                <div class="card-body">
                    <h5 class="card-title">{{ value.name }}</h5>
                    <p class="card-text">{{ value.desc }}</p>
                    <input class="card-text" v-model="quantity" type="number" min="0" placeholder="Quantity">
                    <a @click="addcart(value.id)" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>

    </div>

    <div class="card">
        <!-- <img class="card-img-top" src="..." alt="Card image cap"> -->
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
    </div>


</template>
