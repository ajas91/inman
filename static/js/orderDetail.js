n = document.getElementsByClassName('omr');
    for(let i=0;i<n.length;i++){
        n[i].value=parseFloat(n[i].value).toFixed(3);
    }

// $('.orderline').formset({
//         addText: 'Add Item',
//         deleteText: 'Remove'
// });

total = document.getElementById('total_price')

function updateTotal(price, qty, disc){
    total.value = price*qty*(1-(disc/100));
};


unit_price = document.getElementById('unit_price');
selectedItem = document.getElementById('item');

selectedItem.addEventListener('change',function(){
    filters = [item => item.id == parseInt(selectedItem.value),];
    price = itemsList.filter(item => filters.every(fn => fn(item)));
    unit_price.value = price[0].selling_price;
});


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
