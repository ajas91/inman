<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a href="/" class="navbar-brand"> 
                <img src="assets/image/logo.png" height="50" alt="Brand">
            </a>
            <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <div class="navbar-nav">
                    <router-link to="/inventory" class="nav-item nav-link">Inventory</router-link>
                    <router-link to="/orders" class="nav-item nav-link">Orders</router-link>
                    <router-link to="/customers" class="nav-item nav-link">Customers</router-link>
                    <router-link to="/about" class="nav-item nav-link">About</router-link>
                    <!-- <a href="" class="nav-item nav-link disabled" tabindex="-1">Reports</a> -->
                </div>
                <div class="navbar-nav ms-auto">
                    <!-- <a href="" class="nav-item nav-link">Logout</a> -->
                </div>
            </div>
        </div>
    </nav>
</template>


<script>
export default{
    name: 'Header',
    props: {
      
    },
    components:{
        
    },
}
</script>

<style scoped>

</style>