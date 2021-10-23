from django.db import models

from django.db import models


class usuario(models.Model):
    idTrabajo = models.IntegerField(null = False, blank = False)
    nombre = models.CharField(max_length = 100, blank = False, verbose_name = 'nombre') 
    descripcion = models.TextField(null = False, blank = False)


def __str__(self):
    return self.idTrabajo

class Meta:
    ordering = ['nombre']
    verbose_name = ['trabajo']
    verbose_name_plural = ['Trabajos']

