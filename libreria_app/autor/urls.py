from django.urls import path
from . import views


urlpatterns = [
path('<int:pk>', views.AutorRetrieveAPIView.as_view()),
path('create', views.AutorListCreateAPIView.as_view()),
path('update/<int:pk>', views.AutorUpdateAPIView.as_view()),
path('delete/<int:pk>', views.AutorDestroyAPIView.as_view()),
 ]


