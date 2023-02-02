import datetime
from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import Cliente, Automovil, Service, Avatar, Comentarios
from AppEntrega.forms import AutoFormulario, ClienteFormulario, ServiceFormulario, UserRegisterForm, UserEditForm, ComentarioFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def inicio(request):
    
    return render(request, "AppEntrega/inicio.html")




# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppEntrega/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppEntrega/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})




@login_required
def autoFormulario(request):
      
    if request.method == "POST":
       
        miFormulario = AutoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            auto = Automovil(marca=informacion["marca"], modelo=informacion["modelo"], patente=informacion["patente"]) #constructor de la clase automovi
            auto.save()  #guarda la instancia de auto en la base
            return render(request, "AppEntrega/inicio.html")
    else:
        miFormulario = AutoFormulario()
      
    return render(request, "AppEntrega/autoFormulario.html", {"miFormulario": miFormulario})

@login_required
def clienteFormulario(request):
      
    if request.method == "POST":
       
        miFormulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(dni=informacion["dni"], nombre=informacion["nombre"], telefono=informacion["telefono"]) #constructor de la clase cliente
            cliente.save()  #guarda la instancia de cliente en la base
            return render(request, "AppEntrega/inicio.html")
    else:
        miFormulario = ClienteFormulario()
      
    return render(request, "AppEntrega/clienteFormulario.html", {"miFormulario": miFormulario})


@login_required
def serviceFormulario(request):
      
    if request.method == "POST":
       
        miFormulario = ServiceFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            service = Service(comprobante=informacion["comprobante"],fecha=informacion["fecha"], cambioAceite=informacion["cambioAceite"], cambioFiltros=informacion["cambioFiltros"], valor=informacion["valor"])
            service.save()  #guarda la instancia de service en la base
            return render(request, "AppEntrega/inicio.html")
    else:
        miFormulario = ServiceFormulario()
      
    return render(request, "AppEntrega/serviceFormulario.html", {"miFormulario": miFormulario})



@login_required
def busquedaAuto(request):

      return render(request,"AppEntrega/busquedaAuto.html")


@login_required
def buscarAuto(request):
      
      if request.GET["patente"]:
            patente = request.GET['patente']
            autos = Automovil.objects.filter(patente__icontains=patente)
            
            return render(request, "AppEntrega/resultadosBusquedaAuto.html",{"autos":autos, "patente": patente})
      else:
            return render(request, "AppEntrega/paginaError.html",{"mensaje":"No se enviaron datos para la búsqueda"})



@login_required
def busquedaCliente(request):

      return render(request,"AppEntrega/busquedaCliente.html")



@login_required
def buscarCliente(request):
      
      if request.GET["nombre"]:
            nombre = request.GET['nombre']
            clientes = Cliente.objects.filter(nombre__icontains=nombre)
            
            return render(request, "AppEntrega/resultadosBusquedaCliente.html",{"Clientes": clientes, "nombre": nombre})
      else:
            return render(request, "AppEntrega/paginaError.html",{"mensaje":"No se enviaron datos para la búsqueda"})


@login_required
def busquedaService(request):

      return render(request,"AppEntrega/busquedaService.html")

@login_required
def buscarService(request):
      
      if request.GET["fecha"]:
            fecha = request.GET['fecha']
            services = Service.objects.filter(fecha__icontains=fecha)
            
            return render(request, "AppEntrega/resultadoBusquedaService.html",{"services": services, "fecha": fecha})
      else:
            return render(request, "AppEntrega/paginaError.html",{"mensaje":"No se enviaron datos para la búsqueda"})
            

@login_required
def leerAutos(request):
    
    autos = Automovil.objects.all() #trae todos los autos
    contexto= {"autos": autos}
    return render(request, "AppEntrega/leerAutos.html",contexto)

@login_required
def leerClientes(request):

    clientes = Cliente.objects.all() #trae todos los clientes
    contexto= {"clientes": clientes}
    return render(request, "AppEntrega/leerClientes.html",contexto)

@login_required
def leerServices(request):

    services = Service.objects.all() #trae todos los autos
    contexto= {"services": services}
    return render(request, "AppEntrega/leerServices.html",contexto)


@login_required
def eliminarAuto(request, patenteAuto):
    
    auto = Automovil.objects.get(patente = patenteAuto)
    auto.delete()   # elimina el objeto auto
    autos = Automovil.objects.all() # trae todos los autos 
    contexto = {"autos": autos}
    return render(request, "AppEntrega/leerAutos.html", contexto)

@login_required
def eliminarCliente(request, dni):

    cliente = Cliente.objects.get(dni = dni) #trae todos los clientes
    cliente.delete()
    clientes = Cliente.objects.all()
    contexto= {"clientes": clientes}
    return render(request, "AppEntrega/leerClientes.html",contexto)

@login_required
def eliminarService(request, comprobanteNro):

    service = Service.objects.get(comprobante = comprobanteNro)
    service.delete()
    services = Service.objects.all() #trae todos los services
    contexto= {"services": services}
    return render(request, "AppEntrega/leerServices.html",contexto)

@login_required
def editarAuto(request, patente):

    auto = Automovil.objects.get(patente = patente)
    
    if request.method == 'POST':
        miFormulario = AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid: 
            informacion = miFormulario.cleaned_data
            auto.patente = informacion['patente']
            auto.marca = informacion['marca']
            auto.modelo = informacion['modelo']
            auto.save()

        return render(request, "AppEntrega/leerAutos.html")
    
    else:
    
        miFormulario = AutoFormulario(initial={'patente': auto.patente, 'marca': auto.marca, 'modelo': auto.modelo})

    # Voy al html que me permite editar
    return render(request, "AppEntrega/editarAuto.html", {"miFormulario": miFormulario, "patente": patente})

@login_required
def editarCliente(request, dni):

    cliente = Cliente.objects.get(dni = dni)
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente.dni = informacion['dni']
            cliente.nombre = informacion['nombre']
            cliente.telefono = informacion['telefono']
            cliente.save()
        return render(request, "AppEntrega/leerClientes.html")
    
    else:
        miFormulario = ClienteFormulario(initial={'dni': cliente.dni, 'nombre': cliente.nombre, 'telefono': cliente.telefono})

    return render(request,"AppEntrega/editarCliente.html",{"miFormulario":miFormulario,"dni":dni})



@login_required
def editarService(request, comprobante):

    service = Service.objects.get(comprobante = comprobante)
    
    if request.method == 'POST':
        miFormulario = ServiceFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid: 
            informacion = miFormulario.cleaned_data
            service.comprobante = informacion['comprobante']
            service.fecha = informacion['fecha']
            service.cambioAceite = informacion['cambioAceite']
            service.cambioFiltros = informacion['cambioFiltros']
            service.valor = informacion['valor']
            service.save()

        return render(request, "AppEntrega/leerServices.html")
    
    else:
    
        miFormulario = ServiceFormulario(initial={'comprobante': service.comprobante, 'fecha': service.fecha,
                                                   'cambioAceite': service.cambioAceite, 'cambioFiltros': service.cambioFiltros,
                                                   'valor': service.valor})

    # Voy al html que me permite editar
    return render(request, "AppEntrega/editarService.html", {"miFormulario": miFormulario, "comprobante": comprobante})


def login_request(request):
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                avatar = Avatar.objects.filter(user=user)[0].imagen.url
                
                login(request, user)
                return render(request, "AppEntrega/inicio.html", {"mensaje":f"Bienvenido {usuario}","avatar":avatar})
            else:
                return render(request, "AppEntrega/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppEntrega/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AppEntrega/login.html", {"form": form})


def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppEntrega/inicio.html" , {"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
    return render(request,"AppEntrega/registro.html" , {"form":form})


def aboutMe(request):

    return render(request,"AppEntrega/aboutMe.html")



@login_required
def pages(request):
    
    comentarios = Comentarios.objects.all()
    contexto= {"comentarios": comentarios}
    return render(request, "AppEntrega/pages.html",contexto)



def comentarioFormulario(request):
      
    if request.method == "POST":
       
        miFormulario = ComentarioFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            comentario = Comentarios(fecha=datetime.date.today(), titulo=informacion["valoracion"], comentario=informacion["comentario"], autor=informacion["nombre"])
            comentario.save()  
            return render(request, "AppEntrega/inicio.html")
    else:
        miFormulario = ComentarioFormulario()
      
    return render(request, "AppEntrega/comentarioFormulario.html", {"miFormulario": miFormulario})




@login_required
def verMas(request, id):

    comentario = Comentarios.objects.get(id = id) 
    contexto = {"comentario" : comentario}
    
    return render(request, "AppEntrega/leerComentario.html", contexto)
    

def home(request):

    return render(request, "AppEntrega/home.html")


def aboutMe(request):

    return render(request, "AppEntrega/aboutMe.html")