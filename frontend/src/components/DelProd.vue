<template>
    <div>
        <h1>DELETE PRODUCT</h1>
        <ul>
            <li v-for="(value,key) in products" :key="key">
                    {{ value }}
                <button @click="delete_products(key)">Delete</button>

            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name : 'DeleteProduct',
        data() {
            return {
                products : {}
            }
        },
        mounted() {
            axios.get('http://localhost:5000/view_product')
            .then(response => {
                this.products = response.data.product;
                console.log('products fetched');
            })
            .catch(error => {
                console.error(error);
            });
        },
        methods : {
            delete_products(key) {
                axios.post('http://localhost:5000/delete_product', {pid : key})
                .then(response => {
                    console.log(response.data.message);
                    window.alert('Product deleted successfully!');
                    window.location.reload();
                })
            }
        }
    }   
</script>