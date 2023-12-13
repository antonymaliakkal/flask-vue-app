<script setup>
import { managerStore } from "../store/managerStore";
import Products from "../components/Manager/Products.vue";
import CategoryForm from "../components/Admin/CategoryForm.vue";
</script>
<template>
  <div class="d-flex">
    <div class="d-flex flex-column px-4 py-3" style="gap: 10px">
      <button type="button" @click="managerStore.path = 1" class="btn btn-primary">
        Products
      </button>
      <button type="button" @click="managerStore.path = 2" class="btn btn-success">
        Categories
      </button>
    </div>
    <div class="content w-100 p-3">
      <Products v-if="managerStore.path == 1" />
      <CategoryForm v-if="managerStore.path == 2" />
    </div>
  </div>
</template>
