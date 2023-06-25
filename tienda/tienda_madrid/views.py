from django.shortcuts import render
from rest_framework import generics
from .models import Tienda
from .serializers import TiendaSerializer
from django.http import JsonResponse

class TiendaListCreateView(generics.ListCreateAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
    

class TiendaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer


def mostrar_dias_abiertas(request):
    queryset = Tienda.objects.all()
    tiendas_dias = {}
    for i in range(len(queryset)):
        tiendas_dias[queryset[i].id] = queryset[i].dias_abierta
   
    return JsonResponse(tiendas_dias)