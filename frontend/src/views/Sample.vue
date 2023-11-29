<template>
    <h1>HOME</h1>
    <br><br>
    <div class="samp">
        <div>
            <LogIn/>
        </div>
        <div>
            <SignUp/>
    
        </div>
    </div>
</template>


<script>

    import LogIn from '@/components/Login.vue'    
    import SignUp from '@/components/SignUp.vue'

    export default{
        name : 'HomePageOld',
        components : {
            LogIn,
            SignUp
        }
    }
</script>

<style>
    .samp{
        display: flex;
        justify-content: space-around;
    }
</style>