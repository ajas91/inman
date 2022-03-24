from django.db import models
import os

# Create your models here.
class ItemCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(default="",unique=True)

    def __str__(self):
        return self.category_name




class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.TextField(default="",null=True)
    desc = models.TextField(null=True)
    ordered_qty = models.IntegerField(default=0,null=True)
    remaining_qty = models.IntegerField(default=0,null=True)
    item_image = models.ImageField(null=True,upload_to='static/image/uploads/')
    item_category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    purchase_price = models.FloatField(default=0.0,null=True)
    vat = models.FloatField(default=0.0,null=True)
    shipping_cost = models.FloatField(default=0.0,null=True)
    other_cost = models.FloatField(default=0.0,null=True)
    profit_margin = models.FloatField(default=0.0,null=True)
    selling_price = models.FloatField(default=0.0,null=True)

    def __str__(self):
        return self.item_name

    def getTotalCost(self):
        return self.purchase_price*0.1+self.vat+self.shipping_cost+self.other_cost