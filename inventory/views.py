from django.shortcuts import render, redirect
from .models import *
from .forms import ItemForm

# Create your views here.
def inventory(request):
    inventory = Item.objects.all()
    categories = ItemCategory.objects.all()
    context = {'inventory':inventory,
               'categories':categories,
              }

    return render(request,'inventory/inventory.html',context=context)




def newItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        print(f'''Details of the Item:
                name: {form.data['item_name']}
                desc: {form.data['desc']}
                Ordered Quantity: {form.data['ordered_qty']}
                Remaining Quantity: {form.data['remaining_qty']}
                Category: {form.data['item_category']}
                Purchase Price: {form.data['purchase_price']}
                VAT: {form.data['vat']}
                Shipping Cost: {form.data['shipping_cost']}
                Other Cost: {form.data['other_cost']}
                Profit Margin: {form.data['profit_margin']}
                Selling Price: {form.data['selling_price']}''')
        if form.is_valid():
            form.save()
            # print(f'################ I am a valid form')
        return redirect('inventory')

    context = { "form":form,
              }
    return render(request,'inventory/itemDetail.html',context=context)




def updateItem(request,pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)

    if request.method == 'POST':
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('inventory')
    
    context = {'form':form,
               'item':item,
              }
    return render(request,'inventory/itemDetail.html',context=context)




def newCategory(request,pk):
    context = {}
    return render(request,'newCategory.html',context=context)