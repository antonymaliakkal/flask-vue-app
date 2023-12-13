<script setup>
import { onMounted } from "vue";
import { managerStore } from "../../store/managerStore";
import { productStore } from "../../store/productStore";
import ProductForm from "./ProductForm.vue";
import ProductDelete from "./ProductDelete";

onMounted(() => {
  productStore.get();
});

const addProduct = () => {
  managerStore.dialogueType = 1;
};

const deleteProd = (id, index) => {
  managerStore.dialogueType = 3;
  productStore.prodId = id;
  productStore.prodPos = index;
};

const editProduct = (product) => {
  managerStore.dialogueType = 2;
  productStore.prodObj = product;
  productStore.prodId = product.id;
};
</script>
<template>
  <v-fragment>
    <div>
      <div class="category-head d-flex justify-content-between align-items-center py-2">
        <h3 class="text-left mb-0">Products</h3>
        <button
          class="btn btn-success"
          data-toggle="modal"
          data-target="#adminModal"
          @click="addProduct()"
        >
          Add Product
        </button>
      </div>
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Si No</th>
            <th scope="col">Name</th>
            <th scope="col">Category</th>
            <th scope="col">Description</th>
            <th scope="col">Price</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key, index) in productStore.products" :key="key">
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ value.name }}</td>
            <td>{{ value.cat }}</td>
            <td>{{ value.desc }}</td>
            <td>{{ value.price }}</td>
            <td class="d-flex justify-content-center" style="gap: 5px">
              <button
                @click="editProduct({ ...value, id: key })"
                type="button"
                class="btn btn-outline-warning btn-sm"
                data-toggle="modal"
                data-target="#adminModal"
              >
                Edit
              </button>
              <button
                @click="deleteProd(key, index)"
                type="button"
                class="btn btn-outline-danger btn-sm"
                data-toggle="modal"
                data-target="#adminModal"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div
      class="modal fade"
      id="adminModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="AdminModal"
      aria-hidden="true"
    >
      <ProductForm
        v-if="managerStore.dialogueType == 1 || managerStore.dialogueType == 2"
      />
      <ProductDelete v-else />
    </div>
  </v-fragment>
</template>
