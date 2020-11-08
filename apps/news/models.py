from django.db import models
from apps.utils.models import BaseModel, DescribedModelMixin
from apps.organizers.models import Organizer
from django.utils.translation import ugettext as _



class News(BaseModel, DescribedModelMixin):
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='news',
        verbose_name=_('organizer'),
        help_text=_("to which organizer does the news belong?"),
        on_delete=models.CASCADE
    )
    icon = models.ImageField(
        verbose_name=_('icon'),
        help_text=_("an icon for the news"),
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("an image for the news."),
        blank=True,
        null=True
    )
    date = models.DateTimeField(
        verbose_name=_('date'),
        help_text=_("news date"),
        blank=True,
        null=True
    )
    extra_link = models.URLField(
        verbose_name=_('extra link'),
        help_text=_("any extra link related to the talk?"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")
        ordering = ["organizer", "title"]