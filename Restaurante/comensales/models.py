from django.db import models


class Comensal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
