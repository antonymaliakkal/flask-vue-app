import axios from "axios";
import { reactive } from "vue";

const categoryStore = reactive({
  categories: [],
  cat_new : {},
  async get(){
    console.log('som');
    await axios.get('http://localhost:5000/edit_category')
    .then(response => {
        this.categories = response.data.category;
        this.cat_new = response.data.category_new;
    })
  }
})

export {
  categoryStore
}