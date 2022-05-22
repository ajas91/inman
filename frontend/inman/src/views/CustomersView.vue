<template>
  <div class="customers">
    <div class="contrainer-fluid">
      <form action="" method="get">
          <div class="row filter-bar mb-3 mt-2">
              <h5>Filter Bar</h5>
              <div class="col-7">
                  <div class="row">
                      <div class="col-sm">
                          <label for="customer_name" class="form-label">Customer Name</label>
                          <input type="text" class="form-control" id="customer_name" name="customer_name">
                      </div>
                      <div class="col-sm">
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
          <div class="col-9"></div>
          <div class="col-2"><router-link class="btn btn-success" to="/customers/new_customer">New Customer</router-link></div>
      </div>
      
      <div class="row mb-2">
          <table class="table table-hover">
              <thead>
              <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Name</th>
                  <th scope="col">Phone Number</th>
                  <th scope="col">Address</th>
                  <th scope="col"># Orders</th>
                  <th scope="col">Details</th>
              </tr>
              </thead>
              <tbody>
              for customer in customers
                  <tr>
                      <th scope="row">customer.id</th>
                      <td>customer.name</td>
                      <td>customer.phone_number</td>
                      <td>customer.address</td>
                      <td>customer.number_of_orders</td>
                      <td><router-link class="btn btn-primary btn-sm" to="customers/customer.id">Check</router-link></td>
                  </tr>
              endfor
              </tbody>
          </table>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "CustomersView",

};
</script>