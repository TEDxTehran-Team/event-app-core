import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Organizer(models.Model):
    """
    Stores an Event organizer, which may have many accounts and users who manage them. e.g. TEDxTehran.
    """
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("name of the current organizer. e.g. TEDxTehran."),
        max_length=255,
        unique=True
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("a few paragraphs of info about the current organizer."),
        blank=True,
        null=True
    )
    slug = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        verbose_name = _("organizer")
        verbose_name_plural = _("organizers")
        ordering = ["title"]


class OrganizerAccount(models.Model):
    """
    Represents a user's access to an organizer's events in admin.
    """
    user = models.OneToOneField(
        to=User,
        related_name='organizer_account',
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        help_text=_("a user who has access to organizer's events")
    )
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='organizer_accounts',
        on_delete=models.CASCADE,
        verbose_name=_("organizer"),
        help_text=_("the organizer to whom's events user has access.")
    )
    # todo implement access level management.

    class Meta:
        verbose_name = _("organizer account")
        verbose_name_plural = _("organizers accounts")
        ordering = ["organizer", "user"]
