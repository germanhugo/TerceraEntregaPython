from django.urls import path 

from AppEntrega import views

urlpatterns = [
    
    path('', views.inicio, name='Inicio'),
    path('inicio', views.inicio, name='Inicio'),
    path('autoFormulario',views.autoFormulario, name="AutoFormulario"),
    path('clienteFormulario',views.clienteFormulario, name="ClienteFormulario"),
    path('serviceFormulario',views.serviceFormulario, name="ServiceFormulario"),
    path('busquedaAuto', views.busquedaAuto, name="BusquedaAuto"),
    path('buscarAuto',views.buscarAuto, name="BuscarAuto"),
    path('busquedaCliente', views.busquedaCliente, name="BusquedaCliente"),
    path('buscarCliente',views.buscarCliente, name="BuscarCliente"),
    path('busquedaService', views.busquedaService, name="BusquedaService"),
    path('buscarService',views.buscarService, name="BuscarService"),
]