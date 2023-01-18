from django import forms

class AutoFormulario(forms.Form):
    
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    patente = forms.CharField(max_length=7)


class ClienteFormulario(forms.Form):

    nombre= forms.CharField(max_length=50)
    telefono= forms.CharField(max_length=11)


class ServiceFormulario(forms.Form):

    fecha = forms.DateField()
    cambioAceite = forms.BooleanField()
    cambioFiltros = forms.BooleanField()
    valor = forms.FloatField()



