from django.contrib import admin
from viveros.models.ModelViveros import Viveros

@admin.register(Viveros)
class ViverosAdmin(admin.ModelAdmin): 
    list_display = ('nombre','ciudad','numero','codigo')
    search_fields = ('nombre',)
