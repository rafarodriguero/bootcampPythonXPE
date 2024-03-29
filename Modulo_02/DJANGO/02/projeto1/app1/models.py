from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.IntegerField('telefone')
    email = models.CharField('email', max_length=30)

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


