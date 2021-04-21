import pydoc

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _

from .settings import graphql_auth_settings as app_settings


def _generate_random_token():
    return get_random_string(32)


def _generate_code():
    return get_random_string(app_settings.CODE_LENGTH, '0987654321')


class AuthenticationAttempt(models.Model):
    token = models.CharField(
        _('token'),
        max_length=64,
        unique=True,
        default=_generate_random_token,
    )

    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='authentication_attempts',
    )

    verification_code = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        default=_generate_code,
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    date_succeeded = models.DateTimeField(
        blank=True,
        null=True,
    )

    def send_verification_code(self):
        pydoc.locate(app_settings.SMS_BACKEND).send(
            self.user.phone,
            format_lazy(_('Your verification code is: {code}'), code=self.verification_code)
        )
