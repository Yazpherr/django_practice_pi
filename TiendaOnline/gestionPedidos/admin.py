from django.contrib import admin
from gestionPedidos.models import Clientes, Articulo, Pedido

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion', 'tfno')
    search_fields = ('nombre','tfno')

class ArticuloAdmin(admin.ModelAdmin):
    list_filter = ("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ('fecha',)
    date_hierarchy = ('fecha')
    
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidosAdmin)