
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import MeseroSerializer
from .models import Mesero

# Tus vistas existentes
def lista_meseros(request):
    meseros = Mesero.objects.all()
    return render(request, 'meseros/lista_meseros.html', {'meseros': meseros})

def meseros_jovenes_peruanos(request):
    jovenes_meseros = Mesero.objects.filter(nacionalidad='Perú', edad__lt=30)
    return render(request, 'meseros/meseros_jovenes_peruanos.html', {'meseros': jovenes_meseros})

def actualizar_edades(request):
    meseros = Mesero.objects.all()
    for mesero in meseros:
        mesero.edad += 5
        mesero.save()
    return render(request, 'meseros/edades_actualizadas.html')

def meseros_mayores_25(request):
    queryset = Mesero.objects.filter(edad__gt=25)
    data = serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')

# Nuevas vistas basadas en clases
class CrearMesero(CreateView):
    model = Mesero
    fields = ['nombre', 'nacionalidad', 'edad', 'dni']
    template_name = 'meseros/crear_mesero.html'
    success_url = '/meseros/lista/'

class ListarMeserosPeruanos(ListView):
    model = Mesero
    template_name = 'meseros/listar_meseros_peruanos.html'
    context_object_name = 'meseros'

    def get_queryset(self):
        """Filtra meseros de Perú."""
        return Mesero.objects.filter(nacionalidad='Perú')

class EditarMesero(UpdateView):
    model = Mesero
    fields = ['nombre', 'nacionalidad', 'edad', 'dni']
    template_name = 'meseros/editar_mesero.html'
    success_url = '/meseros/lista/'


class ListaMeseros(ListView):
    model = Mesero
    template_name = 'meseros/lista_meseros.html'

class EliminarMesero(DeleteView):
    model = Mesero
    template_name = 'meseros/eliminar_mesero.html'
    success_url = reverse_lazy('meseros_lista')


class CrearMesero(generics.CreateAPIView):
    queryset = Mesero.objects.all()
    serializer_class = MeseroSerializer

class EditarMesero(generics.UpdateAPIView):
    queryset = Mesero.objects.all()
    serializer_class = MeseroSerializer


class DetalleMesero(generics.RetrieveAPIView):
    queryset = Mesero.objects.all()
    serializer_class = MeseroSerializer
    permission_classes = [permissions.IsAuthenticated]

class EliminarMesero(generics.DestroyAPIView):
    queryset = Mesero.objects.all()
    serializer_class = MeseroSerializer
    permission_classes = [permissions.IsAuthenticated]