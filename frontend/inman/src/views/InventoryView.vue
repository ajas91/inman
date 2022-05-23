<template>
    <div class="inventory">
        <div class="contrainer-fluid">
            <form action="" method="get">
                <div class="row filter-bar mb-3 mt-2">
                    <h5>Filter Bar</h5>
                    <div class="col-2">   
                        <div class="btn-group">
                            <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            Category
                            </button>
                            <ul class="dropdown-menu">
                                for category in categories
                                    <li>
                                        <a class="dropdown-item" href="#" name="selected_category">category.category_name</a>
                                    </li>
                                endfor
                            </ul>
                        </div>
                    </div>
                    <div class="col-2">
                        <label for="code" class="form-label">Item Code</label>
                        <input type="text" class="form-control" id="code" name="item_code">
                    </div>
                    <div class="col-2">
                        <label for="price" class="form-label">Price Less than</label>
                        <input type="text" class="form-control" id="price" name="price_less_than">
                    </div>
                
                    <div class="col-2">

                    </div>
                    <div class="col-2" style="text-align: right;">
                        <input class="btn btn-outline-primary" type="submit" value="Apply" name="apply">
                    </div>
                </div>    
            </form>

            <hr>
            
            <div class="row mb-2 mt-2" style="text-align: right;">
                <div class="col-10"></div>
                <div class="col-2">
                    <router-link to="/inventory/new_item" class="btn btn-success">New Item</router-link>
                </div>
            </div>
            
            <div class="row mb-2">
                <table class="table table-hover">
                    <thead>
                    <tr>
                        <th scope="col">Item Code</th>
                        <th scope="col">Item Image</th>
                        <th scope="col">Item Name</th>
                        <th scope="col">Total Cost (OMR)</th>
                        <th scope="col">Selling Price (OMR)</th>
                        <th scope="col">Remaining Quantity</th>
                        <th scope="col">Details</th>
                    </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in this.$root.itemsData">
                            <th scope="row">{{item.id}}</th>
                            <td v-if="item.item_image"><img src = "item.item_image.url" width="100" height="100"></td>
                            <td v-else></td>
                            <td>{{item.item_name}}</td>
                            <td class="omr">{{item.getTotalCost}}</td>
                            <td class="omr">{{item.selling_price}}</td>
                            <td>{{item.remaining_qty}}</td>
                            <td><route-link class="btn btn-primary btn-sm" to="/inventory/{{item.id}}">Check</route-link></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>


<script>
  export default {
    name: 'InventoryView',
    data(){
        return {
        }
    },
    // methods:{
    //   updateNumberFormat(){
    //     n = document.querySelector(".omr");
    //     for(let i=0;i<n.length;i++){
    //         n[i].innerText=parseFloat(n[i].innerText).toFixed(3);
    //     }
    //   },
    // },
    // mounted(){
    //   this.updateNumberFormat();
    // },
  }
</script>