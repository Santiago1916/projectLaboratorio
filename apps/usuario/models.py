from django.db import models


class usuario(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, verbose_name = 'Nombre')
    apellido = models.CharField(max_length = 100, blank = False, verbose_name = 'Apellido') 
    correo = models.EmailField(unique = True, max_length = 100, verbose_name = 'Correo')
    dni = models.IntegerField(null = True, blank = True)
    telefono = models.IntegerField(null = True, blank = True)

def __str__(self):
    return self.nombre

class Meta:
    ordering = ['nombre']
    verbose_name = ['Usuario']
    verbose_name_plural = ['Usuarios']


