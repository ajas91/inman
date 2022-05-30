<template>
    <div class="itemDetails">
        <div class="row mb-2 mt-2" style="text-align: center;">
            <div class="col-2">
                <input type=button value="Back" class="btn btn-secondary" @click="this.$router.go(-1)">
            </div>
            <div class="col-8"></div>
            <div class="col-2"><router-link class="btn btn-success" to="#">New Category</router-link></div>
        </div>
        <div class="card">
            <div class="card-header" style="text-align: center;">
                <h1> Item Details </h1>
            </div>
            <div class="card-body" style="text-align:left">
                <form class="row g-3" method="POST" action="" enctype="multipart/form-data">
                    <!-- <div class="col-12" style="text-align: center;">
                        if img == 'new'
                                <label for="image" class="form-label">Item Image</label>
                                {{form.item_image}}
                        elif item.item_image
                            <img src = "{{ item.item_image.url }}" width="200" height="200">
                        endif
                    </div> -->
                    <div class="col-6">
                        <label for="id" class="form-label">Item Code</label>
                        <input type="text" class="form-control" id="id" v-model="item_id" readonly>
                    </div>
                    <div class="col-6">
                        <label for="item_name" class="form-label">Item Name</label>
                        <input class="form-control" type="text" v-model="itemDetails.item_name" >
                    </div>
                    <div class="col-6">
                        <label for="item_desc" class="form-label">Item Description</label>
                        <input class="form-control" type="text" v-model="itemDetails.desc" >
                    </div>
                    <div class="col-6">
                        <label for="item_category" class="form-label">Item Category</label>
                        <select class="form-select" name="item_category" id="item_category">
                            <option v-for="category in categories" :key="category.id" :selected="category.id == itemDetails.item_category">{{category.category_name}}</option>
                        </select>
                    </div>
                    <div class="col-3">
                        <label for="purchase_price" class="form-label">Purchase Price (SAR)</label>
                        <input class="form-control" type="number" v-model="itemDetails.purchase_price" @change="updateVAT()">
                    </div>
                    <div class="col-3">
                        <label for="vat" class="form-label">VAT</label>
                        <input class="form-control" type="number" v-model="itemDetails.vat" @change="updateSellingPrice()">
                    </div>
                    <div class="col-3">
                        <label for="shipping_cost" class="form-label">Shipping Cost</label>
                        <input class="form-control" type="number" v-model="itemDetails.shipping_cost" @change="updateSellingPrice()">
                    </div>
                    <div class="col-3">
                        <label for="other_cost" class="form-label">Other Cost</label>
                        <input class="form-control" type="number" v-model="itemDetails.other_cost" @change="updateSellingPrice()">
                    </div>
                    <div class="col-6">
                        <label for="profit_margin" class="form-label">Profit Margin (in Percentage %)</label>
                        <input class="form-control" type="number" v-model="itemDetails.profit_margin" @change="updateSellingPrice()">
                    </div>
                    <div class="col-md-6">
                        <label for="selling_price" class="form-label">Selling Price</label>
                        <input class="form-control" type="number" v-model="itemDetails.selling_price" >
                    </div>
                    <div class="col-6">
                        <label for="ordered_qty" class="form-label">Ordered Quantity</label>
                        <input class="form-control" type="number" v-model="itemDetails.ordered_qty" @change="updateQTY()">
                    </div>
                    <div class="col-6">
                        <label for="remaining_qty" class="form-label">Remaining Quantity</label>
                        <input class="form-control" type="number" v-model="itemDetails.remaining_qty" readonly>
                    </div>
                    
                    if img == 'new'
                        <div class="col-6">
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
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios"

export default {
    name: "ItemDetailsView",
    props: {
    },
    data (){
        return{
            itemDetails: [],
            item_id: String,
            categories: [],
        }
    },
    methods: {
        async fetchItem(id){
            this.itemDetails = await this.$root.fetchDetails('items',id)
        },
        updateVAT(){
            this.itemDetails.vat = this.itemDetails.purchase_price * 0.05 /10;
        },
        updateSellingPrice(){
            let totalCost = (parseFloat(this.itemDetails.purchase_price)/10)+parseFloat(this.itemDetails.vat)+parseFloat(this.itemDetails.shipping_cost) + parseFloat(this.itemDetails.other_cost)
            this.itemDetails.selling_price = totalCost * (1+(parseFloat(this.itemDetails.profit_margin)/100))

        },
        updateQTY(){
            this.itemDetails.remaining_qty = this.itemDetails.ordered_qty
        },
        async getCategories(){
            let categoriesData = await axios.get('http://localhost:8000/api/items_category/')
            this.categories = categoriesData.data.results
        }
    },
    created(){
        this.item_id = this.$route.params.itemID
    },
    mounted(){
        Promise.all(
            [this.fetchItem(this.item_id),this.getCategories()]
        )
    },
    computed(){
    }
}
</script>
