from django.contrib import admin

from core.models import PontoTuristico


@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'aprovado', )
