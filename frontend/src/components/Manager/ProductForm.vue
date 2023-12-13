<script setup>
import { onMounted } from "vue";
import { managerStore } from "../../store/managerStore";
import { categoryStore } from "../../store/miscStore";
import { productStore } from "../../store/productStore";

onMounted(() => {
  categoryStore.get();
});
</script>
<template>
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="SignIn/SignUp" v-if="managerStore.dialogueType == 1">
          Add Product
        </h5>
        <h5
          class="modal-title"
          id="SignIn/SignUp"
          v-else-if="managerStore.dialogueType == 2"
        >
          Edit Product
        </h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="row mb-3">
            <div class="col">
              <input
                type="text"
                class="form-control"
                placeholder="Name"
                v-model="productStore.prodObj.name"
              />
            </div>
            <div class="col">
              <select v-model="productStore.prodObj.cat" style="width: 100%">
                <option v-for="i in categoryStore.categories" :key="i.key" :value="i.key">
                  {{ i.value.name }}
                </option>
              </select>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col">
              <!-- <label for="description">Description</label> -->
              <textarea
                class="form-control"
                id="description"
                rows="3"
                placeholder="Description"
                v-model="productStore.prodObj.desc"
              ></textarea>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <input
                type="text"
                class="form-control"
                placeholder="Price"
                v-model="productStore.prodObj.price"
              />
            </div>
            <div class="col">
              <input
                type="text"
                class="form-control"
                placeholder="Stock"
                v-model="productStore.prodObj.stock"
              />
            </div>
          </div>
        </form>
        <div class="dropdown-divider"></div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-outline-danger" data-dismiss="modal">
          Close
        </button>
        <button
          type="button"
          class="btn btn-success"
          data-dismiss="modal"
          v-if="managerStore.dialogueType == 1"
          @click="productStore.add()"
        >
          Add
        </button>
        <button
          type="button"
          class="btn btn-success"
          data-dismiss="modal"
          v-if="managerStore.dialogueType == 2"
          @click="productStore.edit()"
        >
          Save
        </button>
      </div>
    </div>
  </div>
</template>
