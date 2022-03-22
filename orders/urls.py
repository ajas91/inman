from django.urls import path
from .views import *

urlpatterns = [
    path('orders/',orders, name='orders'),
    path('orders/<str:pk>/',orderDetails, name='order_details'),
]