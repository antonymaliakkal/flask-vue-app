<template>
  <!-- <router-link to="/login">Sample</router-link> -->
  <!-- <HomePage/> -->
  <!-- <NavBar/> -->
  <div>
    <NavBar />

    <router-view></router-view>
  </div>
</template>

<script>
// import HomePage from './components/HomePage.vue'
import NavBar from "./components/NavBar.vue";
export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
