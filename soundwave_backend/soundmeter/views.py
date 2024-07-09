# views.py
from rest_framework import generics
from .models import Sound
from .serializers import SoundSerializer

class SoundList(generics.ListCreateAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer
