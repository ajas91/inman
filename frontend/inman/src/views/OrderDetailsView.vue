<template>
  <div class="orders">
    <div class="row mb-2 mt-2" style="text-align: center;">
        <div class="col-2">
            <input type=button value="Back" class="btn btn-secondary" @click="this.$router.go(-1)">
        </div>
        <div class="col-9"></div>
    </div>
    <form method="POST" action="" enctype="multipart/form-data" id="myForm">
        <div class="card">
            <div class="card-header" style="text-align: center;"><h1> Order Details </h1></div>
            <div class="card-body" style="text-align: left;">
                <div class="card-text">
                    <div class="row">
                        <div class="col-md-6">
                            <label for="id" class="form-label">Order ID</label>
                            <input type="text" class="form-control" id="id" v-model="order_id" readonly>
                        </div>
                        <div class="col-6">
                            <label for="order_date" class="form-label">Order Date</label>
                            <input type="date" class="form-control" name="order_date" id="order_date" v-model="orderDetails.order_date">
                        </div>
                        <div class="col-6">
                            <label for="customer" class="form-label">Customer Name</label>
                            <select class="form-select" name="customer" id="customer">
                                <option v-for="customer in customers" :key="customer.id" :selected="customer.id == orderDetails.customer">({{customer.id}}) {{customer.name}}</option>
                            </select>
                        </div>
                        <div class="col-6">
                            <label for="status" class="form-label">Order Status</label>
                            <select class="form-select" name="status" id="status">
                                <option v-for="s in status" :key="s.id" :selected="s.name == orderDetails.status">{{s.name}}</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <br>
        </div>
        <div class="card">
            <div class="card-body">
                <div class="card-text">
                    <table class="table table-hover">
                        <thead>
                        <tr>
                            <th scope="col">Item</th>
                            <th scope="col">Unit Price</th>
                            <th scope="col">Quantity</th>
                            <th scope="col">Discount</th>
                            <th scope="col">Total</th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody id="orders">
                            <tr class="orderline" v-for="orderLine in orderLines" :key="orderLine.id">
                                <th>
                                    <select name="orderline_item" id="orderline_item" class="form-select">
                                        <option v-for="item in items" :key="item.id" :selected="item.id == orderLine.item">{{item.item_name}}</option>
                                    </select>
                                </th>
                                <td><input type="text" v-model="orderLine.item" id="unit_price" class="form-control unit_price" readonly></td>
                                <td><input type="number" class="form-control" id="disc" v-model="orderLine.qty"></td>
                                <td class="omr" id="discount"><input type="number" class="form-control" id="disc" v-model="orderLine.disc"></td>
                                <td class="omr" id="total_price_"><input type="text" v-model="orderLine.total_price" id="unit_price" class="form-control unit_price" readonly></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="row">
                        <div class="col-10"></div>
                        <div class="col-2" style="text-align: right;">
                            <label for="total" class="form-label">Total</label>
                            <input class="form-control" type="number" name="total" id="total" v-model="orderDetails.total" readonly>
                        </div>
                        <div class="col-12"> <br></div>
                        if status == 'new'
                            <div class="col-12" style="text-align: center;">
                                <input type="submit" name="update" class="btn btn-success" value="Add">
                            </div>
                        else
                            <div class="col-6">
                                <input type="submit" name="update" class="btn btn-success" value="Update">
                            </div>
                            <div class="col-6">
                                <input type="submit" name="delete" class="btn btn-danger" value="Delete">
                            </div>
                        endif
                    </div>
                </div>
            </div>            
        </div>
    </form>
      
  </div>
</template>


<script>
import axios from "axios"

export default {
  name: "OrderDetailsView",
  props:{
    
  },
  data(){
    return {
      orderDetails: [],
      order_id: String,
      customers: [],
      orderLines: [],
      status: [{id: 1, name:'New'},{id:2,name:'Pending Payment'},{id:3,name:'Pending Delivery'},{id:4,name:'Done'}],
      items: []
    }
  },
  methods: {
    async fetchOrder(id){
        Promise.all([this.orderDetails = await this.$root.fetchDetails('orders',id),
            await this.fetchOrderLines(id)
        ])
        console.log(this.items)
    },
    async fetchOrderLines(id){
        let orderlineDetails = await axios.get(`http://localhost:8000/api/orderline?order=${id}`)
        this.orderLines = orderlineDetails.data.results
    }
  },
  created(){
    this.order_id = this.$route.params.orderID
  },
  mounted(){
    Promise.all([this.fetchOrder(this.order_id),this.customers = this.$root.customersData, this.items = this.$root.itemsData])
  }
};
    // n = document.getElementsByClassName('omr');

    // for(let i=0;i<n.length;i++){
    //     n[i].innerText=parseFloat(n[i].innerText).toFixed(3);
    // }
</script>