from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import Cancha
# Create your views here.

def getInfoCanchaById (request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    print(cancha)
    result_layout = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}</h3>"

    return HttpResponse(result_layout)
