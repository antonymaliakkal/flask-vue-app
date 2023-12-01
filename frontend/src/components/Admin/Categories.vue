<script setup>
import { categoryStore } from "../../store/miscStore";
import { onMounted } from "vue";
import CategoryForm from "./CategoryForm.vue";
import CategoryDelete from "./CategoryDelete.vue";
import { adminStore } from "../../store/adminStore";

onMounted(() => {
  categoryStore.get();
});

const editCat = ({ key, value }, index) => {
  adminStore.dialogueType = 2;
  categoryStore.catName = value.name;
  categoryStore.catDesc = value.desc;
  categoryStore.catId = key;
  categoryStore.catPos = index;
};

const deleteCat = (id, index) => {
  adminStore.dialogueType = 3;
  categoryStore.catId = id;
  categoryStore.catPos = index;
};

const addCategory = () => {
  adminStore.dialogueType = 1;
  categoryStore.catName = "";
  categoryStore.catDesc = "";
};
</script>

<template>
  <v-fragment>
    <div>
      <div class="category-head d-flex justify-content-between align-items-center py-2">
        <h3 class="text-left mb-0">Categories</h3>
        <button
          class="btn btn-success"
          data-toggle="modal"
          data-target="#adminModal"
          @click="addCategory()"
        >
          Add category
        </button>
      </div>
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Si No</th>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key) in categoryStore.categories" :key="key">
            <th scope="row">{{ key + 1 }}</th>
            <td>{{ value.value.name }}</td>
            <td>{{ value.value.desc }}</td>
            <td class="d-flex justify-content-center" style="gap: 5px">
              <button
                @click="editCat(value, key)"
                type="button"
                class="btn btn-outline-warning btn-sm"
                data-toggle="modal"
                data-target="#adminModal"
              >
                Edit
              </button>
              <button
                @click="deleteCat(value.key, key)"
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
      <CategoryForm v-if="adminStore.dialogueType == 1 || adminStore.dialogueType == 2" />
      <CategoryDelete v-else />
    </div>
  </v-fragment>
</template>
