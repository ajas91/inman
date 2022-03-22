from django.forms import ModelForm, TextInput, DateInput, Select
from .models import *
from django.utils.translation import gettext_lazy as _

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
