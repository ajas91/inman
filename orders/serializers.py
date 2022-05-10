from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.username')
    customer = serializers.HyperlinkedRelatedField(many=True, view_name='customer-detail', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer','order_date','total',
                  'status',
                #   'created_by', 
                 ]




class OrderLineSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.HyperlinkedRelatedField(many=True, view_name='order-detail', read_only=True)
    item = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'item','qty','disc',
                  'total_price','order',
                 ]