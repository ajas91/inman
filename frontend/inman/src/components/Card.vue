<template>
    <div class="card stats" :style="{background:background_color}">
        <div class="card-body" :style="{color:card_color}">
            <h5 class="card-title"> {{card_title}}</h5>
            <span class="numberSpan" >{{indicator}}</span>
        </div>
    </div>
</template>


<script>
export default{
    name: 'Card',
    props: {
        card_title: String,
        indicator: Number,
        background_color: String,
        card_color: String,
    },
    components:{
        
    },
}
</script>

<style scoped>
.stats {
    height: 8em;
}

.numberSpan{
    font-size:130%;
    font-weight: bold;
}
.card-title{
    font-size: 100%;
}
</style>