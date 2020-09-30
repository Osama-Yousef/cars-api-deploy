from django.shortcuts import render
from rest_framework import generics

from .models import Car
from .serializer import CarSerializer
from .permissions import IsAuthorOrReadOnly

class CarsList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Car.objects.all()
    serializer_class = CarSerializer