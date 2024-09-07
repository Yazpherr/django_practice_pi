from django.urls import path
from . import views


from django.conf import settings #importamos para que se vean las imagene s
from django.conf.urls.static import static # importamos para que se vean las imagenes


urlpatterns = [
    path('', views.blog, name="Blog"),
    # ahora vamos a filtrar por categoria 
    path('categoria/<int:categoria_id>/', views.categoria, name = 'categoria')
]

