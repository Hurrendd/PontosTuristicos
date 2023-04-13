from rest_framework.viewsets import ModelViewSet

from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecoViewset(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
