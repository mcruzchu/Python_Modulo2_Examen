from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_platos, name='lista_platos'),
    path('peruanos/', views.platos_peruanos, name='platos_peruanos'),
    path('eliminar-baratos/', views.eliminar_platos_baratos, name='eliminar_platos_baratos'),
    path('caros/', views.platos_caros, name='platos_caros'),
]

