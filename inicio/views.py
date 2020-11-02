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
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    mensage = 'Pagina Principal '

    return render(
        request, 'inicio_index.html',
        context={'mensage': mensage}
    )
