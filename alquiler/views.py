import requests
from django.core import serializers
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def usuarios_lista_api(request):
    # Obtenemos todos los usuarios
    response = requests.get('http://0.0.0.0:8080/api/v1/usuarios')
    # Trasformamos la respuesta en JSON
    usuarios= response.json()
    return render(request, 'Usuario/lista_api.html', {"usuarios":usuarios})