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

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")
        ordering = ["organizer", "title"]