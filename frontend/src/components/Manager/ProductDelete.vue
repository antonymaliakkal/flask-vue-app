<script setup>
import { productStore } from "../../store/productStore";

productStore;
</script>
<template>
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="SignIn/SignUp">Delete Product</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Are you sure, you want to delete this product?</p>
        <div class="dropdown-divider"></div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-outline-success" data-dismiss="modal">
          No
        </button>
        <button
          type="button"
          class="btn btn-danger"
          data-dismiss="modal"
          @click="productStore.delete()"
        >
          Yes
        </button>
      </div>
    </div>
  </div>
</template>
