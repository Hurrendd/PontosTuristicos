from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        db_table = 'PontoTuristico'
        managed = True
        verbose_name = 'Ponto Turistico'
        verbose_name_plural = 'Pontos Turistico'
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado',
                  'foto', 'endereco', 'atracoes', 'comentarios')
