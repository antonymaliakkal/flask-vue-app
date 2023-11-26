<template>
    <div>
        <h1>DELETE PRODUCT</h1>
        <ul>
            <li v-for="(value,key) in category" :key="key">
                    {{ value }}
                <button @click="delete_products(key)">Delete</button>

            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name : 'DeleteCategory',
        data() {
            return {
                category : {}
            }
        },
        mounted() {
            axios.get('http://localhost:5000/view_category')
            .then(response => {
                this.category = response.data.category;
                console.log('products fetched');
            })
            .catch(error => {
                console.error(error);
            });
        },
        methods : {
            delete_products(key) {
                axios.post('http://localhost:5000/delete_category', {cid : key})
                .then(response => {
                    console.log(response.data.message);
                    window.alert('Product deleted successfully!');
                    window.location.reload();
                })
            }
        }
    }   
</script>