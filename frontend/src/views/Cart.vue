<script setup>
    // import  { productStore } from '../store/productStore.js'
    // import { categoryStore } from '@/store/miscStore';
    // import { userStore } from '@/store/userStore';
    import { cartStore } from '@/store/cartStore';
    import { onMounted} from 'vue';

    // let products = reactive({})
    // let selectede = ref('')
    // let quantity = ref(0)

   onMounted(async () => {
    await cartStore.get();
   }) 

</script>
<template>
    <h2>CART</h2>

    
    <div class="container"  v-for="(value,key) in cartStore.cart" :key="key">
        <div class="row m-3 p-2 border rounded">
          <div class="col-sm">
            {{value.name}}
          </div>
          <div class="col-sm">
            {{value.quantity}}
          </div>
          <div class="col-sm">
            {{value.price}}
          </div>
          <div class="col-sm">
          <a href="#" class="btn btn-primary text-white">Delete</a>
          </div>
        </div>
      </div>

      <div class="btn-group" role="group" aria-label="Basic example">
        <button type="button" class="btn btn-secondary rounded-circle">-</button>
        <button type="button" class="btn btn-secondary">Quantity</button>
        <button type="button" class="btn btn-secondary rounded-circle">+</button>
      </div>



</template> 
