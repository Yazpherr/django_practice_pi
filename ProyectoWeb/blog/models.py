from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.nombre  # metodo string para que devuelva el nombre 
    

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)

    # debemos decir quien es el autor que crea un post, maneja la logica de la base de datos 
    # para que elimine todo los post en cascada que haya hecho ese autor 
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    
    categorias = models.ManyToManyField(Categoria)
            
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
    
    def __str__(self):
        return self.titulo 
        