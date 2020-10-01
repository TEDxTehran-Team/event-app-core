
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from apps.utils.models import BaseModel, DescribedModelMixin
from apps.organizers.models import Organizer


class Venue(BaseModel, DescribedModelMixin):
    adress = models.TextField(
        max_length=1023,
        verbose_name=_('address'),
        help_text=_("venue's address."),
        blank=True,
        null=True
    )
    # Using the django GIS for lat and long, although would bear some benefits, but would be an overkill, at least for now.
    # It may be good to come up with a system to read lat and long from google map link.
    longitude = models.FloatField(
        verbose_name=_('longitude'),
        blank=True,
        null=True
    )
    latitude = models.FloatField(
        verbose_name=_('latitude'),
        blank=True,
        null=True
    )
    map_link = models.URLField(
        verbose_name=_('map link'),
        help_text=_(
            "a link to venue's location on the map (e.g. google map link)."),
        blank=True,
        null=True
    )
    map_image = models.ImageField(
        verbose_name=_('map image'),
        help_text=_("an image showing venue's location on the map."),
        blank=True,
        null=True
    )
    website = models.URLField(
        verbose_name=_('website'),
        help_text=_(
            "a link to the venue's website, or any social page (e.g. in Instagram)."),
        blank=True,
        null=True
    )
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='venues',
        verbose_name=_('organizer'),
        help_text=_("the organizer to whom the venue belongs."),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("venue")
        verbose_name_plural = _("venues")
        ordering = ['title']
