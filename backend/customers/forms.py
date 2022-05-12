from django.forms import ModelForm, TextInput, DateInput, Select
from .models import *
from django.utils.translation import gettext_lazy as _

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

	def __init__(self,*args,**kwargs):
		super(CustomerForm,self).__init__(*args,**kwargs)

		self.fields['name'].widget=TextInput(attrs = {
								'class':'form-control',
								'id': 'name',
								})

		self.fields['phone_number'].widget=TextInput(attrs = {
						'class':'form-control',
						'id': 'phone_number',
						})

		self.fields['address'].widget=TextInput(attrs = {
						'class':'form-control',
						'id': 'address',
						})
		
		self.fields['number_of_orders'].widget.attrs['class'] = 'form-control'
		self.fields['number_of_orders'].widget.attrs['id'] = 'number_of_ rders'
		self.fields['number_of_orders'].widget.attrs['readonly'] = True 