import axios from "axios";
import { reactive } from "vue";
import { userStore } from "./userStore";

const cartStore = reactive({
    cart : {},
    config: {headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      }},
    async get(){
        await axios.get('http://localhost:5000/cart', this.config)
            .then(response => {
                console.log('fetched cart',response.data)
                this.cart = response.data['cart']
            })
    },
    async add_cart(data){
        console.log('add to cart function')
        if(userStore.token) {
            await axios.post('http://localhost:5000/cart' , data , this.config)
            .then(response => {
                console.log('added to cart',response)
            })
        }
    },
    async delete_cart(data){
        console.log('delete cart function')
        console.log(data)
        if(userStore.token) {
            await axios.post('http://localhost:5000/cart_delete' , {'id' : data} , this.config)
            .then(response => {
                console.log(response.data['message'])
            })
        }
    }
})

export { cartStore }