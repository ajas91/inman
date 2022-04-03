from django.forms import ModelForm, DateTimeInput
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
			})

		self.fields['customer'].widget.attrs['class'] = 'form-select'
		self.fields['customer'].widget.attrs['id'] = 'customer'

		self.fields['status'].widget.attrs['class'] = 'form-select'
		self.fields['status'].widget.attrs['id'] = 'status'

		self.fields['total'].widget.attrs['class'] = 'form-control omr'
		self.fields['total'].widget.attrs['id'] = 'total'
		self.fields['total'].widget.attrs['readonly'] = True




class OrderLineForm(ModelForm):
	class Meta:
		model = OrderLine
		fields = '__all__'

	def __init__(self,*args,**kwargs):
		super(OrderLineForm,self).__init__(*args,**kwargs)

		self.fields['item'].widget.attrs['class'] = 'form-select'
		self.fields['item'].widget.attrs['id'] = 'item'

		self.fields['qty'].widget.attrs['class'] = 'form-control'
		self.fields['qty'].widget.attrs['id'] = 'qty'

		self.fields['disc'].widget.attrs['class'] = 'form-control omr'
		self.fields['disc'].widget.attrs['id'] = 'disc'

		self.fields['total_price'].widget.attrs['class'] = 'form-control omr'
		self.fields['total_price'].widget.attrs['id'] = 'total_price'