from rest_framework.serializers import ModelSerializer

from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        db_table = 'Endereco'
        managed = True
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        model = Endereco
        fields = ('id', 'linha1', 'linha2', 'cidade', 'estado',
                  'pais', 'latitude', 'longitude',)
