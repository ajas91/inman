from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Customer
        fields = ['id', 'name','phone_number','date_created',
                  'address', 'number_of_orders', 'created_by', 'active']




class UserSerializer(serializers.HyperlinkedModelSerializer):
    customers = serializers.HyperlinkedRelatedField(many=True, view_name='customers', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'customers']