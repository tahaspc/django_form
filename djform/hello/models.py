from django.db import models
from django.core.validators import RegexValidator
from django import forms


# Create your models here.
Departments = [('Aerospace', 'Aerospace'), ('Mechanical', 'Mechanical'), ('Chemical', 'Chemical'),
               ('MEMS', 'MEMS'), ('CS', 'CS'), ('EE', 'EE'), ('EP', 'EP'), ('Civil', 'Civil'), ('ESE', 'ESE')]


class User(models.Model):
    name = models.CharField(max_length=70, blank=False)
    email = models.EmailField(max_length=100)
    roll_no = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    departments = models.CharField(
        max_length=20, choices=Departments, default='Aerospace'
    )

    is_webd = models.BooleanField('Web Developer', default=False)
    is_gd = models.BooleanField('Graphic Designer', default=False)
    is_ma = models.BooleanField('Marketting', default=False)
    is_ui = models.BooleanField('UI/UX Designer', default=False)
    is_ve = models.BooleanField('Video Editor', default=False)

    comments = models.TextField(
        'Comments', default='Motivation for Joinig Hyperloop Team')
