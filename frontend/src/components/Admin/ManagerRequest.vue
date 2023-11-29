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
            user: {},
            
        };
    },
    mounted() {
        
    const token = localStorage.getItem('token')
    const config = {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    };


    axios.get('http://localhost:5000/manager_request' , config)
        .then(response => {
            this.user = response.data.user;
            console.log(this.user);
            const token = localStorage.getItem('role'); // Retrieve token from local storage
            console.log('role : ' , token)
        })
        .catch(error => {
            console.error(error);
        });
    },
    methods : {

        approve(key) {

            const token = localStorage.getItem('token')
            const config = {
                headers: {
                Authorization: `Bearer ${token}`,
                },
            };


            axios.post('http://localhost:5000/manager_request' , {key : key} , config)
                .then(response => {
                    console.log(response.data['message'])
                    window.location.reload();
                })
        
            // window.location.reload();
        }
    },
}
</script>