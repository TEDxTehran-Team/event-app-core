from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TalksConfig(AppConfig):
    name = 'apps.talks'
    verbose_name = _(u'Talks')
