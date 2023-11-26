<template>
    <div class="main">
        <div v-for="(value,key) in cat" :key="key">
            {{ value.name }}
            <br><br>
            {{ value.desc }}
        </div>
    </div>
</template>
<script>

    import axios from 'axios';

    export default {
        name : 'EditCat',
        data() {
            return {
                cat : {}
            };
        },
        mounted() {
            axios.get('http://localhost:5000/edit_cat')
                .then(response => {
                    this.cat = response.data.category;
                    console.log(this.cat)
                })
        }

    }

</script>
<style>
    .main {
        display : flex;
    }
</style>