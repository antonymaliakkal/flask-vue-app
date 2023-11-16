<template>
    <div>
        <h1>LOGIN</h1>
        <input v-model="email" type="text" placeholder="Email">
        <br><br>
        <input v-model="password" type="text" placeholder="Password">
        <br>
        <button @click="login">Submit</button>
    
        <br><br>
        <router-link to="/signup">New user</router-link>

    
    </div>
</template>


<script>

import axios from 'axios';

export default {
  name: 'LogIn',
  data() {
    return {
      email: '',
    };
  },
  methods: {
    login() {
      // Move the Axios POST request to the script section
      // You can send the email data in the request
      axios.post('http://localhost:5000/login', { email : this.email , password : this.password })
        .then(response => {
          console.log(response.data['message']);
          if(response.data['login'])
             this.$router.push('/signup')
        });
    },
  },
};
</script>