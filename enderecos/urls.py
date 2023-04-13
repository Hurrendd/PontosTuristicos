from django.urls import include, path
from rest_framework import routers

from enderecos.api.viewsets import EnderecoViewset

router = routers.DefaultRouter()
router.register('enderecos', EnderecoViewset)

urlpatterns = [
    path('', include(router.urls))
]
