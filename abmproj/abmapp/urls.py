from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('carga', views.carga, name='carga'),
    path('ajax/load_pisos/', views.load_pisos, name='ajax_load_pisos'),
    path('ajax/load_areas/', views.load_areas, name='ajax_load_areas'),
    path('ajax/save_area/', views.save_area, name='ajax_save_area'),
    path('ajax/delete_area/', views.delete_area, name='ajax_delete_area'),
]