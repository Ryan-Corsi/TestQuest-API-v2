from django.contrib import admin
from .models import *

class detProcessos(admin.ModelAdmin):
    list_display = ('id','titulo', 'descricao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 10

class detPessoas(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'idProcessoFK', 'provaFK', 'respostas', 'genero', 'etnia', 'pcd')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

class detProvas(admin.ModelAdmin):
    list_display = ('id', 'idProcessoFK', 'qtdQuestoes', 'qtdAlternativas', 'gabaritoPadrao', 'dtProva')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10



admin.site.register(Processo, detProcessos)
admin.site.register(Pessoa, detPessoas)
admin.site.register(Prova, detProvas)
