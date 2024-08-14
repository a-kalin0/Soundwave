# urls.py
from django.urls import path
from .views import SoundList, SoundDetail, ElectronicSoundMeter, ImportMeasureAPIView

urlpatterns = [
    path('sounds/', SoundList.as_view(), name='sound-list'),
    path('sounds/<int:pk>/', SoundDetail.as_view(), name='sound-detail'),
    path('electronic_sound_meter/', ElectronicSoundMeter.as_view(), name='electronic-sound-meter'),
    path('import_measure/', ImportMeasureAPIView.as_view(), name='import-measure'),
]
