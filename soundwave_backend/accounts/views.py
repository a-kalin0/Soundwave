from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.mail import send_mail
from djoser import utils
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.utils import timezone

from soundmeter.models import Sound 

class DeleteAccountView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class DeactivateAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.is_active = False
        user.save()

        uid = utils.encode_uid(user.pk)
        token = default_token_generator.make_token(user)

        reactivate_link = f"{request.scheme}://localhost:8080/activate/{uid}/{token}"
        
        html_message = render_to_string('email/reactivation.html', {'user': user, 'reactivate_link': reactivate_link})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = user.email

        send_mail(
            'Reactivate your account',
            plain_message,
            from_email,
            [to],
            html_message=html_message,
            fail_silently=False,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


class GetStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        user = request.user

        time_spent = (timezone.now() - user.date_joined).total_seconds()

        sounds_recorded = Sound.objects.filter(owner=user).count()

        sounds_shared = Sound.objects.filter(owner=user, is_shared=True).count()

        stats = {
            'time_spent': time_spent,
            'sounds_recorded': sounds_recorded,
            'sounds_shared': sounds_shared,
        }

        return Response(stats, status=status.HTTP_200_OK)
    