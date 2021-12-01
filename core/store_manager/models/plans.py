import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Plan(ActivityTracking):

    name = models.CharField(
        max_length=255, default="", blank=True, null=True, verbose_name=_("Name")
    )
    price = models.FloatField(default=0, blank=True, null=True, verbose_name=_("Price"))
    description = models.CharField(
        max_length=255, default="", blank=True, null=True, verbose_name=_("Description")
    )
    days = models.IntegerField(
        default=0, blank=True, null=True, verbose_name=_("Number of days")
    )
    months = models.IntegerField(
        default=0, blank=True, null=True, verbose_name=_("Number of months")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "plans"
        ordering = ["-created_at"]
