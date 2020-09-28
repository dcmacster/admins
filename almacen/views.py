from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
#from .models import Book, Author, BookInstance, Genre, Language, Perfil
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import datetime

#from .forms import SingUpForm, RenewBookForm, OnloanBookForm, MaintenanceBookForm, AviableBookForm



# Create your views here.
from .models import Producto,Inventario,Imagen

def index(request):
    mensage='Bienvenido '

    return render(
        request,'index.html',
        context={'mensage':mensage}
    )


class ProductoListView(generic.ListView):
    redirect_field_name = 'redirect_to'
    model = Producto
    paginate_by = 10
