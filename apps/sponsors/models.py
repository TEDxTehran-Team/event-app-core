from apps.events.models import Event
from django.db import models
from django.utils.translation import ugettext as _

from apps.utils.models import BaseModel, DescribedModelMixin
from apps.organizers.models import Organizer

class SponsorsType(BaseModel, DescribedModelMixin):
    class Meta:
        verbose_name = _("sponsor type")
        verbose_name_plural = _("sponsor types")
        ordering = ["title"] 


class Sponsors(BaseModel, DescribedModelMixin):
    type = models.ForeignKey(
        to=SponsorsType,
        related_name="sponsors",
        verbose_name=_('type'),
        help_text=_("what is the type of this sponsor"),
        on_delete=models.CASCADE
    )
    organizer = models.ManyToManyField(
        to=Organizer,
        related_name='sponsors',
        verbose_name=_('organizer'),
        help_text=_("to which organizer does the sponsor belong?"),
        blank=True
    )
    event = models.ManyToManyField(
        Event,
        related_name='sponsors',
        verbose_name=_('event'),
        help_text=_("to which event does the sponsor belong?"),
        blank=True
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("a thumbnail image for the sponsor."),
        blank=True,
        null=True
    )

    logo = models.ImageField(
        verbose_name=_('logo'),
        help_text=_("logo of the sponsor."),
        blank=True,
        null=True
    )
