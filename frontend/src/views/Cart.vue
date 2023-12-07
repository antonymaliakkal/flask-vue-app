<script>
    import { cartStore } from '@/store/cartStore';
    import { onMounted, reactive } from 'vue';

    let product = reactive({})

    onMounted(async () => {
        let user_id = localStorage.getItem('id')
        product.value = Object.values(cartStore.cart).filter(cart => (cart.user_id == user_id))
    })

</script>
<template>
    <div class="main">
        <div class="products">
            
        </div>
    </div>
</template>