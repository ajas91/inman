from django.urls import path
from .views import *

urlpatterns = [
    path('customers/',customes, name='orders'),
    path('customer/new_customer/',newCustomer, name='new_customer'),
    path('customer/<str:pk>/',updateCustomer, name='update_customer'),
]