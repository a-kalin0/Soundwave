import requests
from rest_framework import generics, viewsets, status
from rest_framework.response import Response 
from rest_framework.decorators import action
from .models import Sound
from .serializers import SoundSerializer

class SoundList(generics.ListCreateAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer 
