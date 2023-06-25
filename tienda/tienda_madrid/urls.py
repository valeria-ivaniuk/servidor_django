from django.urls import path
from .views import TiendaListCreateView, TiendaRetrieveUpdateDestroyView,mostrar_dias_abiertas

urlpatterns = [
    path('', TiendaListCreateView.as_view(), name='tienda-list-create'),
    path('<int:pk>/', TiendaRetrieveUpdateDestroyView.as_view(), name='tienda-retrieve-update-destroy'),
    path('dias_abierta',mostrar_dias_abiertas , name='tienda-dias-abierta'),
]