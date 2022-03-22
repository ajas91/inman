from django.shortcuts import render
from .models import *
from .forms import CustomerForm

# Create your views here.
def customes(request):
    context = {}
    render(request,'base.html',context=context)




def newCustomer(request):
    context = {}
    render(request,'base.html',context=context)




def updateCustomer(request,pk):
    context = {}
    render(request,'base.html',context=context)