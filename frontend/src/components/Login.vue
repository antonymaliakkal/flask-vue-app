<template>
    <div>
        <input v-model="email" type="text" placeholder="Email">
        <button @click="submitForm">Submit</button>
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
    submitForm() {
      // Move the Axios POST request to the script section
      // You can send the email data in the request
      axios.post('/login_new', { name: this.email })
        .then(response => {
          console.log(response.data);
        });
    },
  },
};
</script>