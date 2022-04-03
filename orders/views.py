from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, OrderLineForm
from django.forms.formsets import formset_factory

# Create your views here.
def orders(request):
    orders = Order.objects.all()
    context = {'orders':orders,
              }

    return render(request,'orders/orders.html',context=context)





def newOrder(request):
    orderForm = OrderForm()
    orderLineForm = formset_factory(OrderLineForm)
    itemsList = list(Item.objects.values())
    if request.method == 'POST':
        orderDate = request.POST['order_date']
        orderCustomer = request.POST['customer']
        orderStatus = request.POST['status']
        orderTotal = request.POST['total']
        order = Order(order_date = orderDate, 
                      customer = Customer.objects.get(id=int(orderCustomer)),
                      status = orderStatus,
                      total = orderTotal)
        order.save()

        for i in range(int(request.POST['form-TOTAL_FORMS'][0])):
            item = request.POST[f'form-{i}-item']
            qty = request.POST[f'form-{i}-qty']
            disc = request.POST[f'form-{i}-disc']
            total_price = request.POST[f'form-{i}-total_price']
            orderLine = OrderLine(item=Item.objects.get(id=int(item)),
                                  qty=qty,
                                  disc=disc,
                                  total_price=total_price,
                                  order=order
                                )
            orderLine.save()
        return redirect('orders')

    context = { 'orderForm':orderForm,
                'orderLineForm':orderLineForm,
                'status':'new',
                'itemsList':itemsList,
              }
    return render(request,'orders/orderDetail.html',context=context)





def updateDeleteOrder(request,pk):
    itemsList = list(Item.objects.values())
    order = Order.objects.get(id=pk)
    orderForm = OrderForm(instance=order)
    orderLines = OrderLine.objects.filter(order=order)
    # orderLineForm = formset_factory(OrderLineForm,queryset=orderLines)
    if request.method == 'POST':
        orderForm = OrderForm(request.POST,instance=order)
        if orderForm.is_valid() and request.POST.get('update'):
            orderForm.save()
        elif request.POST.get('delete'):
            order.delete()
        return redirect('customers')
    
    context = {'orderForm':orderForm,
               'order':order,
               'status':'existing',
               'itemsList':itemsList,
              }
    return render(request,'orders/orderDetail.html',context=context)