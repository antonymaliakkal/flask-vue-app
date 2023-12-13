<style>
@import "../styles/Component/navbar.css";
</style>

<script setup>
import { userStore } from "../store/userStore";
import LogIn from "../components/LogIn.vue";
import { productStore } from "../store/productStore";
import router from "@/router";

function cart() {
  router.push("/cart");
}

function home() {
  router.push("/");
}

function exportcsv() {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${userStore.token}`,
    },
    body: JSON.stringify({ mail: userStore.username }),
  };
  fetch("http://localhost:5000/productsummary", options)
    .then((response) => {
      if (response.status == 200) {
        alert("Product summary has been mailed!");
      }
    })
    .catch((err) => {
      console.error(err);
    });
}
</script>

<template>
  <v-fragment>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#" @click="home()">Grocery Store</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <form class="form-inline my-2 my-lg-0">
          <input
            class="form-control mr-sm-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
            v-model="productStore.search"
          />
          <button
            class="btn btn-outline-success my-2 my-sm-0"
            type="button"
            @click="productStore.searching()"
          >
            Search
          </button>
        </form>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item dropdown" v-if="!userStore.token">
            <button
              class="btn btn-outline-success"
              type="button"
              data-toggle="modal"
              data-target="#loginModal"
            >
              Login
            </button>
          </li>
          <li class="nav-item dropdown" v-else>
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              {{ userStore.username }}
            </a>
            <div
              class="dropdown-menu"
              style="right: 0; left: unset"
              aria-labelledby="navbarDropdown"
            >
              <p class="dropdown-item" @click="userStore.logOut()">LogOut</p>
            </div>
          </li>
          <li class="nav-item">
            <button
              class="btn btn-outline-success my-2 my-sm-0"
              type="button"
              @click="cart()"
              v-if="userStore.role == 'user'"
            >
              Cart
            </button>
            <button
              class="btn btn-outline-success my-2 my-sm-0"
              type="button"
              @click="exportcsv()"
              v-else-if="userStore.role == 'manager'"
            >
              Export
            </button>
          </li>
        </ul>
      </div>
    </nav>
    <div
      class="modal fade"
      id="loginModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="SignIn/SignUp"
      aria-hidden="true"
    >
      <LogIn />
    </div>
  </v-fragment>
</template>
