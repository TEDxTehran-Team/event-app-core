from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class EventsConfig(AppConfig):
    name = 'apps.events'
    verbose_name = _(u'Events')
