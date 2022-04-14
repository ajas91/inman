from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, OrderLineForm
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

# Create your views here.
def is_valid_queryparam(param):
    return param != '' and param is not None




@login_required(login_url='/accounts/login/')
def orders(request):
    phone_number = request.GET.get('phone_number')
    order_number = request.GET.get('order_number')
    orders = Order.objects.all()

    if is_valid_queryparam(phone_number):
        orders = orders.filter(customer__phone_number__contains=phone_number)

    elif is_valid_queryparam(order_number):
        orders = orders.filter(id=order_number)

    context = {'orders':orders,
              }

    return render(request,'orders/orders.html',context=context)




@login_required(login_url='/accounts/login/')
def newOrder(request):
    orderForm = OrderForm()
    orderLineFormset = inlineformset_factory(Order,OrderLine,OrderLineForm,can_delete=True,extra=1,max_num=10)
    formset = orderLineFormset(prefix='orderline')
    itemsList = list(Item.objects.values())
    if request.method == 'POST':
        print(request.POST)
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid():
            order = orderForm.save(commit=False)
            formset = orderLineFormset(request.POST,instance=order,prefix='orderline')
            if formset.is_valid():
                order.save()
                formset.save()
        return redirect('orders')

    context = { 'orderForm':orderForm,
                'formset':formset,
                'status':'new',
                'itemsList':itemsList,
              }
    return render(request,'orders/orderDetail.html',context=context)





@login_required(login_url='/accounts/login/')
def updateDeleteOrder(request,pk):
    itemsList = list(Item.objects.values())
    order = Order.objects.get(id=pk)
    orderForm = OrderForm(instance=order)
    orderLines = OrderLine.objects.filter(order=order)
    orderLineFormset = inlineformset_factory(Order,OrderLine,OrderLineForm,can_delete=True,extra=0,max_num=10)
    formset = orderLineFormset(instance=order,queryset=orderLines,prefix='orderline')

    if request.method == 'POST':
        orderForm = OrderForm(request.POST,instance=order)
        formset = orderLineFormset(request.POST,instance=order, queryset=orderLines,prefix='orderline')
        if orderForm.is_valid() and formset.is_valid() and request.POST.get('update'):
            orderForm.save()
            formset.save()
        elif request.POST.get('delete'):
            order.delete()
            for orderLine in orderLines:
                orderLine.delete()
        return redirect('orders')
    
    context = {'orderForm':orderForm,
               'order':order,
               'status':'existing',
               'itemsList':itemsList,
               'formset':formset,
               'orderLines':orderLines,
              }
    return render(request,'orders/orderDetail.html',context=context)