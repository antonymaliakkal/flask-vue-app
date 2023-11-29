<template>

    <div>
        <EditCat />
        <!-- <h2>MANAGER APPROVALS</h2> -->
        <br><br>
        <ManagerRequest />
        <br><br>
        <!-- <h2>CREATE CATEGORY</h2> -->
        <CreateCat />


    </div>
        
    

  </template>
  
  <script>
  import ManagerRequest from './../components/ManagerRequest.vue'
  import CreateCat from './../components/CatCreate.vue';
  import EditCat from './../components/EditCat.vue';
  
  export default {
    name : 'AdminPage',
    components: {
      ManagerRequest,
      CreateCat,
      EditCat
      
    },
  };
  </script>
 