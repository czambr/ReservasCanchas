from django.shortcuts import render
from django.http import HttpResponse
from django.views .generic import TemplateView
import datetime
from .models import Cancha, Horario
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

class MainView(TemplateView):
    template_name = "main.html"