from django.conf.urls import url

from almacen import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    #url(r'^producto/crear', views.ProductoCrear,name='producto'),
    url(r'^producto/(?P<id>[-\w]+)/detalle',views.ProductoDetalle, name='producto-detail'),
    #url(r'^lproducto/', views.ProductoEliminar,name='eliminarp'),
    #url(r'^producto/editar', views.ProductoEditar,name='editarp'),
    url(r'^inventario/', views.ProductoListView,name='lproducto'),
    url(r'^inventario/crear', views.InventarioCrear,name='inventario'),

    url(r'^entrada/',views.EntradaView,name='entrada'),
    url(r'^buscar/',views.postBuscar,name='buscar'),
    url(r'^ingresar/', views.postIngresar, name='ingresar'),
    url(r'^salida/', views.SalidaView, name='salida'),
    url(r'^sbuscar/',views.postSbuscar,name='sbuscar'),
    url(r'^reduccion/', views.postReducir, name='reduccion'),
    url(r'^lentradas/', views.EntradaListView,name='lentradas'),
    url(r'^lsalidas/', views.SalidaListView,name='lsalidas'),

    
]
