from django.contrib import admin

from avaliacoes.models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'comentario', 'nota', 'data_criacao',)
