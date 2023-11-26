<template>
    <div>
      <h1>Welcome Admin!</h1>
  
      <div>
        <button @click="showManagerRequest">Approve Managers</button>
        <br><br>
        <button @click="showCreateCat">Create Category</button>
        <br><br>
        <button @click="showEditCat">Edit Category</button>
      </div>
  
      <div v-if="currentComponent === 'ManagerRequest'">
        <ManagerRequest />
      </div>
      <div v-else-if="currentComponent === 'CreateCat'">
        <CreateCat />
      </div>
      <!-- <div v-else-if="currentComponent === 'EditCat'">
        <EditCat />
      </div> -->
    </div>
  </template>
  
  <script>
  import ManagerRequest from './../components/ManagerRequest.vue'
  import CreateCat from './../components/CatCreate.vue';
//   import EditCat from './../components/EditCat.vue';
  
  export default {
    name : 'AdminPage',
    components: {
      ManagerRequest,
      CreateCat,
      
    },
    data() {
      return {
        currentComponent: null,
      };
    },
    methods: {
      showManagerRequest() {
        this.currentComponent = 'ManagerRequest';
      },
      showCreateCat() {
        this.currentComponent = 'CreateCat';
      },
    //   showEditCat() {
    //     this.currentComponent = 'EditCat';
    //   },
    },
  };
  </script>
 