from django.contrib import admin

from comentarios.models import Comentario


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'data_criacao', 'aprovado')
