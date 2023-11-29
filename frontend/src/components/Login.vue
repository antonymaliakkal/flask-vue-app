<script setup>
// import { userStore } from "../store/userStore";
</script>
<template>
  <!-- <div>
    <h1>LOGIN</h1>
    <input v-model="this.email" type="text" placeholder="Email" />
    <br /><br />
    <input v-model="password" type="text" placeholder="Password" />
    <br />
    <button @click="userStore.logIn(email, password)">Submit</button>

    <br /><br />
    <router-link to="/signup">New user</router-link>
  </div> -->
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="SignIn/SignUp">Modal title</h5>
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
              id="exampleDropdownFormEmail1"
              placeholder="email@example.com"
            />
          </div>
          <div class="form-group">
            <label for="exampleDropdownFormPassword1">Password</label>
            <input
              type="password"
              class="form-control"
              id="exampleDropdownFormPassword1"
              placeholder="Password"
            />
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="dropdownCheck" />
            <label class="form-check-label" for="dropdownCheck"> Remember me </label>
          </div>
        </form>
        <div class="dropdown-divider"></div>
        <a class="dropdown-item" href="#">New around here? Sign up</a>
        <a class="dropdown-item" href="#">Forgot password?</a>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">SignIn</button>
      </div>
    </div>
  </div>
</template>
