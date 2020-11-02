from django.conf.urls import url

from inicio import views

urlpatterns = [

    url(r'^$', views.index, name='index'),



]
