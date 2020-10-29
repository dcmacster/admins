from django.contrib import admin

# Register your models here.
from .models import Proveedor, DCompra, ECompra


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion', 'email')
    fields = ['nombre', 'direccion',('contacto','email'), ('telefono', 'celular'),'observacion']
    search_fields = ['nombre']
    
