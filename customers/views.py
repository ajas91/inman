from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerForm
from inventory.models import *
from orders.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):

    totalCustomers = Customer.objects.all().count()
    totalItems = Item.objects.all().count()
    totalOrders = Order.objects.all().count()
    totalPendingD = Order.objects.filter(status = 'Pending Delivery')
    totalPendingDCount = totalPendingD.count()
    totalPendingP = Order.objects.filter(status = 'Pending Payment')
    totalPendingPCount = totalPendingP.count()

    context={"totalCustomers":totalCustomers,
             "totalItems":totalItems,
             "totalOrders":totalOrders,
             "totalPendingD":totalPendingD,
             "totalPendingDCount":totalPendingDCount,
             "totalPendingP":totalPendingP,
             "totalPendingPCount":totalPendingPCount,
            }
    return render(request,'index.html',context=context)




@login_required(login_url='/accounts/login/')
def customers(request):
    customers = Customer.objects.all()
    context = {'customers':customers,
              }

    return render(request,'customers/customers.html',context=context)





@login_required(login_url='/accounts/login/')
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





@login_required(login_url='/accounts/login/')
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