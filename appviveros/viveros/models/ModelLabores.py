from django.db import models
from viveros.models.ModelTipoLabores import TipoLabores

class Labor(models.Model):
    codigo = models.CharField(max_length=6,unique=True)
    fecha = models.DateField()
    descripcion = models.TextField(max_length=500)
    tipoLabor = models.ForeignKey(TipoLabores, null=True)

    def __str__(self):
        
        return f'Codigo:{self.codigo} Fecha: {self.fecha}, Descripcion: {self.descripcion}, Tipo Labor: {self.descripcion.__str__()}'