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
from django.conf import settings
from django.conf.urls.static import static

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
    path('alta_players.html', views.alta_player, name='alta_player'),
    path('eliminar_player_<int:id>', views.eliminar_player , name='eliminar_player'),
    path('alta_teams.html', views.alta_team, name='alta_team'),
    path('alta_team', views.alta_team, name='alta_team'),
    path('eliminar_team_<int:id>', views.eliminar_team , name='eliminar_team'),
    path('alta_tournament', views.alta_tournament, name='alta_tournament'),
    path('alta_tournaments.html', views.alta_tournament, name='alta_tournament'),
    path('eliminar_tournament_<int:id>', views.eliminar_tournament , name='eliminar_tournament'),
    path('detalles_teams_<int:id>', views.detalles_teams, name='detalles_teams'),
    path('detalles_players_<int:id>', views.detalles_players, name='detalles_players'),
    path('detalles_tournaments_<int:id>', views.detalles_tournaments, name='detalles_tournaments'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    path('editarperfil.html', views.editarPerfil, name="editarPerfil"),
    path('editar_player/<int:id>/', views.editar_players, name='editar_players'),
    path('editar_tournaments/<int:id>/', views.editar_tournaments, name='editar_tournaments'),
    path('editar_teams_<int:id>/', views.editar_teams, name='editar_teams'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
