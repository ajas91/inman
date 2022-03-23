from django.db import models
from customers.models import Customer
from inventory.models import Item

# Create your models here.
class OrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    disc = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.item.item_name




class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    orderline = models.ManyToManyField(OrderLine)
    total = models.FloatField(default=0.0)
    statusChoice = [('New','New'),
                    ('Pending Payment','Pending Payment'),
                    ('Pending Delivery','Pending Delivery'),
                    ('Done','Done')
                   ]
    status = models.TextField(choices=statusChoice,default='New')

    def __str__(self):
        return self.id

