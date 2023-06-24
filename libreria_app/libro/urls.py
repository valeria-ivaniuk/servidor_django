from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter 



urlpatterns = [
    path('', views.api_libros),
    path('<int:pk>', views.LibroRetrieveAPIView.as_view()),
    path('create', views.LibroListCreateAPIView.as_view()),
    path('update/<int:pk>', views.LibroUpdateAPIView.as_view()),
    path('delete/<int:pk>', views.LibroDestroyAPIView.as_view()),
    path('delete/<int:pk>', views.LibroDestroyAPIView.as_view()),
] 