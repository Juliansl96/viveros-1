from django.contrib import admin
from viveros.models.ModelCiudades import Ciudades

@admin.register(Ciudades)
class Ciudadesadmin(admin.ModelAdmin):
    list_display = ('id' ,'codigo_dane', 'nombre_ciudad')
    search_fields = ('codigo_dane', 'nombre_ciudad')
    list_editable = ('nombre_ciudad',)
    list_filter = ('codigo_dane','nombre_ciudad')
    ordering = ('id',)