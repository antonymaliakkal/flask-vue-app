// import router from '@router';
import axios  from 'axios';
import {reactive} from 'vue';

const  productStore = reactive({
  products : {},
  search : '',
  async get(){
    console.log('product store')
    await axios.get('http://localhost:5000/view_product')
        .then(response => {
            this.products = response.data.product;
        })
  },
  async searching(){
    console.log('searched : ',this.search); 
    console.log('products before' , this.products)
    await axios.post('http://localhost:5000/cache',{search : this.search})
      .then(response => {
          this.products = response.data.product;
          console.log(this.products)
          console.log(response.data['message']);
      })    
  }

})

export { productStore }