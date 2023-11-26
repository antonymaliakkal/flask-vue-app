<template>
    <nav>
        <ul>
            <li>
                <router-link to="/">HOME</router-link> 

            </li>
            <li v-if="logged_in" @click="signout" >
                SIGNOUT
            </li>
            <li v-else>
                <router-link to="/register">SIGNIN</router-link>
            </li>
        </ul>
    </nav>
</template>
<script>
    export default { 
        name : 'NavBar',
        data() { 
            return {
                logged_in : localStorage.getItem('logged')
            }
        },
        methods : {
            signout() {
                localStorage.clear();

            }
        }

    }
</script>