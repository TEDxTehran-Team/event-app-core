from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from apps.utils.models import BaseModel, Link
from apps.organizers.models import Organizer
from apps.locations.models import Venue


class EventType(BaseModel):
    """
    Represents an event type, as each organizer may hold many different events.
    """
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
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='event_types',
        verbose_name=_('organizer'),
        help_text=_("the organizer to whom the event type belongs."),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("event type")
        verbose_name_plural = _("event types")
        ordering = ["title"]
        # make it abstract until it's complete!
        abstract = True

    def __str__(self):
        return self.title


class Event(BaseModel):
    """
    Represents an event, hold by an organizer. This is all the system is about!
    """
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

    # todo create event type model

    links = models.ManyToManyField(
        to=Link,
        related_name='+',
        verbose_name=_('links'),
        help_text=_(
            "a set of links related to this event, such as website link, registration link, etc."),
        blank=True
    )
    venue = models.ForeignKey(
        to=Venue,
        related_name='events',
        verbose_name=_('venue'),
        help_text=_("where is the event held?"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='events',
        verbose_name=_('organizer'),
        help_text=_("the organizer to whom the event belongs."),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["created_at", "title"]
        # make it abstract until it's complete!
        abstract = True

    def __str__(self):
        return self.title
