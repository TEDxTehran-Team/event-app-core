import uuid

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from apps.utils.models import BaseModel
from apps.organizers.models import Organizer


class Event(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
        help_text=_("event's main title.")
    )
    description = models.TextField(
        verbose_name=_('description'),
        help_text=_("a description about event, shown in the applications."),
        blank=True,
        null=True
    )
    logo = models.ImageField(
        verbose_name=_('logo'),
        help_text=_("event official logo"),
        blank=True,
        null=True
    )
    banner = models.ImageField(
        verbose_name=_('banner'),
        help_text=_("a banner for the event to be shown on the applications."),
        blank=True,
        null=True
    )

    # todo create aa venue model

    # todo create event type model

    # todo create a event links model with proper and dynamic roles

    organizer = models.ForeignKey(
        to=Organizer,
        verbose_name=_('organizer'),
        help_text=_("the organizer to whom the event belongs."),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["start_date", "title"]
        # make it abstract until it's complete!
        abstract = True

    def __str__(self):
        return self.title