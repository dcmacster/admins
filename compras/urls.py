from django.conf.urls import url

from compras import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^proveedor/(?P<id>[-\w]+)/detalle',views.ProveedorDetalle, name='proveedor-detail'),
    url(r'^directorio/', views.ProveedorListView,name='proveedor-list'),
    url(r'^detalle/(?P<id>[-\w]+)', views.CompraDetalle, name='compra-detail'),
    url(r'^nuevo/', views.CompraNuevo, name='compra-nuevo'),
    #url(r'^buscar/',views.postBuscar,name='buscar'),
    url(r'^lista/', views.CompraListView,name='compra-list'),
    

    
]
