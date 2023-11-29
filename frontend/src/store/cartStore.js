import axios from "axios";
import { reactive } from "vue";
import { userStore } from "./userStore";

const cartStore = reactive({
    cart : {},
    async get(){
        await axios.get('http://localhost:5000/view_product')
            .then(response => {
                console.log('fetched cart',response)
            })
    },
    async add_cart(data){
        if(userStore.isLoggedIn) {
            await axios.post('http://localhost:5000/cart' , data)
            .then(response => {
                console.log('added to cart',response)
            })
        }

    }
})

export { cartStore }