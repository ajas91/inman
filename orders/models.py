from django.db import models
from customers.models import Customer
from inventory.models import Item
from datetime import datetime

# Create your models here.
class DateTimeWithoutTZField(models.DateTimeField):
    def db_type(self, connection):
        return 'timestamp'




class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = DateTimeWithoutTZField(default=datetime.now, blank=True)
    total = models.FloatField(default=0.0)
    statusChoice = [('New','New'),
                    ('Pending Payment','Pending Payment'),
                    ('Pending Delivery','Pending Delivery'),
                    ('Done','Done')
                   ]
    status = models.TextField(choices=statusChoice,default='New')

    def __str__(self):
        return str(self.id)




class OrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    disc = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item.item_name