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
			'id':'item_name',
		})

		self.fields['desc'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'desc',
		})

		self.fields['ordered_qty'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'ordered_qty',
		})

		self.fields['remaining_qty'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'remaining_qty',
		})
		self.fields['remaining_qty'].disabled = True

		self.fields['item_category'].widget = TextInput(attrs={
			'class':'select-control',
			'id':'item_category',
		})

		self.fields['purchase_price'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'purchase_price',
			'placeholder': 'Price in SAR',
		})

		self.fields['vat'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'vat',
		})

		self.fields['shipping_cost'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'shipping_cost',
			'placeholder': 'Price in OMR',
		})

		self.fields['other_cost'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'other_cost',
			'placeholder': 'Price in OMR',
		})
		self.fields['other_cost'].required = False

		self.fields['profit_margin'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'profit_margin',
			'placeholder': 'Percentage (Number only)',
		})

		self.fields['selling_price'].widget = TextInput(attrs={
			'class':'form-control',
			'id':'selling_price',
			'placeholder': 'Price in OMR',
		})




class CategoryForm(ModelForm):
	class Meta:
		model = ItemCategory
		fields = '__all__'
	def __init__(self,*args,**kwargs):
		super(CategoryForm,self).__init__(*args,**kwargs)

		self.fields['category_name'].widget = TextInput(attrs={
			'class':'form-control',
		})