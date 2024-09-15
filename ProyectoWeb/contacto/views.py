from django.shortcuts import render, redirect 

from.forms import FormularioContacto

from django.core.mail import EmailMessage


# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto() # Creamos una instancia de la clase creada anteriormente 
    

    
    if request.method == 'POST':
        # Si se ha hecho POST (se le ha dado el boton de enviar) rescata la info del formulario
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            # Una vez capturados los datos procedemos a enviarlos 
            email = EmailMessage("Mensaje desde APP django",
                                 "El usuario con el nombre {} con la direccion de correo {} te escribe lo siguiente:\n\n {}".format(nombre , email, contenido),
                                 "", ["7b6e25002@smtp-brevo.com"], 
                                 reply_to = [email])
           
            # Creamos instancias de prueba para que el usuario tenga conocimiento si el envio se ha hecho correctamente
            try:
                email.send()
                return redirect("/contacto/?valido")      
            except: 
                return redirect('/contacto/?novalido')
            
            
    return render(request, "contacto/contacto.html", { "miFormulario" : FormularioContacto })
