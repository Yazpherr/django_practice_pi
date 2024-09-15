from django.contrib import admin
from .models import CategoriaProd, Producto

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


#     list_display = ('nombre')
#     search_fields = ('nombre')

# class Productos(admin.ModelAdmin):
#     list_display = ("nombre",
#                     "categoria",
#                     "imagen",
#                     "precio",
#                     "disponibilidad",
#                     )
#     list_filter = ('categoria',)
#     date_hierarchy = ('fecha')
    
admin.site.register(CategoriaProd,CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
