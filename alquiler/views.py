import requests
from django.core import serializers
from django.shortcuts import render,redirect
from .forms import *

def index(request):
    return render(request, "index.html")




def usuarios_lista_api(request):
    response = requests.get('https://IsraelJimenez.pythonanywhere.com/api/v1/usuarios')
    usuarios = response.json()
    return render(request, 'Usuario/lista_api.html', {"usuarios": usuarios})

def usuarios_lista_api2(request):
    response = requests.get('https://IsraelJimenez.pythonanywhere.com/api/v1/usuarios')
    usuarios = response.json()
    return render(request, 'Usuario/lista_api2.html', {"usuarios": usuarios})

def propiedades_lista_api(request):
    response = requests.get('https://israeljimenez.pythonanywhere.com/api/v1/propiedades/')
    propiedades = response.json()
    return render(request, 'Propiedad/propiedad_lista_api.html', {"propiedades": propiedades})

def categorias_lista_api(request):
    response = requests.get('https://israeljimenez.pythonanywhere.com/api/v1/categorias/')
    categorias = response.json()
    return render(request, 'Categoria/categoria_lista_api.html', {"categorias": categorias})

def usuarios_busqueda_simple(request):
    formulario = BusquedaUsuarisForm(request.GET)

    if formulario.is_valid():
        response = requests.get(
            'http://0.0.0.0:8080/api/v1/usuarios/busqueda_simple/',  # Cambia esta URL si es necesario por la de pythonanywhere, yo lo hago en loocal pero seria ls siguiente: https://israeljimenez.pythonanywhere.com/api/v1/usuarios/busqueda_simple/ 
            params={'textoBusqueda': formulario.cleaned_data.get("textoBusqueda")}
        )

        if response.status_code == 200:
            usuarios = response.json()  

            return render(request, 'Usuario/usuarios_busqueda_simple.html', {'usuarios_mostrar': usuarios})
        else:
            print("Error en la búsqueda:", response.status_code, response.text)

    return render(request, 'Usuario/usuarios_busqueda_simple.html', {'formulario': formulario})


def usuarios_busqueda_avanzada(request):
    formulario = BusquedaAvanzadaUsuarioForm(request.GET)

    if request.GET and formulario.is_valid():  
        response = requests.get(
            'http://0.0.0.0:8080/api/v1/usuarios/busqueda_avanzada/',  #cambiar ls url si es necesario por  https://israeljimenez.pythonanywhere.com/api/v1/usuarios/busqueda_avanzada/
            params=formulario.cleaned_data
        )

        if response.status_code == 200:
            usuarios = response.json()
            return render(request, 'Usuario/usuarios_busqueda_avanzada_resultado.html', {'usuarios_mostrar': usuarios})

    return render(request, 'Usuario/usuarios_busqueda_avanzada.html', {'formulario': formulario})
def categorias_busqueda_avanzada(request):
    formulario = BusquedaCategoriaForm(request.GET)

    if request.GET and formulario.is_valid():
        response = requests.get(
            'http://0.0.0.0:8080/api/v1/categorias/busqueda_avanzada/',  
            params=formulario.cleaned_data
        )

        if response.status_code == 200:
            categorias = response.json()
            return render(request, 'Categoria/categorias_busqueda_avanzada_resultado.html', {'categorias': categorias})

    return render(request, 'Categoria/categorias_busqueda_avanzada.html', {'formulario': formulario})


def propiedades_busqueda_avanzada(request):
    formulario = BusquedaPropiedadForm(request.GET)

    if request.GET and formulario.is_valid():
        response = requests.get(
            'http://0.0.0.0:8080/api/v1/propiedades/busqueda_avanzada/',  
            params=formulario.cleaned_data
        )

        if response.status_code == 200:
            propiedades = response.json()
            return render(request, 'Propiedad/propiedades_busqueda_avanzada_resultado.html', {'propiedades': propiedades})

    return render(request, 'Propiedad/propiedades_busqueda_avanzada.html', {'formulario': formulario})


def servicios_extra_busqueda_avanzada(request):
    formulario = BusquedaServicioExtraForm(request.GET)

    if request.GET and formulario.is_valid():
        response = requests.get(
            'http://0.0.0.0:8080/api/v1/servicios_extra/busqueda_avanzada/',  
            params=formulario.cleaned_data
        )

        if response.status_code == 200:
            servicios_extra = response.json()
            return render(request, 'Servicio_extra/servicios_extra_busqueda_avanzada_resultado.html', {'servicios_extra': servicios_extra})

    return render(request, 'Servicio_extra/servicios_extra_busqueda_avanzada.html', {'formulario': formulario})