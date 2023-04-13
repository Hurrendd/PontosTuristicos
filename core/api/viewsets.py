from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao',]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        nome = self.request.query_params.get('nome')
        qs = PontoTuristico.objects.filter(aprovado=True)

        if id:
            qs = qs.filter(pk=id)

        if nome:
            qs = qs.filter(nome__icontains=nome)

        return qs

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()[0].id
        print(f'Teste {qs}')

        print(request.data)
        # super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
        if qs:
            return super().list(request, *args, **kwargs)
        else:
            return Response({'Hello': 'Lista Vazia'})

    def create(self, request, *args, **kwargs):
        # super().create(request, *args, **kwargs)
        # return Response({'Hello': request.data['nome']})
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # Criando uma action personalizada
    @ action(methods=['get',], detail=True)
    def denunciar(self, request, pk=None):
        pass
