from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.db.models import Max, Min, Count, Sum, Avg
#from .models import Book, Author, BookInstance, Genre, Language, Perfil
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import datetime

import json
#from .forms import SingUpForm, RenewBookForm, OnloanBookForm, MaintenanceBookForm, AviableBookForm


# Create your views here.
from .models import Producto,Inventario,Imagen
from .forms import BuscarCodigoForm

def index(request):
    mensage='Bienvenido '

    return render(
        request,'index.html',
        context={'mensage':mensage}
    )

'''
class ProductoListView(generic.ListView):
    redirect_field_name = 'redirect_to'
    model = Producto
    paginate_by = 10
'''

def ProductoListView(request):
    producto_list=Producto.objects.all().annotate(Cant_total=Sum('inventario__cantidad'))
    return render(
        request,'producto_list.html',
       {'producto_list':producto_list}
    )

def EntradaView(request):
    form = BuscarCodigoForm()
    inventarios=Inventario.objects.select_related('producto')
    return render(request,"entrada.html",{"form":form,"inventarios":inventarios})

def postEntrada(request):
    #if request.is_ajax and request.method=="GET":
       # form=BuscarCodigoForm(request.POST)

        #if form.is_valid():
    buscodigo=request.GET.get('codigo')
    inventarios=Inventario.objects.filter(codigob=buscodigo).select_related('producto')
    inventarios=[inventario_serializer(inventario) for inventario in inventarios]
    return HttpResponse(json.dumps(inventarios), content_type='application/json')
    #return JsonResponse({"instance":inventarios}, status=200)
    #instance = {'id':inventarios.Inventario.id,'codigob':inventarios.codigob,'nombre':inventarios.nombre,'descripcion':inventarios.descripcion,'cantidad':inventarios.cantidad}
    #ser_instance= serializers.serialize('json',[instance,])
    #return JsonResponse({"instance":ser_instance}, status=200)
    #else:
    #   return JsonResponse({"error":form.errors},status=400)

    #return JsonResponse({"error":"no entra"}, status=400)


def inventario_serializer(inventario):
    #return {'id':inventario.id,'codigob':inventario.codigob,'cantidad':inventario.cantidad}
    return {'id':inventario.id,'codigob':inventario.codigob,'nombre':inventario.producto.nombre,'descripcion':inventario.producto.descripcion,'cantidad':inventario.cantidad}

        

