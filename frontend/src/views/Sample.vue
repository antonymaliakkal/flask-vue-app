<template>
  <h1>HOME</h1>
  <br /><br />
  <div class="samp">
    <div>
      <LogIn />
    </div>
    <div>
      <SignUp />
    </div>
  </div>
</template>

<script>
import LogIn from "@/components/LogIn.vue";
import SignUp from "@/components/SignUp.vue";

export default {
  name: "HomePage",
  components: {
    LogIn,
    SignUp,
  },
};
</script>

<style>
.samp {
  display: flex;
  justify-content: space-around;
}
</style>
