from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    #cliente
 
    path('usuarios_lista_api/', views.usuarios_lista_api, name='usuarios_lista_api'),
    path('usuarios_lista_api2/', views.usuarios_lista_api2, name='usuarios_lista_api2'),
    path('categoria_lista_api/', views.categorias_lista_api, name='categorias_lista_api'),
    path('propiedades_lista_api/', views.propiedades_lista_api, name='propiedades_lista_api'),
    path('usuarios_busqueda_simple/', views.usuarios_busqueda_simple, name='usuarios_busqueda_simple'),
    path('usuarios_busqueda_avanzada/', views.usuarios_busqueda_avanzada, name='usuarios_busqueda_avanzada'),
    path('buscar/categorias/', views.categorias_busqueda_avanzada, name='categorias_busqueda_avanzada'),
    path('buscar/propiedades/', views.propiedades_busqueda_avanzada, name='propiedades_busqueda_avanzada'),
    path('buscar/servicios_extra/', views.servicios_extra_busqueda_avanzada, name='servicios_extra_busqueda_avanzada'),



    
]