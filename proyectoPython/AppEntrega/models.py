from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Automovil(models.Model):

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    patente = models.CharField(max_length=7)

    def __str__(self):
        return("El vehiculo patente "+self.patente+" es un "+self.marca+" "+self.modelo)



class Service(models.Model):

    comprobante = models.IntegerField()
    fecha = models.DateField()
    cambioAceite = models.BooleanField()
    cambioFiltros = models.BooleanField()
    valor = models.FloatField()
    factura = models.ImageField(upload_to='factura', null=True, blank=True)

    def __str__(self):
        return("Comprobante: "+str(self.comprobante)+", fecha: "+str(self.fecha)+", precio: "+str(self.valor))

class Cliente(models.Model):

    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)

    def __str__(self):
        return("Cliente: "+self.dni+" - "+self.nombre+", teléfono: "+self.telefono)


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

    




class Comentarios(models.Model):

    fecha = models.DateField()
    titulo = models.CharField(max_length=15)
    comentario = models.CharField(max_length=500)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fecha} - {self.titulo} - {self.comentario} - {self.autor}"