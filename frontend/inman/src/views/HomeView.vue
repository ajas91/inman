<template>
  <div class="home">
    <div class="row mb-4 mt-2">
      <div class="col-4">
        <Card card_title="Total Customers" 
              :indicator="this.$root.numberOfCustomers" 
              background_color="#c6d8e4"
              card_color="#1A5276"
        />
      </div>
      <div class="col-4">
        <Card card_title="Total Items" 
              :indicator="this.$root.numberOfItems" 
              background_color="#A9DFBF"
              card_color="#196F3D"
        />
      </div>
      <div class="col-4">
        <Card card_title="Total Orders" 
              :indicator="this.$root.numberOfOrders" 
              background_color="#F9E79F"
              card_color="#9A7D0A"
        />
      </div>
    </div>
  
    <div class="container-fluid">
      <div class="row mb-2">
          <div class="col-sm">
              <div class="card">
                  <div class="card-header">
                      <h4>Pending Payment<span class="pending"> ({{this.getFilteredOrders('Pending Payment').length}})</span></h4>
                  </div>
                  <div class="card-body">
                      <table class="table">
                          <thead>
                          <tr>
                              <th scope="col">Order ID</th>
                              <th scope="col">Customer Name</th>
                              <th scope="col">Order Value</th>
                              <th scope="col">Details</th>
                          </tr>
                          </thead>
                          <tbody>
                              <tr v-for="pendingPayment in this.getFilteredOrders('Pending Payment')" :key="pendingPayment.id">
                                  <th scope="row">{{pendingPayment.id}}</th>
                                  <td>{{this.$root.getCustomer(pendingPayment.customer)[0].name}}</td>
                                  <td>{{pendingPayment.total}}</td>
                                  <td><a class="btn btn-primary btn-sm" href="#">Check</a></td>
                              </tr>
                          </tbody>
                      </table>
                  </div>
              </div>
          </div>

          <div class="col-sm">
              <div class="card">
                  <div class="card-header">
                      <h4>Pending Delivery <span class="pending"> ({{this.getFilteredOrders('Pending Delivery').length}})</span></h4>
                  </div>
                  <div class="card-body">
                      <table class="table">
                          <thead>
                          <tr>
                              <th scope="col">Order ID</th>
                              <th scope="col">Customer Name</th>
                              <th scope="col">Order Value</th>
                              <th scope="col">Details</th>
                          </tr>
                          </thead>
                          <tbody>
                              <tr v-for="pendingDelivery in this.getFilteredOrders('Pending Delivery')" :key="pendingDelivery.id">
                                  <th scope="row">{{pendingDelivery.id}}</th>
                                  <td>{{this.$root.getCustomer(pendingDelivery.customer)[0].name}}</td>
                                  <td>{{pendingDelivery.total}}</td>
                                  <td><a class="btn btn-primary btn-sm" href="#">Check</a></td>
                              </tr>
                          </tbody>
                      </table>
                  </div>
              </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Card from '../components/Card'

export default {
  name: "HomeView",
  components: {
    Card,
  },
  props:{

  },
  data (){
    return{
    }
  },
  methods: {
    getFilteredOrders(statusName){
      var filteredOrders = this.$root.ordersData.filter(function(el){
        return el.status == statusName;
      })
      return filteredOrders;
    }
  },
  mounted(){
  },
};
</script>
