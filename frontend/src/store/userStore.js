import router from '@/router';
import axios from 'axios';
import { reactive } from 'vue'

const userStore = reactive({
  token: localStorage.getItem('token') || '',
  username: localStorage.getItem('username'),
  logOut() {
    console.log('logout');
    localStorage.setItem("token", null);
    localStorage.setItem("id", null);
    localStorage.setItem("role", null);
    localStorage.setItem("username", null);
    localStorage.setItem("logged", false);
    this.token = ''
    router.push('/')
  },
  async logIn(email, password) {
    const response = await axios
      .post("http://localhost:5000/login", {
        email: email,
        password: password,
      })
    if (response.status == 200) {
      localStorage.setItem("id", response.data["user_id"]);
      localStorage.setItem("token", response.data["access_token"]);
      localStorage.setItem("role", response.data["role"]);
      localStorage.setItem("username", response.data["username"]);
      localStorage.setItem("logged", true);
      this.token = response.data['access_token']
      this.username = response.data['username']

      if (localStorage.getItem("role") == "admin") router.push("/admin");
      else if (localStorage.getItem("role") == "user") router.push("/");
    } else {
      alert('Bad credentials')
    }
  },
  async signUp(email, password, role) {
    const response = await axios.post('http://localhost:5000/signup', { email, password, role })
    return response.status
  }
})

export { userStore }