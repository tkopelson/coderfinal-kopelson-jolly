from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.models import User

class Teams(models.Model):
    nombre = models.CharField(max_length=40)
    region = models.CharField(max_length=40)

    def __str__(self) :
        return f'Team : { self.nombre }'

class Players(models.Model):
    nombre = models.CharField(max_length=40)
    team = models.CharField(max_length=40)

class Tournaments(models.Model):
    nombre = models.CharField(max_length=40)
    region = models.CharField(max_length=40)


"""
class UserEditForm(UserCreationForm)
    usuario = forms.CharField(max_length=40)
    password1= forms.Charfield(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.Charfield(label='Repetir la constraseña', widget=forms.PasswordInput)

class Meta:
    model = User
    fields = { 'usuario', 'password1', 'password2' }
    help_texts = {k:"" for k in fields}

"""



