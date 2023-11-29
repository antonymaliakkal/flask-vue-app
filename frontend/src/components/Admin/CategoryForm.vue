<script setup>
import { adminStore } from "../../store/adminStore";
import { categoryStore } from "../../store/miscStore";
</script>
<template>
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="SignIn/SignUp" v-if="adminStore.dialogueType == 1">
          Add Category
        </h5>
        <h5
          class="modal-title"
          id="SignIn/SignUp"
          v-else-if="adminStore.dialogueType == 2"
        >
          Edit Category
        </h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form class="px-4 py-3">
          <div class="form-group">
            <label for="exampleDropdownFormEmail1">Name</label>
            <input
              type="text"
              class="form-control"
              id="name"
              placeholder="Category Name"
              v-model="categoryStore.catName"
            />
          </div>
          <div class="form-group">
            <label for="exampleDropdownFormPassword1">Description</label>
            <input
              type="textarea"
              class="form-control"
              id="description"
              placeholder="Category Description"
              v-model="categoryStore.catDesc"
            />
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
          v-if="adminStore.dialogueType == 1"
        >
          Add
        </button>
        <button
          type="button"
          class="btn btn-success"
          data-dismiss="modal"
          v-if="adminStore.dialogueType == 2"
          @click="categoryStore.edit()"
        >
          Save
        </button>
      </div>
    </div>
  </div>
</template>
