from django.db import models
from django.utils.translation import ugettext as _

from apps.utils.models import BaseModel, OrderedModelMixin, DescribedModelMixin
from apps.organizers.models import Organizer
from apps.events.models import Event


class Album(BaseModel, OrderedModelMixin, DescribedModelMixin):
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='albums',
        verbose_name=_('organizer'),
        help_text=_("to which organizer does the album belong?"),
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        to=Event,
        related_name='albums',
        verbose_name=_('event'),
        help_text=_("to which event does the album belong?"),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('album')
        verbose_name_plural = _('albums')
        ordering = ['ordering', 'title']

    def __str__(self):
        return self.title


class Media(BaseModel, OrderedModelMixin):
    album = models.ForeignKey(
        to=Album,
        related_name='%(class)s',
        verbose_name=_('album'),
        help_text=_("to which album does the media belong?"),
        on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(
        verbose_name=_('thumbnail'),
        help_text=_("a thumbnail to show in album.")
    )
    link = models.URLField(
        verbose_name=_('link'),
        help_text=_("an external link to the media."),
        blank=True,
        null=True
    )
    caption = models.TextField(
        verbose_name=_("caption"),
        help_text=_("an optional text, describing the media."),
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.album.__str__()


class Photo(Media):
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_(
            "the main photo file, if we're saving in in our own system."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("photo")
        verbose_name_plural = _("photos")
        ordering = ["album", "ordering"]


class Video(Media):
    video = models.FileField(
        verbose_name=_('video'),
        help_text=_(
            "the main video file, if we're saving in in our own system."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("video")
        verbose_name_plural = _("videos")
        ordering = ["album", "ordering"]
