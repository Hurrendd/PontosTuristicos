from django.urls import include, path
from rest_framework import routers

from atracoes.api.viewsets import AtracoesViewSet

router = routers.DefaultRouter()
router.register(r'atracoes', AtracoesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
