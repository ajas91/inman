<template>
  <div class="home">
    <div class="row mb-4 mt-2">
      <div class="col-4">
        <Card card_title="Total Customers" 
              indicator="" 
              background_color="#c6d8e4"
              card_color="#1A5276"
        />
      </div>
      <div class="col-4">
        <Card card_title="Total Items" 
              indicator="" 
              background_color="#A9DFBF"
              card_color="#196F3D"
        />
      </div>
      <div class="col-4">
        <Card card_title="Total Orders" 
              indicator="" 
              background_color="#F9E79F"
              card_color="#9A7D0A"
        />
      </div>
    </div>
  </div>
  <div class="container-fluid">
    <div class="row mb-2">
        <div class="col-sm">
            <div class="card">
                <div class="card-header">
                    <h4>Pending Payment<span class="pending">(totalPendingPCount)</span></h4>
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
                        for pending in totalPendingP
                            <tr>
                                <th scope="row">{{pending.id}}</th>
                                <td>{{pending.customer.name}}</td>
                                <td>{{pending.total}}</td>
                                <td><a class="btn btn-primary btn-sm" href="{% url 'update_delete_order' pending.id %}">Check</a></td>
                            </tr>
                        endfor
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="col-sm">
            <div class="card">
                <div class="card-header">
                    <h4>Pending Delivery <span class="pending">({{totalPendingDCount}})</span></h4>
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
                        {% for pending in totalPendingD %}
                            <tr>
                                <th scope="row">{{pending.id}}</th>
                                <td>{{pending.customer.name}}</td>
                                <td>{{pending.total}}</td>
                                <td><a class="btn btn-primary btn-sm" href="{% url 'update_delete_order' pending.id %}">Check</a></td>
                            </tr>
                        {% endfor %}
                        </tbody>
                    </table>
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
};
</script>
