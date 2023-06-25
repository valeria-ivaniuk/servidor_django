from django.contrib import admin
from django.urls import include, path
from tienda_madrid.views import TiendaListCreateView, TiendaRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('tienda_madrid.urls')),
]
