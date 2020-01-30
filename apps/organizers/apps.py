from django.apps import AppConfig
from django.utils.translation import ugettext as _


class OrganizersConfig(AppConfig):
    name = 'tedxapp.organizers'
    verbose_name = _(u'Organizers')
