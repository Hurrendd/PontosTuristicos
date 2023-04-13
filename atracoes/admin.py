from django.contrib import admin

from atracoes.models import Atracao


@admin.register(Atracao)
class Atracao(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'horario_func', 'idade_minima',)
