// import router from '@router';
import axios  from 'axios';
import {reactive} from 'vue';

const  productStore = reactive({
  products : {},
  async get(){
    console.log('product store')
    await axios.get('http://localhost:5000/view_product')
        .then(response => {
            this.products = response.data.product;
        })
  },


})

export { productStore }