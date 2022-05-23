<template>
  <div class="container-fluid">
    <Header />
    <div class="container-fluid">
      <div class="row mt-2 mb-2 ml-2 mr-2">
        <router-view/>
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
      numberOfCustomers: 0,
      numberOfOrders: 0,
      numberOfItems: 0,
      customersData: [],
      ordersData: [],
      itemsData: [],
    }
  },
  methods: {
    async fetchCustomers(){
    // async fetchData(){
      const dataCustomers = await fetch('http://localhost:8000/api/customers/').then(res => {return res.json()})
      this.numberOfCustomers = dataCustomers.count//.toString()
      this.customersData = dataCustomers.results
    },
    async fetchOrders(){
      const dataOrders = await fetch('http://localhost:8000/api/orders/').then(res => {return res.json()})
      this.numberOfOrders = dataOrders.count//.toString()
      this.ordersData = dataOrders.results
    },
    async fetchItems(){
      const dataItems = await fetch('http://localhost:8000/api/items/').then(res => {return res.json()})
      this.numberOfItems = dataItems.count//.toString()
      this.itemsData = dataItems.results
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
