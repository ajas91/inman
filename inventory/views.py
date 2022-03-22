from django.shortcuts import render
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
    context = {}
    render(request,'itemDetail.html',context=context)




def updateItem(request,pk):
    context = {}
    render(request,'itemDetail.html',context=context)