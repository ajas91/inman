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
import axios from "axios"

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
    
    async fetchData(){
      try{
        let [dataCustomers,dataOrders,dataItems] = await Promise.all([
        axios.get('http://localhost:8000/api/customers/'),
        axios.get('http://localhost:8000/api/orders/'),
        axios.get('http://localhost:8000/api/items/')
      ])
        this.numberOfCustomers = dataCustomers.data.count
        this.numberOfOrders = dataOrders.data.count
        this.numberOfItems = dataItems.data.count
        this.customersData = dataCustomers.data.results
        this.itemsData = dataItems.data.results
        this.ordersData = dataOrders.data.results
      }
      catch(err) {
        console.warn(err)
      }
    },

    getCustomer(id){
      var customer = this.$root.customersData.filter(function(el){
        return el.id == id;
      });
      return customer;
    },
  },
  mounted(){
    this.fetchData();
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
