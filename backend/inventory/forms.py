from django.forms import ModelForm, TextInput, DateInput, Select,ChoiceField
from .models import *
from django.utils.translation import gettext_lazy as _

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'
	
	def __init__(self,*args,**kwargs):
		super(ItemForm,self).__init__(*args,**kwargs)

		self.fields['item_image'].required = False
		self.fields['item_name'].widget=TextInput(attrs = {
								'class':'form-control',
								'id': 'item_name',
								})

		self.fields['desc'].widget=TextInput(attrs = {
								'class':'form-control',
								'id': 'desc',
								})

		self.fields['ordered_qty'].widget.attrs['class'] = 'form-control'
		self.fields['ordered_qty'].widget.attrs['id'] = 'ordered_qty'
		self.fields['ordered_qty'].widget.attrs['onchange'] = 'updateQTY();'


		self.fields['remaining_qty'].widget.attrs['class'] = 'form-control'
		self.fields['remaining_qty'].widget.attrs['id'] = 'remaining_qty'
		self.fields['remaining_qty'].widget.attrs['readonly'] = True
		# self.fields['remaining_qty'].disabled = True

		self.fields['item_category'].widget.attrs['class'] = 'form-select'
		self.fields['item_category'].widget.attrs['id'] = 'item_category'

		self.fields['purchase_price'].widget.attrs['class'] = 'form-control omr'
		self.fields['purchase_price'].widget.attrs['id'] = 'purchase_price'
		self.fields['purchase_price'].widget.attrs['placeholder'] = 'Price in SAR'
		self.fields['purchase_price'].widget.attrs['onchange'] = 'updateVAT();'

		self.fields['vat'].widget.attrs['class'] = 'form-control omr'
		self.fields['vat'].widget.attrs['id'] = 'vat'
		self.fields['vat'].widget.attrs['onchange'] = 'updateSellingPrice();'


		self.fields['shipping_cost'].widget.attrs['class'] = 'form-control omr'
		self.fields['shipping_cost'].widget.attrs['id'] = 'shipping_cost'
		self.fields['shipping_cost'].widget.attrs['placeholder'] = 'Price in OMR'
		self.fields['shipping_cost'].widget.attrs['onchange'] = 'updateSellingPrice();'

		self.fields['other_cost'].widget.attrs['class'] = 'form-control omr'
		self.fields['other_cost'].widget.attrs['id'] = 'other_cost'
		self.fields['other_cost'].widget.attrs['placeholder'] = 'Price in OMR'
		self.fields['other_cost'].required = False
		self.fields['other_cost'].widget.attrs['onchange'] = 'updateSellingPrice();'

		self.fields['profit_margin'].widget.attrs['class'] = 'form-control'
		self.fields['profit_margin'].widget.attrs['id'] = 'profit_margin'
		self.fields['profit_margin'].widget.attrs['placeholder'] = 'Percentage (Number only)'
		self.fields['profit_margin'].widget.attrs['onchange'] = 'updateSellingPrice();'

		self.fields['selling_price'].widget.attrs['class'] = 'form-control omr'
		self.fields['selling_price'].widget.attrs['id'] = 'selling_price'
		self.fields['selling_price'].widget.attrs['placeholder'] = 'Price in OMR'




class CategoryForm(ModelForm):
	class Meta:
		model = ItemCategory
		fields = '__all__'
	def __init__(self,*args,**kwargs):
		super(CategoryForm,self).__init__(*args,**kwargs)
		self.fields['category_name'].widget=TextInput(attrs = {
						'class':'form-control',
						'id': 'item_name',
						})