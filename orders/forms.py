from django.forms import ModelForm, TextInput, DateInput, Select
from .models import *
from django.utils.translation import gettext_lazy as _

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'




class OrderLineForm(ModelForm):
	class Meta:
		model = OrderLine
		fields = '__all__'
