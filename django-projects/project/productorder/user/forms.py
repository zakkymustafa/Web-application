from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"
	
class LoginForm(forms.ModelForm):
	class Meta:
		model=User
		fields=("email","password")
						