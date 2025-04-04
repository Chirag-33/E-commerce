from django import forms
from .models import Vendor, Product,UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

class VendorCreationForm(UserCreationForm):
    class Meta:
        model = Vendor
        fields = ['username', 'password1', 'password2', 'user_type']

class VendorLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, widget=TextInput)
    password = forms.CharField(max_length=300, widget=PasswordInput)

class vendor_products(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number']

class PaymentForm(forms.Form):
    stripe_token = forms.CharField(max_length=255)
    