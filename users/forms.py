from typing import Any
from django import forms
from .models import User
from django.core.mail import send_mail

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

    



