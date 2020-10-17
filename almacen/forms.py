from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from .models import Producto, Inventario, Imagen

class BuscarCodigoForm(forms.Form):
    codigo = forms.CharField(max_length=140, required=True, help_text="Ingrese Codigo de barra de producto")
    
    def __init__(self,*args, **kwargs):
        super(BuscarCodigoForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })

    class Meta:
        model=Inventario
        fields=("__all__")    

class EntradaCantidadForm(forms.Form):
    cantidad = forms.IntegerField(required=True, help_text="Ingrese Cantidad de producto")
    
    def __init__(self,*args, **kwargs):
        super(EntradaCantidadForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })

    class Meta:
        model=Inventario
        fields=("__all__")    


class BuscarProductForm(forms.Form):
    producto = forms.CharField(max_length=140, required=True, help_text="Ingrese producto a buscar")
    
    def __init__(self,*args, **kwargs):
        super(BuscarProductForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })

    class Meta:
        model=Producto
        fields=("__all__")    


class ProductoForm(forms.Form):
    producto = forms.CharField(max_length=140, required=True, help_text="nombre del producto")
    descripcion=forms.CharField(required=False,help_text="Descripcion del producto",widget=forms.Textarea(attrs={'col':80,'rows':20,'style':'resize none'}))
    Minimo=forms.IntegerField(required=True,help_text="Cantidad Minima de producto en almacen")
    Maximo=forms.IntegerField(required=True,help_text="Cantidad Maxima de producto en almacen")
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Producto
        fields = ("__all__")
        
class ProductoFormE(forms.Form):
    pk=forms.CharField(widget=forms.HiddenInput())
    accion=forms.CharField(widget=forms.HiddenInput())
    producto = forms.CharField(max_length=140, required=True, help_text="nombre del producto")
    descripcion=forms.CharField(required=False,help_text="Descripcion del producto",widget=forms.Textarea(attrs={'col':80,'rows':20,'style':'resize none'}))
    Minimo=forms.IntegerField(required=True,help_text="Cantidad Minima de producto en almacen")
    Maximo=forms.IntegerField(required=True,help_text="Cantidad Maxima de producto en almacen")
    def __init__(self, *args, **kwargs):
        super(ProductoFormE, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Producto
        fields = ("__all__")
