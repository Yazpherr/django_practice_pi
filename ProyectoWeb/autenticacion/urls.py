from django.urls import path

from .views import Vregistro, cerrar_sesion, login, logear

urlpatterns = [
    path('', Vregistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion,  name="cerrar_sesion"),
    path('logear', logear,  name="logear"),
]

