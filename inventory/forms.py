from django.forms import ModelForm, TextInput, DateInput, Select
from .models import *
from django.utils.translation import gettext_lazy as _

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'