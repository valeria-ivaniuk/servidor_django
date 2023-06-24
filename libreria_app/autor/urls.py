from autor.views import  AutorViewSet, AutorAPIView
from rest_framework.routers import DefaultRouter 
from django.contrib import admin
from django.urls import path, include




router = DefaultRouter()
router.register('autor_viewset', AutorViewSet)

urlpatterns = [
    path('autores/', AutorAPIView.as_view()),
   ]  + router.urls
    


# from django.urls import path
# from . import views


# urlpatterns = [
# path('<int:pk>', views.AutorRetrieveAPIView.as_view()),
# path('create', views.AutorListCreateAPIView.as_view()),
# path('update/<int:pk>', views.AutorUpdateAPIView.as_view()),
# path('delete/<int:pk>', views.AutorDestroyAPIView.as_view()),
#  ]


