from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        db_table = 'Atracao'
        managed = True
        verbose_name = 'Atracao'
        verbose_name_plural = 'Atracoes'
        model = Atracao
        fields = ('id', 'nome', 'descricao',
                  'horario_func', 'idade_minima', 'foto',)
