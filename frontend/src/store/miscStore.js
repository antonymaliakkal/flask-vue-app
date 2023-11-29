import axios from "axios";
import { reactive } from "vue";

const categoryStore = reactive({
  categories: [],
  async get(){
    console.log('som');
    axios.get('http://localhost:5000/edit_category')
    .then(response => {
        this.categories = response.data.category;
    })
  }
})

export {
  categoryStore
}