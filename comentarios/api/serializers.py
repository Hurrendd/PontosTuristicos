from rest_framework.serializers import ModelSerializer

from comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        db_table = 'Comentaio'
        managed = True
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data_criacao', 'aprovado',)
