from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor
from .serializer import AutorSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Autor
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions, authentication
# Create your views here.

class AutorAPIView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        autores = Autor.objects.all()
        serializer = AutorSerializer(productos, many=True)
        
        return Response(serializer.data)
    def post(self,request):
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            return Response(serializer.errors)
    
class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)



# class AutorRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer

# class AutorListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer

# class AutorUpdateAPIView(generics.UpdateAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer

# class AutorDestroyAPIView(generics.DestroyAPIView):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer
