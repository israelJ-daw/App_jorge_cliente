import requests
from django.core import serializers
from django.shortcuts import render


def index(request):
    return render(request, "index.html")



def usuarios_lista_api(request):
    response = requests.get('https://IsraelJimenez.pythonanywhere.com/api/v1/usuarios')
    usuarios = response.json()
    return render(request, 'Usuario/lista_api.html', {"usuarios": usuarios})