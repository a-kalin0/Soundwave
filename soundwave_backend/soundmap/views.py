from django.http import JsonResponse
from django.conf import settings

def get_mapbox_api_key(request):
    return JsonResponse({'mapbox_api_key': settings.MAPBOX_API_KEY})
