from django.db import models
class Usuarios(models.Model):
    identificacion = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=255,unique=True)
    apellido = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255,unique=True)
    clave = models.CharField(max_length=255,unique=True,label="Password")
    tipoUsuario = models.CharField(max_length=1,unique=True)

    def __str__(self):
        
        return f'Identificacion:{self.identificacion} Nombre: {self.nombre}, Apellido: {self.apellido},
        Correo: {self.correo}'