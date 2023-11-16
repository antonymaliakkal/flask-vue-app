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
    <select v-model="category_id">
        <option v-for="(value,key) in category" :key="key">
            {{ key }}: {{ value }} 
       </option>
    </select>
    <button @click="submit(catid)">Submit</button>
</template>
<script>
import axios from 'axios';

    export default{
        name : 'ProdCreate',
        data() {
            return{
                category : {}
            }
        },
        mounted(){
            axios.get('http://localhost:5000/create_product')
                .then(response => {
                    this.category = response.data.category;
                })
        },
        methods : {
            submit(catid){
                axios.post('http://localhost:5000/create_product',{name : this.name , desc : this.desc , price : this.price , stock : this.stock , cat_id : catid})
                    .then(response => {
                        console.log(response.data['message'])
                    })
            }
        }
    }
</script>