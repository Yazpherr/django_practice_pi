from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulo 
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        producto = request.GET["prd"]
        if len(producto)>20: 
            mensaje = "texto de busqueda demasiado largo"
        else:
            # mensaje = "Articulo Buscado: %r" % request.GET["prd"]
            articulos = Articulo.objects.filter(nombre__icontains = producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})
        
    else: 
        mensaje = "no has introducido nada"
    return HttpResponse(mensaje)


# def contacto(request):
#     if request.method == "POST":
#         subject = request.POST["asunto"]
#         message = request.POST["mensaje"] + " " + request.POST["email"]
#         email_from = settings.EMAIL_HOST_USER
        
#         recipient_list = ["felipe.coliman.c@gmail.com"]
        
#         send_mail(subject, message, email_from,  recipient_list)
        
#         return render(request, "gracias.html")
#     return render(request, "contacto.html")

def contacto(request):
    if request.method == "POST": # Si el usuario a pinchado el boton de enviar
        miFormulario = FormularioContacto(request.POST)
        
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data # Obtengo los datos del diccionario 
            
            send_mail(infForm['asunto'],infForm['mensaje'],
                      infForm.get('email', '7b6e25002@smtp-brevo.com'),['felipe.coliman.c@gmail.com'],)        

            return render(request, "gracias.html")
    
    else: 
        miFormulario=FormularioContacto()
            
        # Ahora debemos decirle que construya un documento HTML  que contenga los info que hay dentro
    return render(request, "formulario_contacto.html", {"form": miFormulario})