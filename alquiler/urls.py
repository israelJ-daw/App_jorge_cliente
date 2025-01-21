from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    #cliente
 
    path('usuarios_lista_api/', views.usuarios_lista_api, name='usuarios_lista_api'),
    
]