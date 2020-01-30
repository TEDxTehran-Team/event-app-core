import uuid

from django.db import models
from django.utils.translation import ugettext as _
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel


class BaseModel(SafeDeleteModel):
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
