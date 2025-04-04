from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=300, widget=TextInput)
    password = forms.CharField(max_length=300, widget=PasswordInput)