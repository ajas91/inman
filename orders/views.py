from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, OrderLineForm
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import formset_factory

# Create your views here.
def orders(request):
    orders = Order.objects.all()
    context = {'orders':orders,
              }

    return render(request,'orders/orders.html',context=context)





def newOrder(request):
    orderForm = OrderForm()
    orderLineFormset = inlineformset_factory(Order,OrderLine,OrderLineForm,can_delete=True,extra=1,max_num=10)
    formset = orderLineFormset(prefix='orderline')
    itemsList = list(Item.objects.values())
    if request.method == 'POST':
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