from django.contrib import admin

# Register your models here.
from .models import Producto, Inventario, Imagen


class ProductoInventarioInline(admin.TabularInline):
    model = Inventario

class ProductoImagenInline(admin.TabularInline):
    model = Imagen


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','minimo','maximo')
    fields=['nombre','descripcion',('minimo','maximo')]
    inlines = [ProductoInventarioInline, ProductoImagenInline]

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display=('producto','cantidad','codigob')
        

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display=('producto','imagen')
    
