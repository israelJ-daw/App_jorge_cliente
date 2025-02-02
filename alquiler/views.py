import requests
from django.core import serializers
from django.shortcuts import render


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
    