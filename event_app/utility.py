from apps.events.models import Organizer
from apps.applications.models import ApplicationToken
from django.conf import settings

def get_organizer(info):
    token = info.context.META.get('HTTP_APPLICATION_TOKEN')
    if token is not None:
        try:
            app = ApplicationToken.objects.get(key=token)
            return app.application.organizer.id
        except ApplicationToken.DoesNotExist:
            return settings.DEFAULT_ORGANIZER_ID
    else:
        return settings.DEFAULT_ORGANIZER_ID