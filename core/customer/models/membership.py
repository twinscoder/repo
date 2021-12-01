import uuid

from config.models import ActivityTracking
from core.store_manager.models import Plan
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Membership(ActivityTracking):

    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, blank=True, verbose_name=_("Customer")
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, blank=True, verbose_name=_("Plan")
    )
    card_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_("Membership Card Number")
    )
    start_date = models.DateTimeField(
        blank=True, null=True, verbose_name=_("Start Date")
    )
    end_date = models.DateTimeField(blank=True, null=True, verbose_name=_("End Date"))

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return f"{self.unique_id}"

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "membership"
        ordering = ["-created_at"]
