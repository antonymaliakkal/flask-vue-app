<script setup>
    // import  { productStore } from '../store/productStore.js'
    // import { categoryStore } from '@/store/miscStore';
    // import { userStore } from '@/store/userStore';
    import { cartStore } from '@/store/cartStore';
    import { onMounted} from 'vue';

  let name = localStorage.getItem('username')

   onMounted(async () => {
    await cartStore.get();
   }) 


   function cart(key) {
    cartStore.delete_cart(key);
    cartStore.get();
   }

   function multiply(a,b) {
    var num =  a*b
    return num.toLocaleString('en-IN')
   }

   function total() {
      let t = 0
      let y = 0
      let x = 0
      for(x in cartStore.cart){
          y = cartStore.cart[x].price * cartStore.cart[x].quantity
          t = t + y
      }

      return t.toLocaleString('en-IN')
   }


   function checkout() {
      cartStore.order()
      cartStore.get()
   }

</script>
<template>
    <div class="main">
      <div class="sub1">
      <div class="container"  v-for="(value,key) in cartStore.cart" :key="key">
          <div class="row m-3 p-2 border rounded">
            <div class="col-sm text-uppercase font-weight-bold">
              {{value.name}}
            </div>
            <div class="col-sm">
              {{value.quantity}} nos
            </div>
            <div class="col-sm">
              ₹{{ multiply(value.price,value.quantity) }}
            </div>
            <div class="col-sm">
              <a @click="cart(value.id)" class="btn btn-primary text-white">Delete</a>
            </div>
          </div>
      </div>
    </div>
    <div class="card bg-primary text-white text-center p-3">
        <div>
          <h5>BILLING DETAILS</h5>
          <p>USER NAME : {{ name }}</p>
          <p>TOTAL : ₹{{ total() }}</p>
          <a  @click="checkout()" class="btn btn-success text-white">Checkout</a>

        </div>
    </div>
    </div>


</template> 
<style>
  .main{
    display: flex;
  }

  .sub1 {
    display : flex;
    flex-direction: column;
    flex : 3;
  }

  .sub2 {
    flex : 1;
  }
</style>