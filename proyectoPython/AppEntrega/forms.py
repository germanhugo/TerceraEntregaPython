from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AutoFormulario(forms.Form):
    
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    patente = forms.CharField(max_length=7)


class ClienteFormulario(forms.Form):

    dni = forms.CharField(max_length=8)
    nombre = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=11)


class ServiceFormulario(forms.Form):

    comprobante = forms.CharField()
    fecha = forms.DateField()
    cambioAceite = forms.BooleanField(required= False)
    cambioFiltros = forms.BooleanField(required= False)
    valor = forms.FloatField()


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']# Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
    


class ComentarioFormulario(forms.Form):

    valoracion = forms.CharField(max_length=15)
    comentario = forms.CharField(max_length=500)
    nombre = forms.CharField(max_length=100)




    