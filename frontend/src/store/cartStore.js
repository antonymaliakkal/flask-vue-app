import axios from "axios";
import { reactive } from "vue";
import { userStore } from "./userStore";

const cartStore = reactive({
    cart : {},
    async get(){

        const token = userStore.token
        const config = {
            headers: {
            Authorization: `Bearer ${token}`,
            },
        };

        await axios.get('http://localhost:5000/view_product' , config)
            .then(response => {
                console.log('fetched cart')
                 

            })
    },
    async add_cart(data){
        console.log('entered')
        const token = userStore.token
        const config = {
            headers: {
            Authorization: `Bearer ${token}`,
            },
        };
        await axios.post('http://localhost:5000/cart' , data , config)
        .then(response => {
            console.log('added to cart',response)
        })
    

    }
})
    
export { cartStore }