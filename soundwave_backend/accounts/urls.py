from django.urls import path 
from .views import *

urlpatterns = [
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
    path('deactivate-account/', DeactivateAccountView.as_view(), name='deactivate-account'),
    path('get_stats/', GetStatsView.as_view(), name='get_stats'),
]