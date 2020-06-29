from django.db import models
from django.utils.translation import ugettext as _

from apps.utils.models import BaseModel, OrderedModelMixin, DescribedModelMixin
from apps.organizers.models import Organizer
from apps.events.models import Event


class News(BaseModel, OrderedModelMixin, DescribedModelMixin):
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='news',
        verbose_name=_('organizer'),
        help_text=_("to which organizer does the news belong?"),
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        to=Event,
        related_name='news',
        verbose_name=_('event'),
        help_text=_("to which event does the news belong?"),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        verbose_name=_('thumbnail'),
        help_text=_("a thumbnail to show in album."),
        blank=True,
        null=True
    )
    summary = models.CharField(
        max_length=511,
        verbose_name=_('summary'),
        help_text=_("a short summary for the news."),
        blank=True,
        null=True
    )
    link = models.URLField(
        verbose_name=_('link'),
        help_text=_("an external link for the news item."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ['ordering', 'title']
        abstract = True

    def __str__(self):
        return self.title
