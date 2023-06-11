from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor
from .serializer import AutorSerializer
from rest_framework import generics
# Create your views here.

class AutorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorUpdateAPIView(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDestroyAPIView(generics.DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
