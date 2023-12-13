<script setup>
import { productStore } from "../store/productStore.js";
import { categoryStore } from "../store/miscStore.js";
import { onMounted, reactive, ref } from "vue";
import { userStore } from "@/store/userStore";
import { cartStore } from "@/store/cartStore";

let x = ref("");
let quantity = reactive({});
let buy = reactive({});

function applyCategory() {
  if (productStore.selectedCat == "all") {
    return productStore.products;
  } else {
    return Object.values(productStore.products).filter(
      (products) => products.cat == productStore.selectedCat
    );
  }
}

onMounted(async () => {
  await productStore.get();
  await categoryStore.get();

  if (userStore.token) {
    await cartStore.get();
    for (x in productStore.products) {
      let y = productStore.products[x].name;
      if (incart(y)) {
        buy[y] = true;
      } else {
        buy[y] = false;
      }
    }
    console.log(buy);
  }
});

function incart(key) {
  for (x in cartStore.cart) {
    if (key == cartStore.cart[x].name) {
      return true;
    }
  }
  return false;
}

function quant() {
  for (x in productStore.products) {
    console.log(x);
    quantity[x] = 0;
  }
}

function viewcat(key) {
  quant();
  productStore.selectedCat = key;
}

function addcart(key, name) {
  if (userStore.token) {
    console.log(key);
    let data = {
      p_id: key,
      qty: quantity[key],
      user_id: localStorage.getItem("id"),
    };
    console.log(quantity[key]);
    console.log(data);
    cartStore.add_cart(data);
    buy[name] = true;
  } else {
    console.log(userStore.isLoggedIn);
    console.log("not logged in!!!");
  }
}
</script>
<template>
  <div class="main">
    <div class="col card">
      <!-- Category list -->
      <ul class="list-group list-group-flush">
        <li
          class="list-group-item text-uppercase"
          :class="productStore.selectedCat == 'all' && 'bg-info text-white'"
          @click="viewcat('all')"
        >
          ALL
        </li>
        <li
          class="list-group-item text-uppercase"
          v-for="(value, key) in categoryStore.cat_new"
          :class="productStore.selectedCat == key ? 'bg-info text-white' : ''"
          :key="key"
          @click="viewcat(key)"
        >
          {{ value.name }}
        </li>
      </ul>
    </div>

    <div class="products parent">
      <div
        class="card border-success mb-3 child"
        style="max-width: 18rem"
        v-for="(value, key) in applyCategory()"
        :key="key"
      >
        <div
          class="card-header bg-transparent border-success text-uppercase font-weight-bold"
        >
          {{ value.name }}
        </div>
        <div v-if="buy[value.name]">
          <div class="card-body text-success">
            <h5 class="card-title">₹{{ value.price }}</h5>
            <p class="card-text">{{ value.desc }}</p>
          </div>
          <a class="btn btn-primary text-white">ADDED TO CART</a>
        </div>
        <div v-else>
          <div v-if="value.stock == 0">
            <div class="card-body text-success">
              <h5 class="card-title">₹{{ value.price }}</h5>
              <p class="card-text">{{ value.desc }}</p>
            </div>
            <a class="btn btn btn-danger text-white">OUT OF STOCK</a>
          </div>
          <div v-else>
            <div class="card-body text-success">
              <h5 class="card-title">₹{{ value.price }}</h5>
              <p class="card-text">{{ value.desc }}</p>
              <input
                class="card-text"
                v-model="quantity[value.id]"
                type="number"
                min="0"
                :max="value.stock"
                placeholder="Quantity"
              />
            </div>
            <a @click="addcart(value.id, value.name)" class="btn btn-primary text-white"
              >ADD TO CART</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.main {
  display: flex;
}

.col {
  flex: 1;
  cursor: pointer;
}

.products {
  flex: 3;
}

.parent {
  display: flex;
  flex-wrap: wrap;
}

.child {
  flex: 1 0 30%;
  margin-right: 10px;
}
</style>
