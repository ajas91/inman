from django.shortcuts import render
from .models import *
from .forms import OrderForm

# Create your views here.
def orders(request):
    context = {}
    render(request,'base.html',context=context)




def orderDetails(request,pk):
    context = {}
    render(request,'base.html',context=context)