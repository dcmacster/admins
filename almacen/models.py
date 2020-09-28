from django.db import models

# Create your models here.
from django.urls import reverse
import uuid  # Requerida para las instancias de libros únicos
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000,  help_text="Ingrese una breve descripción del producto")
    minimo = models.IntegerField(default=0)
    maximo = models.IntegerField(default=0)

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('producto-detail', args=[str(self.id)])


class Inventario(models.Model):
    producto=models.ForeignKey('Producto', on_delete=models.CASCADE, null=True)
    cantidad=models.IntegerField(default=0)
    codigob = models.CharField(max_length=200)
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('inventario')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s) %s' % (self.id, self.producto.nombre,self.cantidad)

class Imagen(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=True)
    imagen= models.ImageField(upload_to='pic_folder/',default='pic_folder/None/no-img.jpg')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s) %s' % (self.id, self.producto.nombre,self.imagen)
 
