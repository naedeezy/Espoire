from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Transaction

#Create a Transaction form

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields = ('trans_type', 'number', 'amount', 'name', 'trans_id')



		widgets = {
			'trans_type': forms.TextInput(attrs={'class': "form-control"}),
			'number': forms.NumberInput(attrs={'class': "form-control"}),
			'amount': forms.TextInput(attrs={'class': "form-control"}),
			'name': forms.TextInput(attrs={'class': "form-control"}),
			'trans_id': forms.TextInput(attrs={'class': "form-control"}),
		}

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']