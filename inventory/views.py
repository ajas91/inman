from django.shortcuts import render, redirect
from .models import *
from .forms import ItemForm, CategoryForm
import os
from django.contrib.auth.decorators import login_required

# Create your views here.
def is_valid_queryparam(param):
    return param != '' and param is not None




@login_required(login_url='/accounts/login/')
def inventory(request):
    category = request.GET.get('selected_category')
    item_code = request.GET.get('item_code')
    price_less_than = request.GET.get('price_less_than')   
    inventory = Item.objects.all()

    if is_valid_queryparam(category):
        inventory = inventory.filter(item_category_category_name=category)

    elif is_valid_queryparam(item_code):
        inventory = inventory.filter(id=item_code)

    elif is_valid_queryparam(price_less_than):
        inventory = inventory.filter(selling_price__lte=price_less_than)

    categories = ItemCategory.objects.all()
    context = {'inventory':inventory,
               'categories':categories,
              }

    return render(request,'inventory/inventory.html',context=context)




@login_required(login_url='/accounts/login/')
def newItem(request):
    img = 'new'
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('inventory')

    context = { 'form':form,
                'img':img,
              }
    return render(request,'inventory/itemDetail.html',context=context)




@login_required(login_url='/accounts/login/')
def updateDeleteItem(request,pk):
    img = 'existing'
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid() and request.POST.get('update'):
            form.save()
        elif request.POST.get('delete'):
            item.delete()
            if item.item_image:
                os.remove(str(item.item_image))
        return redirect('inventory')
    
    context = {'form':form,
               'item':item,
               'img':img,
              }
    return render(request,'inventory/itemDetail.html',context=context)




@login_required(login_url='/accounts/login/')
def newCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inventory')

    context = { 'form':form,
              }
    return render(request,'inventory/newCategory.html',context=context)