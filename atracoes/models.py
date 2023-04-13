from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150, blank=False)
    descricao = models.TextField(blank=False)
    horario_func = models.TextField()
    idade_minima = models.IntegerField(blank=False)
    foto = models.ImageField(
        upload_to='atracoes', null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
