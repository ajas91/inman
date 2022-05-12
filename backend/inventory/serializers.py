from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name','desc','ordered_qty','remaining_qty',
                  'item_image', 'item_category', 'purchase_price', 'vat', 
                  'shipping_cost','other_cost','profit_margin','selling_price',
                  'created_date','created_by',
                 ]




class ItemCategorySerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)
    class Meta:
        model = ItemCategory
        fields = ['id', 'category_name','items']

