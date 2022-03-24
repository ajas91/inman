from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import ItemForm, CategoryForm
import os

# Create your views here.
def inventory(request):
    inventory = Item.objects.all()
    categories = ItemCategory.objects.all()
    context = {'inventory':inventory,
               'categories':categories,
              }

    return render(request,'inventory/inventory.html',context=context)




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
            os.remove(str(item.item_image))
        return redirect('inventory')
    
    context = {'form':form,
               'item':item,
               'img':img,
              }
    return render(request,'inventory/itemDetail.html',context=context)




def newCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inventory')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = { 'form':form,
              }
    return render(request,'inventory/newCategory.html',context=context)