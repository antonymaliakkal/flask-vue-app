<template>
  <h2>SIGNUP</h2>
  EMAIL : <input v-model="email" type="text" /><br /><br />
  PASSWORD : <input v-model="password" type="text" /> <br /><br />

  MANAGER : <input type="radio" name="role" value="manager" v-model="role" />
  <br />
  USER : <input type="radio" name="role" value="user" v-model="role" />
  <br />
  <br />

  <button @click="submitForm">Submit</button>
  <br /><br />
  <!-- <router-link to="/login">Already registered???</router-link> -->
</template>

<script></script>
