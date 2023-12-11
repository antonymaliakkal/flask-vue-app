<script setup>
import { ref } from "vue";
import { userStore } from "../store/userStore";

// import { userStore } from "../store/userStore";
let isLogin = ref(true);
let email = ref("");
let password = ref("");
let role = ref("");

const swapLogin = () => {
  isLogin.value = !isLogin.value;
};

const signUp = async () => {
  const response = await userStore.signUp(email.value, password.value, role.value);
  email.value = password.value = role.value = "";
  console.log(response);
};

const logIn = async () => {
  await userStore.logIn(email.value, password.value);
  email.value = password.value = "";
};
</script>
<template>
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="SignIn/SignUp" v-if="isLogin">Sign In</h5>
        <h5 class="modal-title" id="SignIn/SignUp" v-else>Sign Up</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form class="px-4 py-3">
          <div class="form-group">
            <label for="exampleDropdownFormEmail1">Email address</label>
            <input
              type="email"
              class="form-control"
              id="email"
              placeholder="email@example.com"
              v-model="email"
            />
          </div>
          <div class="form-group">
            <label for="exampleDropdownFormPassword1">Password</label>
            <input
              type="password"
              class="form-control"
              id="password"
              placeholder="Password"
              v-model="password"
            />
          </div>
          <div class="form-group" v-if="!isLogin">
            <label for="manager-cb">Manager</label>
            <input
              type="radio"
              name="role"
              value="manager"
              id="manager-cb"
              v-model="role"
            />
            <br />
            <label for="user-cb">User</label>
            <input type="radio" name="role" value="role" id="user-cb" v-model="role" />
          </div>
          <div class="form-check" v-if="isLogin">
            <input type="checkbox" class="form-check-input" id="dropdownCheck" />
            <label class="form-check-label" for="dropdownCheck"> Remember me </label>
          </div>
        </form>
        <div class="dropdown-divider"></div>
        <p class="" @click="swapLogin()" v-if="isLogin">New around here? Sign up</p>
        <p class="" @click="swapLogin()" v-else>Already have an account? Sign In</p>
        <!-- <a class="dropdown-item" href="#">Forgot password?</a> -->
      </div>
      <div class="modal-footer">
        <button
          type="button"
          class="btn btn-primary"
          data-dismiss="modal"
          v-if="isLogin"
          @click="logIn()"
        >
          Sign In
        </button>
        <button
          type="button"
          class="btn btn-primary"
          data-dismiss="modal"
          v-else
          @click="signUp()"
        >
          Sign Up
        </button>
      </div>
    </div>
  </div>
</template>
