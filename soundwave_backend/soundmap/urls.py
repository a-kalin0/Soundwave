from django.urls import path
from . import views

urlpatterns = [
    path('get-mapbox-api-key/', views.get_mapbox_api_key, name='get_mapbox_api_key'),
    path('get-maptiler-api-key/', views.get_maptiler_api_key, name='get_maptiler_api_key'),
]
