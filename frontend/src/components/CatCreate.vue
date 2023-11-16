<template>
    <h1>CREATE CATEGORY</h1>
    NAME : <input v-model="name" type="text">
    <br>
    DESCRIPTION : <input v-model="desc" type="text">
    <br><br>
    <button @click="submit">Submit</button>
</template>
<script>
import axios from 'axios';

    export default{
        name : 'CatCreate',
        methods : {
            submit(){
                axios.post('http://localhost:5000/create_category',{name : this.name , desc : this.desc})
                    .then(response => {
                        console.log(response.data['message'])
                    })
            }
        }
    }
</script>