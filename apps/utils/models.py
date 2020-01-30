import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel


class BaseModel(SafeDeleteModel):
    """
    An abstract class with slug and timestamps, the fields we need for most of our classes.
    """
    _safedelete_policy = SOFT_DELETE_CASCADE

    slug = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at")
    )

    class Meta:
        abstract = True


class Link(BaseModel):
    """
    Merely a humble model, showing a simple link, to be used by other moldels whenever needed.
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_('title'),
        help_text=_("an optional title describing the link."),
        blank=True,
        null=True
    )
    # todo do we need to make the roles hardcode, or a related model? I don't really feel good about this one!
    role = models.SlugField(
        max_length=31,
        verbose_name=_('role'),
        help_text=_(
            'an optional slug, describing the link for other programs, such as applications.'),
        blank=True,
        null=True
    )
    url = models.URLField(
        verbose_name=_('url'),
        help_text=_('the url address for the link.')
    )
    created_by = models.ForeignKey(
        to=User,
        related_name='+',
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        help_text=_("who has created the link?")
    )

    class Meta:
        verbose_name = _("link")
        verbose_name_plural = _("links")
        ordering = ['created_at']

    def __str__(self):
        if self.title:
            return self.title
        elif self.role:
            return self.role
        else:
            return self.url[:63]+'...'
