from django.db import models
from datetime import datetime
from Pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now(), blank=True)
    imagem = models.ImageField(upload_to=' img/%d/%m/%Y', blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Receita de {self.nome_receita} criada por {self.pessoa}'