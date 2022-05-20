from django import forms
from .models import User
from django.core import validators


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'roll_no',
                  'phone_number', 'departments', 'is_webd', 'is_gd', 'is_ma', 'is_ui', 'is_ve', 'comments']
        labels = {'comments': ''}
