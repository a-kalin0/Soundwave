# urls.py
from django.urls import path
from .views import SoundList, SoundDetail

urlpatterns = [
    path('sounds/', SoundList.as_view(), name='sound-list'),
    path('sounds/<int:pk>/', SoundDetail.as_view(), name='sound-detail'),
]
