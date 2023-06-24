from django.shortcuts import render
from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer
from autor.models import Autor
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status


class LibroRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroUpdateAPIView(generics.UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroDestroyAPIView(generics.DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

@api_view(['GET'])
def api_libros(request):
    instanceAutor = Autor.objects.all().order_by('?').first()
    instanceLibro = Libro.objects.filter(autor=instanceAutor)
    data = {}
    if instanceLibro:
        data = LibroSerializer(instanceLibro[0]).data
        return Response(data)

