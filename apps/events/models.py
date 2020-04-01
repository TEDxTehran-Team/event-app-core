from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from apps.utils.models import BaseModel, Link, OrderedModelMixin, DescribedModelMixin
from apps.organizers.models import Organizer
from apps.locations.models import Venue


class EventType(BaseModel, DescribedModelMixin):
    """
    Represents an event type, as each organizer may hold many different events.
    """
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

    def __str__(self):
        return self.title


class Event(BaseModel, DescribedModelMixin):
    """
    Represents an event, hold by an organizer. This is all the system is about!
    """
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
    start_date = models.DateTimeField(
        verbose_name=_('start date'),
        help_text=_("shows the staring date and time for event."),
        blank=True,
        null=True
    )
    end_date = models.DateTimeField(
        verbose_name=_('end date'),
        help_text=_("shows the ending date and time for event."),
        blank=True,
        null=True
    )

    links = models.ManyToManyField(
        to=Link,
        related_name='+',
        verbose_name=_('links'),
        help_text=_(
            "a set of links related to this event, such as website link, registration link, etc."
        ),
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
    event_type = models.ForeignKey(
        to=EventType,
        related_name='events',
        verbose_name=_('event type'),
        help_text=_("does this event have any specific type?"),
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

    def __str__(self):
        return self.title


class AboutEvent(BaseModel, OrderedModelMixin, DescribedModelMixin):
    organizer = models.ForeignKey(
        Event,
        related_name='abouts',
        on_delete=models.CASCADE,
        verbose_name=_('event'),
        help_text=_("the event we're giving the info about.")
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("an optional image for the 'about' section."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("about event")
        verbose_name_plural = _("abouts on events")
        ordering = ["organizer", "ordering"]

    def __str__(self):
        return self.title
