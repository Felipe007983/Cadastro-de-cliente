from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro


def home(request):
    Data = {}
    return render(request, 'PaginaInicial/Home.html', Data)

def inicio(request):
    return render(request, 'PaginaInicial/inicio.html')
