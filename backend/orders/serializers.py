from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class OrderSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.username')
    orderlines = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer','order_date','total',
                  'status','orderlines','created_by', 
                 ]




class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['id', 'item','qty','disc',
                  'total_price','order',
                 ]