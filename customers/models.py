from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200,default="")
    phone_number = models.TextField(max_length=8,default="",unique=True)
    date_created = models.DateField(auto_now_add=True)
    address = models.TextField(default="")
    number_of_orders = models.IntegerField(default=0)
    created_by = models.ForeignKey('auth.User', related_name='customers', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    def updateNumberOfOrders(self):
        self.number_of_orders +=1