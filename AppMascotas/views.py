from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from AppMascotas.models import PostPerro, PostGato
from AppMascotas.forms import Perros_form, Gatos_form
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
def show(request):
    return render(request, "index.html")


class GatosList(ListView):
    model = PostGato
    template_name = "AppMascotas/gatos.html"
    context_object_name = "mascotas"


class GatosAgregar(LoginRequiredMixin,CreateView):
    model = PostGato
    form_class = Gatos_form
    success_url = "/app/gatoslist/"
    template_name = "AppMascotas/agregar_gato.html"

class PerrosList(ListView):
    model = PostPerro
    template_name = "AppMascotas/perros.html"
    context_object_name = "mascotas"


class PerrosAgregar(LoginRequiredMixin,CreateView):
    model = PostPerro
    form_class = Perros_form
    success_url = "/app/perroslist/"
    template_name = "AppMascotas/agregar_perro.html"
