from django.urls import include, path
from rest_framework import routers

from comentarios.api.viewsets import ComentaioViewset

rota = routers.DefaultRouter()
rota.register(r'comentarios', ComentaioViewset)

urlpatterns = [
    path('', include(rota.urls)),
]
