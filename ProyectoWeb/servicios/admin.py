from django.contrib import admin
from .models import Servicio # como estan en el mismo directorio .models 

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated") # esto para decirle a los campos que son en cuestion que son solo de lectura

admin.site.register(Servicio, ServicioAdmin)

