import axios from "axios";
import { reactive } from "vue";

const categoryStore = reactive({
  categories: [],
  cat_new: {},
  catName: '',
  catDesc: '',
  catId: '',
  catPos: '',
  async get() {
    if (this.categories.length <= 0) {
      axios.get('http://localhost:5000/edit_category')
        .then(response => {
          this.categories = response.data.category;
          this.cat_new = response.data.category_new;
        })
    }
  },
  async edit() {
    if (this.catName && this.catDesc && this.catId) {
      await axios
        .patch("http://localhost:5000/edit_category", { id: this.catId, name: this.catName, desc: this.catDesc })
        .then((response) => {
          if (response.status == 200) {
            this.categories[this.catPos] = response.data.data
            this.catName = this.catDesc = this.catId = this.catPos = ''
          } else {
            alert('An error occured')
          }
        });
    }
  },
  async delete() {
    axios
      .post("http://localhost:5000/delete_category", { id: this.catId })
      .then((response) => {
        if (response.status == 200) {
          this.categories.splice(this.catPos, 1)
          this.catId = this.catPos = ''
        } else {
          alert('An error occured')
        }
      });
  },
  async add(){
    axios
      .post("http://localhost:5000/create_category", { name: this.catName, desc: this.catDesc })
      .then((response) => {
        if (response.status == 200) {
          this.categories.push(response.data.data)
        } else {
          alert('An error occured')
        }
      });
  }
})

export {
  categoryStore
}