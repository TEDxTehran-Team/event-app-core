import uuid

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from apps.utils.models import BaseModel, OrderedModelMixin, DescribedModelMixin
from apps.organizers.models import Organizer


class Application(BaseModel, DescribedModelMixin):
    active = models.BooleanField(
        default=True,
        verbose_name=_('active'),
        help_text=_("is the application currently active and functional?")
    )
    organizer = models.ForeignKey(
        to=Organizer,
        on_delete=models.PROTECT,
        related_name='applications',
        verbose_name=_("Organizer"),
        help_text=_("to which organizer does this app belong?")
    )

    class Meta:
        verbose_name = _("application")
        verbose_name_plural = _("applications")
        ordering = ['organizer', 'title']

    def __str__(self):
        return self.title


class ApplicationToken(BaseModel):
    application = models.ForeignKey(
        to=Application,
        related_name='tokens',
        on_delete=models.CASCADE,
        verbose_name=_('application'),
        help_text=_("to which application does this key belong?"),
    )
    key = models.UUIDField(
        verbose_name=_('key'),
        help_text=_(
            "a unique key sent in header to authorize the application."),
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_("active"),
        help_text=_("is the application token currently active and functional?")
    )

    class Meta:
        verbose_name = _("Application Token")
        verbose_name_plural = _("Application Tokens")

    def __str__(self):
        return self.application.__str__()


class ApplicationHit(BaseModel):
    application = models.ForeignKey(
        to=Application,
        related_name='hits',
        on_delete=models.CASCADE,
        verbose_name=_('application'),
        help_text=_("which application user has used?"),
    )
    user = models.ForeignKey(
        to=User,
        related_name='hits',
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        help_text=_("which user (if authenticated) has used the system?"),
        blank=True,
        null=True
    )
    # todo find a way to capture user request on graphql

    class Meta:
        verbose_name = _("application hit")
        verbose_name_plural = _("application hits")
