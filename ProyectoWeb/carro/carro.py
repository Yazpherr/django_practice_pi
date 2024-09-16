class Carro: 
    def __init__(self, request):
        self.request = request 
        self.session = request.session
        
        self.carro = self.session.get('carro', {})

        # construimos un carro de compra para la sesion 
        # carro = self.session.get('carro')
        # Si no tenemos carro entonces lo creamos
        # if not carro: 
        #     carro = self.session["carro"]={}
        # # si el usuario se va de la pagina y despues vuelve 
        
        # # else: 
        # self.carro = carro
            
    # Ahora creamos una funcion para agregar productos
    def agregar(self, producto):
        # si no encuentras los productos en el carro entonces los agregamos
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url
            }
        
        # Ahora le debemos indicar que hacer en caso de que el producto ya se encuentre en el carro 
        else: 
            # recorremos todas las clave:valor de nuestro carro 
            for key, value in self.carro.items():
                if key==str(producto.id):
                    # si el producto ya se encuentra en el carro entonces aumentamos la cantidad
                    value['cantidad'] = value['cantidad'] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        
        # Llamaremos a una funcion la cual se encarga de actualizar la session 
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"] = self.carro
        # se modifica la session despues de agregar y restar etc 
        self.session.modified = True
    
    # Funcion para eliminar productos de nuestro carro 
    def eliminar(self, producto):
        # almacenamos el id del producto para poder manejarlo 
        producto.id = str(producto.id)
        if producto.id in self.carro: 
            del self.carro[producto.id]
            self.guardar_carro()
    
    # Funcion para restar productos de nuestro carro 
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                # si el producto ya se encuentra en el carro entonces aumentamos la cantidad
                value['cantidad'] = value['cantidad'] - 1
                value["precio"] = float(value["precio"]) - producto.precio

                if value["cantidad"]<1:
                    self.eliminar(producto)
                    
                break
        self.guardar_carro()
    
    def limpiar_carro(self):
    # Cuando se inicia el carro construye un diccionario vacio
        self.session["carro"] = {}
        self.session.modified = True
        
        

                    
        