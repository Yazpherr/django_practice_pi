# def importe_total_carro(request):
#     total = 0
#     # yo quiero que en estar varible global vallan sumandose los precios de los artiuculos que yo valla agregando al carro
    
#     # Primero miramos si el usuario esta autenticado
#     if request.user.is_authenticated:
#         # Si esta autenticado, entonces obtenemos el carro de compras del usuario
#         for key, value in request.session["carro"].items():
#             total = total + (float(value["precio"])*value["cantidad"])
#     return {"importe_total_carro": total}

def importe_total_carro(request):
    total = 1
    
    # Verificamos si el usuario está autenticado
    if request.user.is_authenticated:
        # Verificamos si el carrito ya está en la sesión
        carro = request.session.get('carro', {})
        # Si el carro existe, sumamos los precios de los artículos en el carro
        for key, value in carro.items():
            total += float(value['precio']) * value['cantidad']
    
    return {"importe_total_carro": total}
