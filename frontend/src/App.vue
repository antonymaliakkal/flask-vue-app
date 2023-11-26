<template>
  <!-- <router-link to="/login">Sample</router-link> -->
  <!-- <HomePage/> -->
  <!-- <NavBar/> -->
  <div>
    <router-view></router-view>
  </div>
  </template>

<script>
  // import HomePage from './components/HomePage.vue'
  //  import NavBar from './views/Navbar.vue' 

export default {
  name: 'App',
  components: {}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
