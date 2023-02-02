from django.urls import path 

from AppEntrega import views

from django.contrib.auth.views import LogoutView

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.inicio, name='Inicio'),
    path('autoFormulario',views.autoFormulario, name="AutoFormulario"),
    path('clienteFormulario',views.clienteFormulario, name="ClienteFormulario"),
    path('serviceFormulario',views.serviceFormulario, name="ServiceFormulario"),
    path('busquedaAuto', views.busquedaAuto, name="BusquedaAuto"),
    path('buscarAuto',views.buscarAuto, name="BuscarAuto"),
    path('busquedaCliente', views.busquedaCliente, name="BusquedaCliente"),
    path('busquedaService', views.busquedaService, name="BusquedaService"),
    path('buscarService',views.buscarService, name="BuscarService"),
    path('leerServices',views.leerServices, name="LeerServices"),
    path('leerAutos',views.leerAutos, name="LeerAutos"),
    path('leerClientes',views.leerClientes, name="LeerClientes"),
    path('eliminarAuto/<patenteAuto>', views.eliminarAuto, name="EliminarAuto"),
    path('eliminarCliente/<dni>', views.eliminarCliente, name="EliminarCliente"),
    path('eliminarService/<comprobanteNro>', views.eliminarService, name="EliminarService"),
    path('editarAuto/<patente>', views.editarAuto, name="EditarAuto"),
    path('editarCliente/<dni>', views.editarCliente, name="EditarCliente"),
    path('editarService/<comprobante>', views.editarService, name="EditarService"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppEntrega/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('aboutMe', views.aboutMe, name="AboutMe"),
    path('home', views.home, name="Home"),
    path('pages', views.pages, name="Pages"),
    path('verMas/<id>', views.verMas, name="VerMas"),
    path('comentarioFormulario', views.comentarioFormulario, name="ComentarioFormulario")

]

