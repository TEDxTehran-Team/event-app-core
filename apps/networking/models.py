from django.db import models
from django.utils.translation import gettext_lazy as _


class Interest(models.Model):
    name = models.TextField()


class MatchmakingRequest(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )

    match = models.ForeignKey(
        'Match',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    date_created = models.DateTimeField(
        _('date created'),
        auto_now_add=True,
    )

    date_matched = models.DateTimeField(
        _('date matched'),
        null=True,
        blank=True,
    )

    date_expired = models.DateTimeField(
        _('date expired'),
        null=True,
        blank=True,
    )


class Match(models.Model):
    parties = models.ManyToManyField(
        'accounts.User',
        related_name='matches',
    )

    conversation_id = models.TextField(
        _('conversation id'),
        null=True,
        blank=True
    )

    date_created = models.DateTimeField(
        _('date created'),
        auto_now_add=True,
    )
