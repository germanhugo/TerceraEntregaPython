from django.db import models

# Create your models here.

class Automovil(models.Model):

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    patente = models.CharField(max_length=7)

    def __str__(self):
        return("El vehiculo patente "+self.patente+" es un "+self.marca+" "+self.modelo)



class Service(models.Model):

    fecha = models.DateField()
    cambioAceite = models.BooleanField()
    cambioFiltros = models.BooleanField()
    valor = models.FloatField()

    def __str__(self):
        return("Fecha: "+str(self.fecha)+", precio: "+str(self.valor))

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)

    def __str__(self):
        return("Cliente: "+self.nombre+", teléfono: "+self.telefono)


