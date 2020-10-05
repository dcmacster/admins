from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    #url(r'^producto/', views.ProductoListView.as_view(),name='producto'),
    url(r'^producto/', views.ProductoListView,name='producto'),
    url(r'^entrada/',views.EntradaView,name='entrada'),
    url(r'^buscar/',views.postBuscar,name='buscar'),
    url(r'^ingresar/', views.postIngresar, name='ingresar'),
    url(r'^salida/', views.SalidaView, name='salida'),
    url(r'^sbuscar/',views.postSbuscar,name='sbuscar'),
    url(r'^reduccion/', views.postReducir, name='reduccion'),
    url(r'^lentradas/', views.EntradaListView,name='lentradas'),
    url(r'^lsalidas/', views.SalidaListView,name='lsalidas'),

]
