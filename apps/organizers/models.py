from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from apps.utils.models import BaseModel, OrderedModelMixin, DescribedModelMixin


class Organizer(BaseModel, DescribedModelMixin):
    """
    Stores an Event organizer, which may have many accounts and users who manage them. e.g. TEDxTehran.
    """
    logo = models.ImageField(
        verbose_name=_('logo'),
        help_text=_("organizer's logo"),
        blank=True,
        null=True
    )

    main_event = models.OneToOneField(
        to='events.Event',
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_("main event"),
        help_text=_(
            "which event is currently the main event for this organizer?"
        ),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("organizer")
        verbose_name_plural = _("organizers")
        ordering = ["title"]


class OrganizerAccount(BaseModel):
    """
    Represents a user's access to an organizer's events in admin.
    """
    user = models.OneToOneField(
        to=User,
        related_name='organizer_account',
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        help_text=_("a user who has access to organizer's events")
    )
    organizer = models.ForeignKey(
        to=Organizer,
        related_name='organizer_accounts',
        on_delete=models.CASCADE,
        verbose_name=_("organizer"),
        help_text=_("the organizer to whom's events user has access.")
    )
    # todo implement access level management.

    class Meta:
        verbose_name = _("organizer account")
        verbose_name_plural = _("organizers accounts")
        ordering = ["organizer", "user"]


class AboutOrganizer(BaseModel, OrderedModelMixin, DescribedModelMixin):
    organizer = models.ForeignKey(
        Organizer,
        related_name='abouts',
        on_delete=models.CASCADE,
        verbose_name=_('organizer'),
        help_text=_("the organizer we're giving the info about.")
    )
    image = models.ImageField(
        verbose_name=_('image'),
        help_text=_("an optional image for the 'about' section."),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        ordering = ["organizer", "ordering"]

    def __str__(self):
        return self.title
