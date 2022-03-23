from django.shortcuts import render
from .models import *
from .forms import CustomerForm

# Create your views here.
def customers(request):
    context = {}
    return render(request,'base.html',context=context)




def newCustomer(request):
    context = {}
    return render(request,'base.html',context=context)




def updateCustomer(request,pk):
    context = {}
    return render(request,'base.html',context=context)