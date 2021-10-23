from django.db import models

from django.db import models


class usuario(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, verbose_name = 'Nombre')
    numParticipantes = models.IntegerField(null = False, blank = False) 
    idTarea = models.IntegerField(null = False, blank = False) 
    Tipo = models.TextField(null = False, blank = False)


def __str__(self):
    return self.nombre

class Meta:
    ordering = ['nombre']
    verbose_name = ['Usuario']
    verbose_name_plural = ['Usuarios']
