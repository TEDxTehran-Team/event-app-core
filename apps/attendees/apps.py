from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AttendeesConfig(AppConfig):
    name = 'apps.attendees'
    verbose_name = _(u'Attendees')
