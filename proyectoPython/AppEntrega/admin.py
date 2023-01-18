from django.contrib import admin

from .models import * #importamos el archivo models

# Register your models here.
# #registramos los modelos
 
admin.site.register(Automovil)

admin.site.register(Cliente)

admin.site.register(Service)

