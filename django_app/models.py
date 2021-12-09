from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'
    
    def __str__(self):
        return self.titulo