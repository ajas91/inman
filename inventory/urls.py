from django.urls import path
from .views import *

urlpatterns = [
    path('inventory/',inventory, name='inventory'),
    path('inventory/newItem/',newItem, name='new_item'),
    path('inventory/<str:pk>/',updateDeleteItem, name='update_delete_item'),
    path('inventory/category/newCategory/',newCategory, name='new_category')

]