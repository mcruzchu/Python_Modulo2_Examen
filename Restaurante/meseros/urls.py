from django.urls import path
from . import views
from .views import CrearMesero, ListarMeserosPeruanos, ListaMeseros, EditarMesero, EliminarMesero

urlpatterns = [
    path('lista/', views.lista_meseros, name='lista_meseros'),
    path('jovenes-peruanos/', views.meseros_jovenes_peruanos, name='meseros_jovenes_peruanos'),
    path('actualizar-edades/', views.actualizar_edades, name='actualizar_edades'),
    path('mayores-25/', views.meseros_mayores_25, name='meseros_mayores_25'),
    path('crear/', CrearMesero.as_view(), name='crear_mesero'),
    path('listar-peruanos/', ListarMeserosPeruanos.as_view(), name='listar_meseros_peruanos'),
    path('lista/', ListaMeseros.as_view(), name='meseros_lista'),
    path('editar/<int:pk>/', EditarMesero.as_view(), name='editar_mesero'),
    path('eliminar/<int:pk>/', EliminarMesero.as_view(), name='eliminar_mesero'),
    path('api/crear-mesero/', CrearMesero.as_view(), name='api_crear_mesero'),
    path('api/editar-mesero/<int:pk>/', EditarMesero.as_view(), name='api_editar_mesero'),
    path('api/detalle-mesero/<int:pk>/', DetalleMesero.as_view(), name='api_detalle_mesero'),
    path('api/eliminar-mesero/<int:pk>/', EliminarMesero.as_view(), name='api_eliminar_mesero'),
]


