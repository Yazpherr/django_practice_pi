from django.shortcuts import render, redirect
from django.views.generic import View
# Ahora hacemos que despues de registrarte desde el login quede logeado automaticamente 
from django.contrib.auth import login, authenticate, logout
# importamos para libreria que gestiona los mensajes que se le da al usuario
from django.contrib import messages

# Importamos la clase para construir el formulario 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
class Vregistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", { "form" : form })
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        # El siguiente proceso se hara solo si el formulario es valido 
        if form.is_valid():
        
        # Ahora guardamos la informacion del usuario en la base de datos
            usuario = form.save()
            login(request, usuario)
            return redirect("Home")
        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", { "form" : form })

# Creammos una vista para cerra la session y redireccionar al home 
def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get( "username" )
            contra = form.cleaned_data.get( "password" )
            # usuario las validaciones para autenticar el usuario
            usuario = authenticate(username = nombre_usuario, password = contra)

            # Si se valida nos devuelve el usuario si no no devuelve nada
            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else: 
                messages.error(request, "Usuario o contraseña incorrectos")
        else: 
            messages.error(request, "Usuario o contraseña incorrectos")
    
    form = AuthenticationForm()
    return render(request, "login/login.html", { "form" : form })





# from django.shortcuts import render, redirect
# from django.views.generic import View
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm

# class Vregistro(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, "registro/registro.html", { "form" : form })
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)
        
#         # El siguiente proceso se hará solo si el formulario es válido 
#         if form.is_valid():
#             # Ahora guardamos la información del usuario en la base de datos
#             usuario = form.save()
#             login(request, usuario)  # Iniciar sesión automáticamente
#             return redirect('Home')  # Redirigir al home después de registrarse
#         else:
#             # Si el formulario no es válido, volvemos a renderizarlo con los errores
#             #return render(request, "registro/registro.html", { "form" : form })
#             pass