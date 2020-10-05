from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User  #Kaunse model mai change karna hai
        fields = ['username','email','password1','password2']  #kis order mai display karna hai register page mai
