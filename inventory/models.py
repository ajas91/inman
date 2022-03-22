from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(default="")

    def __str__(self):
        return self.category_name




class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.TextField(default="")
    desc = models.TextField(null=True)
    ordered_qty = models.IntegerField(defaul=0)
    remaining_qty = models.IntegerField(defaul=0)
    item_image = models.ImageField()
    item_category = models.ForeignKey(ItemCategory)
    purchase_price = models.FloatField(default=0.0)
    vat = models.FloatField(default=0.0)
    shipping_cost = models.FloatField(defaul=0.0)
    other_cost = models.FloatField(defaul=0.0)
    profit_matgin = models.FloatField(default=0.0)
    selling_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.item_name