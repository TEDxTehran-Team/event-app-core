from django.apps import AppConfig
from django.utils.translation import ugettext as _


class EventsConfig(AppConfig):
    name = 'tedxapp.events'
    verbose_name = _(u'Events')
