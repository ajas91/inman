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

    render(request,'inventory.html',context=context)




def newItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('inventory')

    context = { "form":form,
              }
    render(request,'itemDetail.html',context=context)




def updateItem(request,pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)

    if request.method == 'POST':
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
        redirect('inventory')
    
    context = {'form':form,
               'item':item,
              }
    render(request,'itemDetail.html',context=context)




def newCategory(request,pk):
    context = {}
    render(request,'newCategory.html',context=context)