from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LocationsConfig(AppConfig):
    name = 'apps.locations'
    verbose_name = _(u'Locations')
