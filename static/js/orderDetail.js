function calTotalBill(total){
    totalBill = document.getElementById('total');
    var totalBillVal = 0.00;
    for (let i=0; i<total.length; i++){
        totalBillVal = totalBillVal + parseFloat(total[i].value);
    }
    totalBill.value = totalBillVal.toFixed(3);
};



function updateTotal(price, qty, disc,total){
    total.value = price*qty*(1-(disc/100)).toFixed(3);
};



function getUnitPrice(){
    totalForms = document.getElementsByName('orderline-TOTAL_FORMS')[0];
    unit_price = document.getElementsByClassName('unit_price');
    qty = document.getElementsByClassName('quantity');
    disc = document.getElementsByClassName('discount');
    total = document.getElementsByClassName('total_price_');
    for (let i=0;i<totalForms.value;i++){
        selectedItem = document.getElementsByName('orderline-'+i+'-item')[0];
        selectedItem.addEventListener('change',function(){
            filters = [item => item.id == parseInt(selectedItem.value),];
            price = itemsList.filter(item => filters.every(fn => fn(item)));
            unit_price[i].value = price[0].selling_price.toFixed(3);
        });
    
        updateTotal(parseFloat(unit_price[i].value), parseInt(qty[i].value), parseFloat(disc[i].value),total[i]);
    };
    calTotalBill(total);
}

function setDefaultVal(){
    totalForms = document.getElementsByName('orderline-TOTAL_FORMS')[0];
    qty = document.getElementsByClassName('quantity');
    disc = document.getElementsByClassName('discount');
    total = document.getElementsByClassName('total_price_');
    for (let i=0;i<totalForms.value;i++){
        if (total[i].value = ''){
            qty[i].value=1;
            disc[i].value=0.000;
            total[i].value=0.000;
        };
    }
}


orderline = document.getElementById('orders')
orderline.addEventListener('click',function(e){
    
    if (e.target && e.target.id == 'add-btn'){
        // setDefaultVal();
        console.log('im here');
    } else {
        getUnitPrice();
    };
})