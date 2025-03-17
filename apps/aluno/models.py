from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    matricula = models.CharField(max_length=20, unique=True, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome