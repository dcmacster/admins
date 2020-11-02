# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.db.models import Max, Min, Count, Sum, Avg

from django.core.paginator import Paginator

from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import datetime
import time
import json
from django.forms import formset_factory
# Create your views here.
from almacen.models import Producto, Inventario
from .models import Proveedor,ECompra,DCompra
from .forms import BuscarCodigoForm,  BuscarProveedorForm, ECompraForm, DCompraForm


@login_required(login_url='/accounts/login/')
def index(request):
    mensage = 'Bienvenido '

    return render(
        request, 'compra_index.html',
        context={'mensage': mensage}
    )


'''
class ProductoListView(generic.ListView):
    redirect_field_name = 'redirect_to'
    model = Producto
    paginate_by = 10



def ProductoCrear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            regproducto = Producto(nombre=form['producto'].value(), descripcion=form['descripcion'].value(
            ), minimo=form['Minimo'].value(), maximo=form['Maximo'].value())
            regproducto.save()
            mensaje = 'Producto guardado con Exito'
    else:
        mensaje = ''

    form = ProductoForm()
    return render(
        request, 'producto.html',
        {'form': form, 'mensaje': mensaje}
    )
'''
@login_required(login_url='/accounts/login/')
def ProveedorDetalle(request, id=id):
    if request.method == 'GET':
        busproveedor = request.GET.get('id')
        proveedor_det = Proveedor.objects.filter(id=id)
        inventario_det = Inventario.objects.filter(producto=id)

        return render(
            request, 'proveedor_detail.html',
            {'proveedor': proveedor_det, 'inventario': inventario_det}
        )

    else:
        proveedor_list = Proveedor.objects.all()
        form = BuscarProveedorForm()
        paginator = Paginator(proveedor_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request, 'proveedor_list.html',
            {'form': form, 'page_obj': page_obj}
        )


@login_required(login_url='/accounts/login/')
def ProveedorListView(request):
    if request.method == 'POST':
        form = BuscarProveedorForm(request.POST)
        if form.is_valid():
            busproveedor = request.POST.get('proveedor')
            proveedor_list = Proveedor.objects.filter(nombre__icontains=busproveedor)# | Proveedor.objects.filter(descripcion__icontains=busproducto).annotate(Cant_total=Sum('inventario__cantidad'))
    else:
        proveedor_list = Proveedor.objects.all()

    form = BuscarProveedorForm()
    paginator = Paginator(proveedor_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'proveedor_list.html',
        {'form': form, 'page_obj': page_obj}
    )


@login_required(login_url='/accounts/login/')
def CompraListView(request):

    if request.method == 'POST':
        form = BuscarProveedorForm(request.POST)
        if form.is_valid():
            busproveedor = request.POST.get('proveedor')
            ecompra_list = ECompra.objects.select_related('proveedor').filter(
                proveedor__nombre__icontains=busproveedor)
    else:
        ecompra_list = ECompra.objects.select_related(
            'proveedor').all()

    form = BuscarProveedorForm()
    paginator = Paginator(ecompra_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'compra_list.html',
        {'form': form, 'page_obj': page_obj}
    )


@login_required(login_url='/accounts/login/')
def CompraDetalle(request, id=id):
    if request.method == 'GET':
        busproveedor = request.GET.get('id')
        ecompra_det = ECompra.objects.select_related('proveedor').filter(id=id)
        dcompra_det = DCompra.objects.select_related('inventario__producto').filter(compra=id)

        return render(
            request, 'compra_detail.html',
            {'encabezado': ecompra_det, 'detalle': dcompra_det}
        )

    else:
        ecompra_list = ECompra.objects.select_related('proveedor').all()

        form = BuscarProveedorForm()
        paginator = Paginator(ecompra_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request, 'compra_list.html',
            {'form': form, 'page_obj': page_obj}
        )


@login_required(login_url='/accounts/login/')
def CompraNuevo(request):
    DCompraFormSet = formset_factory(DCompraForm, extra=2, can_delete=True)
    if request.method == 'POST':
        form = ECompraForm(request.POST)
        formset = DCompraFormSet(request.POST)
        if form.is_valid() and formset.is_valid() :
            regecompra = ECompra(Proveedor=form['proveedor'].value(), pedido=form['pedido'].value(), factura=form['factura'].value(), fecha=form['fecha'].value(), subtotal=form['subtotal'].value(), iva=form['iva'].value(), total=form['total'].value(),observacion=form['observacion'].value())
            regecompra.save()
            
            
            mensaje = 'Producto guardado con Exito'
    else:
        form = ECompraForm()    
        formset = DCompraFormSet()

    
    return render(
        request, 'compra_nuevo.html',
        {'form': form,'formset':formset}
    )


'''
def ProductoEliminar(request):
    if request.method == 'POST':
        busproducto = request.POST.get('pk')
        producto_inst = get_object_or_404(Producto, pk=busproducto)
        producto_inst.delete()

    producto_list = Producto.objects.all().annotate(
        Cant_total=Sum('inventario__cantidad'))
    form = BuscarProductForm()
    paginator = Paginator(producto_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'producto_list.html',
        {'form': form, 'page_obj': page_obj}
    )


def ProductoEditar(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')
        pk = request.POST.get('pk')
        producto_det = get_object_or_404(Producto, pk=pk)
        if int(accion) == 1:

            #producto_det = Producto.objects.filter(id=id)
            data = {
                'pk': producto_det.id,
                'accion': '2',
                'producto': producto_det.nombre,
                'descripcion': producto_det.descripcion,
                'Minimo': producto_det.minimo,
                'Maximo': producto_det.maximo
            }
            form = ProductoFormE(initial=data)
            return render(
                request, 'producto_editar.html',
                {'form': form}
            )
        elif int(accion) == 2:

            form = ProductoFormE(request.POST)
            if form.is_valid():
                producto_det.nombe = form['producto'].value()
                producto_det.descripcion = form['descripcion'].value()
                producto_det.minimo = form['Minimo'].value()
                producto_det.maximo = form['Maximo'].value()
                producto_det.save()

            producto_list = Producto.objects.all().annotate(
                Cant_total=Sum('inventario__cantidad'))
            form = BuscarProductForm()
            paginator = Paginator(producto_list, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(
                request, 'producto_list.html',
                {'form': form, 'page_obj': page_obj}
            )
        else:
            mensage = 'Bienvenido '
            return render(
                request, 'index.html',
                context={'mensage': mensage}
            )
    else:
        producto_list = Producto.objects.all().annotate(
            Cant_total=Sum('inventario__cantidad'))
        form = BuscarProductForm()
        paginator = Paginator(producto_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request, 'producto_list.html',
            {'form': form, 'page_obj': page_obj}
        )


def InventarioCrear(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            regproducto = Inventario(producto=form['producto'].value(
            ), codigob=form['codigo'].value(), cantidad=form['cantidad'].value())
            regproducto.save()
            mensaje = 'Producto guardado con Exito'
    else:
        mensaje = ''

    form = InventarioForm()
    return render(
        request, 'producto.html',
        {'form': form, 'mensaje': mensaje}
    )


def EntradaView(request):
    form = BuscarCodigoForm()
    inventarios = Inventario.objects.select_related('producto')
    return render(request, "entrada.html", {"form": form, "inventarios": inventarios})


def postBuscar(request):
    if request.method == 'POST':
        form = BuscarCodigoForm(request.POST)
        if form.is_valid():
            buscodigo = request.POST.get('codigo')
            form = EntradaCantidadForm()
            inventarios = Inventario.objects.filter(
                codigob=buscodigo).select_related('producto')
            return render(request, "ingreso.html", {"form": form, "inventarios": inventarios})
    else:
        form = BuscarCodigoForm()
        inventarios = Inventario.objects.select_related('producto')
        return render(request, "entrada.html", {"form": form, "inventarios": inventarios})


def postIngresar(request):
    if request.method == 'POST':
        form = EntradaCantidadForm(request.POST)
        if form.is_valid():
            pk = request.POST.get('pk')
            cantidadf = int(request.POST.get('cantidad'))
            ingresos = get_object_or_404(Inventario, pk=pk)
            #ingresos = Inventario.objects.filter(id=pk)
            cantidadact = ingresos.cantidad
            cantidad = cantidadf+cantidadact
            ingresos.cantidad = cantidad
            ingresos.save()
            rentrada = regEntrada(inventario=Inventario.objects.get(id=pk), cantidad=cantidadf,
                                  fecha=datetime.date.today(), hora=time.strftime("%X"))
            rentrada.save()
            form = BuscarCodigoForm()
            inventarios = Inventario.objects.select_related('producto')
            return render(request, "entrada.html", {"form": form, "inventarios": inventarios})
    else:
        form = BuscarCodigoForm()
        inventarios = Inventario.objects.select_related('producto')
        return render(request, "entrada.html", {"form": form, "inventarios": inventarios})


def SalidaView(request):
    form = BuscarCodigoForm()
    inventarios = Inventario.objects.select_related('producto')
    return render(request, "salida.html", {"form": form, "inventarios": inventarios})


def postSbuscar(request):
    if request.method == 'POST':
        form = BuscarCodigoForm(request.POST)
        if form.is_valid():
            buscodigo = request.POST.get('codigo')
            form = EntradaCantidadForm()
            inventarios = Inventario.objects.filter(
                codigob=buscodigo).select_related('producto')
            return render(request, "reduccion.html", {"form": form, "inventarios": inventarios})
    else:
        form = BuscarCodigoForm()
        inventarios = Inventario.objects.select_related('producto')
        return render(request, "salida.html", {"form": form, "inventarios": inventarios})


def postReducir(request):
    if request.method == 'POST':
        form = EntradaCantidadForm(request.POST)
        if form.is_valid():

            pk = request.POST.get('pk')
            cantidadf = int(request.POST.get('cantidad'))
            ingresos = get_object_or_404(Inventario, pk=pk)
            #ingresos = Inventario.objects.filter(id=pk)
            cantidadact = ingresos.cantidad
            cantidad = cantidadact-cantidadf
            ingresos.cantidad = cantidad
            ingresos.save()
            rsalida = regSalida(inventario=Inventario.objects.get(
                id=pk),  cantidad=cantidadf, fecha=datetime.date.today(), hora=time.strftime("%X"))
            rsalida.save()
            form = BuscarCodigoForm()
            inventarios = Inventario.objects.select_related('producto')
            return render(request, "salida.html", {"form": form, "inventarios": inventarios})
    else:
        form = BuscarCodigoForm()
        inventarios = Inventario.objects.select_related('producto')
        return render(request, "salida.html", {"form": form, "inventarios": inventarios})

def SalidaListView(request):
    salida_list = regSalida.objects.select_related('inventario__producto')
    paginator = Paginator(salida_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request, 'salidas_list.html',
        {'page_obj': page_obj}
    )



*****para trabajar con ajax*****


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
   

    return {
         'id':inventario.id,
        'codigob':inventario.codigob,
        'nombre':inventario.producto.nombre,
        'descripcion':inventario.producto.descripcion,
        'cantidad':inventario.cantidad
    }
'''
