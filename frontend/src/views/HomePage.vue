<script setup>
import { productStore } from '../store/productStore.js'
import { categoryStore } from '../store/miscStore.js'
import { onMounted, reactive, ref, watch } from 'vue';
import { userStore } from '@/store/userStore';
import { cartStore } from '@/store/cartStore';

let products = reactive({})
let selected = ref('')
let x = ref('')
let quantity = reactive({})
let buy = reactive({})

watch(selected, (newValue) => {
    if (newValue == 'all') {
        products.value = productStore.products
        
    } else {
        products.value = Object.values(productStore.products).filter(products => (products.cat == newValue))
    }
})



onMounted(async () => {
    await productStore.get();
    await categoryStore.get();
    selected.value = 'all'  

    if(userStore.token) {
        await cartStore.get()
        for (x in products.value) {
            console.log(x)
            let y = products.value[x].name
            if(incart(y)){
                buy[y] = true
            }   
            else {
                buy[y] = false
            }
        }
        console.log(buy)
    }
   
},

)


 function incart(key) {
       for (x in cartStore.cart) {
            if(key == cartStore.cart[x].name) {
                return true
            }
       }
       return false 
 }

function quant() {
    console.log(products)
    for (x in products.value) {
        console.log(x);  
        quantity[x] = 0;      
    }

}

function viewcat(key) {
    quant()
    selected.value = key;
}

function addcart(key,name){
    if(userStore.token){
        console.log(key)
        let data = {'p_id' : key , 'qty' : quantity[key] , 'user_id' : localStorage.getItem('id')}
        console.log(quantity[key])
        console.log(data)
        cartStore.add_cart(data)
        buy[name] = true

    }
    else {
        console.log(userStore.isLoggedIn)
        console.log('not logged in!!!')
    }
}

</script>
<template>
    <div class="main">
        <div class="col card">
            <!-- Category list -->
            <ul class="list-group list-group-flush">
                <li class="card-header" @click="viewcat('all')">ALL</li>
                <li class="list-group-item text-uppercase" v-for="(value, key) in categoryStore.cat_new" :key="key" @click="viewcat(key)">
                    {{ value.name }}
                </li>
            </ul>
        </div>

        <div class="products parent">
        <div class="card border-success mb-3 child" style="max-width: 18rem;" v-for="(value, key) in products.value" :key="key">
            <div class="card-header bg-transparent border-success text-uppercase font-weight-bold">{{ value.name }}</div>
            <div v-if="buy[value.name]">
                <div class="card-body text-success">
                    <h5 class="card-title">₹{{ value.price }}</h5>
                    <p class="card-text">{{ value.desc }} </p>  
                </div>   
                <a class="btn btn-primary text-white">ADDED</a>
            </div>
            <div v-else>
                <div class="card-body text-success">
                    <h5 class="card-title">₹{{ value.price }}</h5>
                    <p class="card-text">{{ value.desc }} </p>
                    <input class="card-text" v-model="quantity[value.id]" type="number" min="0" placeholder="Quantity">            
                    </div>
                    <a @click="addcart(value.id , value.name)" class="btn btn-primary text-white">ADD TO CART</a>
                </div>
            </div>

        

    </div>

    </div>



</template>
<style>
    .main {
        display : flex;
    }

    .col {
        flex : 1;
    }

    .products {
        flex : 3

    }

    .parent {
        display: flex;
        flex-wrap: wrap;
    }

    .child {
        flex: 1 0 30%;
        margin-right: 10px;
    }
</style>