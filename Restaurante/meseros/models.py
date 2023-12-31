from django.db import models

class Mesero(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8, default='00000000')

    def __str__(self):
        return self.nombre
