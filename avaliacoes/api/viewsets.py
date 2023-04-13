from rest_framework.viewsets import ModelViewSet

from avaliacoes.api.serializers import AvalicaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewset(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer
