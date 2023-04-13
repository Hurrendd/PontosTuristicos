from django.urls import include, path
from rest_framework import routers

from avaliacoes.api.viewsets import AvaliacaoViewset

rotas = routers.DefaultRouter()
rotas.register(r'avaliacoes', AvaliacaoViewset)

urlpatterns = [
    path('', include(rotas.urls)),
]
