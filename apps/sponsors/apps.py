from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SponsorsConfig(AppConfig):
    name = 'apps.sponsors'
    verbose_name = _(u'Sponsors')
