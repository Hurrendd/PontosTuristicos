from rest_framework.serializers import ModelSerializer

from avaliacoes.models import Avaliacao


class AvalicaoSerializer(ModelSerializer):
    class Meta:
        db_table = 'Avalicao'
        managed = True
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliaçôes'
        model = Avaliacao
        fields = ('id', 'user', 'comentario', 'nota', 'data_criacao',)
