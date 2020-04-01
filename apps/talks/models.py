from django.db import models
from django.utils.translation import ugettext as _

from apps.utils.models import BaseModel, OrderedModelMixin, DescribedModelMixin
from apps.organizers.models import Organizer
from apps.timelines.models import Section
from apps.timelines.settings import SectionType


class Speaker(BaseModel, DescribedModelMixin):
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='speakers',
        verbose_name=_('organizer'),
        help_text=_("to which organizer does the speaker belong?"),
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("a thumbnail image for the speaker."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("speaker")
        verbose_name_plural = _("speakers")
        ordering = ["organizer", "title"]


class Talk(Section):
    speakers = models.ManyToManyField(
        to=Speaker,
        related_name='speakers',
        verbose_name=_('speakers'),
        help_text=_("which speaker(s) will be giving the talk?"),
    )
    video_link = models.URLField(
        verbose_name=_('video link'),
        help_text=_("video link?"),
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
        verbose_name = _("talk")
        verbose_name_plural = _("talks")
        ordering = ["session", "ordering", "start_time", "title"]

    def save(self, *args, **kwargs):
        self.type = SectionType.TALK

        return super().save(*args, **kwargs)