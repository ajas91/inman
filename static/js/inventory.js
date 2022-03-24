// purchasePrice = document.getElementById('purchase_price');
// vat = document.getElementById('vat');
// shippingCost = document.getElementById('shipping_cost');
// otherCost = document.getElementById('other_cost');
// profitMargin = document.getElementById('profit_margin');
// sellingPrice = document.getElementById('selling_price');
// orderedQty = document.getElementById('ordered_qty');
// remainingQty = document.getElementById('remaining_qty');

function updateVAT(){
    purchasePrice = document.getElementById('purchase_price');
    vat = document.getElementById('vat');
    vat.value = purchasePrice.value*0.05;
}


// function updateSellingPrice(){
//     totalCost = (purchasePrice.value*0.1) + vat.value + shippingCost.value + otherCost.value;
//     sellingPrice.value = totalCost*(1+(profitMargin.value/100));
// }


// function updateQTY(){
//     remainingQty.value = orderedQty.value;
// }


// purchasePrice.addEventListener('change',funtion(){
//             updateVAT();
//         }
//     );