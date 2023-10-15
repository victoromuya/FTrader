from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

user_model = get_user_model()

class NewUserForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    
    class Meta:
        model = user_model
        fields = [
            'username',
            'password1',
            'password2',
        ]
        help_texts = {
            'username': None,
            'password2': None,
        }
        
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        if commit:
            user.save()
        return user
    