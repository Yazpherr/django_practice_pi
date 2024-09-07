from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') #mod que hace que cuando suba la imagen se guarde en la carpeta media 
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo
    