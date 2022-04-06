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
    # formset = formset_factory(OrderLineForm)
    orderLineFormset = inlineformset_factory(Order,OrderLine,OrderLineForm,can_delete=True,extra=1,max_num=10)
    formset = orderLineFormset()
    itemsList = list(Item.objects.values())
    if request.method == 'POST':
        # print(request.POST)
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid():
            order = orderForm.save(commit=False)
            formset = orderLineFormset(request.POST,instance=order)
            print(formset)
            if formset.is_valid():
                order.save()
                formset.save()

    #     orderLineFormset = modelformset_factory(OrderLine, form=OrderLineForm)
    #     formset = orderLineFormset(queryset=request.POST)
        # print(f'{orderForm.is_valid()} and {formset.is_valid()}')
        # if orderForm.is_valid() and formset.is_valid():
            
            # orderDate = request.POST['order_date']
            # orderCustomer = request.POST['customer']
            # orderStatus = request.POST['status']
            # orderTotal = request.POST['total']
            # order = Order(order_date = orderDate, 
            #             customer = Customer.objects.get(id=int(orderCustomer)),
            #             status = orderStatus,
            #             total = orderTotal)
            # order = orderForm.save()
            # for i in formset:#range(int(request.POST['form-TOTAL_FORMS'][0])):
            #     item = request.POST[f'form-{i}-item']
            #     qty = request.POST[f'form-{i}-qty']
            #     disc = request.POST[f'form-{i}-disc']
            #     total_price = request.POST[f'form-{i}-total_price']
            #     orderLine = OrderLine(item=Item.objects.get(id=int(item)),
            #                         qty=qty,
            #                         disc=disc,
            #                         total_price=total_price,
            #                         order=order
            #                         )
            #     orderLine.save()
        return redirect('orders')

    context = { 'orderForm':orderForm,
                # 'orderLineForm':orderLineFormset,
                'orderLineForm':formset,
                'status':'new',
                'itemsList':itemsList,
              }
    return render(request,'orders/orderDetail.html',context=context)





def updateDeleteOrder(request,pk):
    itemsList = list(Item.objects.values())
    order = Order.objects.get(id=pk)
    orderForm = OrderForm(instance=order)
    orderLines = OrderLine.objects.filter(order=order)
    orderLineFormset = modelformset_factory(OrderLine, form=OrderLineForm,extra=0)
    formset = orderLineFormset(queryset=orderLines)

    if request.method == 'POST':
        orderForm = OrderForm(request.POST,instance=order)
        formset = orderLineFormset(request.POST,queryset=orderLines)
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
               'orderLineForm':formset,
              }
    return render(request,'orders/orderDetail.html',context=context)