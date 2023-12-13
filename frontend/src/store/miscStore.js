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
  async add() {
    if (localStorage.getItem('role') == 'manager') {
      categoryRequestStore.request({ name: this.catName, description: this.catDesc })
      this.catName = ''
      this.catDesc = ''
    } else {
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
  }
})

const initCatObj = {
  name: '',
  descripiton: ''
}
const categoryRequestStore = reactive({
  catObj: initCatObj,
  catReqId: '',
  catRequests: {},
  async request(catObj) {
    axios
      .post("http://localhost:5000/category_request", catObj)
      .then(response => {
        if (response.status == 200) {
          alert('Request created succesfully!')
        } else {
          alert('An error occured')
        }
      })
  },
  async approve(id) {
    axios
      .put("http://localhost:5000/category_request", { id: id })
      .then(response => {
        if (response.status == 200) {
          delete this.catRequests[id]
          alert('Request approved succesfully!')
        } else {
          alert('An error occured')
        }
      })
  },
  async reject(id) {
    axios
      .delete("http://localhost:5000/category_request", { data: {id: id} })
      .then(response => {
        if (response.status == 200) {
          delete this.catRequests[id]
          alert('Request rejected succesfully!')
        } else {
          alert('An error occured')
        }
      })
  },
  async get() {
    axios
      .get("http://localhost:5000/category_request")
      .then(response => {
        if (response.status == 200) {
          this.catRequests = response.data.requests
        } else {
          alert('An error occured')
        }
      })
  },
})

export {
  categoryStore,
  categoryRequestStore
}