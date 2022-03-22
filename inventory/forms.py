from tkinter import Widget
from django.forms import ModelForm, TextInput, DateInput, Select
from .models import *
from django.utils.translation import gettext_lazy as _

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'
	
	def __init__(self,*args,**kwargs):
		super(ItemForm,self).__init__(*args,**kwargs)

		self.fields['item_name'].widget = TextInput(attrs={
			'class':'form-control',
		})

		self.fields['desc'].widget = TextInput(attrs={
			'class':'form-control',
		})

		self.fields['ordered_qty'].widget = TextInput(attrs={
			'class':'form-control',
		})

		self.fields['remaining_qty'].widget = TextInput(attrs={
			'class':'form-control',
		})
		self.fields['remaining_qty'].disabled = True

		self.fields['item_category'].widget = TextInput(attrs={
			'class':'select-control',
		})

		self.fields['purchase_price'].widget = TextInput(attrs={
			'class':'form-control',
			'placeholder': 'Price in SAR',
		})

		self.fields['vat'].widget = TextInput(attrs={
			'class':'form-control',
		})

		self.fields['shipping_cost'].widget = TextInput(attrs={
			'class':'form-control',
			'placeholder': 'Price in OMR',
		})

		self.fields['other_cost'].widget = TextInput(attrs={
			'class':'form-control',
			'placeholder': 'Price in OMR',
		})
		self.fields['other_cost'].required = False

		self.fields['profit_margin'].widget = TextInput(attrs={
			'class':'form-control',
			'placeholder': 'Percentage (Number only)',
		})

		self.fields['selling_price'].widget = TextInput(attrs={
			'class':'form-control',
			'placeholder': 'Price in OMR',
		})