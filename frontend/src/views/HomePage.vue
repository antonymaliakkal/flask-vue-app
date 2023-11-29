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
    if(!userStore.isLoggedIn){
        console.log('not logged in')
    }
    else {
        let data = {'p_id' : key , 'quantity' : quantity , 'id' : userStore.id}
        cartStore.add_cart(data)
    }
}

</script>
<template>
    <h1>HOME PAGE</h1>
    <div class="main">
        <div class="categories">
            <!-- Category list -->
            <ul>
                <li @click="viewcat('all')">ALL</li>
                <li v-for="(value, key) in categoryStore.cat_new" :key="key" @click="viewcat(key)">
                    {{ value.name }}
                </li>
            </ul>
        </div>
        
        <div class="products">
            <!-- Product tabs -->
            <div class="tab-container">
                <div v-for="(value, key) in products.value" :key="key" class="tab">
                    <b>{{ value.name }}</b>
                    <br>
                    PRICE: {{ value.price }}
                    <br>
                    {{ value.desc }}
                    <br>
                    <input v-model="quantity" type="number" min="0" placeholder="Quantity">
                    <br>
                    <button @click="addcart(key)" >ADD TO CART</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.main {
    display: flex;
}

.categories {
    flex: 1;
    /* Categories take up remaining space */
    overflow-y: auto;
    /* Enable vertical scrolling if needed */
    max-height: 100vh;
    /* Limit maximum height */
}

.products {
    flex: 3;
    /* Products take up 3/4 of the space */
    overflow-x: auto;
    /* Enable horizontal scrolling */
}

.tab-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    /* Adjust gap between tabs */
}

.tab {
    width: calc(25% - 20px);
    /* Each tab takes up 25% width with 20px gap */
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
    /* Adjust margin between tabs */
}</style>