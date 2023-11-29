<script setup>
import { categoryStore } from "../store/miscStore";
import { onMounted } from "vue";

onMounted(() => {
  console.log("mounted");
  categoryStore.get();
});
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
//     savechanges() {
//       console.log("save changes");
//       // const a = this.editCategory.id
//       console.log(this.editedCategory.key);
//       console.log(this.$data);
//       axios
//         .patch("http://localhost:5000/edit_category", this.editedCategory)
//         .then((response) => {
//           this.isModalVisible = false;
//           console.log(response.data["message"]);
//           window.location.reload();
//         });
//     },
//     deleteCategory(category) {
//       console.log(category);
//       axios
//         .post("http://localhost:5000/delete_category", { cat: category })
//         .then((response) => {
//           console.log(response.data["message"]);
//           window.location.reload();
//         });
//     },
//   },
// };
</script>

<template>
  <div>
    <h2>EDIT CATEGORY</h2>
    <div class="main">
      <div class="sub1" v-for="key in categoryStore.categories" :key="key">
        {{ key.value.name }}
        <br /><br />
        {{ key.value.desc }}

        <div class="sub2">
          <button @click="editCategory(key)">EDIT</button>
          <button @click="deleteCategory(key)">DELETE</button>
        </div>
      </div>
    </div>

    <div v-if="isModalVisible" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Edit Category</h2>
        <label>Category Name:</label>
        <input type="text" v-model="editedCategory.name" />
        <br />
        <label>Category Description:</label>
        <input type="text" v-model="editedCategory.desc" />
        <br />
        <button @click="savechanges">Save</button>
      </div>
    </div>
  </div>
</template>

<style>
.main {
  display: flex;
  justify-content: space-evenly;
}

.sub1 {
  background-color: antiquewhite;
}

.sub2 {
  display: flex;
  justify-content: space-between;
}
</style>
