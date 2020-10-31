
from apps.events.models import Organizer
from apps.applications.models import Application, ApplicationToken


class OrganizerMiddleware:
    def resolve(self, next, root, info, **args):
        token = info.context.META.get('HTTP_APPLICATION_TOKEN')
        if token is not None:
            try:
                app = ApplicationToken.objects.get(key=token)
                organizer_id = app.application.organizer.id
            except:
                organizer_id = Organizer.objects.all().first().id
        else:
            organizer_id = Organizer.objects.all().first().id
        args["organizer"] = organizer_id
        return_value = next(root, info, **args)
        return return_value