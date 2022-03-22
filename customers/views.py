from django.shortcuts import render
from .models import *
from .forms import CustomerForm
from inventory.models import *
from orders.models import *

# Create your views here.
def index(request):

    totalCustomers = Customer.objects.all().count()
    totalItems = Item.objects.all().count()
    totalOrders = Order.objects.all().count()
    totalPendingD = Order.objects.filter(status = 'Pending Delivery')
    totalPendingDCount = totalPendingD.count()

    context={"totalCustomers":totalCustomers,
             "totalToys":totalItems,
             "totalSwaps":totalOrders,
             "totalPendingD":totalPending,
             "totalPendingDCount":totalPendingDCount
            }
    return render(request,'index.html',context=context)



    
def customes(request):
    context = {}
    render(request,'base.html',context=context)




def newCustomer(request):
    context = {}
    render(request,'base.html',context=context)




def updateCustomer(request,pk):
    context = {}
    render(request,'base.html',context=context)