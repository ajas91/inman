from django.shortcuts import render,redirect
from .models import *
from .forms import CustomerForm
from inventory.models import *
from orders.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def is_valid_queryparam(param):
    return param != '' and param is not None




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
    phone_number = request.GET.get('phone_number')
    customer_name = request.GET.get('customer_name')
    customers = Customer.objects.all()

    if is_valid_queryparam(phone_number):
        customers = customers.filter(phone_number__contains=phone_number)

    elif is_valid_queryparam(customer_name):
        customers = customers.filter(name__icontains=customer_name)


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