from django.urls import path
from .views import *

urlpatterns = [
    path('customers/',customers, name='customers'),
    path('customer/new_customer/',newCustomer, name='new_customer'),
    path('customer/<str:pk>/',updateDeleteCustomer, name='update_delete_customer'),
]