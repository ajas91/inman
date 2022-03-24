from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default="")
    phone_number = models.TextField(max_length=8,default="",unique=True)
    date_created = models.DateField(auto_now_add=True)
    address = models.TextField(default="")
    number_of_orders = models.IntegerField(default=0)

    def __str__(self):
        return self.name