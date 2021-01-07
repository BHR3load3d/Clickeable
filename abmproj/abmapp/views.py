from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import edificio,piso,area
from django import forms

def index(request):
    template = loader.get_template('abmapp/index.html')

    # if 'piso' in request.POST.keys() and request.POST['piso']:
    #     piso_seleccionado = request.POST['piso']
    # else:
    #     piso_seleccionado = -1

    # if 'edificio' in request.POST.keys() and request.POST['edificio']:
    #     edificio_seleccionado = request.POST['edificio']
    # else:
    #     edificio_seleccionado = -1

    # print(edificio_seleccionado)
    # print(piso_seleccionado)

    edificios = edificio.objects.filter(activo=1)
    # pisos = piso.objects.filter(edificio=edificio_seleccionado).filter(activo=1)
    # areas = area.objects.filter(piso=piso_seleccionado).filter(activo=1)

    # context = { 'areas' : areas, 'edificios': edificios, 'pisos': pisos }
    context = { 'edificios': edificios }
    return HttpResponse(template.render(context, request))

def load_pisos(request):
    edificio_id = request.GET.get('edificio')
    pisos = piso.objects.filter(edificio=edificio_id).filter(activo=True).order_by('descripcion')
    return render(request, 'abmapp/pisos_dropdown_list_options.html', {'pisos': pisos})

def load_areas(request):
    piso_id = request.GET.get('piso')
    areas = area.objects.filter(piso=piso_id).order_by('descripcion')
    return render(request, 'abmapp/areas_list.html', {'areas': areas})


def carga(request):
    # Clickleable.objects.create(idSite=1, idArea=1, tipo=1, latitud=227, longitud=58.5, radioMayor=61,radioMenor=47.5, activo=True )
    # Clickleable.objects.create(idSite=1, idArea=2, tipo=1, latitud=349, longitud=58.5, radioMayor=61,radioMenor=47.5, activo=True )
    # Clickleable.objects.create(idSite=1, idArea=3, tipo=2, latitud=568, longitud=57, radioMayor=32,radioMenor=0, activo=True )
    # Clickleable.objects.create(idSite=1, idArea=4, tipo=2, latitud=639, longitud=57, radioMayor=32,radioMenor=0, activo=True )
    # Clickleable.objects.create(idSite=1, idArea=5, tipo=1, latitud=469.5, longitud=58.5, radioMayor=61,radioMenor=47.5, activo=False )
    return HttpResponse("carga exitosa!!")
    