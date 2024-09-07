from django.contrib import admin
from .models import Categoria, Post 


# Register your models here.
# ahora hacemos que se puede que se pueda manipular desde la interfaz de adminisitrador 
# Empezamos a contruir nuestro panel de admin 

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
