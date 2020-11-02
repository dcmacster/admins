from django.contrib import admin

# Register your models here.
from .models import Proveedor, DCompra, ECompra


class DCompraInline(admin.TabularInline):
    model = DCompra

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion', 'email')
    fields = ['nombre', 'direccion',('contacto','email'), ('telefono', 'celular'),'observacion']
    search_fields = ['nombre']
    

@admin.register(ECompra)
class ECompraAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'proveedor', 'factura', 'total')
    fields = ['proveedor', ('factura','pedido','fecha'), ('subtotal', 'iva','total')]
    inlines = [DCompraInline]
    search_fields = ['proveedor', 'fecha','factura']
    list_filter = ['total']
