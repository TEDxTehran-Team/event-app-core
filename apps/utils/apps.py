from django.apps import AppConfig
from django.utils.translation import ugettext as _


class UtilsConfig(AppConfig):
    name = 'tedxapp.utils'
    verbose_name = _(u'Utils')
