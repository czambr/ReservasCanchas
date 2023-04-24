from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import datetime
from .models import Cancha, Horario
from .forms import RegistroForm, LoginForm
# Create your views here.

def getInfoCanchaById (request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    horarios = Horario.objects.filter(cancha__id=cancha.id)
    contexto = { 'nombre': cancha.nombre, 
                 'descripcion': cancha.descripcion,
                 'horarios': horarios
            }
    return render (request, "cancha.html", contexto)

def getListadoCanchas (request):
    canchas = Cancha.objects.all()
    nombre_canchas = []
    for cancha in canchas:
        nombre_canchas.append((cancha.id, cancha.nombre))
    return render (request, "canchas.html", {'listado': nombre_canchas} )

def registro_request(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        print('Evaluacion: ', form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Se ha registrado exitosamente')
            return redirect("landing")

    # Si el formulario no fue válido, retorna formulario vacío
    messages.error(request, 'Información no válida')
    form = RegistroForm()
    return render(request=request,
                  template_name='registro.html', 
                  context={'registro_form': form})

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Ha iniciado sesión como: {username}')
                return redirect("landing")
            messages.error(request, 'Credenciales incorrectas')
        messages.error(request, 'Credenciales incorrectas')
    # Método no válido, retorna formulario vacío
    form = LoginForm()
    return render(request=request, 
                  template_name='login.html', 
                  context={'login_form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect("login")

class MainView(TemplateView):
    template_name = "main.html"