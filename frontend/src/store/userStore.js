import router from '@/router';
import axios from 'axios';
import { reactive } from 'vue'

const userStore = reactive({
  isLoggedIn: localStorage.getItem('logged'),
  username: localStorage.getItem('username'),
  logOut() {
    console.log('logout');
    localStorage.setItem("token", null);
    localStorage.setItem("role", null);
    localStorage.setItem("username", null);
    localStorage.setItem("logged", false);
    this.isLoggedIn = false
    router.push('/register')
  },
  async logIn(email, password) {
    axios
      .post("http://localhost:5000/login", {
        email: email,
        password: password,
      })
      .then((response) => {
        localStorage.setItem("token", response.data["access_token"]);
        localStorage.setItem("role", response.data["role"]);
        localStorage.setItem("username", response.data["username"]);
        localStorage.setItem("logged", true);
        this.isLoggedIn = true
        this.username = response.data['username']


        if (localStorage.getItem("role") == "admin") router.push("/admin");
        else if (localStorage.getItem("role") == "user") router.push("/");
      });
  }
})

export { userStore }