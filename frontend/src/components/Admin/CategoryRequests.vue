<script setup>
import { onMounted } from "vue";
import { categoryRequestStore } from "../../store/miscStore";

onMounted(() => {
  categoryRequestStore.get();
});
</script>
<template>
  <div>
    <h3 class="text-left mb-0">Pending Category Approvals</h3>
    <div v-if="Object.keys(categoryRequestStore.catRequests || {}).length <= 0">
      <p class="text-left">No pending category requests</p>
    </div>
    <div class="card-deck">
      <div
        class="card bg-dark text-white"
        v-for="(value, key) in categoryRequestStore.catRequests"
        :key="key"
      >
        <!-- <img class="card-img-top" src="..." alt="Card image cap" /> -->
        <div class="card-body">
          <h5 class="card-title">{{ value.name }}</h5>
          <p class="card-content">{{ value.description }}</p>
          <div class="d-flex justify-content-center" style="gap: 10px">
            <button
              class="btn btn-outline-danger btn-sm"
              @click="categoryRequestStore.reject(key)"
            >
              Reject
            </button>
            <button
              class="btn btn-success btn-sm"
              @click="categoryRequestStore.approve(key)"
            >
              Approve
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
