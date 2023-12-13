/* eslint-disable */
<style>
@import "../styles/admin.css";
</style>
<script setup>
import Categories from "../components/Admin/Categories.vue";
import ManagerRequest from "../components/Admin/ManagerRequest.vue";
import CategoryRequest from "../components/Admin/CategoryRequests.vue";
import { adminStore } from "../store/adminStore";
</script>
<template>
  <div class="d-flex">
    <div class="d-flex flex-column px-4 py-3" style="gap: 10px">
      <button type="button" @click="adminStore.path = 1" class="btn btn-primary">
        Categories
      </button>
      <button type="button" @click="adminStore.path = 2" class="btn btn-success">
        Approvals
      </button>
    </div>
    <div class="content w-100 p-3">
      <Categories v-if="adminStore.path == 1" />
      <ManagerRequest v-if="adminStore.path == 2" />
      <CategoryRequest v-if="adminStore.path == 2" />
    </div>
  </div>
</template>
