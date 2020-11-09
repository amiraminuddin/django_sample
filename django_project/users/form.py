from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


#class that inherit from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        #field that will be shown
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        #field that will be shown
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
