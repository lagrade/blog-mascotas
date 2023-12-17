from django.contrib import admin
from django.urls import path, include
from AppMascotas.views import show, GatosList, GatosAgregar, PerrosAgregar, PerrosList


urlpatterns = [
    path('agregar-gato', GatosAgregar.as_view(), name="agregarGato"),
    path('gatoslist/', GatosList.as_view(), name="gatoslist"),
    path('agregar-perro', PerrosAgregar.as_view(), name="agregarPerro"),
    path('perroslist/', PerrosList.as_view(), name="perroslist"),

]
