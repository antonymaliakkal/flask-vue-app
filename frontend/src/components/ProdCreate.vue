<template>
    <h1>CREATE PRODUCT</h1>
    NAME : <input v-model="name" type="text">
    <br>
    DESCRIPTION : <input v-model="desc" type="text">
    <br>
    PRICE : <input v-model="price" type="text">
    <br>
    STOCK : <input v-model="stock" type="text">
    <br>
    <!-- <select v-model="category_id">
        <option v-for="(value,key) in category" :key="key">
            {{ key }}: {{ value }} 
       </option> -->
       <select v-model="category_id">
       <option v-for="i in category" :key="i.key" :value="i.key">
            {{ i.value }}
       </option>

    </select>
    <button @click="submit()">Submit</button>
</template>
<script>
import axios from 'axios';

    export default{
        name : 'ProdCreate',
        data() {
            return{
                category : [],
                category_id : null
            } 
        },
        mounted(){
            axios.get('http://localhost:5000/create_product')
                .then(response => {
                    this.category = response.data.category;
                })
        },
        methods : {
            submit(){
                axios.post('http://localhost:5000/create_product',{name : this.name , desc : this.desc , price : this.price , stock : this.stock , cat_id : this.category_id})
                    .then(response => {
                        console.log(response.data['message'])
                    })
                window.alert('Product addedd successfully!');

            }
        }
    }
</script>