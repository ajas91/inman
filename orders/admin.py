from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(OrderLine)
admin.site.register(Order)