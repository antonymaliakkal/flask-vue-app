import axios from "axios";
import { reactive } from "vue";

const categoryStore = reactive({
  categories: [],
  catName: '',
  catDesc: '',
  catId: '',
  catPos: '',
  async get() {
    if (this.categories.length <= 0) {
      axios.get('http://localhost:5000/edit_category')
        .then(response => {
          this.categories = response.data.category;
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
          this.categories.pop(this.catPos)
          this.catId = this.catPos = ''
        }else{
          alert('An error occured')
        }
      });
  }
})

export {
  categoryStore
}