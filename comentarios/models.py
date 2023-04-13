from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.usuario.first_name
