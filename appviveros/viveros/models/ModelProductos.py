from django.db import models

class Productos(models.Model):
    sica = models.CharField(max_length=6,unique=True)
    nombre = models.CharField(max_length=255)
    frecuenciaAplicacion = models.CharField(max_length=255)

    def __str__(self):
        
        return f'Codigo SICA:{self.cod_Identidad} Nombre: {self.nombre}, Frecuencia de aplicacion: {self.frecuenciaAplicacion}'