from re import sub

from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token

from .models import Application, ApplicationToken, ApplicationHit


class ApplicationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        api_key = request.META.get('HTTP_X_API_KEY')
        application_key = ApplicationToken.objects.filter(
            key=api_key,
            active=True,
            application__active=True).first()

        if application_key:
            request.application = application_key.application
        else:
            request.application = None
