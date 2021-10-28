from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Transaction

#Create a Transaction form

class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
		fields = "__all__"

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']