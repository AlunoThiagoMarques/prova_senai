from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Autor, EixoTecnologia, Artigo

def index(request):
    autores = Autor.objects.all()
    eixos = EixoTecnologia.objects.all()
    ha_sete_dias = timezone.now() - timedelta(days=7)
    artigo_ultimos_7_dias = Artigo.objects.filter(data_publicacao__gte=ha_sete_dias).order_by('-data_publicacao')
    todos_artigos = Artigo.objects.all().order_by('-data_publicacao')
    
    context = {
        "autores": autores, 
        "eixos": eixos, 
        "artigo_ultimos_7_dias": artigo_ultimos_7_dias,
        "artigos": todos_artigos
    }
    return render(request, 'motorartigos/index.html', context)


def artigo(request, artigo_id):  
    artigo_obj = get_object_or_404(Artigo, id=artigo_id)
    
    recomendados = Artigo.objects.filter(
        id_fk_eixo=artigo_obj.id_fk_eixo
    ).exclude(id=artigo_obj.id).order_by('-data_publicacao')[:3]
    
    context = {
        'artigo': artigo_obj,
        'recomendados': recomendados
    }
    return render(request, 'motorartigos/artigo.html', context)