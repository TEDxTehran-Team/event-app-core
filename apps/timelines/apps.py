from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TimelinesConfig(AppConfig):
    name = 'apps.timelines'
    verbose_name = _(u'Timelines')
