from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from csgoapp.models import Teams,Players,Tournaments
from csgoapp.forms import TeamForm,PlayerForm,TournamentForm, UserEditForm
from django.shortcuts import render , get_object_or_404 , redirect
from . models import Teams, Players

# Create your views here.

def index(request):
    return render(request, "csgoapp/index.html")

#@login_required
def about(request):
    return render(request, "csgoapp/about.html")

def teams(request):
    teams = Teams.objects.all()
    dic = {
        'teams' : teams
    }
    return render (request, "csgoapp/teams.html", dic)

def tournaments(request):
    tournaments = Tournaments.objects.all()
    diccionario2 = {
        'tournaments' : tournaments
    }
    return render (request, "csgoapp/tournaments.html", diccionario2)

def players(request):
    players = Players.objects.all()
    diccionario = {
        'players' : players
    }
    return render (request, "csgoapp/players.html", diccionario)

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)
                return render(request, "csgoapp/logeado.html",{"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request, "csgoapp/Errorlogin.html", {"mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request, "csgoapp/Errorlogin.html", {"mensaje":"Error, formulario erróneo"})


    form = AuthenticationForm()

    return render ( request, 'csgoapp/login.html', {"form":form})


def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render (request, "csgoapp/index.html",{"mensaje":"Usuario creado"})
        
    else:
            form = UserCreationForm()

    return render (request, "csgoapp/registro.html", {"form":form})
    

def logout(request):
    logout(request)
    return redirect('csgoapp/logout.html')


def buscar_player(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
    if nombre:
        players = Players.objects.filter(nombre__icontains=nombre)
        return render(request, 'csgoapp/players.html', {'players': players})
    else:
        print('Nada para mostrar')
        return request(request, 'csgoapp/players.html', {})


@login_required
def alta_team(request):
    if request.method == "POST":
        mi_form = TeamForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            team = Teams(nombre = datos["nombre"], region = datos["region"])
            team.save()
            return redirect("teams.html")
    return render(request, "csgoapp/alta_team.html")

@login_required
def alta_tournament(request):
    if request.method == "POST":
        mi_form = TournamentForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            tournament = Tournaments(nombre = datos["nombre"], region = datos["region"])
            tournament.save()
        return redirect("tournaments.html")
    return render(request, "csgoapp/alta_tournaments.html")

@login_required
def alta_player(request):
    if request.method == "POST":
        mi_form = PlayerForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            player = Players(nombre = datos["nombre"], team = datos["team"])
            player.save()
        return redirect("players.html")
    return render(request, "csgoapp/alta_players.html")

def editar_teams(request,id):
    team = Teams.objects.get(id=id)
    
    if request.method == 'POST':
        miform = TeamForm(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            team.nombre = datos['nombre']
            team.region = datos['region']
            team.save()
            return redirect('/')
    else:
        miform = TeamForm(initial={'nombre': team.nombre, 'region': team.region})

    return render(request, "csgoapp/editar_teams.html", {'miform':miform , 'team':team})

@login_required
def eliminar_team(request, id):
    team = get_object_or_404(Teams , pk = id)

    if team :
        team.delete()

    return redirect('teams.html')

@login_required
def eliminar_tournament(request, id):
    tournament = Tournaments.objects.get(id=id)
    tournament.delete()

    tournaments = Tournaments.objects.all()
    
    return render(request, "csgoapp/tournaments.html", {"tournaments":tournaments})

@login_required
def eliminar_player(request, id):
    player = get_object_or_404(Players , pk = id)

    if player :
        player.delete()

    return redirect('players.html')
    
   
def detalles_tournaments(request , id) :
    #teams = get_object_or_404(Teams , pk = id)
    tournaments = Tournaments.objects.filter(id=id)

    return render(request, "csgoapp/detalles_tournaments.html", {"tournaments": tournaments})
        
        
def detalles_teams(request , id) :
    #teams = get_object_or_404(Teams , pk = id)
    teams = Teams.objects.filter(id=id)

    return render(request, "csgoapp/detalles_teams.html", {"teams": teams})

def detalles_players(request , id) :
    #teams = get_object_or_404(Teams , pk = id)
    players = Players.objects.filter(id=id)

    return render(request, "csgoapp/detalles_players.html", {"players": players})


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion ['password1']
            usuario.set_password(password)
            usuario.save()

            return redirect('/')
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    
    return render(request, "csgoapp/editarPerfil.html", {"miFormulario": miFormulario, "usuario":usuario})


@login_required
def editar_players(request,id):
    player = Players.objects.get(id=id)

    if request.method == 'POST':
        miform = PlayerForm(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            player.nombre = datos['nombre']
            player.team = datos['team']
            player.save()
            return redirect('/')
    else:
        miform = PlayerForm(initial={'nombre': player.nombre, 'team': player.team})

    return render(request, "csgoapp/editar_players.html", {'miform':miform , 'player':player})

@login_required
def editar_tournaments(request,id):
    tournament = Tournaments.objects.get(id=id)

    if request.method == 'POST':
        miform = TournamentForm(request.POST)
        if miform.is_valid():
            datos = miform.cleaned_data
            tournament.nombre = datos['nombre']
            tournament.region = datos['region']
            tournament.save()
            return redirect('/')
    else:
        miform = TournamentForm(initial={'nombre': tournament.nombre, 'region': tournament.region})

    return render(request, "csgoapp/editar_tournaments.html", {'miform':miform , 'tournament':tournament})