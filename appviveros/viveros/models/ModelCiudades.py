from django.db import models


class Ciudades(models.Model):
    codigo_dane = models.CharField(max_length=6,unique=True)
    nombre_ciudad = models.CharField(max_length=255)

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return f'{self.codigo_dane} : {self.nombre_ciudad}'