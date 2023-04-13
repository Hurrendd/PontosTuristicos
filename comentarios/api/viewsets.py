from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario


class ComentaioViewset(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
