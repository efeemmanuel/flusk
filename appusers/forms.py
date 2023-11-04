from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import CustomerInfo
from .models import *



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Enter username'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Set password'}))
    
        
        

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Enter username'}))
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Enter email address'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Set password'}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 750px;', 'placeholder': 'Confirm password'}))

    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
  
   
   
class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    phone_number = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    email = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    message = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 800px;'}))
    class Meta:
        model = Contact
        fields = ['name','email','phone_number', 'message']