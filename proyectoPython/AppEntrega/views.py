from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import Cliente, Automovil, Service
from AppEntrega.forms import AutoFormulario, ClienteFormulario, ServiceFormulario


# Create your views here.

def inicio(request):
    
    return render(request, "AppEntrega/inicio.html")


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


def clienteFormulario(request):
      
    if request.method == "POST":
       
        miFormulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nombre=informacion["nombre"], telefono=informacion["telefono"]) #constructor de la clase cliente
            cliente.save()  #guarda la instancia de cliente en la base
            return render(request, "AppEntrega/inicio.html")
    else:
        miFormulario = ClienteFormulario()
      
    return render(request, "AppEntrega/clienteFormulario.html", {"miFormulario": miFormulario})



def serviceFormulario(request):
      
    if request.method == "POST":
       
        miFormulario = ServiceFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            service = Service(fecha=informacion["fecha"], cambioAceite=informacion["cambioAceite"], cambioFiltros=informacion["cambioFiltros"], valor=informacion["valor"])
            service.save()  #guarda la instancia de service en la base
            return render(request, "AppEntrega/inicio.html")
    else:
        miFormulario = ServiceFormulario()
      
    return render(request, "AppEntrega/serviceFormulario.html", {"miFormulario": miFormulario})


def busquedaAuto(request):

      return render(request,"AppEntrega/busquedaAuto.html")

def buscarAuto(request):
      
      if request.GET["patente"]:
            patente = request.GET['patente']
            autos = Automovil.objects.filter(patente__icontains=patente)
            
            return render(request, "AppEntrega/resultadosBusquedaAuto.html",{"autos":autos, "patente": patente})
      else:
            return render(request, "AppEntrega/paginaError.html",{"mensaje":"No se enviaron datos para la búsqueda"})

            
def busquedaCliente(request):

      return render(request,"AppEntrega/busquedaCliente.html")

def buscarCliente(request):
      
      if request.GET["nombre"]:
            nombre = request.GET['nombre']
            clientes = Cliente.objects.filter(nombre__icontains=nombre)
            
            return render(request, "AppEntrega/resultadosBusquedaCliente.html",{"clientes": clientes, "nombre": nombre})
      else:
            return render(request, "AppEntrega/paginaError.html",{"mensaje":"No se enviaron datos para la búsqueda"})


def busquedaService(request):

      return render(request,"AppEntrega/busquedaService.html")


def buscarService(request):
      
      if request.GET["fecha"]:
            fecha = request.GET['fecha']
            services = Service.objects.filter(fecha__icontains=fecha)
            
            return render(request, "AppEntrega/resultadoBusquedaService.html",{"services": services, "fecha": fecha})
      else:
            return render(request, "AppEntrega/paginaError.html",{"mensaje":"No se enviaron datos para la búsqueda"})
            