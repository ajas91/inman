from django.shortcuts import render,redirect
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
             "totalPendingD":totalPendingD,
             "totalPendingDCount":totalPendingDCount
            }
    return render(request,'index.html',context=context)



    
def customers(request):
    customers = Customer.objects.all()
    context = {'customers':customers,
              }

    return render(request,'customers/customers.html',context=context)





def newCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customers')

    context = { 'form':form,
                'status':'new'
              }
    return render(request,'customers/customerDetail.html',context=context)





def updateDeleteCustomer(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid() and request.POST.get('update'):
            form.save()
        elif request.POST.get('delete'):
            customer.delete()
        return redirect('customers')
    
    context = {'form':form,
               'customer':customer,
               'status':'existing'
              }
    return render(request,'customers/customerDetail.html',context=context)