from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Item
        fields = ['id', 'item_name','desc','ordered_qty','remaining_qty',
                  'item_image', 'item_category', 'purchase_price', 'vat', 
                  'shipping_cost','other_cost','profit_margin','selling_price',
                  'created_by','created_date',
                 ]




class ItemCategorySerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = ItemCategory
        fields = ['id', 'category_name']

