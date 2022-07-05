"""Csgoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from csgoapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about.html', views.about),
    path('index.html', views.index),
    path('login.html', views.login_request, name='Login'),
    path('registro.html', views.register, name='Register'),
    path('logout.html',LogoutView.as_view(template_name='csgoapp/logout.html'), name='Logout'),
    path('teams.html', views.teams),
    path('tournaments.html', views.tournaments),
    path('players.html', views.players),
    path('alta_player', views.alta_player, name='alta_player'),
    path('buscar_player', views.buscar_player, name='buscar_player'),
    path('eliminar_player<int:id>', views.eliminar_player , name='eliminar_player'),
    path('alta_team.html', views.alta_team, name='alta_team'),
    path('alta_team', views.alta_team, name='alta_team'),
    #path('buscar_team', views.buscar_team, name='buscar_team'),
    path('eliminar_team_<int:id>', views.eliminar_team , name='eliminar_team'),
    path('alta_tournament', views.alta_tournament, name='alta_tournament'),
    path('buscar_tournament', views.buscar_tournament, name='buscar_tournament'),
    path('eliminar_tournament<int:id>', views.eliminar_tournament , name='eliminar_tournament'),
    path('editar_teams/<int:id>/', views.editar_teams, name='editar_teams'),
    #path('editar_team', views.editar_teams, name='editar_team'),
    path('detalles_teams_<int:id>', views.detalles_teams, name='detalles_teams'),

    #path('editar_player/', views.editar_player, name='editar_player'),
    #path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
]
