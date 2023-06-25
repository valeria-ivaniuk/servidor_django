from django.urls import path
from .views import TiendaListCreateView, TiendaRetrieveUpdateDestroyView

urlpatterns = [
    path('', TiendaListCreateView.as_view(), name='tienda-list-create'),
    path('<int:pk>/', TiendaRetrieveUpdateDestroyView.as_view(), name='tienda-retrieve-update-destroy'),
]