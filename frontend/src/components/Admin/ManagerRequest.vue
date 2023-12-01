<script setup>
import { onMounted } from "vue";
import { adminStore } from "../../store/adminStore";

onMounted(() => {
  adminStore.getManagerRequests();
});
</script>
<template>
  <!-- <div>
    <h1>MANAGER REQUEST LIST</h1>
    <ul>
      <li v-for="(value, key) in adminStore.managerRequests" :key="key">
        {{ value }}
        <button @click="approve(key)">Approve</button>
      </li>
    </ul>
  </div> -->
  <div class="card-deck">
    <h3 class="text-left mb-0">Pending Approvals</h3>
    <div
      class="card bg-dark text-white"
      v-for="(value, key) in adminStore.managerRequests"
      :key="key"
    >
      <!-- <img class="card-img-top" src="..." alt="Card image cap" /> -->
      <div class="card-body">
        <h5 class="card-title">{{ value }}</h5>
        <div class="d-flex justify-content-center" style="gap: 10px">
          <button
            class="btn btn-outline-danger btn-sm"
            @click="adminStore.rejectManagerRequest(key)"
          >
            Reject
          </button>
          <button
            class="btn btn-success btn-sm"
            @click="adminStore.approveManagerRequest(key)"
          >
            Approve
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
