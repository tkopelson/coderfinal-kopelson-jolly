from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from csgoapp.models import Teams,Players,Tournaments
from csgoapp.forms import TeamForm,PlayerForm,TournamentForm
from django.shortcuts import render , get_object_or_404 , redirect
from . models import Teams

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
    return render (request, "csgoapp/tournaments.html")

def players(request):
    return render (request, "csgoapp/players.html")

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

def alta_player(request):
    if request.method == "POST":
        mi_form = PlayerForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            player = Players(nombre = datos["nombre"], team = datos["team"])
            player.save()
        return render(request, "csgoapp/players.html") 
    return render(request, "csgoapp/players.html")

def buscar_player(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
    if nombre:
        players = Players.objects.filter(nombre__icontains=nombre)
        return render(request, 'csgoapp/players.html', {'players': players})
    else:
        print('Nada para mostrar')
        return request(request, 'csgoapp/players.html', {})

def eliminar_player(request, id):
    player = Players.objects.get(id=id)
    player.delete()

    players = Players.objects.all()
    
    return render(request, "csgoapp/players.html", {"players":players})


def alta_team(request):
    if request.method == "POST":
        mi_form = TeamForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            team = Teams(nombre = datos["nombre"], region = datos["region"])
            team.save()
            return redirect("teams.html")
    return render(request, "csgoapp/alta_team.html")

"""
def buscar_team(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
    if nombre:
        teams = Teams.objects.filter(nombre__icontains=nombre)
        return render(request, 'csgoapp/teams.html', {'teams': teams})
    else:
        print('Nada para mostrar')
        return request(request, 'csgoapp/teams.html', {})
"""

def eliminar_team(request, id):
    team = get_object_or_404(Teams , pk = id)

    if team :
        team.delete()

    return redirect('teams.html')


def alta_tournament(request):
    if request.method == "POST":
        mi_form = TournamentForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            tournament = Tournaments(nombre = datos["nombre"], region = datos["region"])
            tournament.save()
        return render(request, "csgoapp/tournaments.html") 
    return render(request, "csgoapp/tournaments.html")

def buscar_tournament(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
    if nombre:
        tournaments = Tournaments.objects.filter(nombre__icontains=nombre)
        return render(request, 'csgoapp/tournaments.html', {'tournaments': tournaments})
    else:
        print('Nada para mostrar')
        return request(request, 'csgoapp/tournaments.html', {})

def eliminar_tournament(request, id):
    tournament = Tournaments.objects.get(id=id)
    tournament.delete()

    tournaments = Tournaments.objects.all()
    
    return render(request, "csgoapp/tournaments.html", {"tournaments":tournaments})

"""
def editar_team(request, id):
    team = get_object_or_404(Teams , pk = id)

    if request.method == "POST":
        mi_formulario = TeamForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return redirect('teams.html')

    else:
        mi_formulario = TeamForm()
    
    return render (request, "csgoapp/editar_team.html", {"mi_formulario": mi_formulario})
"""

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
    
   

        
        

def detalles_teams(request , id) :
    #teams = get_object_or_404(Teams , pk = id)
    teams = Teams.objects.filter(id=id)

    return render(request, "csgoapp/detalles_teams.html", {"teams": teams})

"""
def eliminar_player(request, id):
    player = Players.objects.get(id=id)
    player.delete()

    players = Players.objects.all()
    
    return render(request, "csgoapp/players.html", {"players":players})
"""
     

"""
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            usuario.usuario = informacion['usuario']
            usuario.password1 = informacion ['password1']
            usuario.password2 = informacion ['password1']
            usuario.save()

            return render (request, "csgoapp/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'usuario': usuario.usuario})
    
    return render(request, "csgoapp/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

"""
