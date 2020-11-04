from django.db import models

# Create your models here.
from django.urls import reverse
import uuid  # Requerida para las instancias de libros únicos
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from datetime import date
from almacen.models import Producto, Inventario


class Proveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="ID único para este proveedor")
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(
        max_length=1000,  help_text="Ingrese la direccion del proveedor")
    contacto = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=240)
    observacion = models.TextField(
        max_length=1000,  help_text="Ingrese una observacion del proveedor")
    
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return '%s (%s) %s' % ( self.nombre, self.telefono, self.direccion)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('proveedor-detail', args=[str(self.id)])


class ECompra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="ID único para esta compra particular")
    proveedor=models.ForeignKey('Proveedor', on_delete=models.CASCADE, null=True)                          
    pedido = models.CharField(max_length=200)
    factura = models.CharField(max_length=200)
    fecha = models.DateField(null=True, blank=True)
    subtotal=models.DecimalField(max_digits=10,decimal_places=2)
    iva=models.DecimalField(max_digits=10,decimal_places=2)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    observacion = models.TextField(
        max_length=1000,  help_text="Ingrese una observacion de la compra")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return '%s (%s) %s %s' % (self.factura, self.proveedor.nombre, self.fecha, self.total)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('compra-detail', args=[str(self.id)])


class DCompra(models.Model):
    compra=models.ForeignKey('ECompra', on_delete=models.CASCADE, null=True)                          
    inventario=models.ForeignKey('almacen.Inventario', on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=0)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    importe=models.DecimalField(max_digits=10,decimal_places=2)
    observacion = models.TextField(
        max_length=1000,  help_text="Ingrese una observacion")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        """
        String que representa al objeto Book
        """
        return '%s (%s) %s %s' % (self.inventario.producto.nombre, self.cantidad, self.precio, self.importe)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('compra-detail', args=[str(self.id)])

@receiver(pre_save, sender=DCompra)
def modificar_inventario(sender,instance,**kwargs):
    if not instance._state.adding:
        regdcompra=DCompra.objects.get(pk=instance.id)
        reginventario=Inventario.objects.get(pk=regdcompra.inventario.id)
        cantmod=int(regdcompra.cantidad)
        cantactual=int(reginventario.cantidad)
        canttotal=cantactual-cantmod
        reginventario.cantidad=canttotal
        reginventario.save()


@receiver(post_save, sender=DCompra)
def agregar_inventario(sender,instance,**kwargs):
    reginventario=Inventario.objects.get(pk=instance.inventario.id)
    cantnuevo=int(instance.cantidad)
    cantactual=int(reginventario.cantidad)
    canttotal=cantactual+cantnuevo
    reginventario.cantidad=canttotal
    reginventario.save()


@receiver(pre_delete, sender=DCompra)
def  desagregar_inventario(sender,instance,**kwargs):
    reginventario=Inventario.objects.get(pk=instance.inventario.id)
    cantnuevo=int(instance.cantidad)
    cantactual=int(reginventario.cantidad)
    canttotal=cantactual-cantnuevo
    reginventario.cantidad=canttotal
    reginventario.save()
