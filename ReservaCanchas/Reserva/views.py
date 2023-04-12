from django.shortcuts import render
from django.http import HttpResponse
from django.views .generic import TemplateView
import datetime
from .models import Cancha
# Create your views here.

def getInfoCanchaById (request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    result_layout = f"<h3>Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}</h3>"

    return HttpResponse(result_layout)


class MainView(TemplateView):
    template_name = "main.html"