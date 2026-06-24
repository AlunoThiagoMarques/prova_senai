from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Autor, EixoTecnologia, Artigo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome',)


@admin.register(EixoTecnologia)
class EixoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_fk_autor',
        'id_fk_eixo',
        'data_publicacao'
    )

    list_filter = (
        'id_fk_eixo',
        'data_publicacao'
    )

    search_fields = (
        'id_fk_autor__nome',
    )

    ordering = ('-data_publicacao',)