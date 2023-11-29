<template>
    <h1>HOME PAGE</h1>
    <div class="main">
        <div class="categories">
            <!-- Category list -->
            <ul>
                <li v-for="(value, key) in categories" :key="key" @click="viewcat(key)">
                    {{ value }}
                </li>
            </ul>
        </div>
        <div class="products">
            <!-- Product tabs -->
            <div class="tab-container">
                <div v-for="(value, key) in products" :key="key" class="tab">
                    <b>{{ value.name }}</b>
                    <br>
                    PRICE: {{ value.price }}
                    <br>
                    {{ value.desc }}
                </div>
            </div>
        </div>
    </div>
    
</template>
<script>
import axios from 'axios';

    export default {
        name : 'HomePage',
        data()  {
            return {
                categories : {},
                // displaycat : true,
                products : {},

            }
        },
        mounted() {
            axios.get('http://localhost:5000/view_category')
                .then(response => {
                    this.categories = response.data.category;
                    console.log('Categories fetched')
                }) 
            
            axios.get('http://localhost:5000/view_product')
                .then(response => {
                    this.products = response.data.product;
                    console.log('Products fetched!!!')
                })
        },
    }
    
</script>
<style>
.main {
    display: flex;
}

.categories {
    flex: 1; /* Categories take up remaining space */
    overflow-y: auto; /* Enable vertical scrolling if needed */
    max-height: 100vh; /* Limit maximum height */
}

.products {
    flex: 3; /* Products take up 3/4 of the space */
    overflow-x: auto; /* Enable horizontal scrolling */
}

.tab-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px; /* Adjust gap between tabs */
}

.tab {
    width: calc(25% - 20px); /* Each tab takes up 25% width with 20px gap */
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px; /* Adjust margin between tabs */
}
</style>