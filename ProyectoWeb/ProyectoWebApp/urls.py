from django.urls import path

from ProyectoWebApp import views
from django.conf import settings #importamos para que se vean las imagene s
from django.conf.urls.static import static # importamos para que se vean las imagenes


urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)