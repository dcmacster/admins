from django import forms


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.


from almacen.models import Producto,Inventario
from .models import Proveedor, ECompra, DCompra


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
'''
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

'''

class BuscarProveedorForm(forms.Form):
    proveedor = forms.CharField(max_length=200, required=True, help_text="Ingrese Proveedor a buscar")
    
    def __init__(self,*args, **kwargs):
        super(BuscarProveedorForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })

    class Meta:
        model=Proveedor
        fields=("__all__")    

class ECompraForm(forms.Form):
    proveedor =forms.ModelChoiceField(queryset=Proveedor.objects.all(),empty_label=None)
    pedido = forms.CharField(max_length=200)
    factura = forms.CharField(max_length=200)
    fecha = forms.DateField()
    subtotal = forms.DecimalField(max_digits=10, decimal_places=2)
    iva = forms.DecimalField(max_digits=10, decimal_places=2)
    total = forms.DecimalField(max_digits=10, decimal_places=2)
    observacion = forms.CharField(required=False, help_text="Observacion de la compra", widget=forms.Textarea(
        attrs={'col': 80, 'rows': 20, 'style': 'resize none'}))
  
    def __init__(self,*args, **kwargs):
        super(ECompraForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
            })

    class Meta:
        model=ECompra
        fields=("__all__")    


class DCompraForm(forms.Form):
    inventario = forms.ModelChoiceField(
        queryset=Inventario.objects.all().select_related('producto'), empty_label=None)
    cantidad = forms.IntegerField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    importe = forms.DecimalField(max_digits=10, decimal_places=2)
    observacion = forms.CharField(required=False, help_text="Observacion de la compra")
   

    def __init__(self, *args, **kwargs):
        super(DCompraForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = DCompra
        fields = ("__all__")


'''
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

class InventarioForm(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(),empty_label=None)
    codigo=forms.CharField(required=False,help_text="Descripcion del producto",widget=forms.Textarea(attrs={'col':80,'rows':20,'style':'resize none'}))
    cantidad=forms.IntegerField(required=True,help_text="Cantidad Minima de producto en almacen")
    
    def __init__(self, *args, **kwargs):
        super(InventarioForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Inventario
        fields = ("__all__")
        
'''
