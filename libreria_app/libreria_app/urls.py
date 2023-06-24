
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('libro/', include('libro.urls')),
    # path('autor/', include('autor.urls')),
    path('autores/', include('autor.urls')),

]
