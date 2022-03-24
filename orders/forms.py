from django.forms import ModelForm, TextInput, DateTimeInput, Select
from .models import *
from django.utils.translation import gettext_lazy as _

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
	
	def __init__(self,*args,**kwargs):
		super(OrderForm,self).__init__(*args,**kwargs)

		self.fields['order_date'].widget = DateTimeInput(
			attrs={
				'class':'form-control',
				'id':'order_date',
		        'type': 'datetime-local',
				'form':'order'
			})
		# self.fields['order_date'].widget.attrs['class'] = 'form-control'
		# self.fields['order_date'].widget.attrs['id'] = 'order_date'
		# self.fields['order_date'].widget.attrs['type'] = 'datetime-local'

		self.fields['customer'].widget.attrs['class'] = 'form-select'
		self.fields['customer'].widget.attrs['id'] = 'customer'
		self.fields['customer'].widget.attrs['form'] = 'order' 

		self.fields['status'].widget.attrs['class'] = 'form-select'
		self.fields['status'].widget.attrs['id'] = 'status'
		self.fields['status'].widget.attrs['form'] = 'order' 

		self.fields['total'].widget.attrs['class'] = 'form-control omr'
		self.fields['total'].widget.attrs['id'] = 'total'
		self.fields['total'].widget.attrs['form'] = 'order' 





class OrderLineForm(ModelForm):
	class Meta:
		model = OrderLine
		fields = '__all__'

	def __init__(self,*args,**kwargs):
		super(OrderLineForm,self).__init__(*args,**kwargs)

		self.fields['item'].widget.attrs['class'] = 'form-select'
		self.fields['item'].widget.attrs['id'] = 'item'
		self.fields['item'].widget.attrs['form'] = 'orderLine' 

		self.fields['qty'].widget.attrs['class'] = 'form-control'
		self.fields['qty'].widget.attrs['id'] = 'qty'
		self.fields['qty'].widget.attrs['form'] = 'orderLine' 


		self.fields['disc'].widget.attrs['class'] = 'form-control omr'
		self.fields['disc'].widget.attrs['id'] = 'disc'
		self.fields['disc'].widget.attrs['form'] = 'orderLine' 


		self.fields['total_price'].widget.attrs['class'] = 'form-control omr'
		self.fields['total_price'].widget.attrs['id'] = 'total_price'
		self.fields['total_price'].widget.attrs['form'] = 'orderLine' 
