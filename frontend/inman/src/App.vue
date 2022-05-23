<template>
  <div class="container-fluid">
    <Header />
    <div class="container-fluid">
      <div class="row mt-2 mb-2 ml-2 mr-2">
        <router-view />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'

export default {
  name:'App',
  components: {
    Header,
    Footer,
  },
data (){
    return{
      numberOfCustomers: String,
      numberOfOrders: String,
      numberOfItems: String,
      customersData: [],
      ordersData: [],
      itemsData: []
    }
  },
  methods: {
    async fetchCustomers(){
      const res = await fetch('http://localhost:8000/api/customers/')
      const data = await res.json()
      this.numberOfCustomers = data.count.toString()
      this.customersData = data.results
    },
    async fetchOrders(){
      const res = await fetch('http://localhost:8000/api/orders/')
      const data = await res.json()
      this.numberOfOrders = data.count.toString()
      this.ordersData = data.results
    },
    async fetchItems(){
      const res = await fetch('http://localhost:8000/api/items/')
      const data = await res.json()
      this.numberOfItems = data.count.toString()
      this.itemsData = data.results
    },
    getCustomer(id){
      var customer = this.$root.customersData.filter(function(el){
        return el.id == id;
      });
      return customer;
    },
  },
  mounted(){
    this.fetchItems();
    this.fetchOrders();
    this.fetchCustomers();
  }
}

</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
