from django.urls import path 
from .views import DeleteAccountView, DeactivateAccountView

urlpatterns = [
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
    path('deactivate-account/', DeactivateAccountView.as_view(), name='deactivate-account'),
]