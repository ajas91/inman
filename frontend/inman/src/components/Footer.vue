<template>
    <div class="row mb-2 ml-2 mr-2"  style="text-align: center;">
        <span style="text-align: center; font-size: 80%">
            All rights reserverd, &copy;aJaS-Tech <span id="year"></span>
        </span>
    </div> 
</template>


<script>
export default{
    name: 'Footer',
    props: {
      
    },
}

document.getElementById("year").innerHTML = new Date().getFullYear();
</script>