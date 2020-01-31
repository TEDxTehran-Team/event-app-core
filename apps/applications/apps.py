from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ApplicationsConfig(AppConfig):
    name = 'apps.applications'
    verbose_name = _(u'Applications')
