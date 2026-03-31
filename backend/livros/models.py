from django.db import models

class Livro(models.Model):
    titulo  = models.CharField(max_length=200)
    autor   = models.CharField(max_length=100)
    ano     = models.IntegerField()
    genero  = models.CharField(max_length=50)
    nota = models.IntegerField(default=0)
    comentario = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.titulo