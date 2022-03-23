from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ItemCategory)
admin.site.register(Item)