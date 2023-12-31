from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    procedencia = models.CharField(max_length=100, default='Peruano')

    def __str__(self):
        return self.nombre
