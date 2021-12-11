from django.db import models


class TipoLabores(models.Model):
    codigo = models.CharField(max_length=1,unique=True)
    descripcion= models.CharField(max_length=255)

    def __str__(self):
        return f'{self.codigo_dane} : {self.nombre_ciudad}'