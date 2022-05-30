<template>
  <div class="orders">
    <div class="contrainer-fluid">
      <form action="" method="get">
          <div class="row filter-bar mb-3 mt-2">
              <h5>Filter Bar</h5>
              <div class="col-7">
                  <div class="row">
                      <div class="col-4">   
                      </div>
                      <div class="col-4">
                          <label for="order_number" class="form-label">Order Number</label>
                          <input type="text" class="form-control" id="order_number" name="order_number">
                      </div>
                      <div class="col-4">
                          <label for="phone_number" class="form-label">Phone Number</label>
                          <input type="text" class="form-control" id="phone_number" name="phone_number">
                      </div>
                  </div>
              </div>
              <div class="col-3">

              </div>
              <div class="col-2" style="text-align: right;">
                  <input class="btn btn-outline-primary" type="submit" value="Apply" name="apply">
              </div>
          </div>
      </form>
      <hr>
      
      <div class="row mb-2 mt-2" style="text-align: right;">
          <div class="col-10"></div>
          <div class="col-2"><router-link class="btn btn-success" to="/orders/new_order">New Order</router-link></div>
      </div>
      
      <div class="row mb-2">
          <table class="table table-hover">
              <thead>
              <tr>
                  <th scope="col">Order Number</th>
                  <th scope="col">Customer</th>
                  <th scope="col">Phone Number</th>
                  <th scope="col">Total Price</th>
                  <th scope="col">Status</th>
                  <th scope="col">Details</th>
              </tr>
              </thead>
              <tbody>
                  <tr v-for="order in this.$root.ordersData" :key="order.id">
                      <th scope="row">{{order.id}}</th>
                      <td>{{this.$root.getCustomer(order.customer)[0].name}}</td>
                      <td>{{this.$root.getCustomer(order.customer)[0].phone_number}}</td>
                      <td class="omr">{{order.total}}</td>
                      <td>{{order.status}}</td>
                      <td><router-link class="btn btn-primary btn-sm" :to="{name:'orderDetails',params:{orderID:order.id}}">Check</router-link></td>
                  </tr>
              </tbody>
          </table>
      </div>
    </div>  
  </div>
</template>


<script>
import axios from "axios"

export default {
  name: "OrdersView",
  data(){
        return {
            orderDetails: []
        }
  },
  methods:{
      async fetchOrder(id){
          this.orderDetails = await this.$root.fetchDetails('orders',id)
      }
  },
  mounted(){
  },
};
    // n = document.getElementsByClassName('omr');

    // for(let i=0;i<n.length;i++){
    //     n[i].innerText=parseFloat(n[i].innerText).toFixed(3);
    // }
</script>