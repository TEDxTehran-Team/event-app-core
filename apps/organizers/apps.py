from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrganizersConfig(AppConfig):
    name = 'apps.organizers'
    verbose_name = _(u'Organizers')
