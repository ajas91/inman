n = document.getElementsByClassName('omr');
    for(let i=0;i<n.length;i++){
        n[i].value=parseFloat(n[i].value).toFixed(3);
    }

// $('.orderline').formset({
//         addText: 'Add Item',
//         deleteText: 'Remove'
// });

// total = document.getElementById('total_price')

function updateTotal(price, qty, disc,total){
    total.value = price*qty*(1-(disc/100));
};


// unit_price = document.getElementById('unit_price');
// selectedItem = document.getElementById('item');

// selectedItem.addEventListener('change',function(){
//     filters = [item => item.id == parseInt(selectedItem.value),];
//     price = itemsList.filter(item => filters.every(fn => fn(item)));
//     unit_price.value = price[0].selling_price;
// });


qty = document.getElementById('qty');
disc = document.getElementById('disc');
qty.addEventListener('click',function(){
    updateTotal(parseFloat(unit_price.value), parseInt(qty.value), parseFloat(disc.value));
});

disc.addEventListener('click',function(){
    updateTotal(parseFloat(unit_price.value), parseInt(qty.value), parseFloat(disc.value));
});

total.addEventListener('click',function(){
    updateTotal(parseFloat(unit_price.value), parseInt(qty.value), parseFloat(disc.value));
});


function getUnitPrice(){
    totalForms = document.getElementsByName('orderline-TOTAL_FORMS')[0];
    unit_price = document.getElementsByClassName('unit_price');
    qty = document.getElementsByClassName('quantity');
    disc = document.getElementsByClassName('discount');
    total = document.getElementsByClassName('total_price_');
    for (let i=0;i<totalForms.value;i++){
        qty[i].value=1;
        disc[i].value=0;
        total[i].value=0;
        selectedItem = document.getElementsByName('orderline-'+i+'-item')[0];
        selectedItem.addEventListener('change',function(){
            filters = [item => item.id == parseInt(selectedItem.value),];
            price = itemsList.filter(item => filters.every(fn => fn(item)));
            unit_price[i].value = price[0].selling_price;
        });
    
    updateTotal(parseFloat(unit_price[i].value), parseInt(qty[i].value), parseFloat(disc[i].value),total[i]);

    };
}


orderline = document.getElementById('orders')
orderline.addEventListener('click',function(e){
    for(let i=0; i<document.getElementsByName('orderline-TOTAL_FORMS')[0].value;i++){
        if (e.target && e.target.name == ('orderline-'+i+'-item')){
            getUnitPrice();
        }
    }
})