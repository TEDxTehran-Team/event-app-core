from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.networking.models import Interest


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

    job_title = models.CharField(
        _('job title'),
        max_length=70,
        blank=True,
        null=True,
    )

    education_field = models.CharField(
        _('education field'),
        max_length=70,
        blank=True,
        null=True,
    )

    biography = models.TextField(
        _('biography'),
        max_length=5000,
        blank=True,
        null=True,
    )

    interests = models.ManyToManyField(
        Interest,
        related_name='users',
        blank=True,
    )

    @property
    def does_need_profile_update(self):
        return (
            not self.job_title and
            not self.education_field and
            not self.biography and
            not self.interests.exists()
        )

    class Meta:
        db_table = 'auth_user'
