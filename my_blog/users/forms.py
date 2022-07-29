from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=20, required=False)
	last_name = forms.CharField(max_length=20, required=False)

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name',]

class ProfileUpdateForm(ModelForm):

	class Meta:
		model = Profile
		fields = ['image']