<template>
  <div>
    <div v-if="first_component">
      <LogIn />
      <button @click="log">SIGNUP</button>
    </div>

    <div v-else>
      <SignUp />
      <button @click="log">LOGIN</button>
    </div>
  </div>
</template>
<script>
import LogIn from "../components/LogIn.vue";
import SignUp from "./../components/SignUp.vue";

export default {
  name: "RegisterPage",
  data() {
    return {
      first_component: true,
    };
  },
  components: {
    LogIn,
    SignUp,
  },
  methods: {
    log() {
      this.first_component = !this.first_component;
    },
  },
};
</script>
