import axios from "axios";
import { reactive } from "vue";
// import { userStore } from "./userStore";

// path:
//  category = 1
//  manager_approvals = 2

// dialogueType:
//   add = 1
//   edit = 2
//   delete = 2

const adminStore = reactive({
  path: 1,
  dialogueType: 1,
  managerRequests: {},
  config: {headers: {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
  }}, 
  async getManagerRequests() {
    axios
      .get("http://localhost:5000/manager_request", this.config)
      .then((response) => {
        if (response.status == 200) {
          console.log(response.data);
          this.managerRequests = response.data.user
        } else {
          alert('An error occured')
        }
      });
  },
  async approveManagerRequest(key) {
    axios.post('http://localhost:5000/manager_request', { key: key }, this.config)
      .then(response => {
        console.log(response.data['message'])
        delete this.managerRequests[key]
      })
  },
  async rejectManagerRequest(key) {
    axios.put('http://localhost:5000/manager_request', { key: key }, this.config)
      .then(response => {
        console.log(response.data['message'])
        delete this.managerRequests[key]
      })
  }
})

export { adminStore }