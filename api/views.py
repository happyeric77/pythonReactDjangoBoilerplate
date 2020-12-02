from django.shortcuts import render
from rest_framework import generics
from .serializers import DemoSerializer
from .models import Demo 

class DemoView(generics.CreateAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
