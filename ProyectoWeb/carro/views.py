from django.shortcuts import render, redirect

from .carro import Carro
from tienda.models import Producto

# Create your views here.

# Creamos la vista para agregar productos al carro 
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)

    # redireccinamos a la tienda
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto = producto)

    # redireccinamos a la tienda
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto = producto)

    # redireccinamos a la tienda
    return redirect("tienda")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    # redireccinamos a la tienda
    return redirect("tienda")

