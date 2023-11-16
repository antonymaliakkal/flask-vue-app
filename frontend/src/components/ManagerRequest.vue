<template>
    <div>
        <h1>MANAGER REQUEST LIST</h1>
        <ul>
            <li v-for="(value,key) in user" :key="key">
                {{ key }}: {{ value }}
                <button @click="approve(key)">Approve</button>

            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: 'ManagerRequest',
    data() {
        return {
            user: {}
        };
    },
    mounted() {
        
    axios.get('http://localhost:5000/manager_request')
        .then(response => {
            this.user = response.data.user;
            console.log(this.user);
        })
        .catch(error => {
            console.error(error);
        });
    },
    methods : {
        approve(key) {
            axios.post('http://localhost:5000/manager_request' , {key : key})
                .then(response => {
                    console.log(response.data['message'])
                    window.location.reload();
                })
        
            // window.location.reload();
        }
    },
}
</script>

