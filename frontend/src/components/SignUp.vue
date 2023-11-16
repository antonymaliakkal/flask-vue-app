<template>
    <h2>SIGNUP</h2>
    EMAIL :    <input v-model="email" type="text"><br><br>
    PASSWORD : <input v-model="password" type="text">
    <br><br>

    MANAGER : <input type="radio" name="role" value="manager" v-model="role">
    <br>
    USER : <input type="radio" name="role" value="user" v-model="role">
    <br>
    <br>

    <button @click="submitForm">Submit</button>
    <br><br>
    <router-link to="/login">Already registered???</router-link>


</template>

<script>
    
    import axios from 'axios';


    export default{
        name : 'SignUp',
        methods: {
            submitForm() {
            // Move the Axios POST request to the script section
            // You can send the email data in the request
    
            axios.post('http://localhost:5000/signup', { email : this.email , password : this.password , role : this.role})
                .then(response => {
                console.log(response.data['message']);
                   });
                },
             },
    }

</script>