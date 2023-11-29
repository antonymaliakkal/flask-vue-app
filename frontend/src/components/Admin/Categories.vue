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
// export default {
//   name: "EditCat",
//   data() {
//     return {
//       isModalVisible: false,
//       editedCategory: { id: null, name: "", desc: "" },
//     };
//   },
//   mounted() {

//   },
//   methods: {
//     editCategory(category) {
//       this.isModalVisible = true;
//       console.log(category);
//       this.editedCategory.id = category;
//       this.editedCategory.name = category.value.name;
//       this.editedCategory.desc = category.value.desc;
//     },
//     closeModal() {
//       this.isModalVisible = false;
//     },
//   },
// };
</script>

<template>
  <v-fragment>
    <div>
      <h3 class="text-left">Categories</h3>
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
