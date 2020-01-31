
from django.db import models
from django.utils.translation import ugettext as _

from apps.utils.models import BaseModel, OrderedModelMixin, DescribedModelMixin
from apps.organizers.models import Organizer
from apps.locations.models import Venue
from apps.events.models import Event
from .settings import SectionType


class EventDay(BaseModel, DescribedModelMixin):
    event = models.ForeignKey(
        Event,
        related_name='days',
        verbose_name=_('event'),
        help_text=_("to which event does the day belong?"),
        on_delete=models.CASCADE
    )
    date = models.DateField(
        verbose_name=_('date'),
        help_text=_("the date of this event day.")
    )

    class Meta:
        verbose_name = _("event day")
        verbose_name_plural = _("event days")
        ordering = ["event", "date"]

    def __str__(self):
        return self.title


class Session(BaseModel, DescribedModelMixin):
    day = models.ForeignKey(
        EventDay,
        related_name='sessions',
        on_delete=models.CASCADE,
        verbose_name=_('day'),
        help_text=_("to which event day does this session belong?")
    )
    start_time = models.TimeField(
        verbose_name=_('start time'),
        help_text=_("when will the session start?")
    )
    end_time = models.TimeField(
        verbose_name=_('end time'),
        help_text=_("when will the session end?")
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("an optional logo or thumbnail related to the session."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("session")
        verbose_name_plural = _("sessions")
        ordering = ["day", "start_time", "end_time"]

    def __str__(self):
        return self.title


class Section(BaseModel, DescribedModelMixin):
    event = models.ForeignKey(
        Event,
        related_name='sections',
        verbose_name=_('event'),
        help_text=_("to which event does the section belong?"),
        on_delete=models.CASCADE
    )
    sessions = models.ManyToManyField(
        Session,
        related_name='sections',
        verbose_name=_('sessions'),
        help_text=_("in which session(s) this section will be held?")
    )
    start_time = models.TimeField(
        verbose_name=_('start time'),
        help_text=_("when will the section start?")
    )
    end_time = models.TimeField(
        verbose_name=_('end time'),
        help_text=_("when will the section end?")
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("an optional logo or thumbnail related to the section."),
        blank=True,
        null=True
    )
    type = models.CharField(
        max_length=31,
        choices=SectionType.choices,
        default=SectionType.GENERIC,
        verbose_name=_('type'),
        help_text=_(
            "shows type of this program section, whether it's a generic section, a talk or performance, an activity, or else.")
    )

    class Meta:
        verbose_name = _("section")
        verbose_name_plural = _("sections")
        ordering = ["event", "start_time", "end_time"]

    def __str__(self):
        return self.title
