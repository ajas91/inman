<template>
  <div class="customerDetails">
    <div class="row mb-2 mt-2" style="text-align: center;">
        <div class="col-2">
            <input type=button value="Back" class="btn btn-secondary" @Click="this.$router.go(-1)">
        </div>
        <div class="col-10"></div>
    </div>
    <div class="card">
        <div class="card-header" style="text-align: center;">
            <h1> Customer Details </h1>
        </div>
        <div class="card-body">
            <div class="card-text" style="text-align:left">
                <form class="row g-3" method="POST" action="" enctype="multipart/form-data">
                    <div class="col-md-4">
                        <label for="id" class="form-label">Customer ID</label>
                        <input type="text" class="form-control" v-model="customer_id" readonly>
                    </div>
                    <div class="col-4"></div>
                    <div class="col-4">
                        <label for="number_of_orders" class="form-label">Total Number of Orders</label>
                        <input class="form-control" type="number" v-model="customerDetails.number_of_orders" >
                    </div>
                    <div class="col-6">
                        <label for="name" class="form-label">Customer Name</label>
                        <input v-model="customerDetails.name" class="form-control"/>
                    </div>
                    <div class="col-6">
                        <label for="phone_number" class="form-label">Customer Phone Number</label>
                        <input class="form-control" v-model="customerDetails.phone_number"/>
                    </div>
                    <div class="col-12">
                        <label for="address" class="form-label">Customer Address</label>
                        <input class="form-control" v-model="customerDetails.address" />
                    </div>
                    <div class="col-9">
                    </div>
                    <div class="col-6">
                        <input class="btn btn-success" type="submit" name="update" value="Add"/>
                    </div>
                    <div class="col-6">
                        <input class="btn btn-success" type="submit" name="update" value="Update"/>
                    </div>
                    <div class="col-6">
                        <input class="btn btn-danger" type="submit" name="delete" value="Delete"/>
                    </div>
                </form>
            </div>
        </div>
    </div>   
  </div>
</template>


<script>
export default {
  name: "CustomerDetailsView",
  props:{
    
  },
  data(){
    return {
      customerDetails: [],
      customer_id: String
    }
  },
  methods: {
    async fetchCustomer(id){
      this.customerDetails = await this.$root.fetchDetails('customers',id)
    }
  },
  created(){
    this.customer_id = this.$route.params.customerID
  },
  mounted(){
    this.fetchCustomer(this.customer_id)
  }
};
</script>