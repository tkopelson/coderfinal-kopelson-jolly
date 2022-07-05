from django import forms

class TeamForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    region = forms.CharField(max_length=40)

class PlayerForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    team = forms.CharField(max_length=40)

class TournamentForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    region = forms.CharField(max_length=40)

