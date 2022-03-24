from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, OrderLineForm

# Create your views here.
def orders(request):
    orders = Order.objects.all()
    context = {'orders':orders,
              }

    return render(request,'orders/orders.html',context=context)





def newOrder(request):
    orderForm = OrderForm()
    orderLineForm = OrderLineForm()
    itemsList = list(Item.objects.values())
    if request.method == 'POST':
        orderForm = OrderForm(request.POST)
        orderLineForm = OrderLineForm(request.POST)
        if orderForm.is_valid() and orderLineForm.is_valid():
            orderLineForm.save()
            orderForm.save()
        return redirect('orders')

    context = { 'orderForm':orderForm,
                'orderLineForm':orderLineForm,
                'status':'new',
                'itemsList':itemsList,
              }
    return render(request,'orders/orderDetail.html',context=context)





def updateDeleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    orderForm = OrderForm(instance=order)
    if request.method == 'POST':
        orderForm = OrderForm(request.POST,instance=order)
        if orderForm.is_valid() and request.POST.get('update'):
            orderForm.save()
        elif request.POST.get('delete'):
            order.delete()
        return redirect('customers')
    
    context = {'orderForm':orderForm,
               'order':order,
               'status':'existing'
              }
    return render(request,'orders/orderDetail.html',context=context)