from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    username = None

    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        _('email address'),
        blank=True,
        null=True,
    )

    phone = models.CharField(
        _('phone number'),
        max_length=32,
        unique=True,
        validators=[
            RegexValidator(r'^09\d{9}$'),
        ],
    )

    class Meta:
        db_table = 'auth_user'
