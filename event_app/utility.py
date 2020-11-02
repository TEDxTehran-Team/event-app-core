from apps.events.models import Organizer
from apps.applications.models import ApplicationToken


def get_organizer(info):
    token = info.context.META.get('HTTP_APPLICATION_TOKEN')
    if token is not None:
        try:
            app = ApplicationToken.objects.get(key=token)
            organizer_id = app.application.organizer.id
        except:
            organizer_id = Organizer.objects.all().last().id
    else:
        organizer_id = Organizer.objects.all().last().id
    return organizer_id