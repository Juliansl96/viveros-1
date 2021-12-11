from django.db import models

class Productor(models.Model):
    cod = models.AutoField(unique=True)
    identidad = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    def __str__(self):
        
        return f'Identificacion:{self.identidad} Nombre: {self.nombre}, Apellido: {self.apellido}'