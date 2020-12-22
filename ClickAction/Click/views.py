from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Clickleable

def index(request):
    template = loader.get_template('Click/index.html')
    areas = Clickleable.objects.filter(idSite=1).filter(activo=True)
    context = { 'data' : areas }
    return HttpResponse(template.render(context, request))

def carga(request):
    Clickleable.objects.create(idSite=1, idArea=1, tipo=1, latitud=227, longitud=58.5, radioMayor=61,radioMenor=47.5, activo=True )
    Clickleable.objects.create(idSite=1, idArea=2, tipo=1, latitud=349, longitud=58.5, radioMayor=61,radioMenor=47.5, activo=True )
    Clickleable.objects.create(idSite=1, idArea=3, tipo=2, latitud=568, longitud=57, radioMayor=32,radioMenor=0, activo=True )
    Clickleable.objects.create(idSite=1, idArea=4, tipo=2, latitud=639, longitud=57, radioMayor=32,radioMenor=0, activo=True )
    Clickleable.objects.create(idSite=1, idArea=5, tipo=1, latitud=469.5, longitud=58.5, radioMayor=61,radioMenor=47.5, activo=False )
    return HttpResponse("carga exitosa!!")
