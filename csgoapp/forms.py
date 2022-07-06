from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeamForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    region = forms.CharField(max_length=40)

class PlayerForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    team = forms.CharField(max_length=40)

class TournamentForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    region = forms.CharField(max_length=40)

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
