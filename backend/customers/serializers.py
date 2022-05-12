from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User


class CustomersSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='created_by.username')
    orders = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'name','phone_number','date_created',
                  'address', 'number_of_orders', 'active',
                  'created_by','orders' 
                 ]




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']