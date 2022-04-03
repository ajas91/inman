from django.urls import path
from .views import *

urlpatterns = [
    path('orders/',orders, name='orders'),
    path('orders/new_order/',newOrder, name='new_order'),
    path('orders/<str:pk>/',updateDeleteOrder, name='update_delete_order'),
]