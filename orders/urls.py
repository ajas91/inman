from django.urls import path
from .views import *

urlpatterns = [
    path('orders/',orders, name='orders'),
    path('order/new_order/',newOrder, name='new_order'),
    path('order/<str:pk>/',updateDeleteOrder, name='update_delete_order'),
]