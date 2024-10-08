from django.shortcuts import render, redirect 
from django.contrib.auth.decorators  import login_required
from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags 
from django.core.mail import send_mail
# Create your views here.


@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user = request.user)
    carro = Carro(request)
    linea_pedido = list()
    
    for key, value in carro.carro.items():
        linea_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user, 
            pedido = pedido
        ))
    LineaPedido.objects.bulk_create(linea_pedido)
    
    enviar_mail(pedido = pedido,
                lineas_pedido = linea_pedido,
                nombreusuario = request.user.username,
                email = request.user.email)
    
    messages.success(request, "El pedido se ha procesado correctamente")
    
    return redirect("../tienda")


def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedidos.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
    })
    
    mensaje_texto = strip_tags(mensaje)
    from_email = "7b6e25002@smtp-brevo.com"
    # to = kwargs.get("emailusuario")
    to = "felipe.coliman.c@gmail.com"    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)