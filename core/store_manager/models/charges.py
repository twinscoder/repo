import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class DeliveryCharge(ActivityTracking):

    min_amount = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True, default=0, verbose_name=_("Minimum Amount")
    )
    max_amount = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True, default=0, verbose_name=_("Maximum Amount")
    )
    charge_amount = models.FloatField(
        validators=[MinValueValidator(0.0)],
        blank=True, null=True, default=0, verbose_name=_("Charge Amount")
    )
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    def __str__(self):
        return "{0}".format(self.id)

    class Meta:
        verbose_name = "Delivery Charge"
        verbose_name_plural = "delivery charges"
        ordering = ["-created_at"]
