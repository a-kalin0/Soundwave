from rest_framework import generics, viewsets, views
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Sound
from .serializers import SoundSerializer
import subprocess
import sys
import json
import os


class SoundList(generics.ListCreateAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class SoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer 


class ElectronicSoundMeter(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'soundmeter', 'sound_meter_app.py')
            subprocess.Popen([sys.executable, script_path])
            return Response({'success': True})
        except Exception as e:
            print(f"Error: {e}")
            return Response({'success': False, 'error': str(e)}, status=500)
       

class ImportMeasureAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'success': False, 'error': 'No file uploaded'}, status=400)
        
        try:
            data = json.load(file)

            title = data.get('title')
            description = data.get('description')
            min_level = data.get('min_level')
            max_level = data.get('max_level')
            avg_level = data.get('avg_level')
            measurement_time = data.get('measurement_time') 

            if not title or not description or min_level is None or max_level is None or avg_level is None:
                return Response({'success': False, 'error': 'Invalid data in JSON file'}, status=400)
            
            minutes, seconds = map(int, measurement_time.split(':'))
            total_seconds = minutes * 60 + seconds
            
            sound = Sound.objects.create(
                title=title,
                description=description,
                min_db_size=min_level,
                max_db_size=max_level,
                avg_db_size=avg_level,
                duration=total_seconds,
                owner=request.user
            )

            return Response({'success': True, 'sound_id': sound.id})
        
        except json.JSONDecodeError:
            
            return Response({'success': False, 'error': 'Invalid JSON file'}, status=400)
