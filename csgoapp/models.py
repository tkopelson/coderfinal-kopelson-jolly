from cProfile import Profile
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

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

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)








