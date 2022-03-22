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
        if form.is_valid():
            form.save
        redirect('inventory')

    context = { "form":form,
              }
    render(request,'itemDetail.html',context=context)




def updateItem(request,pk):
    context = {}
    render(request,'itemDetail.html',context=context)




def newCategory(request,pk):
    context = {}
    render(request,'newCategory.html',context=context)