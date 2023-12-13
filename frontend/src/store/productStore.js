// import router from '@router';
import axios from 'axios';
import { reactive } from 'vue';

const initProdObj = {
  name: '',
  desc: '',
  price: '',
  stock: '',
  cat: ''
}

const productStore = reactive({
  products: {},
  prodId: '',
  prodPos: '',
  prodObj: {...initProdObj},
  search : '',
  selectedCat: 'all',
  async get() {
    console.log('product store')
    await axios.get('http://localhost:5000/view_product')
      .then(response => {
        this.products = response.data.product;
      })
  },
  async add() {
    axios.post('http://localhost:5000/create_product', { name: this.prodObj.name, desc: this.prodObj.desc, price: this.prodObj.price, stock: this.prodObj.stock, cat_id: this.prodObj.cat })
      .then(response => {
        console.log(response.data['message'])
        this.products[this.prodObj.id] = this.prodObj
        this.prodObj = {...initProdObj}
      })
    window.alert('Product addedd successfully!');
  },
  async delete() {
    axios.post('http://localhost:5000/delete_product', { pid: this.prodId })
      .then(response => {
        console.log(response.data.message);
        window.alert('Product deleted successfully!');
        delete this.products[this.prodId]
        this.prodId = this.prodPos = ''
      })
  },
  async edit() {
    axios.post('http://localhost:5000/edit_product', {
      id: this.prodObj.id,
      name: this.prodObj.name,
      description: this.prodObj.desc,
      price: this.prodObj.price,
      stock: this.prodObj.stock,
      cat_id: this.prodObj.cat
    })
      .then(response => {
        console.log(response.data);
        window.alert('Product edited successfully!');
        this.products[this.prodId] = this.prodObj
        this.prodObj = initProdObj
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
  },

})
export { productStore }