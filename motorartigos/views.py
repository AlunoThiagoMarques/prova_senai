from django.shortcuts import render
from .models import Autor
# Create your views here.

def index(request):

    autores = Autor.objects.all()
    return render(request, 'motorartigos/index.html', {"autores" : autores})


def artigo(request):
    return render(request, 'motorartigos/artigo.html')