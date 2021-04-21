"""
Settings for graphql_auth are all namespaced in the GRAPHQL_AUTH setting.
For example your project's `settings.py` file might look like this:
GRAPHQL_AUTH = {
    "LOGIN_ALLOWED_FIELDS": ["email", "username"],
    "SEND_ACTIVATION_EMAIL": True,
}
This module provides the `graphql_auth_settings` object, that is used to access
Graphene settings, checking for user settings first, then falling
back to the defaults.
"""

from django.conf import settings as django_settings
from django.test.signals import setting_changed

from datetime import timedelta

# Copied shamelessly from Graphene / Django REST Framework

DEFAULTS = {
    "EXPIRATION_ACTIVATION_TOKEN": timedelta(days=7),
    # email stuff
    "USER_NODE_EXCLUDE_FIELDS": ["password", "is_superuser"],
    "USER_NODE_FILTER_FIELDS": {
        "phone": ["exact"],
        "email": ["exact"],
        "is_active": ["exact"],
    },
    # mutation error type
    "CUSTOM_ERROR_TYPE": None,
    "SMS_BACKEND": None,
    "CODE_LENGTH": 5,
}


class GraphQLAuthSettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    For example:
        from graphql_auth.settings import settings
        print(settings)
    """

    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, "_user_settings"):
            self._user_settings = getattr(django_settings, "GRAPHQL_AUTH", {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid graphql_auth setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val


graphql_auth_settings = GraphQLAuthSettings(None, DEFAULTS)


def reload_graphql_auth_settings(*args, **kwargs):
    global graphql_auth_settings
    setting, value = kwargs["setting"], kwargs["value"]
    if setting == "GRAPHQL_AUTH":
        graphql_auth_settings = GraphQLAuthSettings(value, DEFAULTS)


setting_changed.connect(reload_graphql_auth_settings)
